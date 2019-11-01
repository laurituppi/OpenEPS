#!/bin/bash
#SBATCH -p serial
#SBATCH -J 1144
#SBATCH -t 03:00:00
#SBATCH -n 1
#SBATCH --mem-per-cpu=4000
#SBATCH -o outerra144
#SBATCH -e outerra144

module load python-env/2.7.10


FCLEN=144
EXP=ep11
experiment=20mem_${FCLEN}h
outputdir=$TMPDIR/$EXP/processing_scores_$experiment
mkdir -p $outputdir
mkdir $outputdir/eppesdata

declare -a dates
dates=(2016120100 2016120800 2016121500 2016122200 2016122900 2017010500 2017011200 2017011900 2017012600 2017020200 2017020900 2017021600 2017022300 2017030200 2017030900 2017031600 2017032300 2017033000 2017040600 2017041300 2017042000 2017042700 2017050400 2017051100 2017051800 2017052500 2017060100 2017060800 2017061500 2017062200 2017062900 2017070600 2017071300 2017072000 2017072700 2017080300 2017081000 2017081700 2017082400 2017083100 2017090700 2017091400 2017092100 2017092800 2017100500 2017101200 2017101900 2017102600 2017110200 2017110900 2017111600 2017112300 2017113000)

step=$(printf "%06d" $FCLEN)
ref_timestep=-1
calcstyle=1
scale=1
SCRI=/homeappl/home/lautuppi/appl_sisu/OpenEPS/examples/oifs/scripts-parest_dev
datadir=/wrk/lautuppi/openEPS/publ_conv_tests/EPPES/converged_pars_test/level1/20mem_144h/data
#datadir=/wrk/lautuppi/openEPS/benchmarks/level2/20mem_144h/data
for i in $(seq 0 52); do
  r_SH=$datadir/${dates[i]}/pert000/PPSH_$EXP+$step.nc
  r_GG=$datadir/${dates[i]}/pert000/PPGG_$EXP+$step.nc
  mkdir $outputdir/eppesdata/${dates[i]}
  for j in $(seq 1 20); do
    imem=$(printf "%03d" $j)
    f_SH=$datadir/${dates[i]}/pert$imem/PPSH_$EXP+$step.nc
    f_GG=$datadir/${dates[i]}/pert$imem/PPGG_$EXP+$step.nc
    python $SCRI/MTEN.py $f_SH $f_GG $ref_timestep $r_SH $r_GG $outputdir $calcstyle $scale
    score=$(sed -n '1p' < $outputdir/score.dat)
    echo $score >> $outputdir/eppesdata/${dates[i]}/scores.dat
  done
done

destination=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/inner_predictability/converged_pars_test/level1/$experiment/
#destination=/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/inner_predictability/level1/$experiment/
mkdir $destination

mv $outputdir/eppesdata/ $destination
rm -rf $outputdir
