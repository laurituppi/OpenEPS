#!/bin/bash

# Get process id 
nid=$(pwd | grep -o -P "$SUBDIR_NAME.{0,5}" | sed -e "s/$SUBDIR_NAME//g")

# Log
echo `date +%H:%M:%S` parwrite $SUBDIR_NAME${nid} >> $WORK/master.log

# Parameter perturbations
#
if [ $NUMBER_OF_PARS -eq 2 ]; then
  if [ $nid -gt 0 ]; then
      #read par1 < par_values
      par1=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -c 1-24)
      par2=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -c 26-50)
    
      echo "Using par1 value $par1 and par2 value $par2" > parfile
      #echo "using par1 value 2.096 and par2 value 1.67e-03" > parfile

      # Write new parameter values to namelist here
      sed -i -e "s#ENTSHALP=.*#ENTSHALP=$par1,#g" fort.4
#      sed -i -e "s#ENTRORG=.*#ENTRORG=$par2,#g" fort.4
      #sed -i -e "s#ENTSHALP=.*#ENTSHALP=2.096,#g" fort.4
      #sed -i -e "s#ENTRORG=.*#ENTRORG=1.67e-03,#g" fort.4
  else
      echo "Ctrl run" > parfile

      # Delete the line from ctrl
      sed -i -e "s#ENTSHALP=2.0,##g" fort.4
      sed -i -e "s#ENTRORG=1.75E-03,##g" fort.4
      sed -i -e "s#DETRPEN=0.75E-04,##g" fort.4
      sed -i -e "s#RPRCON=0.0014,##g" fort.4
      sed -i -e "s#RDEPTHS=20000.0,##g" fort.4

  fi
fi

if [ $NUMBER_OF_PARS -eq 5 ]; then # this is for 5 parameter convergence/optimization tests
suffix='E+04'
rcalc() { awk "BEGIN{print $*}"; }
  if [ $nid -gt 0 ]; then
      #read par1 < par_values
      par1=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 1)
      par2=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 2)
      par3=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 3)
      par4=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 4)
      par5a=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 5)
      #par5=${par5a}${suffix}
      par5=$(rcalc $par5a*10000)
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
      sed -i -e "s#DETRPEN=0.75E-4,##g" fort.4
      sed -i -e "s#RPRCON=1.4E-03,##g" fort.4
      sed -i -e "s#RDEPTHS=20000.0,##g" fort.4
  fi
fi

if [ $NUMBER_OF_PARS -eq 8 ]; then # this is for 8 parameter convergence/optimization tests
suffix='E+04'
rcalc() { awk "BEGIN{print $*}"; }
  if [ $nid -gt 0 ]; then
      #read par1 < par_values
      par1=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 1)
      par2=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 2)
      par3=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 3)
      par4=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 4)
      par5a=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 5)
      par6=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 6)
      par7=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 7)
      par8=$(sed "${nid}q;d" $DATA/eppes/sampleout.dat | cut -d ' ' -f 8)
      #par5=${par5a}${suffix}
      par5=$(rcalc $par5a*10000)
      echo "Using parameters: par1=$par1, par2=$par2, par3=$par3, par4=$par4, par5=$par5" > parfile
      sed -i -e "s#ENTSHALP=.*#ENTSHALP=$par1,#g" fort.4
      sed -i -e "s#ENTRORG=.*#ENTRORG=$par2,#g" fort.4
      sed -i -e "s#DETRPEN=.*#DETRPEN=$par3,#g" fort.4
      sed -i -e "s#RPRCON=.*#RPRCON=$par4,#g" fort.4
      sed -i -e "s#RDEPTHS=.*#RDEPTHS=$par5,#g" fort.4
      sed -i -e "s#RMFDEPS=.*#RMFDEPS=$par6,#g" fort.4
      sed -i -e "s#RHEBC=.*#RHEBC=$par7,#g" fort.4
      sed -i -e "s#ENTRDD=.*#ENTRDD=$par8,#g" fort.4
  else
      echo "Ctrl run" > parfile
      # Delete the line from ctrl
      sed -i -e "s#ENTSHALP=2.0,##g" fort.4
      sed -i -e "s#ENTRORG=1.75E-03,##g" fort.4
      sed -i -e "s#DETRPEN=0.75E-4,##g" fort.4
      sed -i -e "s#RPRCON=1.4E-03,##g" fort.4
      sed -i -e "s#RDEPTHS=20000.0,##g" fort.4
      sed -i -e "s#RMFDEPS=3600,##g" fort.4
      sed -i -e "s#RHEBC=0.05,##g" fort.4
      sed -i -e "s#ENTRDD=0.0003,##g" fort.4
  fi
fi
