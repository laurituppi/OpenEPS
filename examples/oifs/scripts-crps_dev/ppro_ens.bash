#!/bin/bash

# Post-processing script
# REQUIRES CDO

steps=${1:-"0000"}

# Log
echo `date +%H:%M:%S` post-pro "ens   " >> $WORK/master.log
time=0

# Makes only sense for ENS > 1
if [ $ENS -gt 1 ]; then
    for step in $steps; do
        time=$((time+AN_STEP))
	an_date=`exec $WORK/./mandtg $cdate + $time`
	# Constuct namelist
	enslist=""
	for imem in $(seq 1 $ENS); do
	    imem=$(printf "%03d" $imem)
	    enslist="$enslist $SUBDIR_NAME${imem}/PP_${EXPS}+00$step "
	done
	
	# Calculate ensemble mean
	cdo -ensmean ${enslist} PP_ensmean+00$step
	
	# Calculate ensemble stdev
	cdo -ensstd ${enslist} PP_ensstd+00$step

	rfile=/wrk/lautuppi/playground/${an_date}_an_pl.grb
	echo '*****************************************'
        echo $time $AN_STEP
	echo $rfile
	echo ${enslist}
	echo '*****************************************'
        cdo enscrps,$ENS $rfile ${enslist} obase.enscrps_$step.txt

	# Copy the ctrl pp to date-folder
	cp -f ${SUBDIR_NAME}000/PP_${EXPS}+00${step} PP_ctrl+00$step


    done
fi
