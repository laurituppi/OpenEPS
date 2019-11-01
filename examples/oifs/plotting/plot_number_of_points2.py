import matplotlib.pyplot as plt
import numpy as np
import os

parameter=''
optimizer = str(2)
inputdir1='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/part_1/data2/'
inputdir2='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/part_2/data2/'
outputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/crps_score2/tables/'
string1='fcrps'
string2='.txt'
string3='_all.txt'
fclen='24'

subdirectories = sorted(os.listdir('/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2/6mem_12h/eppesdata'))

my_list1 = []
my_list1.append('6mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('10mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('16mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('20mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('26mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('30mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('36mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('40mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('46mem_'+fclen+'h_' + string1 + parameter + string3)
my_list1.append('50mem_'+fclen+'h_' + string1 + parameter + string3)

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

ya=6
yal=0.5
yb=10
ybl=1.5
yc=16
ycl=2.5
yd=20
ydl=3.5
ye=26
yel=4.5
yf=30
yfl=5.5
yg=36
ygl=6.5
yh=40
yhl=7.5
yi=46
yil=8.5
yj=50
yjl=9.5

table=np.zeros((10,22))
#all_data=np.zeros((10,53))
for i in range(10):
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
    #counter=counter+1

table=table*10000
its=np.arange(23)
ens=np.arange(11)

x,y = np.meshgrid(its,ens)# oikein
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
cax = ax.pcolor(x,y,table,cmap='coolwarm',vmin=0.0,vmax=1.5)
cbar = fig.colorbar(cax)
cbar.set_label('fCRPS * 10${^4}$')
#cbar.set_label('fCRPS')
axes = plt.gca()
axes.invert_yaxis()
axes.set_xlim([2,22])
plt.title('fCRPS; part 1 | part 2')
plt.xlabel('Number of iterations')
plt.ylabel('Ensemble size')
#plt.xticks((x0l,xal,xbl,xcl,xdl,xel,xfl,xgl,xhl,xil,xjl), (x0,xa,xb,xc,xd,xe,xf,xg,xh,xi,xj))
plt.xticks((xal,xbl,xcl,xdl,xel,xfl,xgl,xhl,xil,xjl), (xa,xb,xc,xd,xe,xf,xg,xh,xi,xj))
plt.yticks((yal,ybl,ycl,ydl,yel,yfl,ygl,yhl,yil,yjl), (ya,yb,yc,yd,ye,yf,yg,yh,yi,yj))
plt.hold()
xcoords=[4,6,8,10,12,14,16,18,20]
for xc in xcoords:
    plt.axvline(x=xc, linewidth=7, color='w')

ycoords=[1,2,3,4,5,6,7,8,9]
for yc in ycoords:
    plt.axhline(y=yc, linewidth=7, color='w')

for xc in xcoords:
    plt.axvline(x=xc, linewidth=2, color='k')

for yc in ycoords:
    plt.axhline(y=yc, linewidth=2, color='k')

plt.rcParams.update({'font.size': 25})
plt.savefig('new_figures/entrorg_24h_evolution.eps', dpi=300, format='eps')
plt.savefig('new_figures/entrorg_24h_evolution.png', dpi=300, format='png')
#plt.savefig('new_figures/entrorg_24h_evolution.pdf', dpi=300, format='pdf')
