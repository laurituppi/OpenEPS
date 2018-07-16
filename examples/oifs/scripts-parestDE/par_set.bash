#!/bin/bash

# Get process id 
nid=$(pwd | grep -o -P "$SUBDIR_NAME.{0,5}" | sed -e "s/$SUBDIR_NAME//g")

# Log
echo `date +%H:%M:%S` parwrite $SUBDIR_NAME${nid} >> $WORK/master.log

# Parameter perturbations
#
if [ $nid -gt 0 ]; then
    #read par1 < par_values
    par1=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -c 1-24)
    par2=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -c 26-50)
    
    echo "Using par1 value $par1 and par2 value $par2" > parfile
    # Write new parameter values to namelist here
    sed -i -e "s#ENTSHALP=.*#ENTSHALP=$par1,#g" fort.4
    sed -i -e "s#ENTRORG=.*#ENTRORG=$par2,#g" fort.4
     #1.775835354797680399e+00
     #8.558111404166759495e-04
    #sed -i -e "s#ENTSHALP=.*#ENTSHALP=1.775835354797680399e+00,#g" fort.4
    #sed -i -e "s#ENTRORG=.*#ENTRORG=8.558111404166759495e-04,#g" fort.4
else
    echo "Ctrl run" > parfile

    # Delete the line from ctrl
    sed -i -e "s#ENTSHALP=2.0,##g" fort.4
    sed -i -e "s#ENTRORG=1.75E-03,##g" fort.4
fi


