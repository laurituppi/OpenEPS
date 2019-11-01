# Madeleine Ekblom, 4.7.2019
# Plot of parameter space

import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import cm
from matplotlib import colors as mcols

# folder containing experiment outputs
data_folder = '/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/EPPES/level'
#data_folder = '/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/DE/level'

def plot(nens, fclen, level):
    '''
    Input: ensemble size, forecast length, level of complexity (of experiment)

    Plots parameter space: cost function value as a function of ENTSHALP and ENTRORG. Coloured dots represent the value of the cost function.
    '''
    
    # initialisation times of forecasts
    init_time = ['2016120100','2016120800','2016121500','2016122200','2016122900','2017010500','2017011200','2017011900','2017012600','2017020200','2017020900','2017021600','2017022300','2017030200','2017030900','2017031600','2017032300','2017033000','2017040600','2017041300','2017042000','2017042700','2017050400','2017051100','2017051800','2017052500','2017060100','2017060800','2017061500','2017062200','2017062900','2017070600','2017071300','2017072000','2017072700','2017080300','2017081000','2017081700','2017082400','2017083100','2017090700','2017091400','2017092100','2017092800','2017100500','2017101200','2017101900','2017102600','2017110200','2017110900','2017111600','2017112300','2017113000']

    ninit = len(init_time)
    nens = int(nens)
    
    # Empty matrices for parameter data and corresponding scores
    entrorg_all = np.zeros(nens*ninit)
    entshalp_all = np.zeros(nens*ninit)
    cost_all = np.zeros(nens*ninit)

    # Read in data files:
    for n in range(ninit):
        print(init_time[n])
        params = np.loadtxt(data_folder + level +'/'+ str(nens) +'mem_' + fclen + 'h/eppesdata/' + init_time[n] + '/sampleout.dat')
        scores = np.loadtxt(data_folder +level+'/'+ str(nens) +'mem_' + fclen + 'h/eppesdata/' + init_time[n] + '/scores.dat')

        entshalp_all[n*nens:(n+1)*nens]=params[:,0]
        entrorg_all[n*nens:(n+1)*nens]=params[:,1]
        cost_all[n*nens:(n+1)*nens] = scores[:]

    # Set default values of parameters
    entrorg_default=0.00175
    entshalp_default=2.0

    # Set min/max of entrorg, set min/max of entshalp
    xmin=entshalp_default*0.5
    xmax=entshalp_default*1.5
    ymin=entrorg_default*0.5
    ymax=entrorg_default*1.5    

    # Set fontsize for plot
    fontsize=20

    # Create new figure
    ax = plt.figure(figsize=((10,10)))
    
    # Set axis 
    plt.axis([xmin, xmax, ymin, ymax])

    # Plot vertical and horizontal lines marking default values
    plt.axhline(y=entrorg_default, c='k')
    plt.axvline(x=entshalp_default, c='k')

    # Scatter (ENTSHALP, ENTRORG, cost function)
    vmin = np.min(cost_all)
    vmax = np.max(cost_all)
    print(vmin)
    print(vmax)
    norm = mcols.Normalize(vmin=vmin, vmax=vmax)
    
    plt.scatter(entshalp_all, entrorg_all, c=cost_all, cmap=cm.jet, norm=norm)

    # Set labels, title, colorbar
    plt.xlabel('ENTSHALP', fontsize=fontsize)
    plt.ylabel('ENTRORG', fontsize=fontsize)
    plt.title('Level: '+level+', forecast length:'+fclen+'h', fontsize=fontsize)
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Moist total energy norm', fontsize=fontsize)


    plt.savefig('50mem_12h.png')
    #plt.show()

if __name__=='__main__':
    '''
    Input: ensemble size, forecast length, level of complexity (of experiment)
    '''

    nens = sys.argv[1]
    fclen = sys.argv[2]
    level = sys.argv[3]
    plot(nens, fclen, level)
