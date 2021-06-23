#!/usr/bin/env python
# -*- coding: utf-8 -*-

# enpt_enmapboxapp, A QGIS EnMAPBox plugin providing a GUI for the EnMAP processing tools (EnPT)
#
# Copyright (C) 2018-2021 Daniel Scheffler (GFZ Potsdam, daniel.scheffler@gfz-potsdam.de)
#
# This software was developed within the context of the EnMAP project supported
# by the DLR Space Administration with funds of the German Federal Ministry of
# Economic Affairs and Energy (on the basis of a decision by the German Bundestag:
# 50 EE 1529) and contributions from DLR, GFZ and OHB System AG.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for `enpt_enmapboxapp` package."""

import os
from tempfile import TemporaryDirectory
import pickle

from unittest import TestCase, skipIf
from qgis.core import QgsProcessingAlgorithm, QgsProcessingContext, QgsProcessingFeedback, QgsProcessingProvider, NULL

from enmapbox.testing import initQgisApplication
from enpt_enmapboxapp.enpt_enmapboxapp import EnPTEnMAPBoxApp, EnMAPBoxApplication
from enpt_enmapboxapp.enpt_algorithm import EnPTAlgorithm
from enpt_enmapboxapp.enpt_external_algorithm import ExternalEnPTAlgorithm
# from enpt_enmapboxapp.enpt_enmapboxapp import ExampleAppGUI

# initialize the QGIS API + several background states
APP = initQgisApplication()

# set on True to show widgets and wait until a user closes them.
SHOW_GUI = True

# os.environ['QT_X11_NO_MITSHM'] = "1"

# FIXME replace hardcoded paths
enpt_test_parameters = dict(
    anaconda_root='',
    CPUs=12,
    auto_download_ecmwf=False,
    deadpix_P_algorithm='spectral',
    deadpix_P_interp_spectral='linear',
    deadpix_P_interp_spatial='linear',
    drop_bad_bands=True,
    disable_progress_bars=False,
    output_format='GTiff',
    enable_keystone_correction=False,
    enable_vnir_swir_coreg=False,
    json_config=None,
    n_lines_to_append=NULL,
    mode_ac='combined',
    ortho_resampAlg='bilinear',
    vswir_overlap_algorithm='vnir_only',
    output_dir='TEMPORARY_OUTPUT',
    path_earthSunDist=None,
    path_l1b_enmap_image='D:\\Daten\\Code\\python\\EnPT\\tests\\data\\EnMAP_Level_1B\\'
                         'ENMAP01-____L1B-DT000000987_20130205T105307Z_001_V000101_20190426T143700Z__rows0-99.zip',
    path_l1b_enmap_image_gapfill=None,
    path_dem='D:\\Daten\\Code\\python\\EnPT\\tests\\data\\DLR_L2A_DEM_UTM32.bsq',
    path_reference_image=None,
    path_solar_irr=None,
    run_deadpix_P=True,
    run_smile_P=False,
    scale_factor_boa_ref=10000,
    scale_factor_toa_ref=10000,
    sicor_cache_dir=None,
    target_projection_type='UTM',
    working_dir=None)


class TestExampleEnMAPBoxApp(TestCase):

    # def test_algorithms(self):
    #     """
    #     Test your core algorithms, which might not require any GUI or QGIS.
    #     """
    #
    #     args, kwds = exampleAlgorithm()
    #
    #     self.assertEqual(args, ())
    #     self.assertEqual(kwds, dict())
    #
    #     args, kwds = exampleAlgorithm(42, foo='bar')
    #     self.assertEqual(args[0], 42)
    #     self.assertEqual(kwds['foo'], 'bar')

    def test_processingAlgorithms(self):
        for algname, ALG in zip(['EnPTAlgorithm', 'ExternalEnPTAlgorith'],
                                [EnPTAlgorithm, ExternalEnPTAlgorithm]):

            with self.subTest(ALG=algname):
                try:
                    os.environ['IS_ENPT_GUI_TEST'] = '1'

                    alg = ALG()
                    self.assertIsInstance(alg, QgsProcessingAlgorithm)

                    alg2 = alg.createInstance()
                    self.assertIsInstance(alg2, QgsProcessingAlgorithm)

                    with TemporaryDirectory() as td:
                        params = enpt_test_parameters.copy()
                        params['output_dir'] = td
                        params['path_l1b_enmap_image'] = os.path.join('dummy', 'path', 'to', 'EnMAP_file.zip')
                        params['path_dem'] = os.path.join('dummy', 'path', 'to', 'DEM.bsq')

                        # call the EnPT_Controller with the above params, it will pickle.dump them to disk
                        outputs = alg.processAlgorithm(params,
                                                       QgsProcessingContext(),
                                                       QgsProcessingFeedback())

                        self.assertIsInstance(outputs, dict)

                        # unpickle the dumped args/kwargs and validate that EnPT received them correctly
                        content = None
                        try:
                            with open(os.path.join(td, 'received_args_kwargs.pkl'), 'rb') as inF:
                                content = pickle.load(inF)
                        except FileNotFoundError:
                            pass

                        self.assertIsNotNone(content, 'The EnPT_Controller did not dump the '
                                                      'received arguments or did not receive any.')

                        none_params = [k for k, v in params.items() if params[k] in [None, NULL]]
                        for k, v in params.items():
                            if k not in ['anaconda_root', 'json_config'] + none_params:
                                self.assertTrue(k in content['kwargs'],
                                                f"Missing key '{k}' in received parameters.")
                                self.assertEqual(v, content['kwargs'][k])

                finally:
                    del os.environ['IS_ENPT_GUI_TEST']

    # def test_dialog(self):
    #     """
    #     Test your Qt GUI components, without any EnMAP-Box
    #     """
    #     g = ExampleAppGUI()
    #     g.show()
    #
    #     self.assertIsInstance(g.numberOfClicks(), int)
    #     self.assertEqual(g.numberOfClicks(), 0)
    #
    #     # click the button programmatically
    #     g.btn.click()
    #     self.assertEqual(g.numberOfClicks(), 1)
    #
    #     if SHOW_GUI:
    #         APP.exec_()

    @skipIf(os.getenv('IS_CI_ENV'), reason='to be tested manually')
    def test_with_EnMAPBox(self):
        """
        Finally, test if your application can be added into the EnMAP-Box
        """
        from enmapbox import EnMAPBox
        enmapBox = EnMAPBox(None)
        self.assertIsInstance(enmapBox, EnMAPBox)

        myApp = EnPTEnMAPBoxApp(enmapBox)
        self.assertIsInstance(myApp, EnMAPBoxApplication)
        enmapBox.addApplication(myApp)

        provider = enmapBox.processingProvider()
        self.assertIsInstance(provider, QgsProcessingProvider)
        algorithmNames = [a.name() for a in provider.algorithms()]
        for name in ['EnPTAlgorithm', ]:
            self.assertTrue(name in algorithmNames)

        if SHOW_GUI:
            APP.exec_()


if __name__ == "__main__":
    import unittest
    SHOW_GUI = False

    # quiet matplotlib
    import logging
    mpl_logger = logging.getLogger('matplotlib')
    mpl_logger.setLevel(logging.WARNING)

    # run tests
    unittest.main()
