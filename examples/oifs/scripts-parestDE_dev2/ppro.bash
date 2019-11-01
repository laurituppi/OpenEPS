#!/bin/bash

# Post-processing script
# REQUIRES CDO

steps=${1:-"0000"}

# Get process id
nid=$(pwd | grep -o -P "$SUBDIR_NAME.{0,5}" | sed -e "s/$SUBDIR_NAME//g")

# Log
echo `date +%H:%M:%S` post-pro $SUBDIR_NAME${nid} >> $WORK/master.log

#for step in $steps; do
    # convert to GRIB1
#    $GRIBTOOLS/grib_set -s edition=1 ICMSH${EXPS}+00${step} temp.grb1

    # Select pressure level variables t and z
#    cdo -selzaxis,1 -selvar,var130,var129 temp.grb1 temp.grb
    
    # Do a spectral transform to gg
#    cdo -sp2gpl temp.grb PP_${EXPS}+00${step}

#    rm -f temp.grb temp.grb1
#done

# This block prepares files for DTEN.py
for step in $steps; do
    # convert to GRIB1
    $GRIBTOOLS/grib_set -s edition=1 ICMSH${EXPS}+00${step} temp1.grb1
    $GRIBTOOLS/grib_set -s edition=1 ICMGG${EXPS}+00${step} temp2.grb1

    cdo setgridtype,regular temp2.grb1 temp22.grb1
    cdo -gp2spl temp22.grb1 temp2_2.grb1
    cdo -sp2sp,39 temp2_2.grb1 temp2_3.grb1
    #cdo -sp2sp,$RES temp2_3.grb1 temp2_4.grb1 # ei toimi
    cdo -sp2gpl temp2_3.grb1 temp2_4.grb1
    cdo remapbic,n80 temp2_4.grb1 temp2_5.grb1

    # Select model level variables u, v, t and pressure
    cdo -selvar,var130,var131,var132,var54 temp1.grb1 temp11.grb1
    
    # Do a spectral transform to gg
    cdo -sp2gpl temp11.grb1 temp3.grb1

    # Do a transform to NetCDF
    cdo -t ecmwf -f nc -R copy temp3.grb1 PPSH_${EXPS}+00${step}.nc
    cdo -t ecmwf -f nc -R copy temp2.grb1 PPGG_${EXPS}+00${step}.nc

    cdo -t ecmwf -f nc -R copy temp2_5.grb1 PPGG_alt_${EXPS}+00${step}.nc

    rm -f temp*
done
