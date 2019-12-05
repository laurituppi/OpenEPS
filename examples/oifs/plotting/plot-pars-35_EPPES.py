import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys
import os
plt.rcParams.update({'font.size': 22})
#ndays = int(sys.argv[1])
npars = int(sys.argv[1])
nens = int(sys.argv[2])
inputdir = sys.argv[3]
outputdir = sys.argv[4]
inifiles = sys.argv[5]

def_values = np.zeros(npars)

for k in range(npars):
  def_values[k]=float(sys.argv[k+6])

mufile = "mufile.dat"
sigfile = "sigfile.dat"
samplefile = "sampleout.dat"
winfofile = "winfo.dat"
scores = "scores.dat"

subdirectories = os.listdir(inputdir)
subdirectories = sorted(subdirectories)
ndays = np.size(subdirectories)

t = np.arange(ndays+1)

mu_data = np.zeros((ndays+1, npars))
#mu_data[0] = np.loadtxt("/wrk/lautuppi/DONOTREMOVE/init_mu_sigma/mufile_5par.dat")
mu_data[0,:] = np.loadtxt(inifiles + "mufile.dat")
#mu_data[0] = mu_data[0]*10
sig_data = np.zeros((ndays+1, npars, npars))
#sig_data[0] = np.loadtxt("/wrk/lautuppi/DONOTREMOVE/init_mu_sigma/sigfile_5par.dat")
sig_data[0,:] = np.loadtxt(inifiles + "sigfile.dat")
#sig_data[0] = sig_data[0]*100
sample_data = np.zeros((ndays, nens, npars))
weights_data = np.ones((ndays, nens, npars))
score_data = np.zeros((ndays, nens))
corr_data = np.zeros((ndays, npars, npars))

def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

default_value = np.zeros(ndays+1)
mean_score = np.zeros(ndays)

for i in range(0,ndays):
    mu_data[i+1,:] = np.loadtxt(get_input_file(subdirectories[i], mufile))
    sig_data[i+1,:,:] = np.loadtxt(get_input_file(subdirectories[i], sigfile))
    sample_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i], samplefile))
    corr_data[i,:,:] = np.corrcoef(sample_data[i,:,:].T)

    try:
      score_data[i,:] = np.genfromtxt(get_input_file(subdirectories[i], scores))
    except Exception:
      print('no score data in', subdirectories[i])
      score_data[i,:] = [-10.0,-10.0,-10.0]
    mean_score[i] = np.sum(score_data[i,:])/nens
    if i>=0 and i<ndays-1:
        print('processing date:', subdirectories[i])
        #weights_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i+1], winfofile))

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

