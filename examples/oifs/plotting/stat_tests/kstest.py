
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys
import os
#print('test1')

npars = int(sys.argv[1])
#nens = int(sys.argv[2])
inputdir = sys.argv[2]
outputdir = sys.argv[3]
optimizer = int(sys.argv[4])
parameter = int(sys.argv[5])
calculation_method = int(sys.argv[6])
#print('test2')
name = sys.argv[7]
#print('test3')
#print(name)
#name='figure'
name=name+'_par'+str(parameter)

samplefile = "sampleout.dat"
mufile = "mufile.dat"
sigfile = "sigfile.dat"

mu_def=np.zeros(2)
mu_def[0]=2.0
mu_def[1]=0.00175
sig_def=np.zeros(2)
sig_def[0]=0.3
sig_def[1]=0.0001 #0.000263

bound_def=np.zeros((2,2))
bound_def[0,0] = 1.0
bound_def[1,0] = 3.0
bound_def[0,1] = 0.00155
bound_def[1,1] = 0.00195



subdirectories = sorted(os.listdir(inputdir))
#print(subdirectories)
ndays = np.size(subdirectories)
mu_data = np.zeros(ndays)
sig_data = np.zeros(ndays)

def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

def plot_kstest(ks_data, directories, ndays, outputdir, name):
    plt.figure()
    t2 = np.arange(ndays)
    plt.plot(t2+1, ks_data)
    plt.title('KS test results')
    plt.xlabel('Initialization date')
    plt.ylabel('Score [0, 1]')
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
    plt.savefig(outputdir + '/' + name + '.png')
    print 'printing in ', outputdir, '/', name, '.png'
    plt.clf()

#sig=np.loadtxt(get_input_file(subdirectories[0], "sigfile.dat"))
#print((sig[parameter-1,parameter-1])**0.5)

kstest=np.zeros((ndays,2))

if calculation_method==1:
  if optimizer==1:
    def_distr = stats.norm.rvs(size=1000000, loc=mu_def[parameter-1], scale=sig_def[parameter-1])
    for i in range(ndays):
      mu=np.loadtxt(get_input_file(subdirectories[i], mufile))
      sig=np.loadtxt(get_input_file(subdirectories[i], sigfile))
      distr = stats.norm.rvs(size=1000000, loc=mu[parameter-1], scale=(sig[parameter-1,parameter-1])**0.5)
      d, p = stats.ks_2samp(distr, def_distr)
      kstest[i,0]=d
      kstest[i,1]=subdirectories[i]
      #print(',mu= ',mu[parameter-1], ',dsig= ', sig[parameter-1,parameter-1]**0.5-sig_def[parameter-1],'d= ',d)
      print(d,p)
    plot_kstest(kstest[:,0], subdirectories, ndays, outputdir, name)
    #np.savetxt(kstest, inputdir+'/kstest.dat')
  elif optimizer==2:
    def_distr = np.random.uniform(0.00155, 0.00195, size=1000000)
    for i in range(ndays):
      sample=np.loadtxt(get_input_file(subdirectories[i], samplefile))
      #mu=np.mean(sample[:,parameter-1])
      #sig=np.std(sample[:,parameter-1])
      #distr = stats.norm.rvs(size=1000000, loc=mu, scale=sig)
      #d, p = stats.ks_2samp(distr, def_distr)
      #kstest[i,0]=d
      #kstest[i,1]=subdirectories[i]
      #print('d= ',d, ',mu= ', mu, ',sig= ', sig)
      minimum=min(sample[:,parameter-1])
      maximum=max(sample[:,parameter-1])
      distr=np.random.uniform(minimum, maximum, size=1000000)
      d, p = stats.ks_2samp(distr, def_distr)
      kstest[i,0]=d
      kstest[i,1]=subdirectories[i]
      print(d,p)
    plot_kstest(kstest[:,0], subdirectories, ndays, outputdir, name)
    #np.savetxt(kstest, inputdir+'/kstest.dat')

elif calculation_method==2:
  sample=np.loadtxt(get_input_file(subdirectories[1], samplefile))
  nens=np.size(sample[:,parameter-1])
  if optimizer==1:
    def_distr = stats.norm.rvs(size=1000000, loc=mu_def[parameter-1], scale=sig_def[parameter-1])
    for i in range(ndays):
      sample=np.loadtxt(get_input_file(subdirectories[i], samplefile))
      distr = sample[:,parameter-1]
      d, p = stats.ks_2samp(distr, def_distr)
      kstest[i,0]=d
      kstest[i,1]=subdirectories[i]
      #print(',mu= ',mu[parameter-1], ',dsig= ', sig[parameter-1,parameter-1]**0.5-sig_def[parameter-1],'d= ',d)
      #print(d,p)
    plot_kstest(kstest[:,0], subdirectories, ndays, outputdir, name)
    #np.savetxt(kstest, inputdir+'/kstest.dat')
  elif optimizer==2:
    def_distr=np.random.uniform(0.00155, 0.00205, size=1000000)
    for i in range(ndays):
      sample=np.loadtxt(get_input_file(subdirectories[i], samplefile))
      distr=sample[:,parameter-1]
      d, p = stats.ks_2samp(distr, def_distr)
      kstest[i,0]=d
      kstest[i,1]=subdirectories[i]
      #print('d= ',d, ',mu= ', mu, ',sig= ', sig)
      print(d,p)
    plot_kstest(kstest[:,0], subdirectories, ndays, outputdir, name)
    #np.savetxt(kstest, inputdir+'/kstest.dat')

