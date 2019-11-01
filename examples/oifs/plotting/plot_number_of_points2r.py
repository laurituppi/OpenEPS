import matplotlib.pyplot as plt
import numpy as np
import os
#/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/level1/par2/crps_score2/data2/
#/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/level1/par2/part_1/crps_score2
parameter=''
optimizer = str(2)
inputdir1='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/level1/par2/part_1/crps_score2/data2/'
inputdir2='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/level1/par2/part_2/crps_score2/data2/'
#outputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/level2/par2/crps_score2/tables/'
string1='fcrps'
string2='.txt'
string3='_all.txt'
fclen='24'

subdirectories = sorted(os.listdir('/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2/6mem_12h/eppesdata'))

my_list1 = []
my_list1.append('20mem_'+'48h_1_' + string1 + parameter + string3)
my_list1.append('20mem_'+'48h_2_' + string1 + parameter + string3)
my_list1.append('20mem_'+'48h_3_' + string1 + parameter + string3)
my_list1.append('20mem_'+'48h_4_' + string1 + parameter + string3)

my_list1.append('26mem_'+'24h_1_' + string1 + parameter + string3)
my_list1.append('26mem_'+'24h_2_' + string1 + parameter + string3)
my_list1.append('26mem_'+'24h_3_' + string1 + parameter + string3)
my_list1.append('26mem_'+'24h_4_' + string1 + parameter + string3)

# xticks and yticks
x0=1
x0l=1
xa=6
xal=3
xb=10
xbl=5
xc=16
xcl=7
xd=20
xdl=9
xe=26
xel=11
xf=30
xfl=13
xg=36
xgl=15
xh=40
xhl=17
xi=46
xil=19
xj=50
xjl=21

ya='A1'
yal=0.5
yb='A2'
ybl=1.5
yc='A3'
ycl=2.5
yd='A4'
ydl=3.5
ye='B1'
yel=5.5
yf='B2'
yfl=6.5
yg='B3'
ygl=7.5
yh='B4'
yhl=8.5
#yi=46
#yil=8.5
#yj=50
#yjl=9.5

table=np.empty((10,22))
#all_data=np.zeros((10,53))
for i in range(9):
  if (i<4):
    data1=np.loadtxt(inputdir1 + my_list1[i])
    data2=np.loadtxt(inputdir2 + my_list1[i]) 
    #counter=0
    #for j in range(0,53,5):
      #print i,j
    table[i,0]=data1[0]
    table[i,1]=data2[0]
    table[i,2]=data1[5]
    table[i,3]=data2[5]
    table[i,4]=data1[9]
    table[i,5]=data2[9]
    table[i,6]=data1[15]
    table[i,7]=data2[15]
    table[i,8]=data1[19]
    table[i,9]=data2[19]
    table[i,10]=data1[25]
    table[i,11]=data2[25]
    table[i,12]=data1[29]
    table[i,13]=data2[29]
    table[i,14]=data1[35]
    table[i,15]=data2[35]
    table[i,16]=data1[39]
    table[i,17]=data2[39]
    table[i,18]=data1[45]
    table[i,19]=data2[45]
    table[i,20]=data1[49]
    table[i,21]=data2[49]
  elif (i>4):
    a=i-1
    data1=np.loadtxt(inputdir1 + my_list1[a])
    data2=np.loadtxt(inputdir2 + my_list1[a]) 
    #counter=0
    #for j in range(0,53,5):
      #print i,j
    table[i,0]=data1[0]
    table[i,1]=data2[0]
    table[i,2]=data1[5]
    table[i,3]=data2[5]
    table[i,4]=data1[9]
    table[i,5]=data2[9]
    table[i,6]=data1[15]
    table[i,7]=data2[15]
    table[i,8]=data1[19]
    table[i,9]=data2[19]
    table[i,10]=data1[25]
    table[i,11]=data2[25]
    table[i,12]=data1[29]
    table[i,13]=data2[29]
    table[i,14]=data1[35]
    table[i,15]=data2[35]
    table[i,16]=data1[39]
    table[i,17]=data2[39]
    table[i,18]=data1[45]
    table[i,19]=data2[45]
    table[i,20]=data1[49]
    table[i,21]=data2[49]
    #counter=counter+1

table=table*10000
#table[4,:]=np.nan
its=np.arange(23)
ens=np.arange(11)

x,y = np.meshgrid(its,ens)# oikein
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
cax = ax.pcolor(x,y,table,cmap='coolwarm',vmin=0.0,vmax=1.5)
cbar = fig.colorbar(cax)
cbar.set_label('fCRPS * 10${^4}$')
axes = plt.gca()
#axes.invert_yaxis()
axes.set_xlim([0,22])
axes.set_ylim([0,9])
plt.title('fCRPS; level 1')
plt.xlabel('Number of iterations')
plt.ylabel('Label of convergence test')
plt.xticks((x0l,xal,xbl,xcl,xdl,xel,xfl,xgl,xhl,xil,xjl), (x0,xa,xb,xc,xd,xe,xf,xg,xh,xi,xj))
plt.yticks((yal,ybl,ycl,ydl,yel,yfl,ygl,yhl), (ya,yb,yc,yd,ye,yf,yg,yh))
plt.hold()
xcoords=[2,4,6,8,10,12,14,16,18,20]
for xc in xcoords:
    plt.axvline(x=xc, linewidth=7, color='w')

ycoords=[1,2,3,4,5,6,7,8]
for yc in ycoords:
    plt.axhline(y=yc, linewidth=7, color='w')

for xc in xcoords:
    plt.axvline(x=xc, linewidth=2, color='k')

for yc in ycoords:
    plt.axhline(y=yc, linewidth=2, color='k')

plt.axhline(y=4.5, linewidth=62, color='w')
axes.invert_yaxis()
plt.rcParams.update({'font.size': 25})
plt.savefig('new_figures/entrorg_evolution_24h_level1_r.eps', dpi=300, format='eps')
plt.savefig('new_figures/entrorg_evolution_24h_level1_r.png', dpi=300, format='png')
#plt.savefig('new_figures/entrorg_evolution_24h_level1_r.pdf', dpi=300, format='pdf')
