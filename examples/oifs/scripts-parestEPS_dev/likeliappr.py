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
u_c = control2.variables['U']
v_c = control2.variables['V']

ens_t_data = np.zeros((nens,nlevs,nlats,nlons))
ens_u_data = np.zeros((nens,nlevs,nlats,nlons))
ens_v_data = np.zeros((nens,nlevs,nlats,nlons))
for i in range(0,nens):
  #print sys.argv[i+4]
  ensmem2 = Dataset(sys.argv[i+4],mode='r')
  t = ensmem2.variables['T']
  u = ensmem2.variables['U']
  v = ensmem2.variables['V']
  ens_t_data[i,:,:,:]=t[:]
  ens_u_data[i,:,:,:]=u[:]
  ens_v_data[i,:,:,:]=v[:]

lat_index = np.arange(nlats)
lon_index = np.arange(nlons)

sel_lat = random.sample(lat_index,ncol)
sel_lon = random.sample(lon_index,ncol)

t_ens_r = np.zeros((nlevs*ncol,nens)) # kaikki yhteen ketjuun
u_ens_r = np.zeros((nlevs*ncol,nens))
v_ens_r = np.zeros((nlevs*ncol,nens))
t_c_r = np.zeros(nlevs*ncol)
u_c_r = np.zeros(nlevs*ncol)
v_c_r = np.zeros(nlevs*ncol)
for i in range(ncol):
  start = i*nlevs
  stop = (i+1)*nlevs
  lon = sel_lon[i]
  lat = sel_lat[i]
  #print start, stop, lon, lat
  t_c_r[start:stop] = t_c[:,lat,lon]
  u_c_r[start:stop] = u_c[:,lat,lon]
  v_c_r[start:stop] = v_c[:,lat,lon]
  for j in range(0,nens):
    t_ens_r[start:stop,j] = ens_t_data[j,:,lat,lon]
    u_ens_r[start:stop,j] = ens_u_data[j,:,lat,lon]
    v_ens_r[start:stop,j] = ens_v_data[j,:,lat,lon]

s2t_obs = 0.8**2
s2uv_obs = 0.15**2

ens_mean_t = (sum(t_ens_r.T))/float(nens)
ens_mean_u = (sum(u_ens_r.T))/float(nens)
ens_mean_v = (sum(v_ens_r.T))/float(nens)
apu_t = np.zeros(nlevs*ncol)
apu_u = np.zeros(nlevs*ncol)
apu_v = np.zeros(nlevs*ncol)
for i in range(0,nens):
  apu_t += (t_ens_r[:,i]-ens_mean_t)**2
  apu_u += (u_ens_r[:,i]-ens_mean_u)**2
  apu_v += (v_ens_r[:,i]-ens_mean_v)**2

s2t_ens = sum(apu_t/(float(nens)-1.0))/float(nlevs*ncol)
s2u_ens = sum(apu_u/(float(nens)-1.0))/float(nlevs*ncol)
s2v_ens = sum(apu_v/(float(nens)-1.0))/float(nlevs*ncol)

Jk_t = 0.0
Jk_u = 0.0
Jk_v = 0.0
for j in range(0,nlevs*ncol):
  Jk_t = Jk_t + (t_c_r[j] - ens_mean_t[j])**2 / (s2t_obs + s2t_ens)
  Jk_u = Jk_u + (u_c_r[j] - ens_mean_u[j])**2 / (s2uv_obs + s2u_ens)
  Jk_v = Jk_v + (v_c_r[j] - ens_mean_v[j])**2 / (s2uv_obs + s2v_ens)

Jk_t += np.log(s2t_obs + s2t_ens)
Jk_u += np.log(s2uv_obs + s2u_ens)
Jk_v += np.log(s2uv_obs + s2v_ens)

print 'Jk_t=',Jk_t,'Jk_u=',Jk_u,'Jk_v=',Jk_v
