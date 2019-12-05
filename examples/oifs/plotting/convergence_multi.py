import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys
import os

plt.rcParams.update({'font.size': 18})
# tunge tanne viela se rmsez850 jonkinlaisina kayrina. posteriin ei mahdu enempaa kuvia

indir0 = sys.argv[1]
indir1 = sys.argv[2]
indir2 = sys.argv[3]
indir3 = sys.argv[4]
indir4 = sys.argv[5]

mufile = "mufile.dat"
sigfile = "sigfile.dat"
npars=2

subdirectories0 = sorted(os.listdir(indir0))
subdirectories1 = sorted(os.listdir(indir1))
subdirectories2 = sorted(os.listdir(indir2))
subdirectories3 = sorted(os.listdir(indir3))
subdirectories4 = sorted(os.listdir(indir4))

ndays = np.size(subdirectories0)
def_value1 = np.ones(ndays+1)*2.0
def_value2 = np.ones(ndays+1)*1.75
def_values = np.zeros((ndays+1,2))
def_values[:,0] = def_value1[:]
def_values[:,1] = def_value2[:]

t = np.arange(ndays+1)

mu_data0 = np.zeros((ndays+1, npars))
mu_data1 = np.zeros((ndays+1, npars))
mu_data2 = np.zeros((ndays+1, npars))
mu_data3 = np.zeros((ndays+1, npars))
mu_data4 = np.zeros((ndays+1, npars))
apu1=np.loadtxt("/wrk/lautuppi/DONOTREMOVE/init_mu_sigma/mufile_2par.dat")
mu_data0[0,:] = apu1 #[0:1]
mu_data1[0,:] = mu_data0[0,:]
mu_data2[0,:] = mu_data0[0,:]
mu_data3[0,:] = mu_data0[0,:]
mu_data4[0,:] = mu_data0[0,:]
sig_data0 = np.zeros((ndays+1, npars, npars))
sig_data1 = np.zeros((ndays+1, npars, npars))
sig_data2 = np.zeros((ndays+1, npars, npars))
sig_data3 = np.zeros((ndays+1, npars, npars))
sig_data4 = np.zeros((ndays+1, npars, npars))
apu2=np.loadtxt("/wrk/lautuppi/DONOTREMOVE/init_mu_sigma/sigfile_2par.dat")
sig_data0[0,:,:] = apu2 #[0:1,0:1]
sig_data1[0,:,:] = sig_data0[0,:,:]
sig_data2[0,:,:] = sig_data0[0,:,:]
sig_data3[0,:,:] = sig_data0[0,:,:]
sig_data4[0,:,:] = sig_data0[0,:,:]

