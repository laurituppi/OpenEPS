#!/bin/bash

nens=${1?} #6
fclen=${2?}  #12
optimizer=${3?} #DE
repetition=${4?} #2
dir=${nens}mem_${fclen}h_$repetition
eppesdir=/wrk/lautuppi/openEPS/publ_conv_tests/$optimizer/level2/$dir/data/eppes/eppesdata
mkdir $eppesdir
mv /wrk/lautuppi/openEPS/publ_conv_tests/$optimizer/level2/$dir/data/eppes/201* $eppesdir
mkdir /wrk/lautuppi/DONOTREMOVE/publ_conv_tests/$optimizer/level2/$dir
mv $eppesdir /wrk/lautuppi/DONOTREMOVE/publ_conv_tests/$optimizer/level2/$dir
