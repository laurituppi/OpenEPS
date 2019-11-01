import sys
import netCDF4
from netCDF4 import Dataset
import numpy as np
from numpy import outer
import math as math

def get_area_increments(lat,lon): # input: latitude and longitude vectors.
    nlats=len(lat) # number of latitudes and longitudes
    nlons=len(lon)
    pi=math.pi
    a=6371000.0 # radius of the Earth (unit [m])
    dy=(pi*a)/float(nlats) # increment in y direction (unit [m])
    lat_rv = (2.0*pi/360.0)*lat # degrees -> radians
    vdx = abs((a*2.0*pi*np.cos(lat_rv)))/float(nlons) # increments in x direction (unit [m])
    mda2d = (np.outer(vdx,np.ones((nlons)))) * dy # 2D matrix of area increments using outer product.
    return mda2d

forecast_z=sys.argv[1]
reference_z=sys.argv[2]

outputdir=sys.argv[3]

f_z_file=Dataset(forecast_z,'r')
r_z_file=Dataset(reference_z,'r')

f_z=f_z_file.variables['Z'][:]
r_z=r_z_file.variables['Z'][:]

lat = f_z_file.variables['lat'][:]	 # latitudes
lon = f_z_file.variables['lon'][:]	 # longitudes

nlats = len(lat)
nlons = len(lon)

fz = f_z[0,0,:,:]/9.81
rz = r_z[0,0,:,:]/9.81

area=4*math.pi*6371000.0**2
se_2d = (fz - rz)**2
increments_2d = get_area_increments(lat,lon)

rmse = (sum(sum(se_2d * increments_2d))/area)**0.5
print '---------------------------------------RMSE-------------------------------------------'
print 'RMSE_z850=',rmse
print '--------------------------------------------------------------------------------------'
score = np.zeros(1)
score[0] = rmse
np.savetxt(outputdir + '/score.dat', score)
print '#######################################DONE###########################################'
