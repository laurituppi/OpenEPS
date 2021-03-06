import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys
import os
import matplotlib.lines as mlines
from numpy.linalg import inv, det
from numpy import matmul

npars = int(sys.argv[1])
inputdir = sys.argv[2]
outputdir = sys.argv[3]
optimizer = int(sys.argv[4])
npar = int(sys.argv[5])
calculation_method = int(sys.argv[6])
name = sys.argv[7]
name=name+'_multivariate'

samplefile = "sampleout.dat"
mufile = "mufile.dat"
sigfile = "sigfile.dat"

mu_def=np.array([2.0, 0.00175])
#mu_def[0]=2.0
#mu_def[1]=0.00175
sig_def=np.array([[0.03**2, 0.0], [0.0, 0.00001**2]])
#sig_def[0]=0.3
#sig_def[1]=0.0001 #0.000263

subdirectories = sorted(os.listdir(inputdir))
ndays = np.size(subdirectories)
mu_data = np.zeros(ndays)
sig_data = np.zeros(ndays)

def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

def plot_stat_test(ks_data, directories, ndays, outputdir, name):
    plt.figure()
    t2 = np.arange(ndays)
    avg_f15 = np.mean(ks_data[0:14])
    avg_l15 = np.mean(ks_data[ndays-15:ndays])
    avg_all = np.mean(ks_data)
    plt.plot(t2+1, ks_data, 'b', t2[14]+1, avg_f15, 'gx', t2[ndays-1]+1, avg_l15, 'rx')
    plt.title('Bhattacharyya distance')
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
    first15 = mlines.Line2D([],[], color='g', marker='x',linestyle='', label='First 15 = '+str(avg_f15))
    last15 = mlines.Line2D([],[], color='r', marker='x',linestyle='', label='Last 15 = '+str(avg_l15))
    plt.legend(handles=[sdistance, fdistance, first15, last15], loc=0, fontsize = 'x-small')
    plt.savefig(outputdir + '/' + name + 'multi.png')
    print('printing in ', outputdir, '/', name, '.png')
    plt.clf()
    stats=[ks_data[0],ks_data[ndays-1],avg_f15,avg_l15,avg_all]
    fname1=str(outputdir + '/data/' + name + '.txt')
    fname2=str(outputdir + '/data/' + name + '_all_multi.txt')
    np.savetxt(fname1, stats)
    np.savetxt(fname2, ks_data)

def calc_bhattacharyya_1d(mu, sig, mu_def, sig_def, ndays, parameter):
    distance = np.zeros(ndays)
    for i in range(ndays):
      distance[i] = 0.25 * np.log(0.25 *( (sig[i]**2/sig_def[parameter-1]**2)+(sig_def[parameter-1]**2/sig[i]**2)+2.0 ) + 0.25 * ((mu[i]-mu_def[parameter-1])**2/(sig[i]**2+sig_def[parameter-1]**2)))
    return distance

def get_mu_1d(dirs, parameter, ndays, optimizer):
    mu = np.zeros(ndays)
    if optimizer==1:
      for i in range(ndays):
        mu1=np.loadtxt(get_input_file(dirs[i], "mufile.dat"))
        mu[i]=mu1[parameter-1]
    elif optimizer==2:
      for i in range(ndays):
        sample=np.loadtxt(get_input_file(dirs[i], "sampleout.dat"))
        mu[i]=np.mean(sample[parameter-1])
    return mu

def get_sigma_1d(dirs, parameter, ndays, optimizer):
    sig = np.zeros(ndays)
    if optimizer==1:
      for i in range(ndays):
        sig1=np.loadtxt(get_input_file(subdirectories[i], "sigfile.dat"))
        sig[i]=(sig1[parameter-1,parameter-1])**0.5
    elif optimizer==2:
      for i in range(ndays):
        sample=np.loadtxt(get_input_file(subdirectories[i], "sampleout.dat"))
        sig[i]=np.std(sample[parameter-1])
    return sig

##########################################
def get_mu(dirs, ndays, npars, optimizer):
    mu = np.zeros((npars,ndays))
    if optimizer==1:
      for i in range(ndays):
        mu1=np.loadtxt(get_input_file(dirs[i], "mufile.dat"))
        mu[:,i]=mu1
    elif optimizer==2:
      for i in range(ndays):
        sample=np.loadtxt(get_input_file(dirs[i], "sampleout.dat"))
        mu[:,i]=np.mean(sample)
    return mu

def get_sigma(dirs, ndays, npars, optimizer):
    sig = np.zeros((npars,npars,ndays))
    if optimizer==1:
      for i in range(ndays):
        sig1=np.loadtxt(get_input_file(subdirectories[i], "sigfile.dat"))
        sig[:,:,i]=sig1
    elif optimizer==2:
      for i in range(ndays):
        sample=np.loadtxt(get_input_file(subdirectories[i], "sampleout.dat"))
        #sig1=np.cov(sample)
        
        sig[:,:,i]=np.cov(sample.T)
    return sig

def calc_bhattacharyya(mu, sig, mu_def, sig_def, ndays):
    distance = np.zeros(ndays)
    for i in range(ndays):
      mu_diff = np.ndarray((2,1))
      mu_diff[:,0] = mu[:,i]-mu_def
      sig_comb = (sig[:,:,i]+sig_def)/2.0
      if 1==1:
        a11 = np.matmul(mu_diff.T, inv(sig_comb))
        a22 = np.matmul(a11, mu_diff)
        a2 = 0.5*np.log(det(sig_comb)/(det(sig[:,:,i])*det(sig_def))**0.5)
        #print(a11, a22, a2)
        distance[i] = 0.125*a22+a2
      elif 0==1:
        a1 = np.matmul(mu_diff, mu_diff.T)
        #print(a1)
        #print(np.shape(mu_diff), np.shape(mu_diff.T))
        a2 = np.matmul(inv(sig_comb), a1)
        
        distance[i] = 0.25*np.matrix.trace(a2)
    return distance
###########################################


mu = get_mu(subdirectories, ndays, npars, optimizer)
sig = get_sigma(subdirectories, ndays, npars, optimizer)
#print mu, sig
dist = calc_bhattacharyya(mu, sig, mu_def, sig_def, ndays)
plot_stat_test(dist, subdirectories, ndays, outputdir, name)