def get_input_file(inputdir, day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

#apu1=np.zeros(())
for i in range(0,ndays):
    apu3=np.loadtxt(get_input_file(indir0, subdirectories0[i], mufile))
    mu_data0[i+1,:] = apu3 #[0:1]
    apu4=np.loadtxt(get_input_file(indir1, subdirectories1[i], mufile))
    mu_data1[i+1,:] = apu4 #[0:1]
    apu5=np.loadtxt(get_input_file(indir2, subdirectories2[i], mufile))
    mu_data2[i+1,:] = apu5 #[0:1]
    apu6=np.loadtxt(get_input_file(indir3, subdirectories3[i], mufile))
    mu_data3[i+1,:] = apu6[0:2]
    mu_data4[i+1,:] = np.loadtxt(get_input_file(indir4, subdirectories4[i], mufile))
    #print apu6[0:2] #mu_data3[i+1,:]
    apu7=np.loadtxt(get_input_file(indir0, subdirectories0[i], sigfile))
    sig_data0[i+1,:,:] = apu7 #[0:1,0:1]
    apu8=np.loadtxt(get_input_file(indir1, subdirectories1[i], sigfile))
    sig_data1[i+1,:,:] = apu8 #[0:1,0:1]
    apu9=np.loadtxt(get_input_file(indir2, subdirectories2[i], sigfile))
    sig_data2[i+1,:,:] = apu9 #[0:1,0:1]
    apu10 = np.loadtxt(get_input_file(indir3, subdirectories3[i], sigfile))
    sig_data3[i+1,:,:] = apu10[0:2,0:2]
    sig_data4[i+1,:,:] = np.loadtxt(get_input_file(indir4, subdirectories4[i], sigfile))

a = int(subdirectories0[0])
al = 1
b = int(round(int(subdirectories0[ndays-int(round(ndays/5))])))
bl = int(round(4*ndays/5))
c = int(round(int(subdirectories0[ndays-int(round(2*ndays/5))])))
cl = int(round(3*ndays/5))
d = int(round(int(subdirectories0[ndays-int(round(3*ndays/5))])))
dl = int(round(2*ndays/5))
e = int(round(int(subdirectories0[ndays-int(round(4*ndays/5))])))
el = int(round(ndays/5))
f = int(subdirectories0[ndays-1])
fl = ndays-1

pars = ['ENTSHALP','ENTRORG']

if 0==1: ##### Levels: colorfill option #####
  for i in range(npars):
      print('processing parameter:', pars[i])
      fig, ax=plt.subplots(figsize=(10,7.9))

      #plt.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), 'b.-', linewidth=1.0, label='level 0')
      #plt.plot(t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), 'b.-', linewidth=1.0)
      ax.plot(t, mu_data0[:,i], 'b.-', linewidth=1.0, label='level 0')

      #plt.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), 'r.-', linewidth=1.0, label='level 1')
      #plt.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), 'r.-', linewidth=1.0)
      ax.plot(t, mu_data1[:,i], 'm.-', linewidth=1.0, label='level 1')

      #plt.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), 'k.-', linewidth=1.0, label='level 2')
      #plt.plot(t, mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), 'k.-', linewidth=1.0)
      ax.plot(t, mu_data2[:,i], 'r.-', linewidth=1.0, label='level 2')

      #plt.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), 'm.-', linewidth=1.0, label='level 3')
      #plt.plot(t, mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), 'm.-', linewidth=1.0)
      ax.plot(t, mu_data3[:,i], 'y.-', linewidth=1.0, label='level 3')

      ax.fill_between(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), facecolor='b', alpha=1.0)
      ax.fill_between(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), facecolor='m', alpha=0.25)
      ax.fill_between(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), facecolor='r', alpha=0.25)
      ax.fill_between(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), facecolor='y', alpha=0.25)
  


      ax.plot(t, def_values[:,i], 'g-', linewidth=1.0, label='default value')


      ax.set_xlabel('Initialisation date')
      plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
      if pars[i]=='ENTRORG':
        ax.set_ylabel('Parameter value [m$^{-1}$]')
      else:
        ax.set_ylabel('Parameter value')
    
      ax.set_title(pars[i])

      ax.legend(loc=0)#, fontsize = 'small')

      ax.set_xlim([0.0,ndays+1])

      fig.savefig('new_figures/parameter' + str(i+1) + 'levs.eps', dpi=300, format='eps')
      fig.savefig('new_figures/parameter' + str(i+1) + 'levs.png', dpi=300, format='png')
      fig.savefig('new_figures/parameter' + str(i+1) + 'levs.pdf', dpi=300, format='pdf')
      fig.clf()

