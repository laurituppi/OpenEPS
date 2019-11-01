import numpy as np
#import csv
#import scipy.io as sio
from scipy import stats
import sys
import os

#a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#b = np.array([[9,8,7],[6,5,4],[3,2,1]])
#mda = np.array([[2,2,2],[2,2,2]

#c = a * b

#print c

#cs = sum(sum(c))
#print cs

#summa = 0
#for i in range(0,3):
#  for j in range(0,3):
#    summa = summa + a[i,j] * b[i,j]
#    print a[i,j], b[i,j]

#######print summa

#nens = 1000
#ntime = 10

#mu_f = 2.0
#mu_o = 2.2

#sigma_f = 1.0
#sigma_o = 1.5

npars = int(sys.argv[1])
nens = int(sys.argv[2])
inputdir = sys.argv[3]
outputdir = sys.argv[4]
optimizer = int(sys.argv[5])
parameter = int(sys.argv[6])

samplefile = "sampleout.dat"
mu_def=1.9
sig_def=0.05

subdirectories = sorted(os.listdir(inputdir))
#print(subdirectories)
ntime = np.size(subdirectories)
mu_data = np.zeros(ntime)
sig_data = np.zeros(ntime)

def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

def default_pdf(mu_def, sig_def, nens): # vastaava jakauma default keskiarvolla ja hajonnalla
    distr = sorted(np.random.normal(mu_def, sig_def, nens), key=float)
    return distr

def normpdf(x, mu, sigma):
    u = (x-mu)/abs(sigma)
    y = (1/(np.sqrt(2*np.pi)*abs(sigma)))*np.exp(-u*u/2)
    return y

def normcdf(x, mu, sigma):
    t = x-mu;
    y = 0.5*erfcc(-t/(sigma*np.sqrt(2.0)));
    if y>1.0:
        y = 1.0;
    return y

def erfcc(x):
    """Complementary error function."""
    z = abs(x)
    t = 1. / (1. + 0.5*z)
    r = t * np.exp(-z*z-1.26551223+t*(1.00002368+t*(.37409196+
        t*(.09678418+t*(-.18628806+t*(.27886807+
        t*(-1.13520398+t*(1.48851587+t*(-.82215223+
        t*.17087277)))))))))
    if (x >= 0.):
        return r
    else:
        return 2. - r

def get_def_cdf(nens,mu,sig):
#    x = np.size(sample)
#    cdf = np.zeros((x,2))
#    for i in range(x)
#      cdf[i,0] = sample[i]
#      cdf[i,1] = float(i+1)/float(x)
#    return cdf

#ensf = np.zeros((ntime,nens))
#obs = np.zeros(ntime)
#crps_sum=0.0
    cdf=np.zeros(nens)
    j=0
    step=float(j+1)/float(nens)
    x=0.0
    dx=0.01
    print(normcdf(x, mu, sig))
    for i in range(100000):
      y=normcdf(x, mu, sig)
      #print(x,y)
      if y>step and j<50:
        cdf[j]=x
        j=j+1
        step=float(j+1)/float(nens)
      x=x+dx
      if x>4.0:
        break
    cdf[nens-1]=x
    print(cdf)
    return cdf

#sample_data[i,:,:] = np.loadtxt(get_input_file(subdirectories[i], samplefile))
#xts = default_pdf(2.0, 0.5, nens)

if 0==1:
  for i in range(ntime):
    #ensf = np.random.normal((nens))
    ensf_a = np.loadtxt(get_input_file(subdirectories[i], samplefile))
    ensf_v = ensf_a[:,parameter-1]

    #for j in range(nens):
    #  s = np.random.normal(mu_f,sigma_f)
    #  ensf_v[j] = s

    ensf[i,:]=ensf_v[:]
    #xts = 2.0
    #xts = np.random.normal(mu_o,sigma_o)

    #obs[i]=xts

    xasorted = sorted(ensf_v, key=float)  
    crps = 0.0             
      # calculate crps: 
    for m in range(nens-1):
      if xts[m] <= xasorted[m]:
          tmp = (xasorted[m+1]-xasorted[m])*np.square(1-1.0*(m+1)/nens)
      elif xasorted[m] < xts[m] <= xasorted[m+1]:
          tmp =(xts[m] - xasorted[m])*np.square(1.0*(m+1)/nens) + (xasorted[m+1] - xts[m])*np.square(1-1.0*(m+1)/nens)
      elif xasorted[m+1] < xts[m+1]:
          tmp = (xasorted[m+1] - xasorted[m])*np.square(1.0*(m+1)/nens)
      crps = crps + tmp

    #crps_sum+=crps
    print(crps)
  #print crps_sum/float(ntime)

elif 1==1:
  cdf_d=get_def_cdf(nens,mu_def,sig_def)
  for i in range(1): #(ntime):
    sample = np.loadtxt(get_input_file(subdirectories[i], samplefile))
    cdf_s = sorted(sample[:,parameter-1], key=float)
    crps=0.0
    for j in range(nens-1):
      crps = crps + ((cdf_s[j] - cdf_d[j])/float(nens))**2

    print(crps)



#sio.savemat('ensf.mat',{'mat':ensf})
#sio.savemat('obs.mat',{'vect':obs})
