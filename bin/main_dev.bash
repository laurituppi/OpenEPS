#!/bin/bash

# A script to run an ensemble of models for N-dates.
# Additional tasks can be set for each date by modifying the
# makefile generation (define_makefile.bash and write_makefile.bash)
#

# Stop execution in case of error. More specifically, stop if the last
# command of the line does not return zero.
#
set -e
printf "\n\n4) Now in main.bash\n"


# Set program source, work directories and available resources
#
source configs/exp.*
source configs/env.*
source configs/resources

# Additional make-tasks
if [ ! -z $EXTRA_TASKS ]; then
  EXTRA_TASKS=0
fi

# Loop over dates
#
export cdate ndate
cdate=$SDATE
number_of_ensemble=0

if [ ! -e $DATA/Makefile ]; then
    while [ $cdate -le $EDATE ]; do
        export number_of_ensemble
        
	cd $DATA/$cdate
	# Log
	printf "\nRunning ens for $cdate\n"   >> $WORK/master.log
	echo `date +%H:%M:%S` init            >> $WORK/master.log
	printf "   Processing date $cdate "

	# Ens numbering
	number_of_ensemble=$((number_of_ensemble+1))
	
	# Define next date
	ndate=`exec $WORK/./mandtg $cdate + $DSTEP`
    
	# Let make take over
	if [ $VERBOSE -eq 1 ]; then
	    make    -f makefile_$cdate -j $(( PARALLELS_IN_NODE * PARALLEL_NODES + EXTRA_TASKS ))
	else
	    make -s -f makefile_$cdate -j $(( PARALLELS_IN_NODE * PARALLEL_NODES + EXTRA_TASKS )) > /dev/null 2>&1
	fi
	    

	cdate=$ndate
	printf "\n"
    done
else
    cd $DATA
    make -j $PARALLELS_IN_NODE
fi
    
set +e

printf "\n\nOpenEPS finished \n"
exit 1
