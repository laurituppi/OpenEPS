import numpy as np
import sys
import netCDF4
from netCDF4 import Dataset
import random

control1 = sys.argv[1]
nens = int(sys.argv[2])
ncol = int(sys.argv[3])

control2 = Dataset(control1,mode='r')
nlats = len(control2.variables['lat'])
nlons = len(control2.variables['lon'])
nlevs = len(control2.variables['lev'])
t_c = control2.variables['T']

ens_t_data = np.zeros((nens,nlevs,nlats,nlons))
for i in range(0,nens):
  #print sys.argv[i+4]
  ensmem2 = Dataset(sys.argv[i+4],mode='r')
  t = ensmem2.variables['T']
  ens_t_data[i,:,:,:]=t[:]

lat_index = np.arange(nlats)
lon_index = np.arange(nlons)

sel_lat = random.sample(lat_index,ncol)
sel_lon = random.sample(lon_index,ncol)

tc_15 = np.zeros((nlevs*ncol,nens))
tc_c = np.zeros(nlevs*ncol)
for i in range(ncol):
  start = i*nlevs
  stop = (i+1)*nlevs
  lon = sel_lon[i]
  lat = sel_lat[i]
  #print start, stop, lon, lat
  tc_c[start:stop] = t_c[:,lat,lon]
  for j in range(0,nens):
    tc_15[start:stop,j] = ens_t_data[j,:,lat,lon]

s2_obs = 0.8**2

ens_mean = (sum(tc_15.T))/float(nens)
apu1 = np.zeros(nlevs*ncol)
for i in range(0,nens):
  apu1 += (tc_15[:,i]-ens_mean)**2

s2_ens = sum(apu1/(float(nens)-1.0))/float(nlevs*ncol)

Jk = 0.0
for j in range(0,nlevs*ncol):
  Jk = Jk + (tc_c[j] - ens_mean[j])**2 / (s2_obs + s2_ens)

Jk += np.log(s2_obs + s2_ens)

print 'Jk=',Jk
