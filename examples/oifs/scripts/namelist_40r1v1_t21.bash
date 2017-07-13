#!/bin/bash
#
# Create a namelist
#

if [ $imem -eq 0 ]; then
    name="ctrl"
else
    name=$(printf "%s%03d" $SUBDIR_NAME $imem)
fi
    
cat <<EOF > $SCRI/namelist.$name
&NAMDIM
NPROMA=-24,
/
&NAMGFL
YQ_NL%LGP=true,
YQ_NL%LSP=false,
YO3_NL%LGP=false,
YQ_NL%LGPINGP=true,
YR_NL%NREQIN=-1,
YS_NL%NREQIN=-1,
/
&NAMPAR0
  LSTATS=.TRUE.,
  LDETAILED_STATS=.FALSE.,
  LSYNCSTATS=.false.,
  MP_TYPE=2,
  MBX_SIZE=32000000,
  NPROC=$NPROC,
  NOUTPUT=1,
/   
&NAMCT0
 NFPOS=2,
 LREFOUT=false,
 N3DINI=0,
 NSTOP=$NSTOP,
 NFRDHP=1,
 NFRDHFD=1,
 NFRHIS=$NFRHIS,
 NFRPOS=$NFRPOS,
 NPOSTS=$NPOSTS,
 NHISTS=$NHISTS,
 CTYPE="$CTYPE",
 NFRSDI=1, 
 LSLAG=true,
 LSLPHY=.false.,
 LSLPHY=.true.,
/  
&NAMCVER
  LVERTFE=false,
/  
&NAMPAR1
  LSPLIT=true,
  NFLDIN=0,
  NSTRIN=1,
  NSTROUT=0,
  NOUTTYPE=1,
  LPPTSF=false,
  NPPBUFLEN=100000,
/   
&NAMRIP
  NINDAT=19970115,
  NSSSSS=43200,
/   
&NAMDYN
 TSTEP=$TSTEP,
/
&NAEPHY
 LEPHYS=true,
 LERADI=true,
 LELAIV=false,
 LBUD23=false,
/   
&NAERAD
 NRPROMA=-24,
 CRTABLEDIR="/home/user/oifs/ifsdata/rtable/", ! modify this for your installation
/   
&NAMGEM
  NHTYP=0,
/   
&NAMDPHYDS
/
&NAMDDH
 BDEDDH(1:6,1)=4.0,1.0,0.0,50.0,0.0,49.0,
 NDHKD=120,
 LHDZON=false,
 LHDEFZ=false,
 LHDDOP=false,
 LHDEFD=false,
 LHDGLB=true,
 LHDPRG=true,
 LHDHKS=true,
/   
&NAMNMI
 LNMIRQ=false,
 LASSI=false,
/   
&NAMAFN
  TFP_FUA(1)%LLGP=.false.,
/   
&NAMRES
  NFRRES=9999,
/   
&NAMFPC
    CFPFMT='MODEL',
    NFP3DFS=$NFP3DFS,
    MFP3DFS(1:)=$MFP3DFS,
    NRFP3S=$NRFP3S,
    NFP2DF=$NFP2DF,
    MFP2DF=$MFP2DF,
    NFP3DFP=$NFP3DFP,
    MFP3DFP=$MFP3DFP,
    RFP3P(1:)=$RFP3P,
    NFPPHY=$NFPPHY,
    MFPPHY(1:)=$MFPPHY,
