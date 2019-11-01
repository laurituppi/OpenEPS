#!/bin/bash

#if [ 0 -eq 1 ]; then
#SBATCH -p serial
#SBATCH -J kstest
#SBATCH -t 04:00:00
#SBATCH -n 1
#SBATCH --mem-per-cpu=4000
#SBATCH -o outerr
#SBATCH -e outerr
#fi

#module load python/2.7.13-gnu620 bioconda
module purge
#module load python/3.5.3-gnu620 bioconda


#export XDG_RUNTIME_DIR=/tmp/lautuppi/runtime-lautuppi
#export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb

if [ 1 -eq 1 ]; then # perus EPPES tai DE konvergenssitestin plottaus
  #module load python/2.7.13-gnu620 bioconda #Sisussa
  #export XDG_RUNTIME_DIR=/tmp/lautuppi/runtime-lautuppi
  #source activate /wrk/lautuppi/DONOTREMOVE/sisu-conda-envs/eppes
  source $WRKDIR/DONOTREMOVE/miniconda3/etc/profile.d/conda.sh
  conda activate eppes_python_3
  npars=5
  nens=20
  fclen=24
  dir=${nens}mem_${fclen}h_t159_5par_a
  dv1=2.0
  dv2=0.00175
  dv3=0.75e-04
  dv4=0.0014
  dv5=2.0 #0000

  #eppesdir=/wrk/lautuppi/openEPS/publ_conv_tests/DE/$dir/data/eppes
  #eppesdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2_rmsez850/$dir/
  #eppesdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level25/failed/$dir/
  #eppesdir=/wrk/lautuppi/openEPS/benchmarks/$dir/data/eppes
  #eppesdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/DE/level2/bad_parameters/uusinta/$dir/
  #eppesdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2/$dir/
  #eppesdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level1/rmse_z_850/$dir
  #eppesdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level1/only_ENTSHALP/$dir
  eppesdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/final_test/$dir/
  inputdir=$eppesdir/eppesdata
  inifiles=$eppesdir/init/

  #mkdir $inputdir
  #mv $eppesdir/20* $inputdir
  #outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/DE/$dir
  #outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/DE/level2/bad_parameters/uusinta/$dir
  #outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/EPPES/level2_rmsez850/$dir
  #outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/EPPES/level2/$dir
  #outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/EPPES/level25/failed/$dir
  #outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/EPPES/level1/rmse_z_850/$dir/
  #outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/EPPES/level1/only_ENTSHALP/$dir/
  outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/EPPES/final_test/$dir/
  test -d $outputdir || mkdir -p $outputdir

  #python3 plot-pars-3_EPPES.py ${npars} ${nens} ${inputdir} ${outputdir} ${dv1} ${dv2}

  python3 plot-pars-35_EPPES.py ${npars} ${nens} ${inputdir} ${outputdir} ${inifiles} ${dv1} ${dv2} ${dv3} ${dv4} ${dv5} 

elif [ 0 -eq 1 ]; then # 2D parvien plottaus jokaiselta konvergenssitestin iteraatiolta
  source activate eppes_own
  inputdir=/wrk/lautuppi/openEPS/optimization_tests/parest_opt_MTEN_dec2016-oct2017_DE_15/data/eppes/eppesdata/
  outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/optimization/parest_opt_MTEN_dec2016-oct2017_DE_15/DE_step_plot/
  samplefile=sampleout.dat
  scorefile=score.dat
  sequence=5
  ndays=111

  python DE_step_plot.py $inputdir $outputdir $samplefile $scorefile $sequence $ndays

