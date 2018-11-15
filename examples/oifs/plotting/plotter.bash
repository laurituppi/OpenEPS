#!/bin/bash

module load python/2.7.13-gnu620
export XDG_RUNTIME_DIR=/tmp/lautuppi/runtime-lautuppi

ndays=63
npars=2
nens=20
inputdir=/wrk/lautuppi/openEPS/parest_conv_MTEN_jan2017_DE/data/eppes/eppesdata/
outputdir=/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/
default_value_1=2.0
default_value_2=0.00175

python plot-pars-3_DE.py ${ndays} ${npars} ${nens} ${inputdir} ${outputdir} ${default_value_1} ${default_value_2}
