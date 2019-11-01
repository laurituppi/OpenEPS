import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys
import os

#ndays = int(sys.argv[1])
npars = int(sys.argv[1])
nens = int(sys.argv[2])
inputdir = sys.argv[3]
outputdir = sys.argv[4]

def_values = np.zeros(npars)

for k in range(npars):
  def_values[k]=float(sys.argv[k+5])

subdirectories = os.listdir(inputdir)
subdirectories = sorted(subdirectories)
ndays = np.size(subdirectories)

#mufile = "mufile.dat"
#sigfile = "sigfile.dat"
samplefile = "sampleout.dat"
scores = "score.dat"

t = np.arange(ndays)

mu_data = np.zeros((ndays, npars))
sig_data = np.zeros((ndays, npars))
cov_data = np.zeros((ndays, npars, npars))
sample_data = np.zeros((ndays, nens, npars))
score_data = np.zeros((ndays, nens))


def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

default_value = np.zeros(ndays)
mean_score = np.zeros(ndays)



for i in range(ndays-1):
#for i in subdirectories:
    print('processing date:', subdirectories[i])
    #mu_data[i+1,:] = np.loadtxt(get_input_file(subdirectories[i], mufile))
    #sig_data[i+1,:] = np.loadtxt(get_input_file(subdirectories[i], sigfile))
    sample_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i], samplefile))
    for j in range(npars):
      mu_data[i+1,j] = np.mean(sample_data[i,:,j])
      sig_data[i+1,j] = np.std(sample_data[i,:,j])

    cov_data[i+1,:,:] = np.corrcoef(sample_data[i,:,:].T)
    try:
      score_data[i+1,:] = np.genfromtxt(get_input_file(subdirectories[i], scores))
    except Exception:
      print('no score data in', subdirectories[i])
      score_data[i+1,:] = [-10.0,-10.0,-10.0]
    mean_score[i+1] = np.sum(score_data[i+1,:])/nens

a = int(subdirectories[0])
al = 1
b = int(round(int(subdirectories[ndays-int(round(ndays/5))])))
bl = int(round(4*ndays/5))
c = int(round(int(subdirectories[ndays-int(round(2*ndays/5))])))
cl = int(round(3*ndays/5))
d = int(round(int(subdirectories[ndays-int(round(3*ndays/5))])))
dl = int(round(2*ndays/5))
e = int(round(int(subdirectories[ndays-int(round(4*ndays/5))])))
el = int(round(ndays/5))
f = int(subdirectories[ndays-1])
fl = ndays-1

