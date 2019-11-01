import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.lines as mlines
import matplotlib.patches as mp

#parameter = str(2)
parameter=''
optimizer = str(2)
#inputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/bhattacharyya/multivariate/1' + optimizer + str(2) + '/data/'
#inputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/bhattacharyya_costf/EPPES/data/'
inputdir1='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/part_1/data2/'
inputdir2='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/part_2/data2/'
outputdir='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/combi/tables/'
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
xal=1
xb=24
xbl=3
xc=48
xcl=5
xd=72
xdl=7
xe=96
xel=9
xf=120
xfl=11
xg=144
xgl=13
xh=168
xhl=15

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

part1 = np.zeros(71)
part2 = np.zeros(71)
for i in range(70):
  data1=np.loadtxt(inputdir1 + my_list1[i])
  data2=np.loadtxt(inputdir2 + my_list1[i])
  part1[i] = data1[1]*10000
  part2[i] = data2[1]*10000

avg_table1 = np.empty((10,8))
avg_table1[:,:] = np.nan
avg_table2 = np.empty((10,8))
avg_table2[:,:] = np.nan
avg_table = np.empty((10,16))
avg_table[:,:]=np.nan

avg_table1[0,0:7]=part1[0:7]
avg_table2[0,0:7]=part2[0:7]
avg_table1[1,0:8]=part1[7:15]
avg_table2[1,0:8]=part2[7:15]
avg_table1[2,0:7]=part1[15:22]
avg_table2[2,0:7]=part2[15:22]
avg_table1[3,0:6]=part1[22:28]
avg_table2[3,0:6]=part2[22:28]
avg_table1[4,0:8]=part1[28:36]
avg_table2[4,0:8]=part2[28:36]
avg_table1[5,0:7]=part1[36:43]
avg_table2[5,0:7]=part2[36:43]
avg_table1[6,0:6]=part1[43:49]
avg_table2[6,0:6]=part2[43:49]
avg_table1[7,0:8]=part1[49:57]
avg_table2[7,0:8]=part2[49:57]
avg_table1[8,0:6]=part1[57:63]
avg_table2[8,0:6]=part2[57:63]
avg_table1[9,0:7]=part1[63:70]
avg_table2[9,0:7]=part2[63:70]

avg_table[:,0]=avg_table1[:,0]
avg_table[:,1]=avg_table2[:,0]
avg_table[:,2]=avg_table1[:,1]
avg_table[:,3]=avg_table2[:,1]
avg_table[:,4]=avg_table1[:,2]
avg_table[:,5]=avg_table2[:,2]
avg_table[:,6]=avg_table1[:,3]
avg_table[:,7]=avg_table2[:,3]
avg_table[:,8]=avg_table1[:,4]
avg_table[:,9]=avg_table2[:,4]
avg_table[:,10]=avg_table1[:,5]
avg_table[:,11]=avg_table2[:,5]
avg_table[:,12]=avg_table1[:,6]
avg_table[:,13]=avg_table2[:,6]
avg_table[:,14]=avg_table1[:,7]
avg_table[:,15]=avg_table2[:,7]

#np.savetxt(outputdir + 'b121_l15.txt',last15_table)

masked_array = np.ma.array(avg_table, mask=np.isnan(avg_table))

print np.shape(masked_array)
ens=np.arange(11)
time=np.arange(13)#(17)

x,y = np.meshgrid(time,ens)# oikein
fig = plt.figure(figsize=(12,10))
#ax = fig.add_subplot(figsize=(12,10)) # (111)
ax = fig.add_subplot(111)
#avg_table = avg_table.T
cax = ax.pcolor(x,y,masked_array[:,:12],cmap='coolwarm',vmin=0.0,vmax=1.5)
cbar = fig.colorbar(cax)
cbar.set_label('fCRPS * 10$^{4}$')
#cbar.set_label('fCRPS')
axes = plt.gca()
axes.invert_yaxis()
#axes.set_ylim([1,40])
#axes.set_xlim([0,2])
#plt.title('Average of the last 15 CRPS scores; part 1, part 2')
plt.title('Final fCRPS; part 1 | part 2')
plt.xlabel('Forecast length [h]')
plt.ylabel('Ensemble size')
plt.xticks((xal,xbl,xcl,xdl,xel,xfl), (xa,xb,xc,xd,xe,xf)) #plt.xticks((xal,xbl,xcl,xdl,xel,xfl,xgl,xhl), (xa,xb,xc,xd,xe,xf,xg,xh))
plt.yticks((yal,ybl,ycl,ydl,yel,yfl,ygl,yhl,yil,yjl), (ya,yb,yc,yd,ye,yf,yg,yh,yi,yj))
#plt.savefig(outputdir + 'average_l15.png')
plt.hold()
xcoords=[2,4,6,8,10]#,12,14,16]
for xc in xcoords:
    plt.axvline(x=xc, linewidth=7, color='w')

ycoords=[1,2,3,4,5,6,7,8,9]
for yc in ycoords:
    plt.axhline(y=yc, linewidth=7, color='w')

for xc in xcoords:
    plt.axvline(x=xc, linewidth=2, color='k')

for yc in ycoords:
    plt.axhline(y=yc, linewidth=2, color='k')

mp.rectangle((5,2),2,1,angle=0.0, color='green', fill='false')

plt.rcParams.update({'font.size': 25})
print 'printing'
plt.savefig('new_figures/last_par2_part1part2.eps', dpi=300, format='eps')
plt.savefig('new_figures/last_par2_part1part2.png', dpi=300, format='png')
#plt.savefig('new_figures/last_par2_part1part2.pdf', dpi=300, format='pdf')
#plt.waitforbuttonpress(timeout=-1)
plt.clf()

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

