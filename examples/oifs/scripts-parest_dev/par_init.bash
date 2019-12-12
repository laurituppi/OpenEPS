#!/bin/bash
#
# Initialize EPPES routine
#
if [ "$HOST"=="taito" ]; then
  #module load python-env/2.7.10
  #module load biopython-env
  export CONDA_ENVS_PATH=/projappl/project_2001011/puhti_conda_envs
  source /appl/soft/bio/bioconda/miniconda3/etc/profile.d/conda.sh
  conda activate eppes_python_3
elif [ "$HOST"=="sisu" ]; then
  module load python/2.7.13-gnu620
fi

# link eppes
#ln -sf $EPPES_EXE $DATA/eppes/eppes_routine
ln -sf $EPPES_EXE $DATA/eppes/eppesroutine.py

if [ $NUMBER_OF_PARS -eq 2 ]; then
  #mufile----------------------------------------------------------------
  #printf "%s\n" "2.0" > $DATA/eppes/mufile.dat
  printf "%s\n" "2.2" > $DATA/eppes/mufile.dat
  #printf "%s\n" "2.512960270963074283e+00" > $DATA/eppes/mufile.dat

  printf "%s\n" "1.75E-03" >> $DATA/eppes/mufile.dat
  #printf "%s\n" "1.925E-03" >> $DATA/eppes/mufile.dat
  #printf "%s\n" "2.266698515809868492e-03" >> $DATA/eppes/mufile.dat

  #sigfile---------------------------------------------------------------

  # 1 parameter
  #printf "%s\n" "1.40625E-07" > $DATA/eppes/sigfile.dat

  # 2 parameters
  #printf "%s\n" "1.0E-15        0.0" > $DATA/eppes/sigfile.dat
  printf "%s\n" "0.5625        0.0" > $DATA/eppes/sigfile.dat #oikea
  printf "%s\n" "0.0        1.40625E-15" >> $DATA/eppes/sigfile.dat 
  #printf "%s\n" "0.0        1.40625E-07" >> $DATA/eppes/sigfile.dat #oikea
  #printf "%s\n" "0.0         1.5625E-08" >> $DATA/eppes/sigfile.dat

  #printf "%s\n" "4.010529215980582762e-01 7.475014405629379084e-05" > $DATA/eppes/sigfile.dat
  #printf "%s\n" "7.475014405629379084e-05 6.765582912005412036e-07" >> $DATA/eppes/sigfile.dat

  #bounds----------------------------------------------------------------
  printf "%s\n" "0.5        6.0" > $DATA/eppes/bounds.dat
  printf "%s\n" "1.0E-04   2.0E-02" >> $DATA/eppes/bounds.dat

  #nfile ----------------------------------------------------------------
  printf "%s\n" "5" > $DATA/eppes/nfile.dat
  #printf "%s\n" "2.0" >> $DATA/eppes/nfile.dat

  #wfile ----------------------------------------------------------------

  # 1 parameter
  printf "%s\n" "1" > $DATA/eppes/wfile.dat

  # 2 parameters
  printf "%s\n" "1        0" > $DATA/eppes/wfile.dat
  printf "%s\n" "0        1" >> $DATA/eppes/wfile.dat

  # maxstep--------------------------------------------------------------
  printf "%s\n" "0.05" > $DATA/eppes/maxstep.dat
fi

if [ $NUMBER_OF_PARS -eq 5 ]; then

  a=1.1
  b=0.9

  default1=2.0 # ENTSHALP
  default2=0.00175 # ENTRORG
  default3=0.000075 # DETRPEN
  default4=0.0014 # RPRCON
  default5=2.0 # RDEPTHS #oikeasti 20000, ks. par_set.bash
  rcalc() { awk "BEGIN{print $*}"; }
  mean1=$(rcalc $default1*$a)
  mean2=$(rcalc $default2*$a)
  mean3=$(rcalc $default3*$a)
  mean4=$(rcalc $default4*$a)
  mean5=$(rcalc $default5*$a)
  printf "%s\n" "$mean1" > $DATA/eppes/mufile.dat
  printf "%s\n" "$mean2" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean3" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean4" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean5" >> $DATA/eppes/mufile.dat

  printf "%s\n" "0.5625    0.0          0.0        0.0         0.0" > $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       1.40625E-07  0.0        0.0         0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          2.25E-10   0.0         0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          0.0        7.84E-08    0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          0.0        0.0         0.16" >> $DATA/eppes/sigfile.dat #0.16E+08

  printf "%s\n" "0.5        6.0" > $DATA/eppes/bounds.dat
  printf "%s\n" "1.0E-04   1.0E-02" >> $DATA/eppes/bounds.dat
  printf "%s\n" "1.0E-05   1.0E-03" >> $DATA/eppes/bounds.dat
  printf "%s\n" "1.0E-04   1.0E-02" >> $DATA/eppes/bounds.dat
  printf "%s\n" "0.1       6.0" >> $DATA/eppes/bounds.dat

  printf "%s\n" "1        0        0        0        0" > $DATA/eppes/wfile.dat
  printf "%s\n" "0        1        0        0        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        1        0        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        0        1        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        0        0        1" >> $DATA/eppes/wfile.dat

  printf "%s\n" "5" > $DATA/eppes/nfile.dat

  printf "%s\n" "0.05" > $DATA/eppes/maxstep.dat
