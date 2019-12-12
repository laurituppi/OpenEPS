#!/bin/bash
# This version uses Python version of EPPES.
#module load biopython-env
#module load python-env/2.7.10

date=${1}

# Log
echo `date +%H:%M:%S` pargener "ens   " >> $WORK/master.log

# There are two options how to generate cost func values.

# 1. Generate random cost func values
if [ $COSTFUNCTION == '' ]; then
  # Set up an awk function for real number calculations
  rcalc() { awk "BEGIN{print $*}"; }

  # Generate random parameter values for each ens member
  # $RANDOM € {0 .. 32767}
  #
  rm -f $DATA/eppes/scores.dat
  for imem in $(seq 1 $ENS); do
      imem=$(printf "%03d" $imem)
	    
      number=$RANDOM
      number=$(rcalc $number/32767.-0.5)
      # Scale and add to default value (ENTSHALP=2.0)
      number=$(rcalc $number*0.1+2.0)

      echo $number >> $DATA/eppes/scores.dat
  done

# 2. Use global moist total energy norm as cost function.
elif [ $COSTFUNCTION == 'MTEN' ]; then
  rm -f $DATA/eppes/scores.dat
  if [ "$HOST"=="puhti" ]; then
    #module load python-env/2.7.10
    export CONDA_ENVS_PATH=/projappl/project_2001011/puhti_conda_envs
    source /appl/soft/bio/bioconda/miniconda3/etc/profile.d/conda.sh
    conda activate eppes_python_3
  elif [ "$HOST"=="sisu" ]; then
    module load python/2.7.13-gnu620
  fi
  for imem in $(seq 1 $ENS); do
      imem=$(printf "%03d" $imem)
      step=$(printf "%06d" $FCLEN)
      # *** command line arguments for MTEN.py ***
      # See details in commentation of MTEN.py.
      forecast_SH=$DATA/$date/pert$imem/PPSH_${EXPS}+$step.nc
      forecast_GG=$DATA/$date/pert$imem/PPGG_${EXPS}+$step.nc
      ref_timestep=-1 #$(((number_of_ensemble+4)*4+13))
      echo 'number of ensemble = ' $number_of_ensemble
      echo 'timestep in reference file = ' $ref_timestep
      if [ "$EXPTYPE" = "C" ]; then # use control forecast as reference
        reference_SH=$DATA/$date/pert000/PPSH_${EXPS}+$step.nc
        reference_GG=$DATA/$date/pert000/PPGG_${EXPS}+$step.nc
        echo 'chosen reference data:' $reference_SH
      elif [ "$EXPTYPE" = "O" ]; then # use analysis as reference
        reference_SH=/wrk/lautuppi/DONOTREMOVE/analyses/optimization/t$RES/$an_date/uvtpqsp.nc
        reference_GG=$reference_SH
        echo 'chosen reference data:' $reference_SH
      fi
      outputdir=$DATA/$cdate/pert$imem
      calcstyle=1
      scale=1 #150.0
      # *** ***
      # calculate cost fuction values
      python $SCRI/MTEN.py $forecast_SH $forecast_GG $ref_timestep $reference_SH $reference_GG $outputdir $calcstyle $scale
      score=$(sed -n '1p' < $DATA/$date/pert$imem/score.dat)
      echo $score >> $DATA/eppes/scores.dat
  done

# 3. Use bad cost function; rmse of Z850
elif [ $COSTFUNCTION == 'RMSE_z' ]; then
  rm -f $DATA/eppes/scores.dat
  if [ "$HOST" -eq "puhti" ]; then
    #module load python-env/2.7.10
    export CONDA_ENVS_PATH=/projappl/project_2001011/puhti_conda_envs
    source /appl/soft/bio/bioconda/miniconda3/etc/profile.d/conda.sh
    conda activate eppes_python_3
  elif [ "$HOST" -eq "sisu" ]; then
      module load python/2.7.13-gnu620
  fi
  for imem in $(seq 1 $ENS); do
      imem=$(printf "%03d" $imem)
      step=$(printf "%06d" $FCLEN)
      forecast_SH=$DATA/$date/pert$imem/PPSH_${EXPS}+$step.nc
      reference_SH=$DATA/$date/pert000/PPSH_${EXPS}+$step.nc
      outputdir=$DATA/$cdate/pert$imem
      python $SCRI/RMSE_z.py $forecast_SH $reference_SH $outputdir
      score=$(sed -n '1p' < $DATA/$date/pert$imem/score.dat)
      echo $score >> $DATA/eppes/scores.dat
  done
fi

# Parameter perturbations
#
pushd $DATA/eppes > /dev/null
cp -f sampleout.dat oldsample.dat
#./eppes_routine
#module load biopython-env
python eppesroutine.py eppes.cfg

# Store values
for item in mu sig n w; do
    cp -f ${item}file.dat $date/.
done
cp -f sampleout.dat $date/.
mv -f scores.dat $date/.
mv -f winfo.dat $date/.

popd > /dev/null

