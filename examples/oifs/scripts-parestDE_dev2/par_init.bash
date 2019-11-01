#!/bin/bash
#
# Initialize DE routine
#
#module purge
module load python/3.5.3-gnu620
#module load biopython-env/3.4.5

# link DE
ln -sf $EPPES_EXE $DATA/eppes/DEroutine.py

printf "%s\n" "0.5        6.0" > $DATA/eppes/boundary.dat
printf "%s\n" "0.0001     0.01" >> $DATA/eppes/boundary.dat
#printf "%s\n" "0.00125    0.00225" >> $DATA/eppes/boundary.dat

printf "%s\n" "0" > $DATA/eppes/log.dat

cat > $DATA/eppes/DE.cfg <<EOF
[files]
cur_pop_file = cur_pop.dat
cur_score_file = cur_score.dat
trial_pop_file = sampleout.dat
trial_score_file = score.dat
log_file = log.dat
boundary_file = boundary.dat

[DEparams]
size_of_pop = $ENS
F = 0.5
CR = 0.9
JP = 0.1
mutation_type = 2
scale_factor_type = 5
F_l =  0.5
F_u = 1.0
pop_function = positive
Jttr = 0.01
EOF

# run sampleonly
pushd $DATA/eppes > /dev/null
python DEroutine.py DE.cfg


# change nml to production
#cp -f eppes_run.cfg eppes.cfg

# store init values
mkdir -p init
#for item in mu sig n w; do
for item in sampleout mufile sigfile; do
    cp -f ${item}.dat init/.
done
#cp sampleout.dat init/.

popd > /dev/null

# kokeile:
# JP = 0.0, default=0.1		-> parest_conv_MTEN_dec2016-feb2017_DE_5_x1 # ei auta
# mutation_type = 0, default=2	-> parest_conv_MTEN_dec2016-feb2017_DE_5_x2 #ei toimi
# mutation_type = 1, default=2	-> parest_conv_MTEN_dec2016-feb2017_DE_5_x3 # ~OK
# F_u = 1.1, default=1.0	-> parest_conv_MTEN_dec2016-feb2017_DE_5_x4 # ~OK
# recalculation every 4th iter.	-> parest_conv_MTEN_dec2016-feb2017_DE_5_x5 # ~OK, paras?
