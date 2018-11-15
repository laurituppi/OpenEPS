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

nlevs = np.size(lev)
nlats = np.size(lat)
nlons = np.size(lon)

R = 287.06

p = np.zeros((nlevs+1,nlats,nlons))
zt = np.zeros((nlevs+1,nlats,nlons))
#print np.shape(p)
p_final = np.ndarray(shape=(nlevs,nlats,nlons), dtype=float, order='F')
t_mean = np.zeros((nlevs,nlats,nlons))

p[91,:,:] = np.exp(lnsp[0,0,:,:])

zt[91,:,:] = z_surf[0,0,:,:]
zt[0:nlevs,:,:] = z[:,:,:]
#print(z_surf[0,0,80,80])
#print(zt[:,80,80])

t_mean_temp = (t[0,0:nlevs-1,:,:] + t[0,1:,:,:]) * 0.5
t_mean[0:nlevs-1,:,:] = t_mean_temp
#print np.shape(t_mean), nlevs
t_mean[nlevs-1,:,:] = t_mean[nlevs-2,:,:]

#print np.shape(z)
#print np.shape(t_mean)

for i in range(1,nlevs+1):
  #print 'loop index', nlevs - i
  
  p[nlevs - i,:,:] = p[nlevs-i-1,:,:] * np.exp(-(zt[nlevs-i,:,:]-zt[nlevs-i-1,:,:])/(R * t_mean[nlevs-i,:,:]))
  print(p[nlevs - i,100,100], zt[nlevs-i+1,100,100], zt[nlevs-i,100,100], t_mean[nlevs-i,100,100], nlevs-i)

p_final = p[:nlevs,:,:]

#print(p[:,100,100])

new_nc_file = Dataset(outfile,'w')
new_nc_file.createDimension('latitude',nlats)
new_nc_file.createDimension('longitude',nlons)
new_nc_file.createDimension('model_level',nlevs)
lats = new_nc_file.createVariable('latitude',dtype('float32').char,('latitude',))
lats.axis = 'Y'
lons = new_nc_file.createVariable('longitude',dtype('float32').char,('longitude',))
lons.axis = 'X'
levs = new_nc_file.createVariable('model_level',dtype('int8').char,('model_level',))
levs.axis = 'Z'
lats[:] = lat
lons[:] = lon
levs[:] = lev

pressure = new_nc_file.createVariable('pres',dtype('float32').char,('model_level','latitude','longitude'))
print(np.shape(p_final))
pressure[:,:,:] = p_final
new_nc_file.close()