elif [ 0 -eq 1 ]; then # Bhattacharyyan etäisyys, toimii vain Taidolla
  module load python-env/3.5.3
  #source activate /wrk/lautuppi/DONOTREMOVE/sisu-conda-envs/eppes
  npars=2
  declare -a magazine
  magazine=(50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 6mem_12h 6mem_24h 6mem_48h 6mem_72h 6mem_96h 6mem_120h 6mem_144h 10mem_12h 10mem_24h 10mem_48h 10mem_72h 10mem_96h 10mem_120h 10mem_144h 10mem_168h 16mem_12h 16mem_24h 16mem_48h 16mem_72h 16mem_96h 16mem_120h 16mem_144h 20mem_12h 20mem_24h 20mem_48h 20mem_72h 20mem_96h 20mem_120h 26mem_12h 26mem_24h 26mem_48h 26mem_72h 26mem_96h 26mem_120h 26mem_144h 26mem_168h 30mem_12h 30mem_24h 30mem_48h 30mem_72h 30mem_96h 30mem_120h 30mem_144h 36mem_12h 36mem_24h 36mem_48h 36mem_72h 36mem_96h 36mem_120h 40mem_12h 40mem_24h 40mem_48h 40mem_72h 40mem_96h 40mem_120h 40mem_144h 40mem_168h 46mem_12h 46mem_24h 46mem_48h 46mem_72h 46mem_96h 46mem_120h)
  #magazine=(36mem_24h)
  calc_method=1 # 1=use hyperparameters, 2=use samples
  optimizer=2 # 1=EPPES, 2=DE
  parameter=2 # 1=ENTSHALP, 2=ENTRORG
  #nens=1000000 
  outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/bhattacharyya/multivariate/$calc_method$optimizer$parameter
  test -d $outputdir || mkdir -p ${outputdir} && mkdir -p ${outputdir}/data
  rm -f $outputdir/*.png
  rm -f ${outputdir}/data/*.txt
  for i in $(seq 0 69); do
    if [ $optimizer -eq 1 ]; then
      inputdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/${magazine[i]}/eppesdata
    elif [ $optimizer -eq 2 ]; then
      inputdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/DE/${magazine[i]}/eppesdata
    fi
    #outputdir=/homeappl/home/lautuppi/appl_sisu/OpenEPS/examples/oifs/plotting
    #python2 kstest.py $npars $inputdir $outputdir $optimizer $parameter $calc_method ${magazine[i]}
    python3 stat_tests/bhattacharyya_multi.py $npars $inputdir $outputdir $optimizer $parameter $calc_method ${magazine[i]}
    #python crps_test.py $npars $nens $inputdir $outputdir $optimizer $parameter
  done

elif [ 0 -eq 1 ]; then # esim Bhattacharyyan testien taulukoiminen
  module load python-env/2.7.10
  #python2 plot_stat_table.py
  #python2 plot_stat_table3.py
  #python2 plot_number_of_points2r.py
  #python2 plot_crps1_crps2.py
  python2 plot_mu_error.py

elif [ 0 -eq 1 ]; then # Bhattacharyyan pituuden laskenta
  module load python-env/3.5.3

  outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/bhattacharyya_costf/EPPES
  calc_method=1

  declare -a magazine1
  declare -a magazine2
  magazine1=(50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 50mem_168h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 50mem_168h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 50mem_168h 50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h)
  magazine2=(50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 6mem_12h 6mem_24h 6mem_48h 6mem_72h 6mem_96h 6mem_120h 6mem_144h 10mem_12h 10mem_24h 10mem_48h 10mem_72h 10mem_96h 10mem_120h 10mem_144h 10mem_168h 16mem_12h 16mem_24h 16mem_48h 16mem_72h 16mem_96h 16mem_120h 16mem_144h 20mem_12h 20mem_24h 20mem_48h 20mem_72h 20mem_96h 20mem_120h 26mem_12h 26mem_24h 26mem_48h 26mem_72h 26mem_96h 26mem_120h 26mem_144h 26mem_168h 30mem_12h 30mem_24h 30mem_48h 30mem_72h 30mem_96h 30mem_120h 30mem_144h 36mem_12h 36mem_24h 36mem_48h 36mem_72h 36mem_96h 36mem_120h 40mem_12h 40mem_24h 40mem_48h 40mem_72h 40mem_96h 40mem_120h 40mem_144h 40mem_168h 46mem_12h 46mem_24h 46mem_48h 46mem_72h 46mem_96h 46mem_120h)
  #magazine=(50mem_24h)

  test -d $outputdir || mkdir -p ${outputdir} && mkdir -p ${outputdir}/data
  rm -f $outputdir/*.png
  rm -f ${outputdir}/data/*.txt
  for i in $(seq 0 69); do
    inputdir1=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/inner_predictability/${magazine1[i]}
    inputdir2=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/${magazine2[i]}/eppesdata
    python3 stat_tests/bhattacharyya_costf.py $inputdir1 $inputdir2 $outputdir $calc_method ${magazine2[i]}
  done

elif [ 0 -eq 1 ]; then # Leutbecherin fair CRPS:n laskeminen
  module load python-env/3.5.3
  declare -a magazine1
  declare -a magazine2
  parameter=2
  optimizer=EPPES
  part=2
  if [ 0 -eq 1 ]; then
    magazine1=(50 50 50 50 50 50 50 6 6 6 6 6 6 6 10 10 10 10 10 10 10 10 16 16 16 16 16 16 16 20 20 20 20 20 20 26 26 26 26 26 26 26 26 30 30 30 30 30 30 30 36 36 36 36 36 36 40 40 40 40 40 40 40 40 46 46 46 46 46 46)
    magazine2=(50mem_12h 50mem_24h 50mem_48h 50mem_72h 50mem_96h 50mem_120h 50mem_144h 6mem_12h 6mem_24h 6mem_48h 6mem_72h 6mem_96h 6mem_120h 6mem_144h 10mem_12h 10mem_24h 10mem_48h 10mem_72h 10mem_96h 10mem_120h 10mem_144h 10mem_168h 16mem_12h 16mem_24h 16mem_48h 16mem_72h 16mem_96h 16mem_120h 16mem_144h 20mem_12h 20mem_24h 20mem_48h 20mem_72h 20mem_96h 20mem_120h 26mem_12h 26mem_24h 26mem_48h 26mem_72h 26mem_96h 26mem_120h 26mem_144h 26mem_168h 30mem_12h 30mem_24h 30mem_48h 30mem_72h 30mem_96h 30mem_120h 30mem_144h 36mem_12h 36mem_24h 36mem_48h 36mem_72h 36mem_96h 36mem_120h 40mem_12h 40mem_24h 40mem_48h 40mem_72h 40mem_96h 40mem_120h 40mem_144h 40mem_168h 46mem_12h 46mem_24h 46mem_48h 46mem_72h 46mem_96h 46mem_120h)
  elif [ 1 -eq 1 ];then
    magazine1=(20 20 20 20 26 26 26 26)
    magazine2=(20mem_48h 20mem_48h_2 20mem_48h_3 20mem_48h_4 26mem_24h 26mem_24h_2 26mem_24h_3 26mem_24h_4)
  fi
  #nens=50
  #inputdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/50mem_24h/eppesdata
  outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/$optimizer/level2/par$parameter/part_$part/crps_score2
  test -d $outputdir || mkdir -p ${outputdir} && mkdir -p ${outputdir}/data2

  for i in $(seq 0 7); do #69
    inputdir=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/$optimizer/level2/${magazine2[i]}/eppesdata
    python3 fair_crps.py ${magazine1[i]} $inputdir $outputdir $parameter ${magazine2[i]}
  #name=50mem_24h
  done
  #python3 fair_crps.py $nens $inputdir $outputdir $parameter $name

elif [ 0 -eq 1 ]; then
  #module load python/2.7.13-gnu620 bioconda
  #export XDG_RUNTIME_DIR=/tmp/lautuppi/runtime-lautuppi
  #source activate /wrk/lautuppi/DONOTREMOVE/sisu-conda-envs/eppes

  source $WRKDIR/DONOTREMOVE/miniconda3/etc/profile.d/conda.sh
  conda activate eppes_python_3

  indir0=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level00/50mem_48h/eppesdata
  indir1=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level1/50mem_48h/eppesdata
  indir2=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2/50mem_48h/eppesdata
  indir3=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level25/50mem_48h/eppesdata
  #indir4=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2_rmsez850/50mem_48h/eppesdata
  indir4=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level1/rmse_z_850/50mem_48h/eppesdata
  
  python3 convergence_multi.py $indir0 $indir1 $indir2 $indir3 $indir4
fi


