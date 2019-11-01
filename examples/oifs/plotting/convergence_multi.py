import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys
import os
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

if 0==1:
  for i in range(npars):
      print('processing parameter:', pars[i])
      #print mu_data3[:,i]
      #plt.figure()
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

      #axes = plt.gca()
      ax.set_xlim([0.0,ndays+1])
      plt.rcParams.update({'font.size': 18})
      fig.savefig('new_figures/parameter' + str(i+1) + 'levs.eps', dpi=300, format='eps')
      fig.savefig('new_figures/parameter' + str(i+1) + 'levs.png', dpi=300, format='png')
      fig.savefig('new_figures/parameter' + str(i+1) + 'levs.pdf', dpi=300, format='pdf')
      fig.clf()

if 1==1:
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
  for i in range(1,-1,-1):
  #for i in range(npars):
    print('processing parameter:', pars[i])

    fig, ax=plt.subplots(figsize=(10,7.9))

    if 0==1:
      ax.plot(t, mu_data0[:,i], 'bX-', linewidth=1.5, markersize=6.0, label='level 0; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], 'md-', linewidth=1.5, markersize=6.0, label='level 1; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], 'ro-', linewidth=1.5, markersize=6.0, label='level 2; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], 'ys-', linewidth=1.5, markersize=6.0, label='level 3; $\mu$, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), 'bX', t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), 'bX')
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), 'md', t,  mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), 'md')
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), 'ro', t,  mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), 'ro')
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), 'ys', t,  mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), 'ys')
    elif 0==1:
      ax.plot(t, mu_data0[:,i], 'b.-', linewidth=1.5, markersize=8.0, label='level 0, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data1[:,i], 'm.-', linewidth=1.5, markersize=8.0, label='level 1, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data2[:,i], 'r.-', linewidth=1.5, markersize=8.0, label='level 2, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data3[:,i], 'y.-', linewidth=1.5, markersize=8.0, label='level 3, $\mu \pm 2\sigma$')
      ax.plot(t, mu_data0[:,i]-2*np.sqrt(sig_data0[:,i,i]), 'bP', t, mu_data0[:,i]+2*np.sqrt(sig_data0[:,i,i]), 'bP')
      ax.plot(t, mu_data1[:,i]-2*np.sqrt(sig_data1[:,i,i]), 'mP', t,  mu_data1[:,i]+2*np.sqrt(sig_data1[:,i,i]), 'mP')
      ax.plot(t, mu_data2[:,i]-2*np.sqrt(sig_data2[:,i,i]), 'rP', t,  mu_data2[:,i]+2*np.sqrt(sig_data2[:,i,i]), 'rP')
      ax.plot(t, mu_data3[:,i]-2*np.sqrt(sig_data3[:,i,i]), 'yP', t,  mu_data3[:,i]+2*np.sqrt(sig_data3[:,i,i]), 'yP')
    elif 1==1:
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

    ax.set_xlabel('Number of ensemble')#('Initialisation date')
    #plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
    if pars[i]=='ENTRORG':
      ax.set_ylabel('ENTRORG [10$^{-3}$ m$^{-1}$]')
    else:
      ax.set_ylabel('ENTSHALP')
    
    ax.set_title('Mean values and uncertainties')

    ax.legend(loc=0)#, fontsize = 'small')
    plt.rcParams.update({'font.size': 18})
      #axes = plt.gca()
    ax.set_xlim([0.0,ndays+1])
    #plt.rcParams.update({'font.size': 20})
    fig.savefig('new_figures/parameter' + str(i+1) + 'levs.png', dpi=300, format='png')

if 1==1:
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
      ax.set_xlabel('Number of ensemble')
      #plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
      if pars[i]=='ENTRORG':
        ax.set_ylabel('ENTRORG [10$^{-3}$ m$^{-1}$]')
      else:
        ax.set_ylabel('ENTSHALP')
    
      ax.set_title('Mean values and uncertainties')

      ax.legend(loc=0)#, fontsize = 'small')

      #axes = plt.gca()
      ax.set_xlim([0.0,ndays+1])
      plt.rcParams.update({'font.size': 18})
      fig.savefig('new_figures/parameter' + str(i+1) + 'costf.eps', dpi=300, format='eps')
      fig.savefig('new_figures/parameter' + str(i+1) + 'costf.png', dpi=300, format='png')
      fig.savefig('new_figures/parameter' + str(i+1) + 'costf.pdf', dpi=300, format='pdf')
      fig.clf()