if (1==1):
  for i in range(npars):
      #sample_data_0 = np.copy(sample_data)
      #sample_data_1 = np.copy(sample_data)
      plt.figure(figsize=(12,10))
      weights = weights_data[:,:,1]
      color_w = np.ones((ndays,nens)) - weights/np.max(weights, axis=0)

      for tind in range(ndays):
          #default_value[tind] = def_values[i]
          if tind<ndays-1:
              for ensind in range(nens):
                  col=color_w[tind, ensind]
                  if pars[i]=='DETRPEN':
                    if col>0.93:
                      plt.plot(tind+1, sample_data[tind,ensind,i]*10000, color=str(0.93), marker='.', linestyle='')
                    else:
                      plt.plot(tind+1, sample_data[tind,ensind,i]*10000, color=str(col), marker='.', linestyle='')
                  elif pars[i]=='ENTRORG' or pars[i]=='RPRCON':
                    if col>0.93:
                      plt.plot(tind+1, sample_data[tind,ensind,i]*1000, color=str(0.93), marker='.', linestyle='')
                    else:
                      plt.plot(tind+1, sample_data[tind,ensind,i]*1000, color=str(col), marker='.', linestyle='')
                  else:
                    if col>0.93:
                      plt.plot(tind+1, sample_data[tind,ensind,i], color=str(0.93), marker='.', linestyle='')
                    else:
                      plt.plot(tind+1, sample_data[tind,ensind,i], color=str(col), marker='.', linestyle='')
                    #plt.plot(tind+1, sample_data_1[tind,ensind,i], color=(str(color_w[tind, ensind])), marker='o', linestyle='')
  #        elif tind==ndays-1:
  #            if pars[i]=='DETRPEN':
  #              for ensind in range(nens):
  #                  plt.plot(tind+1, sample_data[tind,ensind,i], color='k', marker='x', linestyle='')
  #            else:
  #              for ensind in range(nens):
  #                  plt.plot(tind+1, sample_data[tind,ensind,i], color='k', marker='x', linestyle='')
                  #plt.plot(tind+1, sample_data_1[tind,ensind,i], color='k', marker='.', linestyle='')
  
      for tind in range(ndays):
          default_value[tind] = def_values[i]
    
        #default_value[ndays+1] = def_values[i]
      if pars[i]=='DETRPEN':
        plt.plot(t[:ndays], mu_data[0:ndays,i]*10000, 'r*-', linewidth=2.0)
        plt.plot(t[:ndays], (mu_data[0:ndays,i]-2*np.sqrt(sig_data[0:ndays,i,i]))*10000, 'b.-', linewidth=2.0)
        plt.plot(t[:ndays], (mu_data[0:ndays,i]+2*np.sqrt(sig_data[0:ndays,i,i]))*10000, 'b.-', linewidth=2.0)
        plt.plot(t[:ndays], default_value[0:ndays]*10000, 'g-', linewidth=2.0)
      elif pars[i]=='ENTRORG' or pars[i]=='RPRCON':
        plt.plot(t[:ndays], mu_data[0:ndays,i]*1000, 'r*-', linewidth=2.0)
        plt.plot(t[:ndays], (mu_data[0:ndays,i]-2*np.sqrt(sig_data[0:ndays,i,i]))*1000, 'b.-', linewidth=2.0)
        plt.plot(t[:ndays], (mu_data[0:ndays,i]+2*np.sqrt(sig_data[0:ndays,i,i]))*1000, 'b.-', linewidth=2.0)
        plt.plot(t[:ndays], default_value[0:ndays]*1000, 'g-', linewidth=2.0)
      else:
        plt.plot(t[:ndays], mu_data[0:ndays,i], 'r*-', linewidth=2.0)
        plt.plot(t[:ndays], (mu_data[0:ndays,i]-2*np.sqrt(sig_data[0:ndays,i,i])), 'b.-', linewidth=2.0)
        plt.plot(t[:ndays], (mu_data[0:ndays,i]+2*np.sqrt(sig_data[0:ndays,i,i])), 'b.-', linewidth=2.0)
        plt.plot(t[:ndays], default_value[0:ndays], 'g-', linewidth=2.0)

      axes = plt.gca()
      axes.set_xlim([0.0,ndays+1])
      #if i==0:
      #  axes.set_ylim([0.0,4.5])
      #elif i==1:
      #  axes.set_ylim([-0.001,0.005])

      plt.xlabel('Number of iterations')
      #plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
      if pars[i]=='ENTSHALP':
        plt.ylabel('Parameter value')
      elif pars[i]=='ENTRORG':
        plt.ylabel('Parameter value [10$^{-3}$ m$^{-1}$]')
      elif pars[i]=='DETRPEN':
        plt.ylabel('Parameter value [10$^{-4}$ m$^{-1}$]')
      elif pars[i]=='RPRCON':
        plt.ylabel('Parameter value [10$^{-3}$ s$^{-1}$]')
      elif pars[i]=='RDEPTHS':
        plt.ylabel('Parameter value [Pa]')
    
      plt.title(pars[i] + ', EPPES')

      sample_0 = mlines.Line2D([],[], color=('0.0'), marker='o',linestyle='', label='Parameter values')
      #sample_1 = mlines.Line2D([],[], color=('0.0'), marker='o',linestyle='', label='Resampled data')
      red_ball = mlines.Line2D([], [], color='red', marker='*', label='$\mu$')
      limits = mlines.Line2D([],[], color='blue', marker='.', label='$\mu \pm 2\sigma$')
      true_value = mlines.Line2D([], [], color='green', marker='_', label='Default value')
    
      plt.legend(handles=[sample_0, red_ball, limits, true_value], loc=0, fontsize = 'x-small')
      #plt.rcParams.update({'font.size': 22})
      print('printing:', outputdir, '  ', pars[i])
      #plt.savefig(outputdir + '/parameter' + str(i+1) + '.eps', dpi=300, format='eps')
      plt.savefig(outputdir + '/parameter' + str(i+1) + '.png', dpi=300, format='png')
      #plt.savefig(outputdir + '/parameter' + str(i+1) + '.pdf', dpi=300, format='pdf')
      plt.clf()

