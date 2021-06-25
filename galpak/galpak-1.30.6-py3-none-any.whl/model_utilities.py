# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

# LOGGING CONFIGURATION
from .galpak3d import *
from .galaxy_parameters import GalaxyParameters

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK: DiskUtilities:')


#################################################################
#
class ModelExt:
    ##Methods to update galaxy parameters

    def set_v22(self, galaxy):
        """
        Computes velocity at 2.2 Re
        :param galaxy: GalaxyParameters | Table
        :return: return V(2.2 Re)

        This Model method will add/update the galaxy property
        """
        #V at 2.2 x Rd
        x = 2.2 * galaxy['radius'] / 1.68
        _v22 = self.set_velocity_profile(galaxy, x)
        #set v22 for galaxy
        if isinstance(galaxy, GalaxyParameters):
            logger.info("Adding v22 property to GalaxyParameters class")
            galaxy.set_v22(_v22)
        elif isinstance(galaxy, Table):
            logger.info("Adding v22 property to Table class")
            if 'v22' not in galaxy.colnames:
                galaxy.add_column(_v22,name='v22')
            else:
                galaxy['v22']=_v22
        else:
            raise Exception("set_v22 must use a GalaxyParameters or a Table")

    def set_dvdx(self, galaxy):
        """
        Computes Velocity inner slope at R=0
        :param galaxy: GalaxyParameters | Table
        :return: dv/dx(r=0) using the units of GalaxyParameters (km/s / pix)

        This Model method will add/update the galaxy property
        """
        dx = 0.1
        _dvdx = (self.set_velocity_profile(galaxy, dx)) / (dx)
        if isinstance(galaxy, GalaxyParameters):
            logger.info("Adding dvdx property to GalaxyParameters class")
            galaxy.set_dvdx(_dvdx)
        elif isinstance(galaxy, Table):
            logger.info("Adding dvdx property to Table class")
            if 'dvdx' not in galaxy.colnames:
                galaxy.add_column(_dvdx,name='dvdx')
            else:
                galaxy['dvdx']=_dvdx
        else:
            raise Exception("set_dvdx(p) must use a GalaxyParameters or Table")


