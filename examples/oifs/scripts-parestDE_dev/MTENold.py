# This is an example script that calculates value of the cost function required for 
# parameter estimation using the EPPES algorithm. In this script scaled dry total energy 
# norm of whole atmosphere is used as metrics of forecast performance. The dry total 
# energy norm calculation algorithm has been coded according to equation [2] in 
# Ollinaho et al. 2014. This script can calculate the cost function only from one time step at a time. 
# All input files must be in netCDF4 form. The value of cost function is then written 
# into a file for later use. This script requires both forecast and reference U wind, V wind, temperature 
# and surface pressure on model levels, and also pressure on model levels either from forecast or from reference data.
# 	The forecast data comes from the ensemble members but the reference data can come for example 
# from control forecast with default parameter values, operational analyses, reanalyses, etc.

# *** Command line arguments ***
# 1. Path to forecast data file that contains U and V wind, temperature and pressure on model levels 
#    if it is not in reference data.
# 2. Path to forecast data file that contains surface pressure.
# 3. Time step of the reference data. If control forecasts generated with OpenEPS are used 
#    as reference data, use value -1. This argument is integer number.
# 4. Path to reference data file that contains U and V wind, temperature and pressure on model levels 
#    if it is not in forecast data.
# 5. Path to reference data file that contains surface pressure.
# 6. Path to directory where the value of the cost function will be saved.
# 7. An ad hoc scaling term. This argument is real number.

# !!! IMPORTANT !!!
# 1. You have to try and adjust the scaling term suitable for your experiments.
#    If the scaling term is too small, the value of the cost function will be large 
#    and the resampling method of EPPES may give too much weight for one ensemble member.
#    If the scaling term is too large, the value of the cost function will be small 
#    and the resampling method of EPPES becomes inefficient as the weights are distributed almost evenly.
# 2. When testing this script with low resolution data, using the control forecast as reference 
#    data is recommended because forecasts with low resolution do not represent reality properly 
#    so comparison to analysis or reanalysis fields may produce unrealistically large values of the cost function.

# In the OpenEPS system this script is called from par_gen.bash but it can be tested using command line 
# if the required datasets are available.

# References:
# Ollinaho, P. et al., 2014. Optimization of NWP model closure parameters using total energy norm of forecast error as a target.
# 	Geoscientific Model Development, 7(5), pp.1889-1900. Available at: https://www.geosci-model-dev.net/7/1889/2014/.

# -*- coding: utf-8 -*-

# Import necessary Python modules.
import sys
import netCDF4
from netCDF4 import Dataset
import numpy as np
from numpy import outer
import math as math
from math import log
from math import pi

# Command line arguments:
forecastUVT = sys.argv[1]	 # File containing forecast U and V wind component, temperature (and pressure) on model levels.
forecastP = sys.argv[2] 	 # File containing forecast ground level pressure
ref_step = int(sys.argv[3]) 	 # Time step of reference data, use -1 if the dataset contains only one time step.
referenceUVT = sys.argv[4]	 # File containing reference U and V wind component, temperature (and pressure) on model levels.
referenceP = sys.argv[5]	 # File containing reference ground level pressure
outputdir = sys.argv[6]		 # Directory where the file with the value of cost function is saved.
scale = float(sys.argv[7])	 # an ad hoc scaling term of the cost function

# Read the data from the given netCDF files.
forecast_mlevs = Dataset(forecastUVT, mode='r') 	# forecast model level data
forecast_surf = Dataset(forecastP, mode='r') 		# forecast surface data

reference_mlevs = Dataset(referenceUVT, mode='r') 	# reference model level data
reference_surf = Dataset(referenceP, mode='r') 		# reference surface data

# Sometimes the names of the fields are in lower case and sometimes in upper case
# depending on the system used so some error handling is required while reading the data.
try:
  f_u_all = forecast_mlevs.variables['u'][:]	 # forecast U wind on model levels
except Exception:
  f_u_all = forecast_mlevs.variables['U'][:]

try:
  f_v_all = forecast_mlevs.variables['v'][:]	 # forecast V wind on model levels
except Exception:
  f_v_all = forecast_mlevs.variables['V'][:]

try:
  f_t_all = forecast_mlevs.variables['t'][:]	 # forecast temperature on model levels
except Exception:
  f_t_all = forecast_mlevs.variables['T'][:]

try:
  f_q_all = forecast_surf.variables['q'][:]
except Exception:
  f_q_all = forecast_surf.variables['Q'][:]

try:
  f_sp_all = forecast_surf.variables['sp'][:]	 # forecast surface pressure
except Exception:
  f_sp_all = forecast_surf.variables['SP'][:]

try:
  ref_u_all = reference_mlevs.variables['u'][:]	 # reference U wind on model levels
except Exception:
  ref_u_all = reference_mlevs.variables['U'][:]

try:
  ref_v_all = reference_mlevs.variables['v'][:]	 # reference V wind on model levels
except Exception:
  ref_v_all = reference_mlevs.variables['V'][:]

try:
  ref_t_all = reference_mlevs.variables['t'][:]	 # reference temperature on model levels
except Exception:
  ref_t_all = reference_mlevs.variables['T'][:]

try:
  ref_q_all = reference_surf.variables['q'][:]
except Exception:
  ref_q_all = reference_surf.variables['Q'][:]

