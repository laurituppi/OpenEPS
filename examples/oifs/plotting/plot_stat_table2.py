import matplotlib.pyplot as plt
import numpy as np

data1=np.loadtxt('b111_l15.txt')
data2=np.loadtxt('b112_l15.txt')
data3=np.loadtxt('b121_l15.txt')
data4=np.loadtxt('b122_l15.txt')

if 1==1:
  mean1=np.mean(data1[~np.isnan(data1)])
  mean2=np.mean(data2[~np.isnan(data2)])
  mean3=np.mean(data3[~np.isnan(data3)])
  mean4=np.mean(data4[~np.isnan(data4)])

  data1=data1/mean1
  data2=data2/mean2
  data3=data3/mean3
  data4=data4/mean4

  data11=data1+data2
  data22=data3+data4

  sums=np.zeros(6)
  sums[0]=sum(data11[:,0])
  sums[1]=sum(data11[:,1])
  sums[2]=sum(data11[:,2])
  sums[3]=sum(data11[:,3])
  sums[4]=sum(data11[:,4])
  sums[5]=sum(data11[:,5])
  print sums

#data11=data1+data2
#data22=data3+data4

masked_array1 = np.ma.array(data11, mask=np.isnan(data11))
masked_array2 = np.ma.array(data22, mask=np.isnan(data22))

time=np.arange(8)
ens=np.arange(11)

x,y = np.meshgrid(time,ens)# oikein
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.pcolor(x,y,masked_array1)#,vmin=0.0,vmax=1.0)
cbar = fig.colorbar(cax)
cbar.set_label('Distance')
axes = plt.gca()
axes.invert_yaxis()
#axes.set_ylim([1,40])
#axes.set_xlim([0,168])
plt.title('Table of Bhattacharyya distances (EPPES)')
plt.xlabel('Forecast length')
plt.ylabel('Ensemble size')
plt.show()

x,y = np.meshgrid(time,ens)# oikein
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.pcolor(x,y,masked_array2)#,vmin=0.0,vmax=1.0)
cbar = fig.colorbar(cax)
cbar.set_label('Distance')
axes = plt.gca()
axes.invert_yaxis()
#axes.set_ylim([1,40])
#axes.set_xlim([0,168])
plt.title('Table of Bhattacharyya distances (DE)')
plt.xlabel('Forecast length')
plt.ylabel('Ensemble size')
plt.show()
