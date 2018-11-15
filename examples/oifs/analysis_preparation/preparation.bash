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

module load bioconda
source activate /wrk/lautuppi/DONOTREMOVE/sisu-conda-envs/eppes
#module load eccodes
module load python/2.7.13-gnu620

cd $TMPDIR
mkdir scratch
cd scratch

infile_SH=/wrk/project_2001029/OIFS_INI/t159/2017010100/ICMSHoifsINIT
infile_ggml_GG=/wrk/project_2001029/OIFS_INI/t159/2017010100/ggml159
infile_z_SH=/wrk/lautuppi/openEPS/parest_conv_MTEN_jan2017_EPPES_5_n10/data/2017010712/pert000/ICMSHpart+000000
targetdir=/wrk/lautuppi/DONOTREMOVE/analyses/optimization/t159/2017010100

z2p=/homeappl/home/lautuppi/appl_sisu/OpenEPS/examples/oifs/analysis_preparation/z2p.py

grib_set -s edition=1 $infile_SH vodtlnsp_SH.grb1
grib_set -s edition=1 $infile_z_SH infile_z_SH.grb1
grib_set -s edition=1 $infile_ggml_GG ggml_GG.grb1

cdo selvar,var133 ggml_GG.grb1 q_GG.grb1
cdo selvar,var129 infile_z_SH.grb1 z_SH.grb1
cdo selvar,var138,var155 vodtlnsp_SH.grb1 vod_SH.grb1
cdo selvar,var130,var152 vodtlnsp_SH.grb1 tlnsp_SH.grb1
cdo selvar,var129 vodtlnsp_SH.grb1 z_surf_SH.grb1

cdo dv2uvl vod_SH.grb1 uv_SH.grb1

cdo sp2gpl uv_SH.grb1 uv_GG.grb1
cdo sp2gpl tlnsp_SH.grb1 tlnsp_GG.grb1
cdo sp2gpl z_SH.grb1 z_GG.grb1
cdo sp2gpl z_surf_SH.grb1 z_surf_GG.grb1

cdo setgridtype,regular q_GG.grb1 q_GG_reg.grb1

cdo -t ecmwf -f nc -R copy uv_GG.grb1 uv_GG_temp.nc
cdo -t ecmwf -f nc -R copy tlnsp_GG.grb1 tlnsp_GG_temp.nc
cdo -t ecmwf -f nc -R copy z_GG.grb1 z_GG_temp.nc
cdo -t ecmwf -f nc -R copy q_GG_reg.grb1 q_GG_temp.nc
cdo -t ecmwf -f nc -R copy z_surf_GG.grb1 z_surf_GG.nc

outputdir=$TMPDIR/scratch
outfile=p_GG_temp.nc

python $z2p tlnsp_GG_temp.nc z_GG_temp.nc z_surf_GG.nc $outfile $outputdir

#cdo merge uv_GG_temp.nc tlnsp_GG_temp.nc q_GG_temp.nc p_GG_temp.nc uvtpqlnsp.nc

#mv uvtpqlnsp.nc $targetdir

#rm -f *.grb1 *.nc



# t=130
# vo=138
# d=155
# lnsp=152
