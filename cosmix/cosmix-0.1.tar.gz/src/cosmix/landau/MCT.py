
# def mct_materials():
#     """TBW."""
#
#     x = [10000, 1000, 1000, 2000, 3000, 1000, 10000, 4000]
#     path = Path(__file__).parent.joinpath('data', 'MCT')
#     g4file_dict = {
#         'Cd': Path(path, 'stepsize_proton_10MeV_1um_Cd_10000_EMopt4.ascii'),
#         'Hg': Path(path, 'stepsize_proton_10MeV_1um_Hg_10000_EMopt4.ascii'),
#         'Te': Path(path, 'stepsize_proton_10MeV_1um_Te_10000_EMopt4.ascii'),
#         r'Hg$_{0.8}$Cd$_{0.2}$Te': Path(path, 'stepsize_proton_10MeV_1um_HgCdTe20_10000_EMopt4.ascii'),
#         # r'Hg$_{0.6}$Cd$_{0.4}$Te': Path(path, 'stepsize_proton_10MeV_1um_HgCdTe40_10000_EMopt4.ascii'),
#         # r'Hg$_{0.4}$Cd$_{0.6}$Te': Path(path, 'stepsize_proton_10MeV_1um_HgCdTe60_10000_EMopt4.ascii'),
#         # r'Hg$_{0.2}$Cd$_{0.8}$Te': Path(path, 'stepsize_proton_10MeV_1um_HgCdTe80_10000_EMopt4.ascii'),
#     }
#     fitted_langau_arrays = []
#     # fitted_langau_arrays[0] -> Cd
#     # fitted_langau_arrays[1] -> Hg
#     # fitted_langau_arrays[2] -> Te
#     mct_edep_cd = []
#     mct_edep_hg = []
#     mct_edep_te = []
#
#     plt.figure()
#     hist_bins = np.linspace(0, 100, 1000)
#
#     for lab, g4file in g4file_dict.items():
#
#         scale = 1.
#         grp_val = None  # 2 or None
#         energy = 10.    # MeV
#         if float(energy) < 100.:
#             grp_val = 2
#
#         geant4_all_edep = load_geant4_histogram(g4file, hist_type='all_edep',
#                                                 skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])
#
#         geant4_all_edep = load_data_into_histogram(geant4_all_edep.values, plato=False, regrp=grp_val)
#
#         # # plt.hist(geant4_all_edep[:, 0] * 1000, bins=hist_bins, weights=geant4_all_edep[:, 1],
#         plt.hist(geant4_all_edep[:, 0] * 1000, bins=geant4_all_edep[::10, 0] * 1000, weights=geant4_all_edep[:, 1],
#                  density=True, histtype='step', label=lab)
#
#         # ########### FITTING landau
#         mpv, eta, sigma, amp, scale = simple_fit_to_data(geant4_all_edep, label=lab, scale_factor=scale)
#         if grp_val is not None:
#             amp /= grp_val
#         mpv /= scale
#         eta /= scale
#         sigma /= scale
#         print('######\n' + lab)
#         print('energy: %1.1e    mpv: %1.3f   eta: %1.3e   sigma: %1.3e   amp: %1.3f   scale: %1.1f' %
#               (float(energy), mpv, eta, sigma, amp, scale))
#
#         import pylandau
#         fitted_langau_arrays += [pylandau.langau(geant4_all_edep[:, 0] * 1000, mpv, eta, sigma, amp * grp_val)]
#         # mpv*scale, eta*scale, sigma*scale, amp*grp_val),
#         # plt.plot(geant4_all_edep[:, 0] * 1000,   # * scale,
#         #          fitted_langau_arrays[-1],
#         #          '--', label=lab + ' langau')
#
#         cum_sum = np.cumsum(fitted_langau_arrays[-1])
#         cum_sum /= np.max(cum_sum)
#         cdf = np.stack((geant4_all_edep[:, 0] * 1000, cum_sum), axis=1)
#         end = int(np.where(cdf[:, 1] >= 1.)[0][0]) + 1
#         cdf = cdf[:end, :]
#         for _ in range(10000):
#             if lab == 'Cd':
#                 mct_edep_cd += [sampling_distribution(cdf)]
#             elif lab == 'Hg':
#                 mct_edep_hg += [sampling_distribution(cdf)]
#             elif lab == 'Te':
#                 mct_edep_te += [sampling_distribution(cdf)]
#         pass
#         # ########### FITTING landau
#
#     plt.title('G4, total energy deposited per event')
#     plt.xlabel('energy (keV)')
#     plt.ylabel('counts')
#     # plt.legend()
#
#     # plt.figure()
#
#     # plt.hist(mct_edep_cd,  bins=geant4_all_edep[::10, 0] * 1000, histtype='step', density=True, label='Cd contr. sampled')
#     # plt.hist(mct_edep_hg,  bins=geant4_all_edep[::10, 0] * 1000, histtype='step', density=True, label='Hg contr. sampled')
#     # plt.hist(mct_edep_te,  bins=geant4_all_edep[::10, 0] * 1000, histtype='step', density=True, label='Te contr. sampled')
#     plt.hist(mct_edep_cd + mct_edep_hg + mct_edep_te,  density=True, bins=geant4_all_edep[::10, 0] * 1000,
#              histtype='step', label='Cd+Hg+Te contr. sampled')
#     plt.legend()
#
#
#     # cd_all_edep = load_geant4_histogram(Path(path, 'stepsize_proton_10MeV_1um_Cd_10000_EMopt4.ascii'),
#     #                                     hist_type='all_edep', skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])
#     # cd_all_edep = load_data_into_histogram(cd_all_edep.values, plato=False)
#     # hg_all_edep = load_geant4_histogram(Path(path, 'stepsize_proton_10MeV_1um_Hg_10000_EMopt4.ascii'),
#     #                                     hist_type='all_edep', skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])
#     # hg_all_edep = load_data_into_histogram(hg_all_edep.values, plato=False)
#     # te_all_edep = load_geant4_histogram(Path(path, 'stepsize_proton_10MeV_1um_Te_10000_EMopt4.ascii'),
#     #                                     hist_type='all_edep', skip_rows=sum(x[:6]) + 4 * 7, read_rows=x[6])
#     # te_all_edep = load_data_into_histogram(te_all_edep.values, plato=False)
#
#     # cd_factor = 0.2
#     # mix_hgcdte_20 = hg_all_edep
#     # mix_hgcdte_20[:, 1] = hg_all_edep[:, 1] * 0.5 * (1. - cd_factor) + \
#     #                       cd_all_edep[:, 1] * 0.5 * cd_factor + \
#     #                       te_all_edep[:, 1] * 0.5
#     # plt.hist(mix_hgcdte_20[:, 0] * 1000, bins=hist_bins, weights=mix_hgcdte_20[:, 1], density=True, histtype='step',
#     #          label=r'mix Hg$_{0.8}$Cd$_{0.2}$Te')
#     #
#     # cd_factor = 0.4
#     # mix_hgcdte_40 = hg_all_edep
#     # mix_hgcdte_40[:, 1] = hg_all_edep[:, 1] * 0.5 * (1. - cd_factor) + \
#     #                       cd_all_edep[:, 1] * 0.5 * cd_factor + \
#     #                       te_all_edep[:, 1] * 0.5
#     # plt.hist(mix_hgcdte_40[:, 0] * 1000, bins=hist_bins, weights=mix_hgcdte_40[:, 1], density=True, histtype='step',
#     #          label=r'mix Hg$_{0.6}$Cd$_{0.4}$Te')
#     #
#     # cd_factor = 0.6
#     # mix_hgcdte_60 = hg_all_edep
#     # mix_hgcdte_60[:, 1] = hg_all_edep[:, 1] * 0.5 * (1. - cd_factor) + \
#     #                       cd_all_edep[:, 1] * 0.5 * cd_factor + \
#     #                       te_all_edep[:, 1] * 0.5
#     # plt.hist(mix_hgcdte_60[:, 0] * 1000, bins=hist_bins, weights=mix_hgcdte_60[:, 1], density=True, histtype='step',
#     #          label=r'mix Hg$_{0.4}$Cd$_{0.6}$Te')
#     #
#     # cd_factor = 0.8
#     # mix_hgcdte_80 = hg_all_edep
#     # mix_hgcdte_80[:, 1] = hg_all_edep[:, 1] * 0.5 * (1. - cd_factor) + \
#     #                       cd_all_edep[:, 1] * 0.5 * cd_factor + \
#     #                       te_all_edep[:, 1] * 0.5
#     # plt.hist(mix_hgcdte_80[:, 0] * 1000, bins=hist_bins, weights=mix_hgcdte_80[:, 1], density=True, histtype='step',
#     #          label=r'mix Hg$_{0.2}$Cd$_{0.8}$Te')
#
#
#     # plt.figure()
#     # hist_bins = np.linspace(-8, 1, 300)
#     #
#     # for lab, g4file in g4file_dict.items():
#     #     geant4_step_size = load_geant4_histogram(g4file, hist_type='step_size', skip_rows=4, read_rows=x[0])
#     #
#     #     geant4_step_size = load_data_into_histogram(geant4_step_size.values, plato=False)
#     #
#     #     # geant4_step_size[:, 0] is in mm not in um, therefore we need to add 3 order of magnitude to it !!!
#     #     plt.hist(geant4_step_size[:, 0] + 3., bins=hist_bins, weights=geant4_step_size[:, 1],
#     #              histtype='step', density=True, label=lab)
#     #
#     # plt.legend(loc='upper left')
#     # plt.title('G4, Proton step size per step')
#     # plt.xlabel('step (um)')
#     # plt.ylabel('Counts')

