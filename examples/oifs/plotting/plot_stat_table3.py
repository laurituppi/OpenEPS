import matplotlib.pyplot as plt
import numpy as np
import os

# print rods of fair CRPS from repeated convergence tests

inputdir1='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/part_1/data2/' # ne taulukot
inputdir2='/homeappl/home/lautuppi/appl_sisu/figures/OpenEPS/publ_conv_tests/fair_crps/EPPES/par2/part_2/data2/'
string1='_fcrps'
string2='.txt'
#string3='_all.txt'

my_list1 = []
my_list1.append('20mem_48h'+string1+string2)
my_list1.append('20mem_48h_2'+string1+string2)
my_list1.append('20mem_48h_3'+string1+string2)
my_list1.append('20mem_48h_4'+string1+string2)

my_list2 = []
my_list2.append('26mem_24h'+string1+string2)
my_list2.append('26mem_24h_2'+string1+string2)
my_list2.append('26mem_24h_3'+string1+string2)
my_list2.append('26mem_24h_4'+string1+string2)

all_column=np.zeros(16)
table = np.empty((4,10))
table[:,:]=np.nan

for i in range(4):
  data1=np.loadtxt(inputdir1 + my_list1[i])
  data2=np.loadtxt(inputdir1 + my_list2[i])
  data3=np.loadtxt(inputdir2 + my_list1[i])
  data4=np.loadtxt(inputdir2 + my_list2[i])
  #all_column[i] = data1[4]
  #all_column[i+4] = data2[4]
  #all_column[i+8] = data3[4]
  #all_column[i+12] = data4[4]
#  table[0,2*i]=data1[4]
#  table[1,2*i]=data2[4]
  #print inputdir1 + my_list1[i]
  #print inputdir1 + my_list2[i]
  #print data1,data3
  table[0,2*i+1]=data3[4]
  table[1,2*i+1]=data4[4]

#table[0,0:4] = all_column[0:4]
#table[2,0:4] = all_column[4:8]
#for i in range(4):
#  table[0,2*i]=all_column[i]
#  table[1,2*i]=all_column[i+8]
#  table[0,2*i+1]=all_column[i+4]
#  table[1,2*i+1]=all_column[i+12]
  
print table

masked_array = np.ma.array(table, mask=np.isnan(table))

xa=1
xal=1
xb=2
xbl=3
xc=3
xcl=5
xd=4
xdl=7

ya='20mem_48h'
yal=0.5
yb='26mem_24h'
ybl=2.5

time=np.arange(10)
ens=np.arange(4)

x,y = np.meshgrid(time,ens)# oikein
fig = plt.figure()
ax = fig.add_subplot(111)
#last15_table = last15_table.T
cax = ax.pcolor(x,y,masked_array,vmin=0.0,vmax=0.00015)
cbar = fig.colorbar(cax)
cbar.set_label('CRPS')
axes = plt.gca()
axes.invert_yaxis()
#axes.set_ylim([1,40])
axes.set_xlim([0,8])
plt.title('Final CRPS, part 1')
plt.xlabel('Number of convergence test')
plt.ylabel('Ensemble size, forecast length')
plt.xticks((xal,xbl,xcl,xdl), (xa,xb,xc,xd))
plt.yticks((yal,ybl), (ya,yb), rotation='90')
#plt.savefig('DE_par1_part1.png')
plt.hold()
xcoords=[2,4,6]
for xc in xcoords:
    plt.axvline(x=xc, linewidth=5, color='w')

for xc in xcoords:
    plt.axvline(x=xc, linewidth=1, color='k')

plt.show()
