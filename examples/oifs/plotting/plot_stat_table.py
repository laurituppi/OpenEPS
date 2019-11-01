import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.lines as mlines

#parameter = str(2)
parameter=''
optimizer = str(2)
#inputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/bhattacharyya/multivariate/1' + optimizer + str(2) + '/data/'
#inputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/bhattacharyya_costf/EPPES/data/'
inputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/crps_score2/data2/'
outputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/crps_score2/tables/'
string1='fcrps'
string2='.txt'
string3='_all.txt'

subdirectories = sorted(os.listdir('/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level2/6mem_12h/eppesdata'))

my_list1 = []
my_list1.append('6mem_12h_' + string1 + parameter + string2)
my_list1.append('6mem_24h_' + string1 + parameter + string2)
my_list1.append('6mem_48h_' + string1 + parameter + string2)
my_list1.append('6mem_72h_' + string1 + parameter + string2)
my_list1.append('6mem_96h_' + string1 + parameter + string2)
my_list1.append('6mem_120h_' + string1 + parameter + string2)
my_list1.append('6mem_144h_' + string1 + parameter + string2)
my_list1.append('10mem_12h_' + string1 + parameter + string2)
my_list1.append('10mem_24h_' + string1 + parameter + string2)
my_list1.append('10mem_48h_' + string1 + parameter + string2)
my_list1.append('10mem_72h_' + string1 + parameter + string2)
my_list1.append('10mem_96h_' + string1 + parameter + string2)
my_list1.append('10mem_120h_' + string1 + parameter + string2)
my_list1.append('10mem_144h_' + string1 + parameter + string2)
my_list1.append('10mem_168h_' + string1 + parameter + string2)
my_list1.append('16mem_12h_' + string1 + parameter + string2)
my_list1.append('16mem_24h_' + string1 + parameter + string2)
my_list1.append('16mem_48h_' + string1 + parameter + string2)
my_list1.append('16mem_72h_' + string1 + parameter + string2)
my_list1.append('16mem_96h_' + string1 + parameter + string2)
my_list1.append('16mem_120h_' + string1 + parameter + string2)
my_list1.append('16mem_144h_' + string1 + parameter + string2)
my_list1.append('20mem_12h_' + string1 + parameter + string2)
my_list1.append('20mem_24h_' + string1 + parameter + string2)
my_list1.append('20mem_48h_' + string1 + parameter + string2)
my_list1.append('20mem_72h_' + string1 + parameter + string2)
my_list1.append('20mem_96h_' + string1 + parameter + string2)
my_list1.append('20mem_120h_' + string1 + parameter + string2)
my_list1.append('26mem_12h_' + string1 + parameter + string2)
my_list1.append('26mem_24h_' + string1 + parameter + string2)
my_list1.append('26mem_48h_' + string1 + parameter + string2)
my_list1.append('26mem_72h_' + string1 + parameter + string2)
my_list1.append('26mem_96h_' + string1 + parameter + string2)
my_list1.append('26mem_120h_' + string1 + parameter + string2)
my_list1.append('26mem_144h_' + string1 + parameter + string2)
my_list1.append('26mem_168h_' + string1 + parameter + string2)
my_list1.append('30mem_12h_' + string1 + parameter + string2)
my_list1.append('30mem_24h_' + string1 + parameter + string2)
my_list1.append('30mem_48h_' + string1 + parameter + string2)
my_list1.append('30mem_72h_' + string1 + parameter + string2)
my_list1.append('30mem_96h_' + string1 + parameter + string2)
my_list1.append('30mem_120h_' + string1 + parameter + string2)
my_list1.append('30mem_144h_' + string1 + parameter + string2)
my_list1.append('36mem_12h_' + string1 + parameter + string2)
my_list1.append('36mem_24h_' + string1 + parameter + string2)
my_list1.append('36mem_48h_' + string1 + parameter + string2)
my_list1.append('36mem_72h_' + string1 + parameter + string2)
my_list1.append('36mem_96h_' + string1 + parameter + string2)
my_list1.append('36mem_120h_' + string1 + parameter + string2)
my_list1.append('40mem_12h_' + string1 + parameter + string2)
my_list1.append('40mem_24h_' + string1 + parameter + string2)
my_list1.append('40mem_48h_' + string1 + parameter + string2)
my_list1.append('40mem_72h_' + string1 + parameter + string2)
my_list1.append('40mem_96h_' + string1 + parameter + string2)
my_list1.append('40mem_120h_' + string1 + parameter + string2)
my_list1.append('40mem_144h_' + string1 + parameter + string2)
my_list1.append('40mem_168h_' + string1 + parameter + string2)
my_list1.append('46mem_12h_' + string1 + parameter + string2)
my_list1.append('46mem_24h_' + string1 + parameter + string2)
my_list1.append('46mem_48h_' + string1 + parameter + string2)
my_list1.append('46mem_72h_' + string1 + parameter + string2)
my_list1.append('46mem_96h_' + string1 + parameter + string2)
my_list1.append('46mem_120h_' + string1 + parameter + string2)
my_list1.append('50mem_12h_' + string1 + parameter + string2)
my_list1.append('50mem_24h_' + string1 + parameter + string2)
my_list1.append('50mem_48h_' + string1 + parameter + string2)
my_list1.append('50mem_72h_' + string1 + parameter + string2)
my_list1.append('50mem_96h_' + string1 + parameter + string2)
my_list1.append('50mem_120h_' + string1 + parameter + string2)
my_list1.append('50mem_144h_' + string1 + parameter + string2)
#print my_list