/
$NAMGRIB
$NAMSPSDT
$NAMSTOPH
$NAMCUMF
&NAEAER
/
&NAEPHY
/
&NAERAD
/
&NALBAR
/
&NALORI
/
&NAM_DISTRIBUTED_VECTORS
/
&NAM926
/
&NAMAFN
/
&NAMANA
/
&NAMARPHY
/
&NAMCA
/
&NAMCAPE
/
&NAMCFU
/
&NAMCHK
/
&NAMCHET
/
&NAMCLDP
/
&NAMCLTC
/
&NAMCOM
/
&NAMCOS
/
&NAMCTAN
/
&NAMCUMF
/
&NAMCUMFS
/
&NAMCT1
/
&NAMCVA
/
&NAMDDH
/
&NAMDFHD
/
&NAMDFI
/
&NAMDIF
/
&NAMDIM
/
&NAMDIMO
/
&NAMDMSP
/
&NAMDPHY
/
&NAMDYN
/
&NAMDYNA
/
&NAMDYNCORE
/
&NAMEMIS_CONF
/
&NAMENKF
/
&NAMFA
/
&NAMFFT
/
&NAMFPC
/
&NAMFPD
/
&NAMFPDY2
/
&NAMFPDYH
/
&NAMFPDYP
/
&NAMFPDYS
/
&NAMFPDYT
/
&NAMFPDYV
/
&NAMFPEZO
/
&NAMFPF
/
&NAMFPG
/
&NAMFPIOS
/
&NAMFPPHY
/
&NAMFPSC2
/
&NAMFPSC2_DEP
/
&NAMFY2
/
&NAMGEM
/
&NAMGFL
/
&NAMGMS
/
&NAMGOES
/
&NAMGOM
/
&NAMGRIB
/
&NAMGWD
/
&NAMGWWMS
/
&NAMHLOPT
/
&NAMINI
/
&NAMIOMI
/
&NAMIOS
/
&NAMJBCODES
/
&NAMJFH
/
&NAMJG
/
&NAMJO
/
&NAMKAP
/
&NAMLCZ
/
&NAMLEG
/
&NAMLFI
/
&NAMMCC
/
&NAMMCUF
/
&NAMMETEOSAT
/
&NAMMTS
/
&NAMMTSAT
/
&NAMMTT
/
&NAMMUL
/
&NAMNMI
/
&NAMNASA
/
&NAMNN
/
&NAMNPROF
/
&NAMNUD
/
&NAMOBS
/
&NAMONEDVAR
/
&NAMOPH
/
&NAMOPTCMEM
/
&NAMPAR0
/
&NAMPARAR
/
&NAMPAR1
/
&NAMPHY
/
&NAMPHY0
/
&NAMPHY1
/
&NAMPHY2
/
&NAMPHY3
/
&NAMPHYDS
/
&NAMPPC
/
&NAMPONG
/
&NAMRAD15
/
&NAMRADCMEM
/
&NAMRCOEF
/
&NAMRES
/
&NAMRINC
/
&NAMRIP
/
&NAMSATS
/
&NAMSCC
/
&NAMSCEN
/
&NAMSCM
/
&NAMSENS
/
&NAMSIMPHL
/
&NAMSKF
/
&NAMSPSDT
/
&NAMSSMI
/
&NAMSTA
/
&NAMSTOPH
/
&NAMTCWV
/
&NAMTESTVAR
/
&NAMTLEVOL
/
&NAMTOPH
/
&NAMTOVS
/
&NAMTRAJP
/
&NAMTRANS
/
&NAMTRM
/
&NAMVAR
/
&NAMVARBC
/
&NAMVARBC_AIREP
/
&NAMVARBC_ALLSKY
/
&NAMVARBC_GBRAD
/
&NAMVARBC_RAD
/
&NAMVARBC_SFCOBS
/
&NAMVARBC_TCWV
/
&NAMVARBC_TO3
/
&NAMVAREPS
/
&NAMVDOZ
/
&NAMVFP
/
&NAMVRTL
/
&NAMVV0
/
&NAMVV1
/
&NAMVV2
/
&NAMVWRK
/
&NAMWAVELETJB
/
&NAMXFU
/
&NAMZDI
/
&NAPHLC
/
&NAV1IS
/
&NAEPHLI
/
&NAMPPVI
/
&NAMRLX
/
&NAMSPNG
/
EOF
