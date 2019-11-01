#!/bin/bash

# Post-processing script
# REQUIRES CDO

steps=${1:-"0000"}

# Get process id
nid=$(pwd | grep -o -P "$SUBDIR_NAME.{0,5}" | sed -e "s/$SUBDIR_NAME//g")

# Log
echo `date +%H:%M:%S` post-pro $SUBDIR_NAME${nid} >> $WORK/master.log

for step in $steps; do
    # convert to GRIB1
    $GRIBTOOLS/grib_set -s edition=1 ICMSH${EXPS}+00${step} temp1.grb1
    $GRIBTOOLS/grib_set -s edition=1 ICMGG${EXPS}+00${step} temp2.grb1

    # Select pressure and surface level variables
    cdo -selzaxis,pressure         temp1.grb1 temp1.grb
    cdo -selzaxis,pressure,surface temp2.grb1 temp2.grb
    
    # Do a spectral transform to gg
    if [ $RES -eq 21 ]; then
	cdo -sp2gp  temp1.grb temp_gg.grb
    else
	cdo -sp2gpl temp1.grb temp_ggsh.grb
    fi
    cdo -remapbic,$SCRI/360x181_grid.txt temp_ggsh.grb temp_ggsh2.grb

    # Transform GG to regular gaussian
    cdo -R copy temp2.grb temp3.grb
    cdo -remapbic,$SCRI/360x181_grid.txt temp3.grb temp4.grb
    cdo selvar,var133 temp4.grb temp5.grb

    # Merge
    cdo -merge temp_ggsh2.grb temp5.grb temp_all.grb #PP_${EXPS}+00${step}

    # Ordering
    cdo selvar,var129 temp_all.grb temp_var129.grb
    cdo selvar,var130 temp_all.grb temp_var130.grb
    cdo selvar,var131 temp_all.grb temp_var131.grb
    cdo selvar,var132 temp_all.grb temp_var132.grb
    cdo selvar,var133 temp_all.grb temp_var133.grb

    cdo merge temp_var129.grb temp_var130.grb temp_var133.grb temp_var131.grb temp_var132.grb PP_${EXPS}+00${step}

    rm -f temp*.grb temp*.grb1
done