fi

if [ $NUMBER_OF_PARS -eq 8 ]; then

  a=1.1
  b=0.9

  default1=2.0 # ENTSHALP
  default2=0.00175 # ENTRORG
  default3=0.000075 # DETRPEN
  default4=0.0014 # RPRCON
  default5=2.0 # RDEPTHS #oikeasti 20000, ks. par_set.bash
  default6=0.3 # RMFDEPS
  default7=0.9 # RHEBC
  default8=0.0003 # ENTRDD
  rcalc() { awk "BEGIN{print $*}"; }
  mean1=$(rcalc $default1*$a)
  mean2=$(rcalc $default2*$b)
  mean3=$(rcalc $default3*$a)
  mean4=$(rcalc $default4*$b)
  mean5=$(rcalc $default5*$a)
  mean6=$(rcalc $default6*$a)
  mean7=$(rcalc $default7*$b)
  mean8=$(rcalc $default8*$b)
  printf "%s\n" "$mean1" > $DATA/eppes/mufile.dat
  printf "%s\n" "$mean2" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean3" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean4" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean5" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean6" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean7" >> $DATA/eppes/mufile.dat
  printf "%s\n" "$mean8" >> $DATA/eppes/mufile.dat

  printf "%s\n" "0.5625    0.0          0.0        0.0         0.0        0.0         0.0        0.0" > $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       1.40625E-07  0.0        0.0         0.0        0.0         0.0        0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          2.25E-10   0.0         0.0        0.0         0.0        0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          0.0        7.84E-08    0.0        0.0         0.0        0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          0.0        0.0         0.16       0.0         0.0        0.0" >> $DATA/eppes/sigfile.dat #0.16E+08
  printf "%s\n" "0.0       0.0          0.0        0.0         0.0        0.08        0.0        0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          0.0        0.0         0.0        0.0         0.01       0.0" >> $DATA/eppes/sigfile.dat
  printf "%s\n" "0.0       0.0          0.0        0.0         0.0        0.0         0.0        0.65E-09" >> $DATA/eppes/sigfile.dat

  printf "%s\n" "0.5        6.0" > $DATA/eppes/bounds.dat
  printf "%s\n" "1.0E-04   1.0E-02" >> $DATA/eppes/bounds.dat
  printf "%s\n" "1.0E-05   1.0E-03" >> $DATA/eppes/bounds.dat
  printf "%s\n" "1.0E-04   1.0E-02" >> $DATA/eppes/bounds.dat
  printf "%s\n" "0.1       6.0" >> $DATA/eppes/bounds.dat
  printf "%s\n" "0.1       0.7" >> $DATA/eppes/bounds.dat
  printf "%s\n" "0.5       1.0" >> $DATA/eppes/bounds.dat
  printf "%s\n" "0.00003   0.003" >> $DATA/eppes/bounds.dat

  printf "%s\n" "1        0        0        0        0        0        0        0" > $DATA/eppes/wfile.dat
  printf "%s\n" "0        1        0        0        0        0        0        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        1        0        0        0        0        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        0        1        0        0        0        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        0        0        1        0        0        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        0        0        0        1        0        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        0        0        0        0        1        0" >> $DATA/eppes/wfile.dat
  printf "%s\n" "0        0        0        0        0        0        0        1" >> $DATA/eppes/wfile.dat

  printf "%s\n" "5" > $DATA/eppes/nfile.dat

  printf "%s\n" "0.05" > $DATA/eppes/maxstep.dat
fi
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
maxn = 5
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
maxn = 5
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

