import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys
import os

ndays = int(sys.argv[1])
npars = int(sys.argv[2])
nens = int(sys.argv[3])
inputdir = sys.argv[4]
outputdir = sys.argv[5]
default_value1 = float(sys.argv[6])
default_value2 = float(sys.argv[7])

mufile = "mufile.dat"
sigfile = "sigfile.dat"
samplefile = "sampleout.dat"
#winfofile = "winfo.dat"
scores = "score.dat"

t = np.arange(ndays)

mu_data = np.zeros((ndays, npars))
mu_data[0] = np.loadtxt("/wrk/lautuppi/DONOTREMOVE/init_mu_sigma/mufile.dat")
sig_data = np.zeros((ndays, npars, npars))
sig_data[0] = np.loadtxt("/wrk/lautuppi/DONOTREMOVE/init_mu_sigma/sigfile.dat")
sample_data = np.zeros((ndays, nens, npars))
weights_data = np.ones((ndays, nens, npars))
score_data = np.zeros((ndays, nens))
def_values = np.zeros(npars)

def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

def_values[0]=default_value1
def_values[1]=default_value2
default_value = np.zeros(ndays+1)
mean_score = np.zeros(ndays)

subdirectories = os.listdir(inputdir)
subdirectories = sorted(subdirectories)

for i in range(ndays-1):
    mu_data[i,:] = np.loadtxt(get_input_file(subdirectories[i], mufile))
    sig_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i], sigfile))
    sample_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i], samplefile))

    try:
      score_data[i,:] = np.genfromtxt(get_input_file(subdirectories[i], scores))
    except Exception:
      print 'no score data in', subdirectories[i]
      score_data[i,:] = [-10.0,-10.0,-10.0]
    mean_score[i] = np.sum(score_data[i,:])/nens
    if i>=0 and i<ndays-1:
        print 'processing date:', subdirectories[i]
        #weights_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i+1], winfofile))

pars = ['ENTSHALP','ENTRORG']
for i in range(npars):
    sample_data_0 = np.copy(sample_data)
    sample_data_1 = np.copy(sample_data)
    
    weights = weights_data[:,:,1]
    color_w = np.ones((ndays,nens)) - weights/np.max(weights, axis=0)

    for tind in range(ndays):
        #default_value[tind] = def_values[i]
        if tind<ndays-1:
            for ensind in range(nens):
                plt.plot(tind+1, sample_data_0[tind,ensind,i], color=(str(color_w[tind, ensind])), marker='o', linestyle='')
                plt.plot(tind+1, sample_data_1[tind,ensind,i], color=(str(color_w[tind, ensind])), marker='o', linestyle='')
        elif tind==ndays-1:
            for ensind in range(nens):
                plt.plot(tind+1, sample_data_0[tind,ensind,i], color='k', marker='x', linestyle='')
                plt.plot(tind+1, sample_data_1[tind,ensind,i], color='k', marker='x', linestyle='')

    for tind in range(ndays+1):
        default_value[tind] = def_values[i]
    
      #default_value[ndays+1] = def_values[i]
    plt.plot(t, mu_data[:,i], 'r*-', linewidth=2.0)
    plt.plot(t, mu_data[:,i]-2*np.sqrt(sig_data[:,i,i]), 'b.-', linewidth=2.0)
    plt.plot(t, mu_data[:,i]+2*np.sqrt(sig_data[:,i,i]), 'b.-', linewidth=2.0)
    plt.plot(t, default_value, 'g-', linewidth=2.0)

    axes = plt.gca()
    axes.set_xlim([0.0,ndays+1])
    if i==0:
      axes.set_ylim([0.0,4.5])
    #elif i==1:
    #  axes.set_ylim([-0.001,0.005])

    plt.xlabel('ENS number')
    plt.ylabel('Parameter value')
    
    plt.title(pars[i])

    sample_0 = mlines.Line2D([],[], color=('0.8'), marker='o',linestyle='', label='Sampled data')
    sample_1 = mlines.Line2D([],[], color=('0.0'), marker='o',linestyle='', label='Resampled data')
    red_ball = mlines.Line2D([], [], color='red', marker='*', label='$\mu$')
    limits = mlines.Line2D([],[], color='blue', marker='.', label='$\mu \pm 2\sigma$')
    true_value = mlines.Line2D([], [], color='green', marker='_', label='Default value')
    
    plt.legend(handles=[sample_0, sample_1, red_ball, limits, true_value], loc=0, fontsize = 'x-small')
    plt.savefig(outputdir + '/sampling_time' + str(i+1) + '.png')
    plt.clf()



plt.figure()
t2 = np.arange(ndays)
for j in range(nens):
  plt.plot(t2+1,score_data[:,j],'g.')

plt.plot(t2+1,mean_score,'r')
ensmem = mlines.Line2D([], [], color='green', marker='_', label='ens members')
ensmean = mlines.Line2D([], [], color='red', marker='_', label='mean score')
axes = plt.gca()
axes.set_xlim([0,ndays+1])
plt.title('Cost function values')
plt.xlabel('ENS number')
plt.ylabel('Cost function value')
plt.legend(handles=[ensmem, ensmean], loc=0)
plt.grid()
plt.savefig(outputdir + '/scores' + '.png')
plt.clf()
