import numpy as np
from datetime import datetime
from apollinaire import __version__

'''
In this file are stored functions dedicated to create
and manage headers of output files.
'''

def make_header_background_param (n_harvey=2, author=None, mcmc=True,
                                  nwalkers=None, nsteps=None, coeff_discard=None, 
                                  apodisation=False, quickfit=False, reboxing_behaviour=None,
                                  low_cut=None) :
  '''
  Design header for saving background fitted parameters file.
  '''

  from apollinaire.peakbagging import create_labels
  dt_string = datetime.now (). strftime("%d/%m/%Y %H:%M:%S")
  labels = create_labels (n_harvey, np.zeros (3*n_harvey + 6, dtype=bool))
  header = 'Background fitted parameters \n'

  header = header + 'Parameters are given in the following order:\n' + np.array2string (labels) + '\n'
  if author is not None :
    header = header + 'Peakbagging performed by ' + author + ' with apollinaire (v' + str(__version__) + ') \n' 
  else :
    header = header + 'Peakbagging performed by with apollinaire (v' + str(__version__) + ') \n' 
  header = header + 'https://apollinaire.readthedocs.io/en/latest \n' 
  header = header + 'File creation date: ' + dt_string + '\n' 

  header = header + 'Column 0: median of the fitted distribution. ' 
  if mcmc :
    header = header + 'Column 1: parameter standard deviation \n'
  else :
    header = header + '\n'
  
  str_args = '######################\nSettings:\n'
  str_args += 'apodisation=' + str (apodisation) + '\n'
  if low_cut is not None :
    str_args += 'low_cut=' + str (low_cut) + '\n'
  if nwalkers is not None :
    str_args += 'nwalkers=' + str (nwalkers) + '\n' 
  if nsteps is not None :
    str_args += 'nsteps=' + str (nsteps) + '\n' 
  if coeff_discard is not None :
    str_args += 'discarded_steps=' + str (nsteps//coeff_discard) + '\n' 
  if quickfit is not None :
    str_args += 'quickfit=' + str (quickfit) + '\n' 
  if reboxing_behaviour is not None :
    str_args += 'reboxing_behaviour=' + reboxing_behaviour + '\n' 
  str_args += '#######################\n'
  header = header + str_args

  return header

def make_header_background_vector (author=None, nwalkers=None, nsteps=None, 
                                   coeff_discard=None, apodisation=False, quickfit=False, 
                                   reboxing_behaviour=None, low_cut=None) :
  '''
  Design header for saving background power vector file.
  '''

  dt_string = datetime.now (). strftime("%d/%m/%Y %H:%M:%S")
  header = 'Background fitted power vector \n'

  if author is not None :
    header = header + 'Peakbagging performed by ' + author + ' with apollinaire (v' + str(__version__) + ') \n'
  else :
    header = header + 'Peakbagging performed by with apollinaire (v' + str(__version__) + ') \n' 
  header = header + 'https://apollinaire.readthedocs.io/en/latest \n' 
  header = header + 'File creation date: ' + dt_string + '\n' 

  str_args = '######################\nSettings:\n'
  str_args += 'apodisation=' + str (apodisation) + '\n'
  if low_cut is not None :
    str_args += 'low_cut=' + str (low_cut) + '\n'
  if nwalkers is not None :
    str_args += 'nwalkers=' + str (nwalkers) + '\n' 
  if nsteps is not None :
    str_args += 'nsteps=' + str (nsteps) + '\n' 
  if coeff_discard is not None :
    str_args += 'discarded_steps=' + str (nsteps//coeff_discard) + '\n' 
  if quickfit is not None :
    str_args += 'quickfit=' + str (quickfit) + '\n' 
  if reboxing_behaviour is not None :
    str_args += 'reboxing_behaviour=' + reboxing_behaviour + '\n' 
  str_args += '#######################\n'
  header = header + str_args

  return header

def make_header_pattern (author=None, fit_l1=True, fit_l3=False,
                         nwalkers=None, nsteps=None, coeff_discard=None,
                         n_order=None) :
  '''
  Design header for saving pattern parameters file.
  '''

  labels = np.array (['eps', 'alpha', 'Dnu', 'numax', 'Hmax', 'Wenv', 'w', 'd02',
                      'b02', 'd01', 'b01', 'd13', 'b03'])
  if not fit_l1 :
    fit_l3 = False
  if not fit_l3 :
    labels = labels[:len (labels)-2]
  if not fit_l1 :
    labels = labels[:len (labels)-2]

  dt_string = datetime.now (). strftime("%d/%m/%Y %H:%M:%S")
  header = 'Acoustic modes pattern fitted parameters \n'

  if author is not None :
    header = header + 'Peakbagging performed by ' + author + ' with apollinaire (v' + str(__version__) + ') \n'
  else :
    header = header + 'Peakbagging performed by with apollinaire (v' + str(__version__) + ') \n' 
  header = header + 'https://apollinaire.readthedocs.io/en/latest \n' 
  header = header + 'File creation date: ' + dt_string + '\n' 

  str_args = '######################\nSettings:\n'
  if nwalkers is not None :
    str_args += 'nwalkers=' + str (nwalkers) + '\n' 
  if nsteps is not None :
    str_args += 'nsteps=' + str (nsteps) + '\n' 
  if coeff_discard is not None :
    str_args += 'discarded_steps=' + str (nsteps//coeff_discard) + '\n' 
  if n_order is not None :
    str_args += 'n_order=' + str (n_order) + '\n'
  str_args += '#######################\n'
  header = header + str_args

  header = header + 'Parameters are given in the following order:\n' + np.array2string (labels) + '\n'

  return header

def make_header_pkb (extended=False, author=None, spectro=False, projected_splittings=False,
                     nwalkers=None, nsteps=None, coeff_discard=None, fit_amp=False) :
  '''
  Design pkb files header.

  :return: pkb file header
  :rtype: str
  '''

  if spectro :
    power = '(m/s)^2/muHz'
  else :
    power = 'ppm^2/muHz'

  if extended :
    param = 'n, l, nu, e_nu-, e_nu+, h, e_h-, e_h+, w, e_w-, e_w+, a, e_a-, e_a+, s, e_s-, e_s+, asym, e_asym-, e_asym+\n'
    units = '., ., muHz, muHz, muHz, ' + 3 * (power+', ') + 'muHz, muHz, muHz, deg, deg, deg, muHz, muHz, muHz, ., ., . \n'

  else :
    param = 'n, l, nu, e_nu, h, e_h, w, e_w, a, e_a, s, e_s, asym, e_asym\n'
    units = '., ., muHz, muHz ' + 2 * (power+', ') + 'muHz, muHz, deg, deg, muHz, muHz, ., . \n'

  param = 'Parameters: ' + param
  units = '            ' + units

  dt_string = datetime.now (). strftime("%d/%m/%Y %H:%M:%S")

  header = param + units

  str_args = '######################\nSettings:\n'
  if nwalkers is not None :
    str_args += 'nwalkers=' + str (nwalkers) + '\n' 
  if nsteps is not None :
    str_args += 'nsteps=' + str (nsteps) + '\n' 
  if coeff_discard is not None :
    str_args += 'discarded_steps=' + str (nsteps//coeff_discard) + '\n' 
  str_args += 'fit_amp' + str (fit_amp) + '\n'
  str_args += '#######################\n'
  header = str_args + header

  if projected_splittings :
    header = 'Indicated splittings are projected splittings nu* = nu sin a \n' + header
  header = 'https://apollinaire.readthedocs.io/en/latest \n' + header
  header = 'File creation date: ' + dt_string + '\n' + header

  if author is not None :
    header = 'Peakbagging performed by ' + author + ' with apollinaire (v' + str(__version__) + ') \n' + header
  else :
    header = 'Peakbagging performed by with apollinaire (v' + str(__version__) + ') \n' + header

  return header

if __name__=='__main__' :

  print ('Example of pkb header for spectroscopic observation (extended case):')
  print ('--------------------------------------------------------------------')
  print (make_header_pkb (extended=True, author='G.A.V.A.A.K', spectro=True, 
         projected_splittings=True, nwalkers=500, nsteps=500, coeff_discard=5))
  print ('Example of pkb header for photometric observation (reduced case):')
  print ('-----------------------------------------------------------------')
  print (make_header_pkb (extended=False, author='G.A.V.A.A.K', spectro=False))
  print ('Example of file header for background parameters:')
  print ('-----------------------------------------------------------------')
  print (make_header_background_param (n_harvey=2, author='G.A.V.A.A.K', 
         nwalkers=500, nsteps=500, coeff_discard=5))
  print ('Example of file header for pattern parameters:')
  print ('-----------------------------------------------------------------')
  print (make_header_pattern (author='G.A.V.A.A.K'))
