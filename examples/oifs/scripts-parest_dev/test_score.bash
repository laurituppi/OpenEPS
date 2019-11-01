#!/bin/bash

module load bioconda
source activate /wrk/lautuppi/DONOTREMOVE/sisu-conda-envs/eppes
module load python/2.7.13-gnu620

forecast_SH=/wrk/lautuppi/openEPS/test_rmse/data/2016120100/pert001/PPSH_ep00+000048.nc
reference_SH=/wrk/lautuppi/openEPS/test_rmse/data/2016120100/pert000/PPSH_ep00+000048.nc
out=/homeappl/home/lautuppi/appl_sisu/OpenEPS/examples/oifs/scripts-parest_dev

python RMSE_z.py $forecast_SH $reference_SH $out