if 1==1: ##### Levels: different linestyles #####
  mu_data0[:,1]=mu_data0[:,1]*1000
  mu_data1[:,1]=mu_data1[:,1]*1000
  mu_data2[:,1]=mu_data2[:,1]*1000
  mu_data3[:,1]=mu_data3[:,1]*1000
  mu_data4[:,1]=mu_data4[:,1]*1000
  sig_data0[:,1,1]=sig_data0[:,1,1]*1000000
  sig_data1[:,1,1]=sig_data1[:,1,1]*1000000
  sig_data2[:,1,1]=sig_data2[:,1,1]*1000000
  sig_data3[:,1,1]=sig_data3[:,1,1]*1000000
  sig_data4[:,1,1]=sig_data4[:,1,1]*1000000
  for i in range(npars):
    print('processing parameter:', pars[i])

    fig, ax=plt.subplots(figsize=(10,7.9))

    if 0==1: ##### Various symbols with different colors #####
      ax.plot(t, mu_data0[:,i], 'bX-', linewidth=1.5, markersize=6.0, label='level 0; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], 'md-', linewidth=1.5, markersize=6.0, label='level 1; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], 'ro-', linewidth=1.5, markersize=6.0, label='level 2; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], 'ys-', linewidth=1.5, markersize=6.0, label='level 3; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), 'bX', t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), 'bX')
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), 'md', t,  mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), 'md')
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), 'ro', t,  mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), 'ro')
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), 'ys', t,  mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), 'ys')
      ax.plot(t, def_values[:,i], 'g.', linewidth=1.5, label='default value')
    elif 0==1: ##### Pluses with different colors #####
      ax.plot(t, mu_data0[:,i], 'b.-', linewidth=1.5, markersize=8.0, label='level 0, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], 'm.-', linewidth=1.5, markersize=8.0, label='level 1, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], 'r.-', linewidth=1.5, markersize=8.0, label='level 2, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], 'y.-', linewidth=1.5, markersize=8.0, label='level 3, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), 'bP', t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), 'bP')
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), 'mP', t,  mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), 'mP')
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), 'rP', t,  mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), 'rP')
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), 'yP', t,  mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), 'yP')
      ax.plot(t, def_values[:,i], 'g.', linewidth=1.5, label='default value')
    elif 0==1: ##### Solid lines for mean values and dash dotted lines for uncertainties, different shades of gray #####
      ax.plot(t, mu_data0[:,i], 'k-', linewidth=2.5, label='L0; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], c='0.25', linestyle='-', linewidth=2.5, label='L1; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], c='0.5', linestyle='-', linewidth=2.5, label='L2; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], c='0.75', linestyle='-', linewidth=2.5, label='L3; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), c='0.0', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), c='0.0', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), c='0.25', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), c='0.25', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), c='0.5', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), c='0.5', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), c='0.75', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), c='0.75', linestyle='-.', linewidth=2.5)
      ax.plot(t, def_values[:,i], 'g.', linewidth=1.5, label='default value')
    elif 0==1: ##### Solid lines for mean values and dash dotted lines for uncertainties, different shades of brown #####
      ax.plot(t, mu_data0[:,i], c='saddlebrown', linestyle='-', linewidth=2.5, label='L0; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], c='chocolate', linestyle='-', linewidth=2.5, label='L1; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], c='burlywood', linestyle='-', linewidth=2.5, label='L2; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], c='wheat', linestyle='-', linewidth=2.5, label='L3; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), c='saddlebrown', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), c='saddlebrown', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), c='chocolate', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), c='chocolate', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), c='burlywood', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), c='burlywood', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), c='wheat', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), c='wheat', linestyle='-.', linewidth=2.5)
      ax.plot(t, def_values[:,i], 'g.', linewidth=1.5, label='default value')
    elif 0==1: ##### Solid lines for mean values and dash dotted lines for uncertainties, different shades of green #####
      ax.plot(t, mu_data0[:,i], c='darkgreen', linestyle='-', linewidth=2.5, label='L0; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], c='#238b45', linestyle='-', linewidth=2.5, label='L1; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], c='#66c2a4', linestyle='-', linewidth=2.5, label='L2; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], c='#b2e2e2', linestyle='-', linewidth=2.5, label='L3; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), c='darkgreen', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), c='darkgreen', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), c='#238b45', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), c='#238b45', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), c='#66c2a4', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), c='#66c2a4', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), c='#b2e2e2', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), c='#b2e2e2', linestyle='-.', linewidth=2.5)
      ax.plot(t, def_values[:,i], 'm.', linewidth=1.5, label='default value')
    elif 0==1: ##### Solid lines for mean values and dash dotted lines for uncertainties, different colors #####
      ax.plot(t, mu_data0[:,i], c='#7fc97f', linestyle='-', linewidth=2.5, label='L0; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], c='#beaed4', linestyle='-', linewidth=2.5, label='L1; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], c='#fdc086', linestyle='-', linewidth=2.5, label='L2; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], c='#ffff99', linestyle='-', linewidth=2.5, label='L3; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), c='#7fc97f', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), c='#7fc97f', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), c='#beaed4', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), c='#beaed4', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), c='#fdc086', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), c='#fdc086', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), c='#ffff99', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), c='#ffff99', linestyle='-.', linewidth=2.5)
      ax.plot(t, def_values[:,i], 'm.', linewidth=1.5, label='default value')
    elif 0==1: ##### Solid lines for mean values and dash dotted lines for uncertainties, different shades of green and brown #####
      ax.plot(t, mu_data0[:,i], c='darkgreen', linestyle='-', linewidth=2.5)
      ax.plot(t, mu_data1[:,i], c='#238b45', linestyle='-', linewidth=2.5)
      ax.plot(t, mu_data2[:,i], c='#66c2a4', linestyle='-', linewidth=2.5)
      ax.plot(t, mu_data3[:,i], c='#b2e2e2', linestyle='-', linewidth=2.5)
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), c='saddlebrown', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), c='saddlebrown', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), c='chocolate', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), c='chocolate', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), c='burlywood', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), c='burlywood', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), c='wheat', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), c='wheat', linestyle='-.', linewidth=2.5)
      ax.plot(t, def_values[:,i], 'm.', linewidth=1.5, label='default value')

      lines = ax.get_lines()
      legend1 = ax.legend([lines[i] for i in [0,1,2,3,12]], ['L0; $\mu$', 'L1; $\mu$', 'L2; $\mu$', 'L3; $\mu$', 'default value'], loc=1)
      legend2 = ax.legend([lines[i] for i in [4,6,8,10]], ['L0; $\mu \pm 2\sigma$', 'L1; $\mu \pm 2\sigma$', 'L2; $\mu \pm 2\sigma$', 'L3; $\mu \pm 2\sigma$'], loc=4)
      ax.add_artist(legend1)
      ax.add_artist(legend2)
    elif 1==1: ##### Separate figures for mean values and uncertainties #####
      fig2, ax2=plt.subplots(figsize=(10,7.9))
      ax.plot(t, mu_data0[:,i], c='darkgreen', linestyle='-', linewidth=2.5, label='L0; $\mu$')
      ax.plot(t, mu_data1[:,i], c='#238b45', linestyle='-', linewidth=2.5, label='L1; $\mu$')
      ax.plot(t, mu_data2[:,i], c='#66c2a4', linestyle='-', linewidth=2.5, label='L2; $\mu$')
      ax.plot(t, mu_data3[:,i], c='#b2e2e2', linestyle='-', linewidth=2.5, label='L3; $\mu$')
      ax.plot(t, def_values[:,i], 'm.', linewidth=1.5, label='default value')
      ax2.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), c='saddlebrown', linestyle='-', linewidth=2.5, label='L0; $\mu \pm 2\sigma$')
      ax2.plot(t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), c='saddlebrown', linestyle='-', linewidth=2.5)
      ax2.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), c='chocolate', linestyle='-', linewidth=2.5, label='L1; $\mu \pm 2\sigma$')
      ax2.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), c='chocolate', linestyle='-', linewidth=2.5)
      ax2.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), c='burlywood', linestyle='-', linewidth=2.5, label='L2; $\mu \pm 2\sigma$')
      ax2.plot(t, mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), c='burlywood', linestyle='-', linewidth=2.5)
      ax2.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), c='wheat', linestyle='-', linewidth=2.5, label='L3; $\mu \pm 2\sigma$')
      ax2.plot(t, mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), c='wheat', linestyle='-', linewidth=2.5)
      ax2.plot(t, def_values[:,i], 'm.', linewidth=1.5, label='default value')

    if 0==1: # use when mean and uncertainty are put to the same figure
      ax.set_xlabel('Number of iterations')#('Initialisation date')
      #plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
      if pars[i]=='ENTRORG':
        ax.set_ylabel('ENTRORG [10$^{-3}$ m$^{-1}$]')
      else:
        ax.set_ylabel('ENTSHALP')
    
      ax.set_title('Mean values and uncertainties')
  
      #ax.legend(loc=0)#, fontsize = 'small')

      ax.set_xlim([0.0,ndays+1])

      fig.savefig('new_figures/parameter' + str(i+1) + 'levs.png', dpi=300, format='png')

    elif 1==1: # use when mean and uncertainty are put to different figures
      textstr1='\n'.join((r'a'))
      textstr2='\n'.join((r'b'))
      textstr3='\n'.join((r'c'))
      textstr4='\n'.join((r'd'))
      props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
      ax.set_xlabel('Number of iterations')
      ax2.set_xlabel('Number of iterations')
      if pars[i]=='ENTRORG':
        ax.set_ylabel('ENTRORG [10$^{-3}$ m$^{-1}$]')
        ax.text(0.1, 0.95, textstr3, transform=ax.transAxes, fontsize=18, verticalalignment='top', bbox=props)
        ax2.set_ylabel('ENTRORG [10$^{-3}$ m$^{-1}$]')
        ax2.text(0.1, 0.95, textstr4, transform=ax2.transAxes, fontsize=18, verticalalignment='top', bbox=props)
      else:
        ax.set_ylabel('ENTSHALP')
        ax.text(0.1, 0.95, textstr1, transform=ax.transAxes, fontsize=18, verticalalignment='top', bbox=props)
        ax2.set_ylabel('ENTSHALP')
        ax2.text(0.1, 0.95, textstr2, transform=ax2.transAxes, fontsize=18, verticalalignment='top', bbox=props)

      ax.set_title('Mean values')
      ax2.set_title('Uncertainties')
      ax.legend(loc=0)
      ax2.legend(loc=0)
      ax.set_xlim([0.0,ndays+1])
      ax2.set_xlim([0.0,ndays+1])
      fig.savefig('new_figures/parameter' + str(i+1) + 'levs_m.png', dpi=300, format='png')
      fig2.savefig('new_figures/parameter' + str(i+1) + 'levs_u.png', dpi=300, format='png')

