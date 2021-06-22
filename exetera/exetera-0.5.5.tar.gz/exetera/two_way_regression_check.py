import numpy as np
from exetera.core.session import Session


with Session() as s:
  oldds = s.open_dataset('/home/ben/covid/ds_20210523_t_old.hdf5', 'r', 'oldds')
  newds = s.open_dataset('/home/ben/covid/ds_20210523_t_new.hdf5', 'r', 'newds')

  olddf = oldds['tests']
  newdf = newds['tests']

  keys = ['mechanism_freetext']
  for k in keys:
    oldf = olddf[k]
    print(len(oldf))
    newf = newdf[k]
    print(len(newf))

    # print('check csv / old')
    # old_dataf = oldf.data[:]
    # new_dataf = newf.data[:]
    # for i in range(min(len(old_dataf), len(new_dataf))):
    #   if old_dataf[i] != new_dataf[i]:
    #     old_entry = "<empty>" if old_dataf[i] == '' else old_dataf[i]
    #     new_entry = "<empty>" if new_dataf[i] == '' else new_dataf[i]
    #     print(i)
    #     print("  old:", old_entry)
    #     print("  new:", new_entry)

    if oldf.indexed:
      old_datai = oldf.indices[:]
      new_datai = newf.indices[:]
      old_datav = oldf.values[:]
      new_datav = newf.values[:]
      for i in range(min(len(oldf), len(newf))):
        oldstart = old_datai[i]
        oldend = old_datai[i+1]
        newstart = new_datai[i]
        newend = new_datai[i+1]
        old_vals = old_datav[oldstart:oldend]
        new_vals = new_datav[newstart:newend]
        if not np.array_equal(old_vals, new_vals) or i < 20:
          print(k, i)
          print('old:', old_vals, old_vals.tobytes())
          print('new:', new_vals, new_vals.tobytes())
    else:
      old_data = oldf.data[:]
      new_data = newf.data[:]
      for i in range(min(len(oldf), len(newf))):
      	if old_data[i] != new_data[i] or i < 20:
          print(k, i)
          print('old:', old_data[i], 'new:', new_data[i])

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
