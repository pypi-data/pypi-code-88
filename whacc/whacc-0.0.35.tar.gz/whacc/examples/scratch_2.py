# # # import h5py
# # # import matplotlib.pyplot as plt
# # # from whacc import image_tools
# # # import os
# # # from whacc import utils
# # #
# # # for h5_file in utils.get_h5s('/Users/phil/Dropbox/Autocurator/data/samsons_subsets/OLD_2'):
# # #     with h5py.File(h5_file, 'r') as h:
# # #         plt.figure(figsize=[20, 10])
# # #         plt.imshow(image_tools.img_unstacker(h['images'][:],40))
# # #         plt.title(h5_file.split('/')[-1])
# # #         plt.savefig(h5_file[:-3] + "_fig_plot.png")
# # #         plt.close()
# # #
# # #
# # # for k in utils.get_h5s('/Users/phil/Dropbox/Autocurator/data/samsons_subsets/OLD_2'):
# # #     with h5py.File(k, 'r') as h:
# # #         k2 = k[:-3]+'_TMP.h5'
# # #         with h5py.File(k2, 'w') as h2:
# # #             h2.create_dataset('all_inds', data=h['all_inds'][50:])
# # #             h2.create_dataset('images', data=h['images'][50:])
# # #             h2.create_dataset('in_range', data=h['in_range'][50:])
# # #             h2.create_dataset('labels', data=h['labels'][50:])
# # #             h2.create_dataset('retrain_H5_info', data=h['retrain_H5_info'][:])
# # #     os.remove(k)
# # #     os.rename(k2, k)
# # #
# # #
# # # import h5py
# # # import matplotlib.pyplot as plt
# # # from whacc import image_tools
# # #
# # # h5_file= '/Users/phil/Downloads/AH1159X18012021xS404_subset (1).h5'
# # # with h5py.File(h5_file, 'r') as h:
# # #     plt.figure(figsize=[20, 10])
# # #     plt.imshow(image_tools.img_unstacker(h['images'][:],10))
# # #     plt.title(h5_file.split('/')[-1])
# # #     print(len(h['labels'][:]))
# # #
# # #
# # #
# # #
# #
# # import numpy as np
# # import whacc
# # from whacc import analysis
# # import matplotlib.pyplot as plt
# #
# #
# # a = analysis.pole_plot(
# #     '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/master_train_test1.h5',
# #     pred_val = [0,0,0,0,0,0,0,.2,.4,.5,.6,.7,.8,.8,.6,.4,.2,.1,0,0,0,0],
# #     true_val = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
# #     len_plot = 10)
# #
# # a.plot_it()
# #
# #
# f1 = "/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/delete_after_oct_2021/AH0000x000000.h5"
# import h5py
#
# with h5py.File(f1, 'r') as h:
#     k = 'file_name_nums'
#     print(k, '   ', h[k].shape)
#     k = 'full_file_names'
#     print(k, '   ', (h[k].shape))
#     k = 'images'
#     print(k, '   ', h[k].shape)
#     k = 'in_range'
#     print(k, '   ', h[k].shape)
#     k = 'labels'
#     print(k, '   ', h[k].shape)
#     k = 'locations_x_y'
#     print(k, '   ', h[k].shape)
#     k = 'max_val_stack'
#     print(k, '   ', h[k].shape)
#     k = 'multiplier'
#     print(k, '   ', h[k].shape)
#     k = 'trial_nums_and_frame_nums'
#     print(k, '   ', h[k].shape)
#
# with h5py.File(save_directory + file_name, 'r+') as hf:  # with -> auto close in case of failure
#     hf.create_dataset("asdfasdf", data=loc_stack_all2)
#     for i, k in enumerate(loc_stack_all):
#         print(i)
#         hf.create_dataset("aaa"+str(i), data=k)
#
# loc_stack_all2 = loc_stack_all.copy()
#
#
#
#
# for i, k in enumerate(loc_stack_all):
#     if not k.shape==(4000, 2):
#         print(i)
#     # for kk in k.flatten():
#     #     print(kk.shape)
#     #         # if not kk.dtype=='int64':
#     #         #     print('booooo')
#     #
#     #


# import h5py
# import numpy as np
# import matplotlib.pyplot as plt
# cnt = 0
# f = "/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000.h5"
# with h5py.File(f, 'r') as h:
#     print(len(h['labels']))
#     for k in range(0, 1163998, 20000):
#         plt.figure()
#         plt.imshow(h['images'][k])
#         cnt+=1
#         # if cnt>=20 :
#         #     asdfasdf

from whacc import utils
from whacc import image_tools
import copy
import h5py
f = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000.h5'
f2 = '/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_80border_single_frame.h5'

h5c = image_tools.h5_iterative_creator(f2,
                 overwrite_if_file_exists=False,
                 max_img_height=61,
                 max_img_width=61,
                 close_and_open_on_each_iteration=True,
                 color_channel=False)
with h5py.File(f, 'r') as h:
    print(len(h['labels'][:]))
    h_cont = copy.deepcopy(h['labels'][:])
utils.create_master_dataset(h5c, [f], [h_cont], borders=80, max_pack_val=100)


####


f = "/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/autoCuratorDiverseDataset/AH0000x000000/AH0000x000000_80border_single_frame.h5"
with h5py.File(f, 'r') as h:
    utils.print_list_with_inds(h.keys())
    tmp1 = copy.deepcopy(h['frame_nums'][:])