pars = ['ENTSHALP','ENTRORG','DETRPEN','RPRCON','RDEPTHS']
for i in range(npars):
    sample_data_0 = np.copy(sample_data)
    sample_data_1 = np.copy(sample_data)
    #plt.figure(figsize=(6.4,7.8))
    plt.figure(figsize=(12,10))
    for tind in range(1,ndays):
        #default_value[tind] = def_values[i]
        #print(subdirectories[tind])
        for ensind in range(nens):
            if pars[i]=='DETRPEN':
              plt.plot(tind, sample_data_0[tind-1,ensind,i]*10000, color='k', marker='.', linestyle='')
            else:
              plt.plot(tind, sample_data_0[tind-1,ensind,i], color='k', marker='.', linestyle='')
            #plt.plot(tind, sample_data_1[tind-1,ensind,i], color='k', marker='.', linestyle='')

    for tind in range(ndays):
        default_value[tind] = def_values[i]
    
      #default_value[ndays+1] = def_values[i]
    if pars[i]=='DETRPEN':
      plt.plot(t[1:], mu_data[1:,i]*10000, 'r*-', linewidth=2.0)
      plt.plot(t[1:], (mu_data[1:,i]-2*(sig_data[1:,i]))*10000, 'b.-', linewidth=2.0)
      plt.plot(t[1:], (mu_data[1:,i]+2*(sig_data[1:,i]))*10000, 'b.-', linewidth=2.0)
      plt.plot(t[1:], default_value[1:]*10000, 'g-', linewidth=2.0)
    else:
      plt.plot(t[1:], mu_data[1:,i], 'r*-', linewidth=2.0)
      plt.plot(t[1:], mu_data[1:,i]-2*(sig_data[1:,i]), 'b.-', linewidth=2.0)
      plt.plot(t[1:], mu_data[1:,i]+2*(sig_data[1:,i]), 'b.-', linewidth=2.0)
      plt.plot(t[1:], default_value[1:], 'g-', linewidth=2.0)

    axes = plt.gca()
    axes.set_xlim([0.0,ndays+1])
    #if i==0:
    #  axes.set_ylim([0.0,10.0])
    #elif i==1:
    #  axes.set_ylim([-0.001,0.003])

    plt.xlabel('Initialisation date')
    plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
    if pars[i]=='ENTSHALP':
      plt.ylabel('Parameter value')
    elif pars[i]=='ENTRORG':
      plt.ylabel('Parameter value [m$^{-1}$]')
    elif pars[i]=='DETRPEN':
      plt.ylabel('Parameter value [10$^{-4}$ m$^{-1}$]')
    elif pars[i]=='RPRCON':
      plt.ylabel('Parameter value [s$^{-1}$]')
    elif pars[i]=='RDEPTHS':
      plt.ylabel('Parameter value [Pa]')
    
    plt.title(pars[i] + ', DE')

    sample_0 = mlines.Line2D([],[], color=('0.0'), marker='.',linestyle='', label='Parameter values')
    red_ball = mlines.Line2D([], [], color='red', marker='*', label='$\mu$')
    limits = mlines.Line2D([],[], color='blue', marker='.', label='$\mu \pm 2\sigma$')
    true_value = mlines.Line2D([], [], color='green', marker='_', label='Default value')
    
    plt.legend(handles=[sample_0, red_ball, limits, true_value], loc=0)#, fontsize = 'x-small')
    plt.rcParams.update({'font.size': 22})
    plt.savefig(outputdir + '/parameter' + str(i+1) + '.eps', dpi=300, format='eps')
    plt.savefig(outputdir + '/parameter' + str(i+1) + '.png', dpi=300, format='png')
    plt.savefig(outputdir + '/parameter' + str(i+1) + '.pdf', dpi=300, format='pdf')
    plt.clf()



plt.figure()
t2 = np.arange(ndays)
t22 = t2[1:]
A = np.vstack([t22, np.ones(len(t22))]).T
m, con = np.linalg.lstsq(A, mean_score[1:], rcond=None)[0]
linear_fit = np.zeros(ndays-1)
linear_fit = t22 * m + con
print('linear fit coefficients: ', m, con)
for j in range(nens):
  plt.plot(t22,score_data[1:,j],'g.')

plt.plot(t22,mean_score[1:],'r')
plt.plot(t22,linear_fit,'b')
ensmem = mlines.Line2D([], [], color='green', marker='.',linestyle='', label='ens members')
ensmean = mlines.Line2D([], [], color='red', marker='_', label='mean score')
ensfit = mlines.Line2D([], [], color='blue', marker='_', label='linear fit')
axes = plt.gca()
axes.set_xlim([0,ndays+1])
plt.title('Moist total energy norm')
plt.xlabel('Initialization date')
plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
plt.ylabel('Cost function value [J/kg]')
plt.legend(handles=[ensmem, ensmean, ensfit], loc=0)
plt.grid()
plt.savefig(outputdir + '/scores' + '.png')
plt.clf()

print('average correlation: ', sum(cov_data[:,0,1])/float(len(cov_data[:,0,1])))
plt.figure()
plt.plot(t2,cov_data[:,0,1],'b')
axes = plt.gca()
axes.set_xlim([0,ndays+1])
plt.title('Correlation')
plt.xlabel('Initialization date')
plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
plt.ylabel('Correlation coefficient')
plt.grid()
plt.savefig(outputdir + '/correlation' + '.png')
plt.clf()


