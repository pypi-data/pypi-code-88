import csv
import numpy as np

src_filename = '/home/ben/covid/patients_export_geocodes_20210523040026.csv'
dest_filename = '/home/ben/covid/ds_patients_20210523.npz'

with open(src_filename) as f:
  csvr = csv.reader(f)
  csvri = iter(csvr)
  fields = next(csvri)
  # keys = ['cancer_clinical_trial_site', 'cancer_type', 'clinical_study_institutions']
  keys = ['diabetes_oral_other_medication']
  # keys = ['clinical_study_names', 'clinical_study_nct_ids', 'diabetes_oral_other_medication',
  #         'outward_postcode_region', 'se_postcode', 'vs_other']
  fieldmap = [fields.index(k) for k in keys]
  fieldmap_len = len(fieldmap)
  print(fieldmap)
  field_lists = [list() for _ in fieldmap]
  for i_r, row in enumerate(csvri):
    for i in range(fieldmap_len):
      field_lists[i].append(row[fieldmap[i]])
    if i_r % 100000 == 0:
      print("parsed {} rows".format(i_r))


  for i_v, v in enumerate(field_lists[0]):
    if v != '':
      print(i_v, v)
  print('done')


  to_persist = dict()
  for i_f, f in enumerate(keys):
    to_persist[f] = np.asarray(field_lists[i_f])
  np.savez(dest_filename, **to_persist)

  ndf = np.load(dest_filename)
  arr = ndf[keys[0]]
  print(len(arr), arr.dtype)
  for v in ndf[keys[0]]:
    if v != '':
      print(v)
  print('done')
