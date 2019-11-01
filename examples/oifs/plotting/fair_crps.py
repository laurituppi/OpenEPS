import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys
import os

#npars = int(sys.argv[1])
nens = int(sys.argv[1])
inputdir = sys.argv[2]
outputdir = sys.argv[3]
parameter = int(sys.argv[4])
name = sys.argv[5]

#nens = 1000
#ntime = 10


#mu_o = 2.2

#sigma_f = 1.0
#sigma_o = 1.5

def get_input_file(inputdir,day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

def get_samples(ndays,nens,inputdir,dirs,parameter,fname):
    samples = np.zeros((ndays,nens))
    for i in range(ndays):
      sample = np.loadtxt(get_input_file(inputdir, dirs[i], fname))
      samples[i,:] = sample[:,parameter-1]
    return samples

def crps(ensf,obs,ndays,nens):
  #ensf = samples
  #obs = np.zeros(ntime)
  #obs=mu_def
  crps_sum=0.0
  crps_vector = np.zeros(ndays)

  for i in range(ndays):
    xasorted = sorted(ensf[i,:], key=float)  
    crps = 0.0             
      # calculate crps: 
    for m in range(nens-1):
      if obs <= xasorted[m]:
          tmp = (xasorted[m+1]-xasorted[m])*np.square(1-1.0*(m+1)/nens)
      elif xasorted[m] < obs <= xasorted[m+1]:
          tmp =(obs - xasorted[m])*np.square(1.0*(m+1)/nens) + (xasorted[m+1] - obs)*np.square(1-1.0*(m+1)/nens)
      elif xasorted[m+1] < obs:
          tmp = (xasorted[m+1] - xasorted[m])*np.square(1.0*(m+1)/nens)
      crps = crps + tmp

    crps_sum+=crps
    crps_vector[i]=crps
  #print crps_sum/float(ndays)
  return crps_vector

def fair_crps(samples,mu_def,ndays,nens):
  ensf = samples
  #obs = np.zeros(ntime)
  obs=mu_def
  crps_sum=0.0
  crps_vector = np.zeros(ndays)

  for i in range(ndays):
    tmp1=0.0
    tmp2=0.0
    for j in range(nens):
      tmp1 = tmp1 + abs(ensf[i,j]-obs)
    for j in range(nens):
      for k in range(nens):
        tmp2 = tmp2 + abs(ensf[i,j]-ensf[i,k])
    
    crps1 = tmp1/float(nens)
    crps2 = tmp2/(float(2*nens)*float(nens-1))
    #crps = crps1 - crps2
    #crps_vector[i]=crps1/crps2-1.0
    crps_vector[i]=crps2 #+crps2
  return crps_vector

def plot_stat_test(ks_data, directories, ndays, outputdir, name):
    plt.figure()
    t2 = np.arange(ndays)
    avg_f15 = np.mean(ks_data[0:14])
    avg_l15 = np.mean(ks_data[ndays-15:ndays])
    avg_all = np.mean(ks_data)
    plt.plot(t2+1, ks_data, 'b', t2[14]+1, avg_f15, 'gx', t2[ndays-1]+1, avg_l15, 'rx')
    plt.title('Fair CRPS, part 2')
    plt.xlabel('Initialization date')
    plt.ylabel('Score')
    a = int(subdirectories[0])
    al = 1
    b = int(round(int(directories[ndays-int(round(ndays/5))])))
    bl = int(round(4*ndays/5))
    c = int(round(int(directories[ndays-int(round(2*ndays/5))])))
    cl = int(round(3*ndays/5))
    d = int(round(int(directories[ndays-int(round(3*ndays/5))])))
    dl = int(round(2*ndays/5))
    e = int(round(int(directories[ndays-int(round(4*ndays/5))])))
    el = int(round(ndays/5))
    f = int(directories[ndays-1])
    fl = ndays-1
    plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
    sdistance = mlines.Line2D([],[], color='b', marker='_',linestyle='', label='First value = '+str(ks_data[0]))
    fdistance = mlines.Line2D([],[], color='b', marker='_',linestyle='', label='Last value = '+str(ks_data[ndays-1]))
    first15 = mlines.Line2D([],[], color='g', marker='x',linestyle='', label='Avg first 15 = '+str(avg_f15))
    last15 = mlines.Line2D([],[], color='r', marker='x',linestyle='', label='Avg last 15 = '+str(avg_l15))
    plt.legend(handles=[sdistance, fdistance, first15, last15], loc=0, fontsize = 'x-small')
    plt.savefig(outputdir + '/' + name + '.png')
    print('printing in ', outputdir, '/', name, '.png')
    plt.clf()
    stats=[ks_data[0],ks_data[ndays-1],avg_f15,avg_l15,avg_all]
    fname1=str(outputdir + '/data2/' + name + '_fcrps.txt')
    fname2=str(outputdir + '/data2/' + name + '_fcrps_all.txt')
    np.savetxt(fname1, stats)
    np.savetxt(fname2, ks_data)
########################################################
########################################################
if parameter==1:
  mu_def = 2.0
elif parameter==2:
  mu_def = 0.00175

subdirectories = sorted(os.listdir(inputdir))
ndays = np.size(subdirectories)
fname = 'sampleout.dat'
all_samples = get_samples(ndays,nens,inputdir,subdirectories,parameter,fname)
crps = fair_crps(all_samples,mu_def,ndays,nens)
#print(crps)
plot_stat_test(crps, subdirectories, ndays, outputdir, name)