my_list2 = []
my_list2.append('6mem_12h_' + string1 + parameter + string3)
my_list2.append('6mem_24h_' + string1 + parameter + string3)
my_list2.append('6mem_48h_' + string1 + parameter + string3)
my_list2.append('6mem_72h_' + string1 + parameter + string3)
my_list2.append('6mem_96h_' + string1 + parameter + string3)
my_list2.append('6mem_120h_' + string1 + parameter + string3)
my_list2.append('6mem_144h_' + string1 + parameter + string3)
my_list2.append('10mem_12h_' + string1 + parameter + string3)
my_list2.append('10mem_24h_' + string1 + parameter + string3)
my_list2.append('10mem_48h_' + string1 + parameter + string3)
my_list2.append('10mem_72h_' + string1 + parameter + string3)
my_list2.append('10mem_96h_' + string1 + parameter + string3)
my_list2.append('10mem_120h_' + string1 + parameter + string3)
my_list2.append('10mem_144h_' + string1 + parameter + string3)
my_list2.append('10mem_168h_' + string1 + parameter + string3)
my_list2.append('16mem_12h_' + string1 + parameter + string3)
my_list2.append('16mem_24h_' + string1 + parameter + string3)
my_list2.append('16mem_48h_' + string1 + parameter + string3)
my_list2.append('16mem_72h_' + string1 + parameter + string3)
my_list2.append('16mem_96h_' + string1 + parameter + string3)
my_list2.append('16mem_120h_' + string1 + parameter + string3)
my_list2.append('16mem_144h_' + string1 + parameter + string3)
my_list2.append('20mem_12h_' + string1 + parameter + string3)
my_list2.append('20mem_24h_' + string1 + parameter + string3)
my_list2.append('20mem_48h_' + string1 + parameter + string3)
my_list2.append('20mem_72h_' + string1 + parameter + string3)
my_list2.append('20mem_96h_' + string1 + parameter + string3)
my_list2.append('20mem_120h_' + string1 + parameter + string3)
my_list2.append('26mem_12h_' + string1 + parameter + string3)
my_list2.append('26mem_24h_' + string1 + parameter + string3)
my_list2.append('26mem_48h_' + string1 + parameter + string3)
my_list2.append('26mem_72h_' + string1 + parameter + string3)
my_list2.append('26mem_96h_' + string1 + parameter + string3)
my_list2.append('26mem_120h_' + string1 + parameter + string3)
my_list2.append('26mem_144h_' + string1 + parameter + string3)
my_list2.append('26mem_168h_' + string1 + parameter + string3)
my_list2.append('30mem_12h_' + string1 + parameter + string3)
my_list2.append('30mem_24h_' + string1 + parameter + string3)
my_list2.append('30mem_48h_' + string1 + parameter + string3)
my_list2.append('30mem_72h_' + string1 + parameter + string3)
my_list2.append('30mem_96h_' + string1 + parameter + string3)
my_list2.append('30mem_120h_' + string1 + parameter + string3)
my_list2.append('30mem_144h_' + string1 + parameter + string3)
my_list2.append('36mem_12h_' + string1 + parameter + string3)
my_list2.append('36mem_24h_' + string1 + parameter + string3)
my_list2.append('36mem_48h_' + string1 + parameter + string3)
my_list2.append('36mem_72h_' + string1 + parameter + string3)
my_list2.append('36mem_96h_' + string1 + parameter + string3)
my_list2.append('36mem_120h_' + string1 + parameter + string3)
my_list2.append('40mem_12h_' + string1 + parameter + string3)
my_list2.append('40mem_24h_' + string1 + parameter + string3)
my_list2.append('40mem_48h_' + string1 + parameter + string3)
my_list2.append('40mem_72h_' + string1 + parameter + string3)
my_list2.append('40mem_96h_' + string1 + parameter + string3)
my_list2.append('40mem_120h_' + string1 + parameter + string3)
my_list2.append('40mem_144h_' + string1 + parameter + string3)
my_list2.append('40mem_168h_' + string1 + parameter + string3)
my_list2.append('46mem_12h_' + string1 + parameter + string3)
my_list2.append('46mem_24h_' + string1 + parameter + string3)
my_list2.append('46mem_48h_' + string1 + parameter + string3)
my_list2.append('46mem_72h_' + string1 + parameter + string3)
my_list2.append('46mem_96h_' + string1 + parameter + string3)
my_list2.append('46mem_120h_' + string1 + parameter + string3)
my_list2.append('50mem_12h_' + string1 + parameter + string3)
my_list2.append('50mem_24h_' + string1 + parameter + string3)
my_list2.append('50mem_48h_' + string1 + parameter + string3)
my_list2.append('50mem_72h_' + string1 + parameter + string3)
my_list2.append('50mem_96h_' + string1 + parameter + string3)
my_list2.append('50mem_120h_' + string1 + parameter + string3)
my_list2.append('50mem_144h_' + string1 + parameter + string3)

