import sys
import netCDF4
from netCDF4 import Dataset
import numpy as np
from numpy import dtype

tlnsp_GG = sys.argv[1]
z_GG = sys.argv[2]
z_surf_GG = sys.argv[3]
outfile = sys.argv[4]
outputdir = sys.argv[5]

tlnsp_GG = Dataset(tlnsp_GG, mode='r')
z_GG = Dataset(z_GG, mode='r')
z_surf_GG = Dataset(z_surf_GG, mode='r')

t = tlnsp_GG.variables['T'][:]
lnsp = tlnsp_GG.variables['LNSP'][:]
z = z_GG.variables['Z'][:]
z_surf = z_surf_GG.variables['Z']
lev = z_GG.variables['lev'][:]
lat = z_GG.variables['lat'][:]
lon = z_GG.variables['lon'][:]
time = z_GG.variables['time'][:]

nlevs = np.size(lev)
nlats = np.size(lat)
nlons = np.size(lon)
ntime = np.size(time)

R = 287.06

p = np.zeros((nlevs+1,nlats,nlons))
zt = np.zeros((nlevs+1,nlats,nlons))
p_final = np.ndarray(shape=(ntime,nlevs,nlats,nlons), dtype=float, order='F')
t_mean = np.zeros((nlevs,nlats,nlons))

p[nlevs,:,:] = np.exp(lnsp[0,0,:,:])

zt[nlevs,:,:] = z_surf[0,0,:,:]
zt[0:nlevs,:,:] = z[:,:,:]

t_mean_temp = (t[0,0:nlevs-1,:,:] + t[0,1:,:,:]) * 0.5
t_mean[0:nlevs-1,:,:] = t_mean_temp
t_mean[nlevs-1,:,:] = t_mean[nlevs-2,:,:]

p_a1 = p[nlevs,:,:]
for i in range(1,nlevs):
  p[nlevs - i,:,:] = p_a1 * np.exp(-(zt[nlevs-i-1,:,:]-zt[nlevs-i,:,:])/(R * t_mean[nlevs-i,:,:]))
  p_a1 = p[nlevs - i,:,:]

p[0,:,:]=0.01
p_final[0,:,:,:] = p[:nlevs,:,:]

new_nc_file = Dataset(outfile,'w')
new_nc_file.createDimension('latitude',nlats)
new_nc_file.createDimension('longitude',nlons)
new_nc_file.createDimension('model_level',nlevs)
new_nc_file.createDimension('time',ntime)
lats = new_nc_file.createVariable('latitude',dtype('float32').char,('latitude',))
lats.axis = 'Y'
lons = new_nc_file.createVariable('longitude',dtype('float32').char,('longitude',))
lons.axis = 'X'
levs = new_nc_file.createVariable('model_level',dtype('int8').char,('model_level',))
levs.axis = 'Z'
times =new_nc_file.createVariable('time',dtype('int8').char,('time',))
times.axis = 'T'
lats[:] = lat
lons[:] = lon
levs[:] = lev
times[:] = time

pressure = new_nc_file.createVariable('pres',dtype('float32').char,('time','model_level','latitude','longitude'))
pressure[:,:,:,:] = p_final
new_nc_file.close()
