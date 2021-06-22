import numpy as np
from exetera.core.session import Session


with Session() as s:
  oldds = s.open_dataset('/home/ben/covid/ds_20210523_p_old.hdf5', 'r', 'oldds')
  newds = s.open_dataset('/home/ben/covid/ds_20210523_pt_new.hdf5', 'r', 'newds')

  for t in oldds.keys():
    if t in newds.keys():
      olddf = oldds[t]
      newdf = newds[t]

      for k in olddf.keys():
        if k in ('j_valid_from', 'j_valid_to'):
          continue
        oldf = olddf[k]
        newf = newdf[k]

        if oldf.indexed:
          oldf_i = oldf.indices[:]
          oldf_v = oldf.values[:]
          newf_i = newf.indices[:]
          newf_v = newf.values[:]
          indices_eq = np.array_equal(oldf_i, newf_i)
          values_eq = np.array_equal(oldf_v, newf_v)
          if indices_eq == False or values_eq == False:
            print(oldf, k, indices_eq, values_eq)
        else:
          oldf_d = oldf.data[:]
          newf_d = newf.data[:]
          if not np.array_equal(oldf_d, newf_d):
            print(oldf, k)