try:
  ref_sp_all = reference_surf.variables['sp'][:] # reference surface pressure
except Exception:
  ref_sp_all = reference_surf.variables['SP'][:]

try:
  try:
    ref_pres_all = reference_mlevs.variables['pres'][:] # pressure on model levels from reference data
    ref_pres = ref_pres_all[ref_step,:,:,:]
  except Exception:
    ref_pres_all = reference_mlevs.variables['PRES'][:]
    ref_pres = ref_pres_all[ref_step,:,:,:]
except Exception:
  try:
    ref_pres_all = forecast_mlevs.variables['pres'][:] # or from forecast data
    ref_pres = ref_pres_all[0,:,:,:]
  except Exception:
    ref_pres_all = forecast_mlevs.variables['PRES'][:]
    ref_pres = ref_pres_all[0,:,:,:]

lat = forecast_mlevs.variables['lat'][:]	 # latitudes
lon = forecast_mlevs.variables['lon'][:]	 # longitudes
lev = forecast_mlevs.variables['lev'][:]	 # model levels

# Size of the grid.
nlats = len(lat)
nlons = len(lon)
nlevs = len(lev)

# One dimension is reduced from the data. This makes the following for-loops simpler.
# Take the desired time step from the data.
# Forecast data contains only one time step
f_u = f_u_all[0,:,:,:]
f_v = f_v_all[0,:,:,:]
f_t = f_t_all[0,:,:,:]
f_q = f_q_all[0,:,:,:]
#f_pres = f_pres_all[0,:,:,:]
f_sp = f_sp_all[0,:,:]

if ref_step==-1: 		# here reference data is from the control forecast
  ref_u = ref_u_all[0,:,:,:]
  ref_v = ref_v_all[0,:,:,:]
  ref_t = ref_t_all[0,:,:,:]
  ref_q = ref_q_all[0,:,:,:]
  ref_sp = ref_sp_all[0,:,:]
elif ref_step>=1: 		# here it is from other source
  ref_u = ref_u_all[ref_step-1,:,:,:]
  ref_v = ref_v_all[ref_step-1,:,:,:]
  ref_t = ref_t_all[ref_step-1,:,:,:]
  ref_q = ref_q_all[ref_step-1,:,:,:]
  ref_sp = ref_sp_all[ref_step-1,:,:]
elif ref_step<-1 or ref_step==0:
  print 'Invalid timestep selected for reference data in DTEN.py!!!'
  print 'Check the time step of the reference dataset.'

# Set some constant values used in calculations.
pi = math.pi
dy = (pi*6731000.0)/nlats 	 # length increment in y direction
Tr = 280.0			 # reference temperature
cp = 1004.0			 # the specific heat constant at constant pressure
Rd = 287.06			 # the gas constant of dry air
pr = 100000.0			 # a reference surface pressure
cq = 1.000
Lw = 2500800
area = 5.1006447190979e14	 # surface area of the Earth

# The wind and temperature differences are calculated at layer mid points by taking average of ith and i+1th model levels.

ref_u_ave = (ref_u[0:nlevs-1,:,:] + ref_u[1:,:,:])*0.5
ref_v_ave = (ref_v[0:nlevs-1,:,:] + ref_v[1:,:,:])*0.5
ref_t_ave = (ref_t[0:nlevs-1,:,:] + ref_t[1:,:,:])*0.5
ref_q_ave = (ref_q[0:nlevs-1,:,:] + ref_q[1:,:,:])*0.5

f_u_ave = (f_u[0:nlevs-1,:,:] + f_u[1:,:,:])*0.5
f_v_ave = (f_v[0:nlevs-1,:,:] + f_v[1:,:,:])*0.5
f_t_ave = (f_t[0:nlevs-1,:,:] + f_t[1:,:,:])*0.5
f_q_ave = (f_q[0:nlevs-1,:,:] + f_q[1:,:,:])*0.5

mdp = -(ref_pres[0:nlevs-1,:,:] - ref_pres[1:,:,:])

lat_rv = (2.0*pi/360.0)*lat
vdx = abs((6371000.0*2.0*pi*np.cos(lat_rv)))/nlons

mda2d = (np.outer(vdx,np.ones((nlons)))) * dy
mda = np.zeros((nlevs-1,nlats,nlons))
for i in range(0,nlevs-1):
  mda[i,:,:] = mda2d

du2 = 0.5 * sum(sum(sum((ref_u_ave - f_u_ave)**2 * mdp * mda)))/area
dv2 = 0.5 * sum(sum(sum((ref_v_ave - f_v_ave)**2 * mdp * mda)))/area
dt2 = 0.5 * sum(sum(sum((cp/Tr) * (ref_t_ave - f_t_ave)**2 * mdp * mda)))/area
dq2 = 0.5 * sum(sum(sum((cq*Lw**2)/(cp*Tr) * (ref_q_ave - f_q_ave)**2 * mdp * mda)))/area
dlnp2 = 0.5 * sum(sum(Rd*Tr*pr * (np.log(ref_sp[:,:]) - np.log(f_sp[:,:]))**2 * mda2d))/area

deltaE2 = du2 + dv2 + dt2 + dq2 + dlnp2
print deltaE2

# The value of the cost function is written into a file named score.dat here.
dten = np.zeros(1)
dten[0] = deltaE2
np.savetxt(outputdir + '/score.dat', dten)

# EOF
