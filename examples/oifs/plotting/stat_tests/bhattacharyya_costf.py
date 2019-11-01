import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sys
import os
import matplotlib.lines as mlines
from numpy.linalg import inv, det
from numpy import matmul

inputdir1 = sys.argv[1]
inputdir2 = sys.argv[2]
outputdir = sys.argv[3]
#optimizer = int(sys.argv[4])
calculation_method = int(sys.argv[4])
name = sys.argv[5]
name=name+'_costf'

subdirectories1 = sorted(os.listdir(inputdir1))
subdirectories2 = sorted(os.listdir(inputdir2))
ndays = np.size(subdirectories1)

def get_input_file(inputdir, day, name):
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
    a = int(directories[0])
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
    plt.savefig(outputdir + '/' + name + '.png')
    print('printing in ', outputdir, '/', name, '.png')
    plt.clf()
    stats=[ks_data[0],ks_data[ndays-1],avg_f15,avg_l15,avg_all]
    fname1=str(outputdir + '/data/' + name + '.txt')
    fname2=str(outputdir + '/data/' + name + '_all.txt')
    np.savetxt(fname1, stats)
    np.savetxt(fname2, ks_data)

def get_mu_sigma_1d(dirs, ndays, inputdir, fname, size):
    mu = np.zeros(ndays)
    sigma = np.zeros(ndays)
    for i in range(ndays):
      costf=np.loadtxt(get_input_file(inputdir, dirs[i], fname))
      costf2=costf[:size-1]
      mu[i]=np.mean(costf2)
      sigma[i]=np.std(costf2)
    return mu, sigma

def calc_bhattacharyya_1d(mu, sig, mu_def, sig_def, ndays):
    distance = np.zeros(ndays)
    for i in range(ndays):
      distance[i] = 0.25 * np.log(0.25 *( (sig[i]**2/sig_def[i]**2)+(sig_def[i]**2/sig[i]**2)+2.0 ) + 0.25 * ((mu[i]-mu_def[i])**2/(sig[i]**2+sig_def[i]**2)))
    return distance

#mu_def, sig_def = get_mu_sigma_1d(subdirectories1, ndays, inputdir1, 'score.dat')
cost=np.loadtxt(get_input_file(inputdir2, subdirectories2[0], 'scores.dat'))
size=np.size(cost)
#print(cost)
mu, sig = get_mu_sigma_1d(subdirectories2, ndays, inputdir2, 'scores.dat', size)
mu_def, sig_def = get_mu_sigma_1d(subdirectories1, ndays, inputdir1, 'score.dat', size)
distances = calc_bhattacharyya_1d(mu, sig, mu_def, sig_def, ndays)
plot_stat_test(distances, subdirectories1, ndays, outputdir, name)
