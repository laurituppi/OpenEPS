import matplotlib.pyplot as plt
import numpy as np

inputdir_a='/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2/'
inputdir_b='/eppesdata/2017113000/'
mufile='mufile.dat'

my_list1 = []
my_list1.append(inputdir_a + '6mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '6mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '6mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '6mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '6mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '6mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '6mem_144h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_144h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '10mem_168h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '16mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '16mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '16mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '16mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '16mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '16mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '16mem_144h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '20mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '20mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '20mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '20mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '20mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '20mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_144h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '26mem_168h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '30mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '30mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '30mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '30mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '30mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '30mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '30mem_144h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '36mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '36mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '36mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '36mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '36mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '36mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_144h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '40mem_168h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '46mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '46mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '46mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '46mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '46mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '46mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '50mem_12h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '50mem_24h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '50mem_48h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '50mem_72h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '50mem_96h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '50mem_120h' + inputdir_b + mufile)
my_list1.append(inputdir_a + '50mem_144h' + inputdir_b + mufile)

xa=12
xal=0.5
xb=24
xbl=1.5
xc=48
xcl=2.5
xd=72
xdl=3.5
xe=96
xel=4.5
xf=120
xfl=5.5
xg=144
xgl=6.5
xh=168
xhl=7.5

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

mu_vector = np.zeros(71)
for i in range(70):
  data=np.loadtxt(my_list1[i])
  mu_vector[i] = data[0]#*1000

mu_table1 = np.empty((10,8))
mu_table1[:,:]=np.nan

mu_table1[0,0:7]=mu_vector[0:7]
mu_table1[1,0:8]=mu_vector[7:15]
mu_table1[2,0:7]=mu_vector[15:22]
mu_table1[3,0:6]=mu_vector[22:28]
mu_table1[4,0:8]=mu_vector[28:36]
mu_table1[5,0:7]=mu_vector[36:43]
mu_table1[6,0:6]=mu_vector[43:49]
mu_table1[7,0:8]=mu_vector[49:57]
mu_table1[8,0:6]=mu_vector[57:63]
mu_table1[9,0:7]=mu_vector[63:70]

print np.nanmean(mu_table1[:,:])
masked_array = np.ma.array(mu_table1, mask=np.isnan(mu_table1))

time=np.arange(9)
ens=np.arange(11)
x,y = np.meshgrid(time,ens)# oikein
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
cax = ax.pcolor(x,y,masked_array,cmap='PiYG_r',vmin=1.5,vmax=2.5) #ENTSHAPL
#cax = ax.pcolor(x,y,masked_array,cmap='PiYG_r',vmin=1.5,vmax=2) #ENTRORG
#cax = ax.pcolor(x,y,masked_array,cmap='coolwarm',vmin=0.003,vmax=0.004) #ENTSHALP*ENTRORG
cbar = fig.colorbar(cax)
#cbar.set_label('ENTRORG [10$^{-3}$ m$^{-1}$]')
cbar.set_label('ENTSHALP')
axes = plt.gca()
axes.invert_yaxis()
plt.xticks((xal,xbl,xcl,xdl,xel,xfl), (xa,xb,xc,xd,xe,xf))
plt.yticks((yal,ybl,ycl,ydl,yel,yfl,ygl,yhl,yil,yjl), (ya,yb,yc,yd,ye,yf,yg,yh,yi,yj))
#axes.set_ylim([1,40])
axes.set_xlim([0,6])
plt.title('Final parameter mean values')
#plt.title('Final shallow entrainment')
plt.xlabel('Forecast length [h]')
plt.ylabel('Ensemble size')
plt.rcParams.update({'font.size': 25})
#plt.savefig('new_figures/final_entrorg.eps', dpi=300, format='eps')
plt.savefig('new_figures/final_entshalp.png', dpi=300, format='png')
#plt.savefig('new_figures/final_entrorg.pdf', dpi=300, format='pdf')
