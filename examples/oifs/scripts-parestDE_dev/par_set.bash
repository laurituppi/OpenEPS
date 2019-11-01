#!/bin/bash

# Get process id 
nid=$(pwd | grep -o -P "$SUBDIR_NAME.{0,5}" | sed -e "s/$SUBDIR_NAME//g")

# Log
echo `date +%H:%M:%S` parwrite $SUBDIR_NAME${nid} >> $WORK/master.log

# Parameter perturbations
#
if [ 0 -eq 1 ]; then # this is for benchmarking the cost function
  par1=2.0
  par2=0.00175
  echo "Using par1 value $par1 and par2 value $par2" > parfile
  sed -i -e "s#ENTSHALP=.*#ENTSHALP=$par1,#g" fort.4
  sed -i -e "s#ENTRORG=.*#ENTRORG=$par2,#g" fort.4
fi

if [ 1 -eq 1 ]; then # this is for two parameter convergence/optimization tests
  if [ $nid -gt 0 ]; then
      #read par1 < par_values
      par1=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 1)
      par2=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 2)
    
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
      sed -i -e "s#DETRPEN=0.00075,##g" fort.4
      sed -i -e "s#RPRCON=0.0014,##g" fort.4
      sed -i -e "s#RDEPTHS=20000.0,##g" fort.4
  fi
fi

if [ 0 -eq 1 ]; then # this is for 5 parameter convergence/optimization tests
  if [ $nid -gt 0 ]; then
      #read par1 < par_values
      par1=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 1)
      par2=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 2)
      par3=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 3)
      par4=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 4)
      par5=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 5)
      echo "Using parameters: par1=$par1, par2=$par2, par3=$par3, par4=$par4, par5=$par5" > parfile
      sed -i -e "s#ENTSHALP=.*#ENTSHALP=$par1,#g" fort.4
      sed -i -e "s#ENTRORG=.*#ENTRORG=$par2,#g" fort.4
      sed -i -e "s#DETRPEN=.*#DETRPEN=$par3,#g" fort.4
      sed -i -e "s#RPRCON=.*#RPRCON=$par4,#g" fort.4
      sed -i -e "s#RDEPTHS=.*#RDEPTHS=$par5,#g" fort.4
  else
      echo "Ctrl run" > parfile
      # Delete the line from ctrl
      sed -i -e "s#ENTSHALP=2.0,##g" fort.4
      sed -i -e "s#ENTRORG=1.75E-03,##g" fort.4
      sed -i -e "s#DETRPEN=0.00075,##g" fort.4
      sed -i -e "s#RPRCON=0.0014,##g" fort.4
      sed -i -e "s#RDEPTHS=20000.0,##g" fort.4
  fi
fi
