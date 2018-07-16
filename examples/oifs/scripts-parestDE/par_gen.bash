#!/bin/bash
# This version uses DE instead of EPPES.

module load python-env/2.7.10

date=${1}

# Log
echo `date +%H:%M:%S` pargener "ens   " >> $WORK/master.log

# There are two options how to generate cost func values.

# 1. Generate random cost func values
if [ 0 -eq 1 ]; then
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
fi

# 2. Use global dry total energy norm as cost function.
if [ 1 -eq 1 ]; then
rm -f $DATA/eppes/score.dat
for imem in $(seq 1 $ENS); do
    imem=$(printf "%03d" $imem)
    step=$(printf "%06d" $FCLEN)
    # *** command line arguments for DTEN.py ***
    # See details in commentation of DTEN.py.
    forecast_SH=$DATA/$date/pert$imem/PPSH_${EXPS}+$step.nc
    forecast_GG=$DATA/$date/pert$imem/PPGG_${EXPS}+$step.nc
    ref_timestep=-1 #$(((number_of_ensemble+4)*4+13))
    echo 'number of ensemble = ' $number_of_ensemble
    echo 'timestep in reference file = ' $ref_timestep
    reference_SH=$DATA/$date/pert000/PPSH_${EXPS}+$step.nc
    reference_GG=$DATA/$cdate/pert000/PPGG_${EXPS}+$step.nc
    outputdir=$DATA/$cdate/pert$imem
    scale=1 #150.0
    # *** ***
    # calculate cost fuction values
    python $SCRI/MTEN.py $forecast_SH $forecast_GG $ref_timestep $reference_SH $reference_GG $outputdir $scale
    score=$(sed -n '1p' < $DATA/$date/pert$imem/score.dat)
    echo $score >> $DATA/eppes/score.dat
done
fi


# Parameter perturbations
#
module purge
module load python-env/3.4.5
module load biopython-env/3.4.5
pushd $DATA/eppes > /dev/null
#cp -f sampleout.dat oldsample.dat
python DEroutine.py DE.cfg # run DE

# Possible recalculation
#
# To prevent stagnation of parameters, recalculation is ordered for the next iteration with about 10% chance.
# Starting of recalculation (run type: RunType.rcl_start) is not allowed on two consecutive iterations.
number=$RANDOM
#echo '############ random number = ' $number
if [ "$number" -ge 29000 ]; then # 29000 -> ~10% probability of recalculation.
  lognum=$(sed "${nid}q;d" $DATA/eppes/log.dat)
  #echo '############## log.dat = ' $lognum
  if [ "$lognum" != "4.000000000000000000e+00" ]; then # double recalculation is not allowed.
    echo '3.0' > $DATA/eppes/log.dat
    echo '################# recalculation ordered for next iteration ################'
  fi
  #python DEroutine.py DE.cfg
fi
#

# Store values
for item in sampleout mufile sigfile; do
    cp -f ${item}.dat $date/.
done
#cp -f sampleout.dat $date/.
#mv -f scores.dat $date/.
#mv -f winfo.dat $date/.

popd > /dev/null