# xticks and yticks
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

last15_column = np.zeros(71)
for i in range(70):
  data=np.loadtxt(inputdir + my_list1[i])
  last15_column[i] = data[3]

last15_table = np.empty((10,8))
last15_table[:,:]=np.nan

last15_table[0,0:7]=last15_column[0:7]
last15_table[1,0:8]=last15_column[7:15]
last15_table[2,0:7]=last15_column[15:22]
last15_table[3,0:6]=last15_column[22:28]
last15_table[4,0:8]=last15_column[28:36]
last15_table[5,0:7]=last15_column[36:43]
last15_table[6,0:6]=last15_column[43:49]
last15_table[7,0:8]=last15_column[49:57]
last15_table[8,0:6]=last15_column[57:63]
last15_table[9,0:7]=last15_column[63:70]
#print last15_column[70]#, last15_column[15]
#print last15_column[7:14]
#print last15_table[9,:]
np.savetxt(outputdir + 'b121_l15.txt',last15_table)

masked_array = np.ma.array(last15_table, mask=np.isnan(last15_table))

time=np.arange(9)
ens=np.arange(11)

x,y = np.meshgrid(time,ens)# oikein
fig = plt.figure()
ax = fig.add_subplot(111)
#last15_table = last15_table.T
cax = ax.pcolor(x,y,masked_array,vmin=0.0,vmax=0.0003)
cbar = fig.colorbar(cax)
cbar.set_label('Score')
axes = plt.gca()
axes.invert_yaxis()
#axes.set_ylim([1,40])
#axes.set_xlim([0,168])
plt.title('Average of last 15 CRPS scores')
plt.xlabel('Forecast length [h]')
plt.ylabel('Ensemble size')
plt.xticks((xal,xbl,xcl,xdl,xel,xfl,xgl,xhl), (xa,xb,xc,xd,xe,xf,xg,xh))
plt.yticks((yal,ybl,ycl,ydl,yel,yfl,ygl,yhl,yil,yjl), (ya,yb,yc,yd,ye,yf,yg,yh,yi,yj))
plt.savefig(outputdir + 'average_l15.png')
#plt.waitforbuttonpress(timeout=-1)
#plt.close()

############################################################
if(0==1):
  all_data=np.zeros((71,53))
  for i in range(70):
    data=np.loadtxt(inputdir + my_list2[i])
    all_data[i,:]=data

  for i in range(53):
    column=np.zeros(71)
    for j in range(70):
      column[j] = all_data[j,i]

    table = np.empty((10,8))
    table[:,:]=np.nan
    table[0,0:7]=column[0:7]
    table[1,0:8]=column[7:15]
    table[2,0:7]=column[15:22]
    table[3,0:6]=column[22:28]
    table[4,0:8]=column[28:36]
    table[5,0:7]=column[36:43]
    table[6,0:6]=column[43:49]
    table[7,0:8]=column[49:57]
    table[8,0:6]=column[57:63]
    table[9,0:7]=column[63:70]
    print 'all_avg= ', sum(column)/71.0
    masked_array = np.ma.array(table, mask=np.isnan(table))

    x,y = np.meshgrid(time,ens)# oikein
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #cax = ax.pcolor(x,y,masked_array,vmin=0.0,vmax=3.0) # for EPPES and ENTRORG
    #cax = ax.pcolor(x,y,masked_array,vmin=0.0,vmax=0.2) # for EPPES and ENTSHALP
    #cax = ax.pcolor(x,y,masked_array,vmin=3.0,vmax=5.0) # for DE and ENTRORG
    #cax = ax.pcolor(x,y,masked_array,vmin=0.3,vmax=0.7) # for DE and ENTSHALP
    #cax = ax.pcolor(x,y,masked_array,vmin=1.0,vmax=3.0)
    #cax = ax.pcolor(x,y,masked_array,vmin=0.0,vmax=1e8)
    cax = ax.pcolor(x,y,masked_array,vmin=0.0,vmax=0.0004)
    cbar = fig.colorbar(cax)
    cbar.set_label('Score')
    axes = plt.gca()
    axes.invert_yaxis()
    #axes.set_ylim([1,40])
    #axes.set_xlim([0,168])
    plt.title('Fair CRPS score ' + str(subdirectories[i]))
    plt.xlabel('Forecast length')
    plt.ylabel('Ensemble size')
    plt.xticks((xal,xbl,xcl,xdl,xel,xfl,xgl,xhl), (xa,xb,xc,xd,xe,xf,xg,xh))
    plt.yticks((yal,ybl,ycl,ydl,yel,yfl,ygl,yhl,yil,yjl), (ya,yb,yc,yd,ye,yf,yg,yh,yi,yj))
    plt.savefig(outputdir + 'figure' + str(i) + '.png')
    #plt.show()
    #plt.waitforbuttonpress(timeout=-1)
    plt.clf()