if (0==1):
  for j in range(npars):
    mu_data[:,j] = mu_data[:,j]/def_values[j]
    sample_data[:,:,j] = sample_data[:,:,j]/def_values[j]
    sig_data[:,j,j] = sig_data[:,j,j]/(def_values[j]**2)

  for i in range(npars):
    plt.figure(figsize=(12,10))
    weights = weights_data[:,:,1]
    color_w = np.ones((ndays,nens)) - weights/np.max(weights, axis=0)

    for tind in range(ndays):
      if tind<ndays-1:
        for ensind in range(nens):
          col=color_w[tind, ensind]
          if col>0.93:
            plt.plot(tind+1, sample_data[tind,ensind,i], color=str(0.93), marker='.', linestyle='')
          else:
            plt.plot(tind+1, sample_data[tind,ensind,i], color=str(col), marker='.', linestyle='')

    for tind in range(ndays):
       default_value[tind] = 1.0 #def_values[i]

    plt.plot(t[:ndays], mu_data[0:ndays,i], 'r*-', linewidth=2.0)
    plt.plot(t[:ndays], (mu_data[0:ndays,i]-2*np.sqrt(sig_data[0:ndays,i,i])), 'b.-', linewidth=2.0)
    plt.plot(t[:ndays], (mu_data[0:ndays,i]+2*np.sqrt(sig_data[0:ndays,i,i])), 'b.-', linewidth=2.0)
    plt.plot(t[:ndays], default_value[0:ndays], 'g-', linewidth=2.0)

    axes = plt.gca()
    axes.set_xlim([0.0,ndays+1])

    plt.xlabel('Iteration number')
    plt.ylabel('Normalised parameter value')
    plt.title('Normalised ' + pars[i] + ', EPPES')

    sample_0 = mlines.Line2D([],[], color=('0.0'), marker='o',linestyle='', label='Parameter values')
    red_ball = mlines.Line2D([], [], color='red', marker='*', label='$\mu$')
    limits = mlines.Line2D([],[], color='blue', marker='.', label='$\mu \pm 2\sigma$')
    true_value = mlines.Line2D([], [], color='green', marker='_', label='Default value')
    plt.legend(handles=[sample_0, red_ball, limits, true_value], loc=0, fontsize = 'x-small')
    print('printing:', outputdir, '  ', pars[i])
    plt.savefig(outputdir + '/parameter' + str(i+1) + '.png', dpi=300, format='png')
    plt.clf()

if (0==1):
  plt.figure()
  t2 = np.arange(ndays)
  t22 = t2[1:]
  A = np.vstack([t22, np.ones(len(t22))]).T
  m, con = np.linalg.lstsq(A, mean_score[1:], rcond=None)[0]
  linear_fit = np.zeros(ndays-1)
  linear_fit = t22 * m + con
  print('linear fit coefficients: ', m, con)
  for j in range(nens):
    plt.plot(t2+1,score_data[:,j],'g.')

  plt.plot(t2+1,mean_score,'r')
  plt.plot(t22,linear_fit,'b')
  ensmem = mlines.Line2D([], [], color='green', marker='_', label='ens members')
  ensmean = mlines.Line2D([], [], color='red', marker='_', label='mean score')
  ensfit = mlines.Line2D([], [], color='blue', marker='_', label='linear fit')
  axes = plt.gca()
  axes.set_xlim([0,ndays+1])
  plt.title('Moist total energy norm')
  plt.xlabel('Initialization date')
  plt.ylabel('Cost function value [J/kg]')
  plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
  plt.legend(handles=[ensmem, ensmean, ensfit], loc=0)
  plt.grid()
  plt.savefig(outputdir + '/scores' + '.png')
  plt.clf()

if (0==1):
  print('average correlation: ', sum(corr_data[:,0,1])/float(len(corr_data[:,0,1])))
  plt.figure()
  plt.plot(t2,corr_data[:,0,1],'b')
  axes = plt.gca()
  axes.set_xlim([0,ndays+1])
  plt.title('Correlation')
  plt.xlabel('Initialization date')
  plt.xticks((al, bl, cl, dl, el, fl), (a, b, c, d, e, f), rotation='352')
  plt.ylabel('Correlation coefficient')
  plt.grid()
  plt.savefig(outputdir + '/correlation' + '.png')
  plt.clf()

if (0==1):
  Fscore = 0
  mean_cor_ff20 = sum(corr_data[19:,0,1])/float(ndays-20)
  ind = ndays-10
  mean_cor_l10 = sum(corr_data[ind:ndays,0,1])/10.0
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

  if(sig_data[ndays-1,0,0] < sig_data[1,0,0]):
    Fscore += 1
    print('reduction of variance of ENTSHALP +1')

  if(sig_data[ndays-1,1,1] < sig_data[1,1,1]):
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
  if (min(sig_data[1:,0,0]))**0.5 < 0.01 or (min(sig_data[1:,1,1]))**0.5 < 0.0000001:
    Fscore = 0
    print('Population collapsed, DSQ')

  print('Fscore = ', Fscore)
