import numpy as np
from exetera.core.session import Session


with Session() as s:
  oldds = s.open_dataset('/home/ben/covid/ds_20210523_patients_old.hdf5', 'r', 'oldds')
  newds = s.open_dataset('/home/ben/covid/ds_20210523_patients_new.hdf5', 'r', 'newds')

  olddf = oldds['patients']
  newdf = newds['patients']

  csvdf = np.load('/home/ben/covid/ds_patients_20210523.npz')
  keys = ['diabetes_oral_other_medication']
  for k in keys:
    csvf = csvdf[k]
    print(len(csvf), csvf.dtype)
    oldf = olddf[k]
    print(len(oldf))
    newf = newdf[k]
    print(len(newf))

    print('check csv / old')
    old_dataf = oldf.data[:]
    new_dataf = newf.data[:]
    for i in range(min(len(old_dataf), len(new_dataf))):
      if old_dataf[i] != new_dataf[i]:
        csv_entry = "<empty>" if csvf[i] == '' else csvf[i]
        old_entry = "<empty>" if old_dataf[i] == '' else old_dataf[i]
        new_entry = "<empty>" if new_dataf[i] == '' else new_dataf[i]
        print(i)
        print("  csv:", csv_entry)
        print("  old:", old_entry)
        print("  new:", new_entry)
#    if oldf.indexed:
#      oldf_i = oldf.indices[:]
#      oldf_v = oldf.values[:]
#      newf_i = newf.indices[:]
#      newf_v = newf.values[:]
#      indices_eq = np.array_equal(oldf_i, newf_i)
#      values_eq = np.array_equal(oldf_v, newf_v)
#      if indices_eq == False or values_eq == False:
#        print(oldf, k, indices_eq, values_eq)
#    else:
#      oldf_d = oldf.data[:]
#      newf_d = newf.data[:]
#      if not np.array_equal(oldf_d, newf_d):
#        print(oldf, k)
