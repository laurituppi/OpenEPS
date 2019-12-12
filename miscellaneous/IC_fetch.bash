#!/bin/bash

res=t159
sdate=2016120800
edate=2016120800 #2017113012
dstep=168
calendar=$HOME/OpenEPS/bin/mandtg

cd /scratch/project_2001011/OIFS_INI

test -d $res || mkdir $res

cd $res

for ((i=0; i<=1000; i=i+1)) do

  cdate=`exec $calendar $sdate + $(($i*$dstep))`

  a-get oifs-$res/${cdate}.tgz
  tar -zxvf ${cdate}.tgz
  rm ${cdate}.tgz

  if [ "$cdate" -eq "$edate" ] ; then
    exit
  fi

done
