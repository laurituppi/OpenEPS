#!/bin/bash
module load climateutils
rfile=/wrk/lautuppi/playground/2016120106_an_pl.grb
#rfile=/wrk/lautuppi/openEPS/EPS_crps/data/2016120100/pert000/PP_eps2+000006
a=/wrk/lautuppi/openEPS/EPS_crps/data/2016120100/pert001/PP_eps2+000006
b=/wrk/lautuppi/openEPS/EPS_crps/data/2016120100/pert002/PP_eps2+000006
c=/wrk/lautuppi/openEPS/EPS_crps/data/2016120100/pert003/PP_eps2+000006

cdo enscrps $rfile $a $b $c enscrps_test
