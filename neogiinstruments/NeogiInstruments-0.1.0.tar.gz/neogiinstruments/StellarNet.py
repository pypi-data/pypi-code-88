# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:42:22 2020

@author: TheFermiSea
"""
import stellarnet as sn
import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from itertools import count


# import usb.core


class StellarNet:  #Instantiated as SN
# =============================================================================
#
#         '''
#         Class to operate the StellarNet spectrometer
#
#         Functions:
#         TBD
#
#         '''
# =============================================================================
# =============================================================================
#     def __init__(self):
#         dev = usb.core.find(find_all=True)
#         dev[0].set_configuration()
#         self.spec = sn.find_devices([0])
# =============================================================================
    def __init__(self):
        '''Initialization:
            finds spectrometer'''
        # dev = usb.core.find(find_all=True) ##seems to fix
        # dev[0].set_configuration()         ##issues with Windows
        self.spec = sn.find_devices()[0]

    def IntTime(self,it=100):
        '''Function has two operations:
            pass '?' to request current integration time
            pass int to set integration time'''
        if it =='?':
           return self.spec.get_config()['int_time']
        elif type(it)==int:
           self.spec.set_config(int_time = it)
        else:
            print('Invalid Input')

    def AvgScans(self,scans=1):
        '''Funtion has two operations:
            pass '?' to request current # of scans averaged
            pass int to set # of scans averaged'''
        if scans =='?':
            return self.spec.get_config()['scans_to_avg']
        elif type(scans)==int:
            self.spec.set_config(scans_to_avg = scans)
        else:
            print('Invalid Input')

    def GetSpec(self,int_time=100, normalize=False):
        '''Function to retrieve spectrum
        will return a list of arrays :
                w= wavelength
                s = intensity
        Function has two operations:
            default (normalize = False) will return raw spectrum
            normalize = True will return spectrum normalized to integration time'''
        self.IntTime(int_time)
        if normalize == False:
            s = np.asarray(self.spec.read_spectrum())
            w = np.asarray([self.spec.compute_lambda(i) for i in range(s.size)])
            return [w,s]
        elif normalize == True:
            s = np.asarray(self.spec.read_spectrum())
            s = s/float(self.IntTime('?'))
            w = np.asarray([self.spec.compute_lambda(i) for i in range(s.size)])
            return [w,s]
        else:
            print('Input invalid')

    # def Live(self, n=100, norm=False):  ##old dumb way. Causes infinite loop
    #     plt.ion()
    #     fig, ax = plt.subplots()
    #     i=0
    #     try:
    #         while i<n:
    #             ax.clear()
    #             ax.plot(*self.GetSpec(normalize = norm))
    #             ax.set(xlabel='Wavelength (nm)')
    #             plt.pause(.001)
    #             i = i+1
    #     except KeyboardInterrupt:
    #         pass
    def CollectBackground(self):
        '''Set equal to a variable'''
        input('Shutter the laser and press enter')
        int_time = self.IntTime('?')
        bkg = self.GetSpec(int_time=int_time)
        return bkg
    # def get_spec_bkg_sub(self,int_time):
    #     bkg = CollectBackground()
    #     spec = self.GetSpec(int_time=int_time)
    #     spec_sub_bkg[0] = bkg[0]
    #     spec_sub_bkg[1] = spec[1]
    #     return spec_sub_bkg

    def IterateCollection(self):  #TBD  Consider IntTime
        pass

    def Live(self, n=100, norm = False):
        index = count()
        fig = plt.figure()
        ax = fig.add_subplot()
        def animate(i):
            plt.cla()
            ax.plot(*self.GetSpec(normalize = norm))
            ax.set(xlabel='Wavelength (nm)', ylabel = 'Counts')
            plt.tight_layout()
            plt.show()
            plt.pause(.01)

        ani = FuncAnimation(plt.gcf(), animate, interval = 1)
        plt.tight_layout()
        plt.show()



StellarNet = StellarNet()


#%%  test bed