if 1==1: ####### Cost functions #######
  for i in range(npars):
      fig, ax=plt.subplots(figsize=(10,7.9))
      ax.plot(t, mu_data1[:,i], 'k-', linewidth=2.5, label='L1; $\mu$, $\mu \pm 2\sigma$')
      #ax.fill_between(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), facecolor='r', alpha=0.7)
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), c='0.0', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), c='0.0', linestyle='-.', linewidth=2.5)
      ax.plot(t, mu_data4[:,i], 'c.-', linewidth=1.0, label='RMSEZ850; $\mu$, $\mu \pm 2\sigma$')
      #ax.plot(t, mu_data4[:,i]-2*np.sqrt(sig_data4[:,i,i]), 'c-', linewidth=1.0)
      #ax.plot(t, mu_data4[:,i]+2*np.sqrt(sig_data4[:,i,i]), 'c-', linewidth=1.0)
      ax.fill_between(t, mu_data4[:,i]-2*np.sqrt(sig_data4[:,i,i]), mu_data4[:,i]+2*np.sqrt(sig_data4[:,i,i]), facecolor='c', alpha=0.25)
      ax.plot(t, def_values[:,i], 'g-', linewidth=1.0, label='default value')
      ax.set_xlabel('Number of iterations')
      #plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
      if pars[i]=='ENTRORG':
        ax.set_ylabel('ENTRORG [10$^{-3}$ m$^{-1}$]')
      else:
        ax.set_ylabel('ENTSHALP')
    
      ax.set_title('Mean values and uncertainties')

      ax.legend(loc=0)#, fontsize = 'small')

      ax.set_xlim([0.0,ndays+1])
      #plt.rcParams.update({'font.size': 18})
      #fig.savefig('new_figures/parameter' + str(i+1) + 'costf.eps', dpi=300, format='eps')
      fig.savefig('new_figures/parameter' + str(i+1) + 'costf.png', dpi=300, format='png')
      #fig.savefig('new_figures/parameter' + str(i+1) + 'costf.pdf', dpi=300, format='pdf')
      fig.clf()