#############
### Utilities
##
#@fixme: make tests
class modelPlots:
    pixscale = None

    def plot_velocity(self, parameters, chain=None, figure=3, xmax=None, v_ymax=None, sigma=None,
                      filename=None, legendOff=False, normalizeX=False):
        """
        plot velocity profile utility
            uses _plot_vprofile private method from original Model class

        :param parameters: galaxy GalaxyParameters
        :param pixscale: float | None [default]
        :param normalizeX: boolean [default=False] to normalize x-axis to Rhalf
        :return:
        """

        fig=plt.figure(figure)
        fig.set_figheight(6)
        fig.set_figwidth(9)

        if filename is not None:
            plt.clf()

        plt.subplot(1,2,2)
        self.plot_vprofile(parameters, chain=chain, normalizeX=normalizeX, xmax=xmax, ymax=v_ymax,
                           legendOff=legendOff, figure=None)

        plt.subplot(1,2,1)
        self.plot_SBprofile(parameters, chain=chain, normalizeX=normalizeX, xmax=xmax,
                            legendOff=legendOff, figure=None, sigma=sigma)


        if filename is None:
            plt.show()
        else:
            plt.savefig(filename)
            plt.close()


    def plot_SBprofile(self, galaxy, chain=None, sigma=None, fmt=None, ymax=None, xmax=None, normalizeX=False, legendOff=False, figure=3, filename=None):
        """

        :param galaxy:
        :param model:
        :param normalizeX:
        :return:
        """
        percentile = galaxy.ICpercentile

        if figure is not None:
            plt.figure(figure,figsize=(6,6))
            if filename is not None:
                    plt.clf()

        if self.pixscale is not None:
            pixscale = self.pixscale
        redshift = self.redshift

        if self.redshift is not None:
            kpc = self.kpc
        else:
            logger.warning("redshift not set")

        xpix = np.r_[0.1:galaxy['radius']*5:0.1]

        if self.redshift is not None and self.pixscale is not None:
            x = xpix * kpc * pixscale
            rhalf = galaxy['radius'] * kpc * pixscale
        else:
            x = xpix.copy()
            rhalf = galaxy['radius']

        if normalizeX:
            x = x / rhalf
            rhalf = 1.

        if fmt is None:
            fmt = 'k-'

        f_x = self.set_flux_profile(galaxy, xpix)
        f_x = f_x/np.max(f_x)
        plt.plot(x,f_x,fmt,label='SB(r) ' + self.flux_profile)

        #add errorbar
        if sigma is not None:
            idx = np.arange(0,len(xpix),len(xpix)/20.,dtype=np.int64)
            plt.errorbar(x[idx],f_x[idx],yerr=sigma)

        if chain is not None and self.flux_profile != 'user':
            if not isinstance(chain, Table):
                raise ValueError("Chain must be passed as an astropy Table")
            else:
                med, low, up = self.predict_SBprofile(xpix, chain=chain, percentile=percentile)
                plt.plot(x, up, 'r', lw=1); plt.plot(x, low, 'r', lw=1);
                plt.fill_between(x.flatten(), low, up, color="grey", alpha=0.5, label='%d%%' % (percentile))

        plt.axvline(2*rhalf,ls=':',label= '2 Rhalf')
        sini = np.sin(np.radians(galaxy['inclination']))
        plt.ylabel('SB profile')

        if normalizeX == False:
            if self.redshift is not None and self.pixscale is not None:
                plt.xlabel('x (kpc)')
            else:
                plt.xlabel('x (pix)')
        else:
            plt.xlabel('r/Rhalf')
        plt.xlim(-0.1*rhalf,5*rhalf)
        plt.ylim([0.001,2])
        plt.yscale('log')

        if legendOff is False:
            plt.legend()

        if filename is not None:
            plt.savefig(filename)
            plt.close()

    def plot_vprofile(self, galaxy, chain=None,  normalizeX=False, legendOff=False, ymax=None, xmax=None, fmt=None, figure=3, filename=None):
        """

        :param parameters:
        :param chain:
        :param xmax: None [Default]
        :param normalizeX: False [Default] | True
        :return:
        """
        if figure is not None:
            plt.figure(figure,figsize=(6,6))
            if filename is not None:
                plt.clf()

        percentile = galaxy.ICpercentile

        if self.pixscale is not None:
            pixscale = self.pixscale
        redshift = self.redshift

        if self.redshift is not None:
            kpc = self.kpc

        if xmax is None:
            xpix = np.r_[0.01:galaxy['radius']*5:0.1]
        else:
            xpix = np.r_[0.01:xmax:1.]

        if self.redshift is not None and self.pixscale is not None:
            x = xpix * kpc * pixscale
            rhalf = galaxy['radius'] * kpc * pixscale
            #plt.title('Rhalf %.2f (kpc)' % (galaxy.radius * kpc * pixscale))
        else:
            x = xpix.copy()
            rhalf = galaxy['radius']
            #plt.title('Rhalf %.2f (pix)' % (galaxy.radius))

        if normalizeX:
            x = x / rhalf
            rhalf = 1.

        #plot error if sub_chain
        if chain is not None:
            if not isinstance(chain, Table):
                raise ValueError("Chain must be passed as an astropy Table")
            else:
                mu, low, up = self.predict_velocity(xpix, chain=chain, percentile=percentile)
                plt.plot(x, up, 'r', lw=1); plt.plot(x, low, 'r', lw=1);
                plt.fill_between(x.flatten(), low, up, color="grey", alpha=0.5, label='%d%%' % (percentile))
                fmt='k'
        elif fmt is None:
            fmt='k+'

        v_x = self.set_velocity_profile(galaxy, xpix)
        plt.plot(x,v_x,fmt,label='V(r) ' + self.rotation_curve)

        plt.axvline(2*rhalf,ls=':',label= '2 Rhalf')
        sini = np.sin(np.radians(galaxy['inclination']))
        plt.ylabel('V(km/s) deproj.')

        if self.pixscale is not None and self.redshift is not None:
            Mdyn = self.compute_Mdyn_at_Rhalf(galaxy)
            title = "Mdyn(Re) = %.2f " %(np.log10(Mdyn))
            Mdyn2 = self.compute_Mdyn_at_Rhalf(galaxy,radius=galaxy['radius']*2)
            title += " Mdyn(2Re) = %.2f " %(np.log10(Mdyn2))
        else:
            title = 'Rotation curve'

        ax=plt.gca()
        #plt.text(0.2,0.8,"log Mdyn(R1/2) = %.2f" %(np.log10(Mdyn)), transform=ax.transAxes)

        if legendOff is False:
            self.set_v22(galaxy)
            v22 = galaxy.v22
            plt.text(0.6,0.95,"V(2.2 Rd) %d km/s" % (v22),transform=ax.transAxes)

        if isinstance(galaxy, GalaxyParameters):
            if 'virial_velocity' in galaxy.names:
                Vvir = galaxy['virial_velocity']
                Mvir, Rvir = self.compute_MvirRvir(Vvir)
                logMvir=np.log10(Mvir)
                plt.axhline(Vvir, label='Vvir')
                #title += "Mvir %.2f " %(logMvir)
                if legendOff is False:
                    plt.text(0.6,0.9,"Vvir %d [km/s]" % (Vvir),transform=ax.transAxes)
                    plt.text(0.6,0.85,"Mvir %.2f [log Msun]" % (np.log10(Mvir)), transform=ax.transAxes)
                    plt.text(0.6,0.8, "Rvir %d [kpc] " % (Rvir), transform=ax.transAxes)

            elif 'maximum_velocity' in galaxy.names:
                vmax = galaxy['maximum_velocity']
                if legendOff is False:
                    plt.axhline(vmax, label='Vmax')
                    plt.text(0.6,0.9,"Vmax %d km/s" % (vmax),transform=ax.transAxes)


        #_xmin, _xmax = -0.1 * np.max(x)/3, 1.1*np.max(x)/3.
        #plt.xlim(_xmin, _xmax)
        if xmax is None:
            plt.xlim(-0.1*rhalf,5*rhalf)
        else:
            plt.xlim(-0.1*rhalf,xmax)
        if ymax is not None:
            plt.ylim(-10,ymax)


        if normalizeX == False:
            if self.redshift is not None and self.pixscale is not None:
                plt.xlabel('x (kpc)')
            else:
                plt.xlabel('x (pix)')
        else:
            plt.xlabel('r/Rhalf')
        #
        if legendOff is False:
            plt.legend(loc=2)
            plt.title(title)

        if filename is not None:
            plt.savefig(filename)
            plt.close()


    def predict_velocity(self, Xnew, chain, percentile=95):
        ci=[(100-percentile)/2.0, 50., 50+percentile/2.0 ]
        #mu = [np.median(self.set_velocity_profile(chain,x)) for x in Xnew]
        res = [np.nanpercentile(self.set_velocity_profile(chain,x),ci) for x in Xnew]
        res = np.array(res)

        #return median, low, upper range
        return res[:,1],res[:,0],res[:,2]

    def predict_SBprofile(self, Xnew, chain, percentile=95):
        ci=[(100-percentile)/2.0, 50., 50+percentile/2.0 ]
        #mu = [np.median(self.set_flux_profile(chain,x)) for x in Xnew]
        res = [np.nanpercentile(self.set_flux_profile(chain,x),ci) for x in Xnew]
        res = np.array(res)

        #return median, low, upper range
        return res[:,1],res[:,0],res[:,2]
