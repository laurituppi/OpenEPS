#!/bin/bash
#
# Initialize EPPES routine
#
#module load python-env/2.7.10
#module load biopython-env
module load python/2.7.13-gnu620

# link eppes
#ln -sf $EPPES_EXE $DATA/eppes/eppes_routine
ln -sf $EPPES_EXE $DATA/eppes/eppesroutine.py

#mufile----------------------------------------------------------------
#printf "%s\n" "2.0" > $DATA/eppes/mufile.dat
printf "%s\n" "2.2" > $DATA/eppes/mufile.dat
#printf "%s\n" "2.512960270963074283e+00" > $DATA/eppes/mufile.dat

#printf "%s\n" "1.75E-03" >> $DATA/eppes/mufile.dat
printf "%s\n" "1.925E-03" >> $DATA/eppes/mufile.dat
#printf "%s\n" "2.266698515809868492e-03" >> $DATA/eppes/mufile.dat

#sigfile---------------------------------------------------------------

# 1 parameter
#printf "%s\n" "0.7" > $DATA/eppes/sigfile.dat

# 2 parameters
printf "%s\n" "0.7        0.0" > $DATA/eppes/sigfile.dat
printf "%s\n" "0.0        1.2E-06" >> $DATA/eppes/sigfile.dat

#printf "%s\n" "4.010529215980582762e-01 7.475014405629379084e-05" > $DATA/eppes/sigfile.dat
#printf "%s\n" "7.475014405629379084e-05 6.765582912005412036e-07" >> $DATA/eppes/sigfile.dat

#bounds----------------------------------------------------------------
printf "%s\n" "0.5        6.0" > $DATA/eppes/bounds.dat
printf "%s\n" "1.0E-04   1.0E-02" >> $DATA/eppes/bounds.dat

#nfile ----------------------------------------------------------------
printf "%s\n" "3" > $DATA/eppes/nfile.dat
#printf "%s\n" "2.0" >> $DATA/eppes/nfile.dat

#wfile ----------------------------------------------------------------

# 1 parameter
#printf "%s\n" "1" > $DATA/eppes/wfile.dat

# 2 parameters
printf "%s\n" "1        0" > $DATA/eppes/wfile.dat
printf "%s\n" "0        1" >> $DATA/eppes/wfile.dat

# maxstep--------------------------------------------------------------
printf "%s\n" "0.05" > $DATA/eppes/maxstep.dat

# ! THIS IS A LOT SIMPLER TO JUST DO BY HAND,
# ! RETHINK IF THIS WOULD BE WORTH IT

if [ 1 -eq 0 ]; then
# Params (mu, sig, lower bound, upper bound)
# ENTSHALP
PAR1=(2.0 0.4 0.5 4.0)
PAR2=(1.0 0.2 0.1 2.0)

ipar=1
mu=()
sig=()
bnd=()
n=()
w=()

while [ 1 ]; do
    temp=PAR$ipar[@]
    tmp2=PAR$ipar[0]
    if [ ! -z ${!tmp2} ]; then	
	# Un- and reroll array
	par=()
	for iatt in ${!temp}; do
	    par+=($iatt)
	done

	# mufile
	mu+=(${par[0]})

	# sigfile
	sig+=(${par[1]})

	# bounds
	bnd+=("${par[2]} ${par[3]}")

	
	(( ipar += 1 ))
    else
	echo $ipar
	break
    fi
done

# Write out necessary files
#
rm -f $DATA/eppes/mufile.dat $DATA/eppes/bounds.dat $DATA/eppes/sigfile.dat

# loop over pars
lead=0
trail=$(( ${#mu[@]} - 1))
aa='"%s %s %s \n"'
for ipar in $(seq 0 $(( ${#mu[@]} - 1)) ); do
    printf "%s\n"    ${mu[$ipar]}  >> $DATA/eppes/mufile.dat
    printf "%s %s\n" ${bnd[$ipar]} >> $DATA/eppes/bounds.dat

    printf $aa $lead ${sig[$ipar]} $trail >> $DATA/eppes/sigfile.dat
    
    (( lead += 1 ))
    (( trail += 1 ))
done
fi

# eppes sampleonly namelist
#cat > $DATA/eppes/eppesconf_init.nml <<EOF
#&eppesconf
# sampleonly = 1
# nsample    = $ENS
# maxn0 = 10
# mufile    = 'mufile.dat'
# sigfile   = 'sigfile.dat'
# wfile     = 'wfile.dat'
# nfile     = 'nfile.dat'
# sampleout = 'sampleout.dat'
# boundsfile = 'bounds.dat'
#/
#EOF
cat > $DATA/eppes/eppes_init.cfg <<EOF
[files]
mufile = mufile.dat
wfile = wfile.dat
sigfile = sigfile.dat
nfile = nfile.dat
scorefile = scores.dat
samplein = oldsample.dat
sampleout = sampleout.dat
boundsfile = bounds.dat
winfofile = winfo.dat
maxstepfile = maxstep.dat

[options]
sampleonly = 1
verbosity = 1
nsample = $ENS
maxn = 3
lognor = 0
useranks = 1
EOF

# eppes update namelist
#cat > $DATA/eppes/eppesconf_run.nml <<EOF
#&eppesconf
# sampleonly = 0
# nsample    = $ENS
# maxn0 = 10
# mufile    = 'mufile.dat'
# sigfile   = 'sigfile.dat'
# wfile     = 'wfile.dat'
# nfile     = 'nfile.dat'
# samplein  = 'oldsample.dat'
# sampleout = 'sampleout.dat'
# scorefile = 'scores.dat'
# boundsfile = 'bounds.dat'
# winfofile = 'winfo.dat'
# combine_method = 'amean'
#/
#EOF
cat > $DATA/eppes/eppes_run.cfg <<EOF
[files]
mufile = mufile.dat
wfile = wfile.dat
sigfile = sigfile.dat
nfile = nfile.dat
scorefile = scores.dat
samplein = oldsample.dat
sampleout = sampleout.dat
boundsfile = bounds.dat
winfofile = winfo.dat
maxstepfile = maxstep.dat

[options]
sampleonly = 0
verbosity = 1
nsample = $ENS
maxn = 3
lognor = 0
useranks = 1
combine_method = amean
EOF



# run sampleonly
pushd $DATA/eppes > /dev/null
cp -f eppes_init.cfg eppes.cfg
python eppesroutine.py eppes.cfg


# change nml to production
cp -f eppes_run.cfg eppes.cfg

# store init values
mkdir -p init
for item in mu sig n w; do
    cp ${item}file.dat init/.
done
cp sampleout.dat init/.

popd > /dev/null

