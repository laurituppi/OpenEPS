import numpy as np
import matplotlib.pyplot as plt
import os
import sys

inputdir=sys.argv[1]
outputdir=sys.argv[2]
samplefile=sys.argv[3]
scorefile=sys.argv[4]
sequence=int(sys.argv[5])
ndays=int(sys.argv[6])

subdirectories = os.listdir(inputdir)
subdirectories = sorted(subdirectories)

def get_input_file(day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

for i in range(ndays-1):
  pars = np.loadtxt(get_input_file(subdirectories[i],samplefile))
  scores = np.loadtxt(get_input_file(subdirectories[i],scorefile))
  
  y=pars[:,0]
  x=pars[:,1]
  print(i)

  plot=plt.scatter(x,y,c=scores,s=30.0,alpha=1.0,cmap='rainbow',vmin=9.0,vmax=20.0)
  axes = plt.gca()
  axes.set_xlim([0.0,0.01])
  axes.set_ylim([0.0,7.0])
  #plt.colorbar(plot)
  plt.hold(True)
  #plt.title('ENS number', str(i+1))
  if ((i+1)%sequence==0):
    plt.colorbar(plot)
    plt.savefig(outputdir + '/ens_num' + str(i+1) + '.png')
    plt.clf()
