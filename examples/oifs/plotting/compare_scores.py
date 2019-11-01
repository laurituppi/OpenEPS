import numpy as np
import os
import sys

string=sys.argv[1]+'h'

#string='96h'
indir1 = '/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/inner_predictability/converged_pars_test/level2/20mem_'+string+'/eppesdata'
indir2 = '/wrk/lautuppi/DONOTREMOVE/publ_conv_tests/inner_predictability/level2/20mem_'+string+'/eppesdata'

def get_input_file(inputdir, day, name):
    o = inputdir + "/" + str(day) + "/" + name
    return o

subdirectories1 = os.listdir(indir1)
subdirectories1 = sorted(subdirectories1)

subdirectories2 = os.listdir(indir2)
subdirectories2 = sorted(subdirectories2)
ndays = np.size(subdirectories1)

mean_differences = np.zeros(ndays)
scores=np.zeros((ndays,20))
scores_ref=np.zeros((ndays,20))
for i in range(ndays):
  score=np.loadtxt(get_input_file(indir1, subdirectories1[i], 'scores.dat'))
  score_ref=np.loadtxt(get_input_file(indir2, subdirectories2[i], 'scores.dat'))
  scores[i,:]=score
  scores_ref[i,:]=score_ref
  #mean_differences[i] = 100*(np.mean(score) - np.mean(score_ref))/np.mean(score_ref)
  mean_differences[i] = np.mean(score) - np.mean(score_ref)

#print 100*np.mean(mean_differences)/np.mean(scores_ref)
print np.mean(mean_differences)
