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
default_value1 = float(sys.argv[5])
default_value2 = float(sys.argv[6])

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
def_values = np.zeros(npars)

def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

def_values[0]=default_value1
def_values[1]=default_value2
default_value = np.zeros(ndays)
mean_score = np.zeros(ndays)



for i in range(ndays-1):
#for i in subdirectories:
    print('processing date:', subdirectories[i])
    #mu_data[i+1,:] = np.loadtxt(get_input_file(subdirectories[i], mufile))
    #sig_data[i+1,:] = np.loadtxt(get_input_file(subdirectories[i], sigfile))
    sample_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i], samplefile))
    mu_data[i+1,0] = np.mean(sample_data[i,:,0])
    mu_data[i+1,1] = np.mean(sample_data[i,:,1])
    sig_data[i+1,0] = np.std(sample_data[i,:,0])
    sig_data[i+1,1] = np.std(sample_data[i,:,1])
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

pars = ['ENTSHALP','ENTRORG']
for i in range(npars):
    sample_data_0 = np.copy(sample_data)
    sample_data_1 = np.copy(sample_data)
    plt.figure(figsize=(12,10))

    for tind in range(1,ndays):
        #default_value[tind] = def_values[i]
        #print(subdirectories[tind])
        for ensind in range(nens):

            plt.plot(tind, sample_data_0[tind-1,ensind,i], color='k', marker='.', linestyle='')
            plt.plot(tind, sample_data_1[tind-1,ensind,i], color='k', marker='.', linestyle='')

    for tind in range(ndays):
        default_value[tind] = def_values[i]
    
      #default_value[ndays+1] = def_values[i]
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
    
    plt.title(pars[i])

    sample_0 = mlines.Line2D([],[], color=('0.0'), marker='.',linestyle='', label='Sampled values')
    red_ball = mlines.Line2D([], [], color='red', marker='*', label='$\mu$')
    limits = mlines.Line2D([],[], color='blue', marker='.', label='$\mu \pm 2\sigma$')
    true_value = mlines.Line2D([], [], color='green', marker='_', label='Default value')
    
    plt.legend(handles=[sample_0, red_ball, limits, true_value], loc=0, fontsize = 'x-small')
    plt.rcParams.update({'font.size': 22})
    print('printing:', outputdir)
    plt.savefig(outputdir + '/parameter' + str(i+1) + '.png', dpi=300)
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

if 0==1:
  Fscore = 0
  mean_cor_ff20 = sum(cov_data[19:,0,1])/float(ndays-20)
  ind = ndays-10
  mean_cor_l10 = sum(cov_data[ind:ndays,0,1])/10.0
  mean_mu_1 = sum(mu_data[ind:ndays,0])/10.0
  mean_mu_2 = sum(mu_data[ind:ndays,1])/10.0
  print('###############################################')
  print('ENTSHALP=',mu_data[ndays-1,0], mean_mu_1)
  print('ENTRORG=',mu_data[ndays-1,1], mean_mu_2)
  print('stdENTSHALP=',sig_data[ndays-1,0],sig_data[1,0])
  print('stdENTRORG=',sig_data[ndays-1,1],sig_data[1,1])
  print('corr_ff20=',mean_cor_ff20)
  print('corr_l10=',mean_cor_l10)
  print('min max ENTSHALP=', min(mu_data[1:,0]), max(mu_data[:,0]))
  print('min max ENTRORG=', min(mu_data[1:,1]), max(mu_data[:,1]))

  print('###############################################')
  #print(mu_data[ind:ndays,0])
  ### Improving cost function values ###
  m12=-0.006270016247527165
  m24=0.006933287899853283
  m48=-0.012372801892942611
  m72=-0.016495023326435803
  m96=-0.020117966868772878
  m120=-0.027490817149602845
  m144=-0.024434605507243124
  m168=-0.01743168746148967
  ######################### these numbers come from bechmark tests

  if(m < m120):
    Fscore += 1
    print('Cost function point +1')

  ### Convergence of parameters towards default values ###
  if(mean_mu_1 < 2.2 and mean_mu_1 > 1.8):
    Fscore += 1
    print('10% goal for ENTSHALP +1')

  if(mean_mu_1 < 2.1 and mean_mu_1 > 1.9):
    Fscore += 1
    print('5% goal for ENTSHALP +1')

  if(mean_mu_2 < 0.001925 and mean_mu_2 > 0.001575):
    Fscore += 1
    print('10% goal for ENTRORG +1')

  if(mean_mu_2 < 0.0018375 and mean_mu_2 > 0.0016625):
    Fscore += 1
    print('5% goal for ENTRORG +1')

  if(sig_data[ndays-1,0] < sig_data[1,0]):
    Fscore += 1
    print('reduction of variance of ENTSHALP +1')

  if(sig_data[ndays-1,1] < sig_data[1,1]):
    Fscore += 1
    print('reduction of variance of ENTRORG +1')

  ### Reward for not exhibiting wild behaviour ###
  if(max(mu_data[:,0]) < 4.0 and min(mu_data[1:,0]) > 1.0):
    Fscore += 1
    print('smooth convergence of ENTSHALP +1')

  if(max(mu_data[:,1]) < 0.00225 and min(mu_data[1:,1]) > 0.00125):
    Fscore += 1
    print('smooth convergence of ENTRORG +1')

  ### Reward for finding correct correlation, (perfect correlation would be -1) ###
  if(mean_cor_ff20 < 0.0):
    Fscore += 1
    print('correlation < 0.0, +1')

  if(mean_cor_ff20 < -0.4):
    Fscore += 1
    print('correlation < -0.4, +1')

  if(mean_cor_l10 < 0.0):
    Fscore += 1
    print('correlation stays negative, +1')

  ### Disqualification due to irrecoverable parameter population collapse ###
  if min(sig_data[1:,0]) < 0.01 or min(sig_data[1:,1]) < 0.0000001:
    Fscore = 0
    print('Population collapsed, DSQ')

  print('Fscore = ', Fscore)
