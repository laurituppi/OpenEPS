#!/bin/bash

# vaihe 1.
# muuta resoluutio T159:iin cdo:lla
# vo+d -> u+v
# liitä z mallitasoilla mukaan jostain muusta filusta
# laske p mallitasoilla ulos z:n ja T:n avulla (ehkä pythonilla) ja korvaa z p:llä

# vaihe 2.
# pidetään kaikki analyysifilut samannimisinä
# jaa kukin timestep omaan directoryyn
# tästä varmaan tulee jonkinlainen loop kaiken muun yli

#########
# 2017071612-2017073112 puuttuu

module load bioconda
source activate /wrk/lautuppi/DONOTREMOVE/sisu-conda-envs/eppes
module load python/2.7.13-gnu620

mkdir -p $TMPDIR/scratch
cd $TMPDIR/scratch

calendar=/homeappl/home/lautuppi/appl_sisu/OpenEPS/bin/mandtg

sdate=2017110100
edate=2017113012
dstep=12

outputdir=$TMPDIR/scratch
outfile=p_GG_temp.nc

z2p=/homeappl/home/lautuppi/appl_sisu/OpenEPS/examples/oifs/analysis_preparation/z2p.py
infile_z_SH=/wrk/lautuppi/openEPS/convergence_tests/parest_conv_MTEN_jan2017_EPPES_5_n10/data/2017010712/pert000/ICMSHpart+000000
grib_set -s edition=1 $infile_z_SH infile_z_SH.grb1
cdo selvar,var129 infile_z_SH.grb1 z_SH.grb1
cdo sp2gpl z_SH.grb1 z_GG.grb1
cdo -t ecmwf -f nc -R copy z_GG.grb1 z_GG_temp.nc

for ((i=0; i<=1000; i=i+1)) do

  cdate=`exec $calendar $sdate + $(($i*$dstep))`

  echo '######################################'
  echo 'processing date ' $cdate
  echo '######################################'

  infile_SH=/wrk/project_2001029/OIFS_INI/t159/$cdate/ICMSHoifsINIT
  infile_ggml_GG=/wrk/project_2001029/OIFS_INI/t159/$cdate/ggml159
  targetdir=/wrk/lautuppi/DONOTREMOVE/analyses/optimization/t159/$cdate
  test -d $targetdir || mkdir $targetdir
  rm -f $targetdir/uvtpqsp.nc

  grib_set -s edition=1 $infile_SH vodtlnsp_SH.grb1
  grib_set -s edition=1 $infile_ggml_GG ggml_GG.grb1

  cdo selvar,var133 ggml_GG.grb1 q_GG.grb1
  cdo selvar,var138,var155 vodtlnsp_SH.grb1 vod_SH.grb1
  cdo selvar,var130,var152 vodtlnsp_SH.grb1 tlnsp_SH.grb1
  cdo selvar,var129 vodtlnsp_SH.grb1 z_surf_SH.grb1

  cdo dv2uvl vod_SH.grb1 uv_GG.grb1

  cdo sp2gpl tlnsp_SH.grb1 tlnsp_GG.grb1
  cdo sp2gpl z_surf_SH.grb1 z_surf_GG.grb1

  cdo setgridtype,regular q_GG.grb1 q_GG_reg.grb1

  cdo -t ecmwf -f nc -R copy uv_GG.grb1 uv_GG_temp.nc
  cdo -t ecmwf -f nc -R copy tlnsp_GG.grb1 tlnsp_GG_temp.nc
  cdo -t ecmwf -f nc -R copy q_GG_reg.grb1 q_GG_temp.nc
  cdo -t ecmwf -f nc -R copy z_surf_GG.grb1 z_surf_GG.nc

  python $z2p tlnsp_GG_temp.nc z_GG_temp.nc z_surf_GG.nc $outfile $outputdir

  cdo selvar,LNSP tlnsp_GG_temp.nc lnsp_GG_temp.nc
  cdo selvar,T tlnsp_GG_temp.nc t_GG_temp.nc
  cdo exp lnsp_GG_temp.nc sp1_GG_temp.nc
  cdo setname,SP sp1_GG_temp.nc sp_GG_temp.nc

  cdo merge uv_GG_temp.nc t_GG_temp.nc sp_GG_temp.nc q_GG_temp.nc p_GG_temp.nc uvtpqsp.nc

  mv uvtpqsp.nc $targetdir

  if [ "$cdate" -eq "$edate" ] ; then
    exit
  fi

  rm -f *.grb1 *.nc
done

rm -rf $TMPDIR/scratch

# t=130
# vo=138
# d=155
# lnsp=152

# ndate=`exec $WORK/./mandtg $cdate + $DSTEP`
