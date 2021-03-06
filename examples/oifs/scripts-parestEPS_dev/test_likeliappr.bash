#!/bin/bash
#start=$SECONDS
# ---------------------------------- Arguments ------------------------------------
work=$WRKDIR/likelihood						# directory where the cost function is calculated
#analysis=/wrk/ollinaho/public/analysis_pl_t159_2018aug.nc 	# analysis file
analysis=$work/analysis_pl_t159_2018aug.nc
ENS=5 								# size of ens forecast, must be at least 2
c=4 								# number of random columns
hour=96 							# forecast time
# ---------------------------------------------------------------------------------

#rm -rf $work/pert*						# remove old stuff
rm -f tmp_analysis.nc

module load cdo

cdo seltimestep,$(($hour/6)) $analysis $work/tmp_analysis.nc	# select correct timestep from analysis
a=$work/tmp_analysis.nc

declare -a ens_members						# initialize array for the ensemble members
for i in $(seq 1 $ENS); do
    imem=$(printf "%03d" $i)					# add digits to member number
    time=$(printf "%06d" $hour)					# and to time
    #mkdir $work/pert$imem
    #cdo -t ecmwf -f nc -R copy /wrk/ollinaho/public/oeps_fcs/pert$imem/PP_inio+$time $work/pert$imem/PP_inio+${time}.nc # grib to nc
    #cdo -sp2gpl $work/pert$imem/ICMSHinio+${time} $work/pert$imem/PP_inio+${time}
    #cdo -t ecmwf -f nc -R copy $work/pert$imem/PP_inio+${time} $work/pert$imem/PP_inio+${time}.nc
    ens_members[$i]=$work/pert$imem/PP_inio+${time}.nc		# wrap the members into array
done

module load python-env/2.7.10

#echo $a $ENS $c ${array[*]}
python likeliappr_v3.py $a $ENS $c ${ens_members[*]}		# the cost function

#duration=$(( SECONDS - start ))
#echo 'Running took ' $duration ' seconds'
