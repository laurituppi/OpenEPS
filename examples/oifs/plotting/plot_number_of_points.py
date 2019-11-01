import matplotlib.pyplot as plt
import numpy as np
import os

parameter=''
optimizer = str(2)
inputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/crps_score2/data2/'
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
x0=0
x0l=0.5
xa=6
xal=1.5
xb=10
xbl=2.5
xc=16
xcl=3.5
xd=20
xdl=4.5
xe=26
xel=5.5
xf=30
xfl=6.5
xg=36
xgl=7.5
xh=40
xhl=8.5
xi=46
xil=9.5
xj=50
xjl=10.5

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

table=np.zeros((10,11))
#all_data=np.zeros((10,53))
for i in range(10):
  data=np.loadtxt(inputdir + my_list1[i])
  #counter=0
  #for j in range(0,53,5):
    #print i,j
  table[i,0]=data[0]
  table[i,1]=data[5]
  table[i,2]=data[9]
  table[i,3]=data[15]
  table[i,4]=data[19]
  table[i,5]=data[25]
  table[i,6]=data[29]
  table[i,7]=data[35]
  table[i,8]=data[39]
  table[i,9]=data[45]
  table[i,10]=data[49]
    #counter=counter+1

its=np.arange(12)
ens=np.arange(11)

x,y = np.meshgrid(its,ens)# oikein
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.pcolor(x,y,table,vmin=0.0,vmax=0.0005)
cbar = fig.colorbar(cax)
cbar.set_label('Score')
axes = plt.gca()
axes.invert_yaxis()
axes.set_xlim([0,11])
plt.title('CRPS scores')
plt.xlabel('Number of iterations')
plt.ylabel('Ensemble size')
plt.xticks((x0l,xal,xbl,xcl,xdl,xel,xfl,xgl,xhl,xil,xjl), (x0,xa,xb,xc,xd,xe,xf,xg,xh,xi,xj))
plt.yticks((yal,ybl,ycl,ydl,yel,yfl,ygl,yhl,yil,yjl), (ya,yb,yc,yd,ye,yf,yg,yh,yi,yj))
plt.savefig(outputdir + 'numpoints.png')
