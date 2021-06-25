# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#IMPORTS
import os,re
import sys

import scipy
from scipy import ndimage
from scipy.signal import convolve2d as conv2d_scipy
import astropy
import astropy.io.ascii as asciitable
from astropy.convolution import convolve_fft as conv2d_astro
from astropy.table import Table

import math
import numpy as np
np.random.seed(seed=1234)
from copy import deepcopy

# LOGGING CONFIGURATION
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK: Plots')

from .galaxy_parameters import GalaxyParameters
from .hyperspectral_cube import HyperspectralCube as HyperCube
from .convolution import convolve_2d as conv2d_intern

# OPTIONAL IMPORTS
try:
    import bottleneck as bn
except ImportError:
    logger.info("bottleneck (optional) not installed, performances will be degraded")
    import numpy as bn

#matplotlib
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import inset_locator as inl
# from matplotlib.ticker import MaxNLocator
from matplotlib import pyplot as plot


class Plots:

    def plot_mcmc(self, filename=None, method=None, plot_likelihood=False, adapt_range='5stdev', fontsize=10):
        """
        Plot the MCMC chain details, and then either show it or save it to a file.

        filepath: string
            If specified, will write the plot to a file instead of showing it.
            The file will be created at the provided filepath, be it absolute or relative.
            The extension of the file must be either png or pdf.
        plot_likelihood: bool
            True to plot -log[chi2] instead
        adapt_range: string
            'boundaries'  to adapt the range to boundaries
            'minmax' [default]  to adapt the range to min/max values
            '3stdev'   to adapt the range to 3 x stdev
            '5stdev'   to adapt the range to 5 x stdev
        fontsize: int
            to change the fontsize

        """
        if self.chain is None:
            raise RuntimeError(self.NO_CHAIN_ERROR)

        if filename is not None:
            name, extension = os.path.splitext(filename)
            supported_extensions = ['.png', '.pdf']
            if not extension in supported_extensions:
                raise ValueError("Extension '%s' is not supported, use %s.",
                                 extension, ', '.join(supported_extensions))

        if method is None:
            method = self.method

        if len(self.chain)>1000:
            fmt='b-'
        else:
            fmt='b.'
        alpha=1
        ms=3

        chain = self.chain.copy()
        xmin = self.chain.xmin
        xmax = self.chain.xmax
        chain_size = np.size(chain, 0)
        idx = np.arange(0,chain_size)

        if method == 'chi_sorted':
            chain.sort('reduced_chi')
            fmt='b.'
            ms=4
            alpha=0.4
            idx = np.random.randint(low=0, high=chain_size, size=1500)
            idx.sort()
            xmin = 0
            xmax = xmax * np.size(idx) / chain_size

        if fontsize is None:
            fontsize = plot.rcParams['font.size']

        fig = plot.figure(1, figsize=(16, 9))

        names = list(self.galaxy.names)
        names.append('reduced_chi')
        short_dict = self.galaxy.short_dict()

        plot.clf()  # clear current figure
        plot.subplots_adjust(wspace=0.32, hspace=0.32,
                             bottom=0.05, top=0.95, left=0.05, right=0.95)
        n = np.size(names)

        rows = 3
        cols = int(math.ceil((n-1) / (rows - 1.)))

        for i, par in enumerate(names):

            if i < n - 1:
                # Parameters
                ax=plot.subplot2grid((rows, cols), (int(math.floor(i / cols)), i % cols))
                if method == 'chi_sorted':
                    plot.plot(chain[par].data[idx], fmt, alpha=alpha, ms=ms)
                elif method == 'MAP':
                    idx_map = self.chain.idxsorted[0]
                    plot.plot(chain[par].data[idx], fmt, alpha=alpha, ms=ms, zorder=0)
                    plot.plot(idx_map, chain[par].data[idx_map], 'r+', alpha=alpha, ms=6, zorder=0)
                else:
                    plot.plot(chain[par].data[idx], fmt, alpha=alpha, ms=ms, zorder=0)
                plot.hlines(y=self.galaxy[i], xmin=xmin, xmax=xmax, color='r', label=r'$\hat P$', zorder=10)
                plot.hlines(y=self.galaxy[i] + self.galaxy.stdev[i], xmin=xmin, xmax=xmax, color='k',lw=2, label=r'$\sigma$', zorder=10)
                plot.hlines(y=self.galaxy[i] - self.galaxy.stdev[i], xmin=xmin, xmax=xmax, color='k',lw=2, zorder=10)
                if self.galaxy.lower is not None:
                    plot.hlines(y=self.galaxy.lower[i], xmin=xmin, xmax=xmax, color='k', linestyles='dotted',lw=2, zorder=10, label='%d ' % (self.percentile) + '% CI')
                if self.galaxy.upper is not None:
                    plot.hlines(y=self.galaxy.upper[i], xmin=xmin, xmax=xmax, color='k', linestyles='dotted',lw=2, zorder=10)

                #plot boundaries except for pa
                if 'pa' not in par:
                    try:
                        plot.axhline(self.min_boundaries[i],color='r',lw=1)
                        plot.axhline(self.max_boundaries[i],color='r',lw=1)
                    except:
                        self.logger.info("Boundaries not present, will not be shown")

                if i == n-2:
                    #plot.legend(loc=0, fontsize=13)
                    #plot.legend(loc=0, fontsize=13, bbox_to_anchor=(0.02, 0.3))
                    plot.legend(loc='lower center', fontsize=fontsize, bbox_to_anchor=(0.5, 0.0), ncol=3, fancybox=True, shadow=True)

                if (adapt_range == '5stdev') and (self.galaxy.stdev is not None):
                    plot.ylim(self.galaxy[i]-5.*self.galaxy.stdev[i], self.galaxy[i]+5.*self.galaxy.stdev[i])
                elif (adapt_range == '3stdev') and (self.galaxy.stdev is not None):
                    plot.ylim(self.galaxy[i]-3.*self.galaxy.stdev[i], self.galaxy[i]+3.*self.galaxy.stdev[i])
                elif (adapt_range =='boundaries') and (self.min_boundaries is not None and self.max_boundaries is not None):
                    plot.ylim(self.min_boundaries[i], self.max_boundaries[i])
                elif (adapt_range == 'minmax') or  (adapt_range is None):
                    plot.ylim(np.min(chain[par]), np.max(chain[par]) )

                title = r"%s" % (short_dict[par])
                title += "(%s)" % (self.galaxy.unit_dict()[par])
                plot.title(title, fontsize=fontsize)

            else:
                # Last row, reduced ki
                ax=plot.subplot2grid((rows, cols), (rows - 1, 0), colspan=cols)
                if (plot_likelihood):
                    ax.plot(np.exp(-chain['reduced_chi'] ))
                    ax.set_ylim([0,1])
                    ax.set_title(r'${\cal L}=\exp$[-$\chi^2$]')
                else:
                    ax.plot(np.log10(chain['reduced_chi'][idx] - np.min(chain['reduced_chi'])))
                    if method == 'MAP':
                        ax.axvline(idx_map,lw=1)
                    ax.set_title(r'$\log$ [$\chi^2 - \chi^2_{min}$]')

            if method is 'chi_sorted':
                ax.set_xticks([])
            else:
                ax.set_xticks(np.arange(2.) / 2 * np.size(idx))


        fig.subplots_adjust(wspace=0.3)

        if filename is None:
            plot.show()
        else:
            plot.savefig(filename)
            plot.close()

    def plot_geweke(self, filepath=None, fontsize=10, Nsigma=2, Nintervals=25, full_chain=False):
        """
        Plot the Geweke score for each parameter (from Geweke 1992: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.27.2952)
         and then either show it or save it to a file.

        See also https://pymc-devs.github.io/pymc/modelchecking.html

        filepath: string
            If specified, will write the plot to a file instead of showing it.
            The file will be created at the provided filepath, be it absolute or relative.
            The extension of the file must be either png or pdf.
        fontsize: int [None default]
            to change the fontsize for plot
            if None will use rcParams
        Nsigma: int [3 default]
            sigma range for convergence test
        Nintervals
            Number of intervals for geweke statistics
        full_chain: boolean
            True if score for full chain

        """
        if self.chain is None:
            raise RuntimeError(self.NO_CHAIN_ERROR)

        if filepath is not None:
            name, extension = os.path.splitext(filepath)
            supported_extensions = ['.png', '.pdf']
            if not extension in supported_extensions:
                raise ValueError("Extension '%s' is not supported, use %s.",
                                 extension, ', '.join(supported_extensions))
        chain = self.chain.copy()

        #plot geweke has no meaning with chi_sorted
        if self.method is not 'chi_sorted':
            if fontsize is None:
                fontsize = plot.rcParams['font.size']

            fig = plot.figure(2, figsize=(16, 9))

            names = chain.dtype.names
            short_dict = self.galaxy.short_dict()

            plot.clf()  # clear current figure
            plot.subplots_adjust(wspace=0.32, hspace=0.32,
                                 bottom=0.05, top=0.95, left=0.05, right=0.95)
            n = np.size(names)
            score = np.zeros( len(self.galaxy.names), dtype='<f8')

            rows = 3
            cols = int(math.ceil((n-1) / (rows - 1.)))

            for i, par in enumerate(self.galaxy.names):
                #if i<n-1:
                # Parameters
                plot.subplot2grid((rows, cols), (int(math.floor(i / cols)), i % cols))
                if i==0:
                    plot.ylabel(r'$\sigma$')

                if full_chain is False:
                    zscore = self._geweke_score(self.sub_chain[par], intervals=Nintervals)
                else:
                    zscore = self._geweke_score(self.chain[par], intervals=Nintervals)
                _x = zscore[:,0]
                _y = zscore[:,1]
                if full_chain is False:
                    plot.plot(_x, _y, color='k', label=r'Sub-chain')
                else:
                    plot.plot(_x, _y, color='k', label=r'Full-chain')

                plot.plot(_x[0], _y[0], 'ks',ms=4,label=r'  Initial at 100\%')
                plot.plot(_x[-1],_y[-1],'ko',ms=7,label=r'  Final at $>50$\%')

                #in red masked array
                _mask = np.ma.masked_inside(_y, -Nsigma, Nsigma)
                score[i] = _mask.mask.sum()/Nintervals #should be 1 if True
                if score[i]==1.0:
                    self.logger.info(r'Parameter {:s} has converged ? {:.2f}'.format(par, score[i]))
                else:
                    self.logger.warning(r'Parameter {:s} has not converged ? {:.2f}'.format(par, score[i]))

                plot.plot(_x,_mask, color='r')
                plot.plot(_x[-1],_mask[-1],'ro',ms=7)

                plot.ylim([-3.5,3.5])
                plot.axhline(-Nsigma,ls='-.',lw=2.5)
                plot.axhline(+Nsigma,ls='-.',lw=2.5, label=r'%s$\sigma$' % (Nsigma) )
                plot.axhline(-1,ls='-.',lw=1)
                plot.axhline(+1,ls='-.',lw=1,label=r'$1\sigma$')

                title = r"%s" % (short_dict[par])
                title += "(%s)" % (self.galaxy.unit_dict()[par])
                plot.title(title, fontsize=fontsize)
            #elif i==n-1:
            plot.xlabel('Start index')
            plot.legend(loc='lower center', fontsize=fontsize, bbox_to_anchor=(0.0, -0.8), ncol=2, fancybox=True, shadow=True)

            self.convergence=Table(score,names=self.galaxy.names)
            #fig.subplots_adjust(wspace=0.3)

            if filepath is None:
                plot.show()
            else:
                plot.savefig(filepath)
                plot.close()
        else:
            self.convergence = None
            self.logger.warning('Plot geweke not allowed')


    def plot_correlations(self):
        """
        old routine
        :return:
        """
        self.logger.warning('plot_deprecated() \n use plot_corner() instead (requires corner package)')
        return None

    def plot_corner(self, filepath=None, smooth=None, nsigma=4, fontsize=10):
        '''
        using corner package to plot chain
        filepath: string [default:None]
            filename for saving the plot
        smooth: [default: None]
            smooth option from corner
        nsigma: int [default:4]
            N-sigma (nsigma x stdev) to determine the ranges for each plot
            using the range option from corner

        '''

        if np.size(self.chain)>200:
            try:
                import corner
                corner_true = True
            except:
                corner_true = False
                self.logger.warning('plot_corner(): Need corner package for this')

            if corner_true:

                fig = plot.figure(3)
                plot.plot()
                fig.set_figwidth(10)
                fig.set_figheight(10)


                shorts_dict = self.galaxy.short_dict()
                shorts_dict.pop('x') #remove x
                shorts_dict.pop('y') #remove y
                shorts_dict.pop('z') #remove z
                params = shorts_dict.keys()

                show = list(params)
                s=show[0]
                ls=[shorts_dict[s]] # also

                #n sigma
                r = [(self.galaxy[s] - self.galaxy.stdev[s] * nsigma, \
                      self.galaxy[s] + self.galaxy.stdev[s] * nsigma)]
                best = list([self.galaxy[s]])
                for s in show[1:]:
                    r.append((self.galaxy[s] - self.galaxy.stdev[s] * nsigma, \
                      self.galaxy[s] + self.galaxy.stdev[s] * nsigma))
                    best.append(self.galaxy[s])
                    ls.append(shorts_dict[s])

                if fontsize is None:
                    fontsize = plot.rcParams['font.size']

                #@fixme how to make onto fig=plot.figure(3)
                corner.corner(self.sub_chain[show].as_array().tolist(),\
                              labels=ls, truths=best, range=r,  \
                              smooth=smooth, label_kwargs={'fontname':'sans-serif', 'fontsize': fontsize})

                if filepath is None:
                    plot.show()
                else:
                    plot.savefig(filepath)
                    plot.close()

            else:
                self.logger.warning('package corner not installed; plot will be skipped')

        else:
            corner_true = False
            self.logger.warning('plot_corner skipped, chain too small (<200)')

        return corner_true


    def plot_true_vfield(self, filepath=None, mask=None, contours=None,
                         fontsize=10, slitwidth=3):
        """
        plot the 2d maps and the 1d along the major axis

        mask: [optional] 2d nd-array
        mask for display purposes
            None: [default] default mask is flux>max(flux)/20.
            1: not apply any mask
            nd array: mask to be used

        contours: [optional] 2d nd-array
        external map to overlay

        fontsize: int
        to change the fontsize

        slitwidth: 3 [default] the slit width used to extract 1d profile

        """

        fmap = self.true_flux_map.data
        vmap = self.true_velocity_map.data
        smap = self.true_disp_map.data
        try:
            vmax = self.galaxy.maximum_velocity
        except:
            try:
                vmax = self.galaxy.virial_velocity
            except:
                try:
                    vmax = self.galaxy.halo_velocity
                except:
                    vmax = None
                    self.logger.warning("Galaxy has no Vmax Vvir halo_velocity")

        if mask is None:
            # default mask is flux>max(flux)/30.
            mask = (fmap > bn.nanmax(fmap) / 50.) * (fmap != 0)

        xc = self.galaxy.x
        yc = self.galaxy.y

        pixscale = self.instrument.xy_step

        ny, nx = np.shape(fmap)

        #matplotlib display tickmarks on half pixels
        x0 = pixscale * (-xc -0.5)
        x1 = pixscale * (nx - xc -0.5)
        y0 = pixscale * (-yc -0.5)
        y1 = pixscale * (ny - yc -0.5)
        extent = [x0, x1, y0, y1]

        if fontsize is None:
            fontsize = plot.rcParams['font.size']

        plot.figure(1,figsize=(16,9))
        plot.clf()

        plot.subplot(2, 3, 1)
        ax1=self._plot2dimage(fmap / mask,
                          vmin=0, vmax=np.nanmax(fmap),
                          xlabel=r'$\Delta \alpha$(")',
                          ylabel=r'$\Delta \delta$(")', interpolation='nearest',
                          extent=extent, contour=contours, title='True Flux map')

        plot.subplot(2, 3, 2)
        ax2=self._plot2dimage(vmap / mask,
                          vmin=np.nanmin(vmap), vmax=bn.nanmax(vmap),
                          xlabel=r'$\Delta \alpha$(")',
                          ylabel=r'$\Delta \delta$(")', interpolation='nearest',
                          extent=extent, contour=contours, title='True Vel. map')

        plot.subplot(2, 3, 3)
        s0 = bn.nanmin(smap)
        s1 = bn.nanmax(smap)*1.1
        ax3=self._plot2dimage(smap / mask, vmin=s0, vmax=s1,
                          xlabel=r'$\Delta \alpha$(")',
                          ylabel=r'$\Delta \delta$(")',
                          extent=extent, contour=contours,
                          interpolation='nearest', title='True Disp. map')

        xx, slice_f = self._slit(fmap, slitwidth, ax=ax1)
        good = (slice_f != 0)

        plot.subplot(2, 3, 4)
        if self.error_maps:
            fmap_err = self.true_flux_map_error.data
            ax4=self._plot2dimage(fmap/fmap_err/mask,
                              vmin=0, vmax=np.nanmax(fmap/fmap_err),
                              xlabel=r'$\Delta \alpha$(")',
                              ylabel=r'$\Delta \delta$(")',
                              extent=extent, contour=fmap,
                              interpolation='nearest', title='True Fmap SNR')
        else:
            plot.plot(pixscale * xx[good], np.log10(slice_f[good]), 'k-')
            plot.xlim([-3, 3])
            plot.ylim([np.min(np.log10(slice_f[good])), bn.nanmax(np.log10(1.3 * slice_f[good]))])
            plot.xlabel(r'$\delta x$')
            plot.ylabel(r'$\log$ I(r)')

        plot.subplot(2, 3, 5)
        xx, slice_v = self._slit(vmap, slitwidth, ax=ax2)

        if self.error_maps:
            vmap_err = self.true_velocity_map_error.data
            ax5=self._plot2dimage(abs(vmap/vmap_err)/mask,
                            vmin=0,
                            vmax=np.nanmax(abs(vmap/vmap_err)),
                              xlabel=r'$\Delta \alpha$(")',
                              extent=extent, contour=fmap,
                              interpolation='nearest', title='True Vmap SNR')
        else:
            plot.plot(pixscale * xx[good], slice_v[good], 'k-')
            plot.xlim([-3, 3])
            if vmax is not None:
                plot.ylim([-vmax, vmax])
                plot.axhline(vmax * np.sin(np.radians(self.galaxy.inclination)), color='k', ls='--')
                plot.axhline(-vmax * np.sin(np.radians(self.galaxy.inclination)), color='k', ls='--')
            plot.xlabel(r'$\delta x$')
            plot.ylabel(r'$V_{los}(x)$')

        plot.subplot(2, 3, 6)
        xx, slice_s = self._slit(smap, slitwidth, ax=ax3)

        if self.error_maps:
            smap_err = self.true_disp_map_error.data
            ax6=self._plot2dimage(smap / smap_err / mask,
                              vmin=0,
                              vmax=np.nanmax(smap / smap_err),
                              xlabel=r'$\Delta \alpha$(")',
                              extent=extent, contour=fmap,
                              interpolation='nearest', title='True Disp SNR')
        else:
            plot.plot(pixscale * xx[good], slice_s[good], 'k-')
            if 'velocity_dispersion' in self.galaxy.names:
                plot.axhline(self.galaxy.velocity_dispersion, ls='-.', label='Vturb')
            plot.xlim([-3, 3])
            plot.ylim([0, s1])
            plot.xlabel(r'$\delta x$')
            plot.legend()

        plot.tight_layout()

        if filepath is None:
            plot.show()
        else:
            plot.savefig(filepath)
            plot.close()

            rotation_curve = [pixscale * xx[good], xx[good]/self.galaxy.radius, slice_f[good], slice_v[good], slice_s[good]]
            rotation_name=re.sub('true_maps','true_Vrot',filepath[:-4])+'.dat'
            asciitable.write(rotation_curve, \
                             output=rotation_name,Writer=asciitable.FixedWidth, \
                             names=['dx_arcsec', 'rad_Re', 'flux_slit', 'v_kms', 'sig_kms'], overwrite=True)


    def plot_obs_vfield(self, filepath=None, mask=None, contours=None,
                         fontsize=10, slitwidth=3):
        """
        plot the observed 2d maps and the 1d along the major axis

        mask: [optional] 2d nd-array
        mask for display purposes
            None: [default] default mask is flux>max(flux)/20.
            1: not apply any mask
            nd array: mask to be used

        contours: [optional] 2d nd-array
        external map to overlay

        fontsize: int
        to change the fontsize

        """
        #Fmap, Vmap, Smap = self._make_moment_maps(self.convolved_cube, mask=True)
        Fmap = self.obs_flux_map
        Vmap = self.obs_velocity_map
        Smap = self.obs_disp_map
        fmap = Fmap.data
        vmap = Vmap.data
        smap = Smap.data

        try:
            vmax = self.galaxy.maximum_velocity
        except:
            try:
                vmax = self.galaxy.virial_velocity
            except:
                try:
                    vmax = self.galaxy.halo_velocity
                except:
                    vmax = None
                    self.logger.warning("Galaxy has no Vmax Vvir halo_velocity")

        if mask is None:
            # default mask is flux>max(flux)/30.
            mask = (fmap > bn.nanmax(fmap) / 50.) * (fmap != 0)

        xc = self.galaxy.x
        yc = self.galaxy.y

        pixscale = self.instrument.xy_step

        ## Matplotlib uses a grid with tickmarks on the middle of the pixels
        ## hence the -0.5
        ny, nx = np.shape(fmap)

        x0 = pixscale * (-xc -0.5)
        x1 = pixscale * (nx - xc -0.5)
        y0 = pixscale * (-yc -0.5)
        y1 = pixscale * (ny - yc -0.5)
        extent = [x0, x1, y0, y1]

        if fontsize is None:
            fontsize = plot.rcParams['font.size']

        plot.figure(1, figsize=(16,9))
        plot.clf()
        plot.title("EXPERIMENTAL products; not used by 3DMODEL ", color='red', fontsize=fontsize)

        plot.subplot(2, 3, 1)
        ax1=self._plot2dimage(fmap / mask,
                          vmin=0, vmax=np.nanmax(fmap),
                          xlabel=r'$\Delta \alpha$(")',
                          ylabel=r'$\Delta \delta$(")', interpolation='nearest',
                          extent=extent, contour=contours, title='Obs. Flux map')

        plot.subplot(2, 3, 2)
        ax2=self._plot2dimage(vmap / mask,
                          vmin=np.nanmin(vmap), vmax=bn.nanmax(vmap),
                          xlabel=r'$\Delta \alpha$(")',
                          ylabel=r'$\Delta \delta$(")', interpolation='nearest',
                          extent=extent, contour=contours, title='Obs. Vel. map')

        plot.subplot(2, 3, 3)
        s1 = bn.nanmax(smap)*1.1
        try:
            s0 = bn.nanmin(smap)  #- 2 * bn.nanstd(smap)
        except:
            s0 = np.nanmin(smap)  #- 2 * np.nanstd(smap)
        ax3=self._plot2dimage(smap / mask, vmin=s0, vmax=s1,
                          xlabel=r'$\Delta \alpha$(")',
                          ylabel=r'$\Delta \delta$(")',
                          extent=extent, contour=contours,
                          interpolation='nearest', title='Obs. Disp. map')

        plot.subplot(2, 3, 4)
        xx, slice_v = self._slit(fmap, slitwidth, ax=ax1)
        good = (slice_v != 0)
        plot.plot(pixscale * xx[good], np.log10(slice_v[good]), 'k-')
        plot.xlim([-3, 3])
        plot.ylim([np.min(np.log10(slice_v[good])), bn.nanmax(np.log10(1.3 * slice_v[good]))])
        plot.xlabel(r'$\delta x$')
        plot.ylabel(r'$\log$ I(r)')

        plot.subplot(2, 3, 5)
        xx, slice_v = self._slit(vmap, slitwidth, ax=ax2)
        plot.plot(pixscale * xx[good], slice_v[good], 'k-')
        plot.xlim([-3, 3])
        if vmax is not None:
            plot.ylim([-vmax, vmax])
            plot.axhline(vmax * np.sin(np.radians(self.galaxy.inclination)), color='k', ls='--')
            plot.axhline(-vmax * np.sin(np.radians(self.galaxy.inclination)), color='k', ls='--')
        plot.xlabel(r'$\delta x$')
        #p.ylabel(r'$V_{los}(x)$')

        plot.subplot(2, 3, 6)
        xx, slice_v = self._slit(smap, slitwidth, ax=ax3)
        plot.plot(pixscale * xx[good], slice_v[good], 'k-')
        if 'velocity_dispersion' in self.galaxy.names:
            plot.axhline(self.galaxy.velocity_dispersion, ls='-.', label='Vturb')
        plot.xlim([-3, 3])
        plot.ylim([0, s1])
        plot.xlabel(r'$\delta x$')
        plot.legend()

        plot.tight_layout()

        if filepath is None:
            plot.show()
        else:
            plot.savefig(filepath)
            plot.close()

    def plot_images(self, filepath=None, z_crop=None):
        """
        Plot a mosaic of images of the cropped (along z) cubes,
        and then either show it or save it to a file.

        filepath: string
            If specified, will write the plot to a file instead of showing it.
            The file will be created at the provided absolute or relative filepath.
            The extension of the file must be either png or pdf.
        z_crop: None|int
            The maximum and total length of the crop (in pixels) along z,
            centered on the galaxy's z position.
            If you provide zero or an even value (2n),
            the closest bigger odd value will be used (2n+1).
            By default, will not crop.
        """

        if self.chain is None:
            raise RuntimeError(self.NO_CHAIN_ERROR)

        if filepath is not None:
            name, extension = os.path.splitext(filepath)
            supported_extensions = ['.png', '.pdf']
            if not extension in supported_extensions:
                raise ValueError("Extension '%s' is not supported, "
                                 "you may use one of %s",
                                 extension, ', '.join(supported_extensions))

        self._plot_images(self.cube, self.galaxy, self.convolved_cube,
                          self.deconvolved_cube, self.residuals_cube,
                          z_crop=z_crop)

        if filepath is None:
            plot.show()
        else:
            plot.savefig(filepath)
            plot.close()

    def _plot_images(self, cube, galaxy, convolved_cube, deconvolved_cube,
                     residuals_cube, z_crop=None):
        """
        Plot a mosaic of images of the cropped (along z) cubes.

        z_crop: None|int
            The maximum and total length of the crop (in pixels) along z,
            centered on the galaxy's z position.
            If you provide zero or an even value (2n),
            the closest bigger odd value will be used (2n+1).
            By default, will not crop.
        """
        if z_crop is None:
            zmin = 0
            zmax = cube.shape[0] - 1
        else:
            if not (z_crop & 1):
                z_crop += 1
            z0 = galaxy.z
            zd = (z_crop - 1) / 2
            zmin = max(0, z0 - zd)
            zmax = z0 + zd + 1

        fig = plot.figure(1, figsize=(16, 9))
        plot.clf()
        plot.subplots_adjust(wspace=0.25, hspace=0.25, bottom=0.05, top=0.95, left=0.05, right=0.95)

        # MEASURE
        sub = fig.add_subplot(2, 2, 1)
        sub.set_title('Measured')
        measured_cube_cropped = cube.data[zmin:zmax, :, :]
        image_measure = (measured_cube_cropped.sum(0) / measured_cube_cropped.shape[0])
        plot.imshow(image_measure, interpolation='nearest', origin='lower')
        plot.xticks(fontsize=8)
        plot.yticks(fontsize=8)
        colorbar = plot.colorbar()
        colorbar.ax.tick_params(labelsize=8)

        # CONVOLVED
        sub = fig.add_subplot(2, 2, 2)
        sub.set_title('Convolved')
        convolved_cube_cropped = convolved_cube.data[zmin:zmax, :, :]
        image_convolved = (convolved_cube_cropped.sum(0) / convolved_cube_cropped.shape[0])
        plot.imshow(image_convolved, interpolation='nearest', origin='lower')
        plot.xticks(fontsize=8)
        plot.yticks(fontsize=8)
        colorbar = plot.colorbar()
        colorbar.ax.tick_params(labelsize=8)

        # DECONVOLVED
        sub = fig.add_subplot(2, 2, 3)
        sub.set_title('Deconvolved')
        deconvolved_cube_cropped = deconvolved_cube.data[zmin:zmax, :, :]
        image_deconvolved = (deconvolved_cube_cropped.sum(0) / deconvolved_cube_cropped.shape[0])
        plot.imshow(image_deconvolved, interpolation='nearest', origin='lower')
        plot.xticks(fontsize=8)
        plot.yticks(fontsize=8)
        colorbar = plot.colorbar()
        colorbar.ax.tick_params(labelsize=8)

        # ERROR
        sub = fig.add_subplot(2, 2, 4)
        sub.set_title('Error')
        square_error_cube_cropped = residuals_cube.data[zmin:zmax, :, :]
        nz = square_error_cube_cropped.shape[0]
        #normalized error image in sigmas:
        image_error = (square_error_cube_cropped.sum(0) / nz) * np.sqrt(nz)
        #vmin = np.amin(image_measure)
        #vmax = np.amax(image_measure)
        #plot.imshow(image_error, interpolation='nearest', origin='lower', vmin=vmin, vmax=vmax)
        plot.imshow(image_error, vmin=-2.5, vmax=2.5, interpolation='nearest', origin='lower')
        plot.xticks(fontsize=8)
        plot.yticks(fontsize=8)
        colorbar = plot.colorbar()
        colorbar.ax.tick_params(labelsize=8)

        return fig

    def _plot2dimage(self, image, vmin=-10, vmax=10, pos=None,
                    xlabel=None, ylabel=None, contour=None,
                    extent=None, title=None, interpolation=None, **kwargs):
        """
          Plot a 2D image with colorbars.
        """

        # Matplotlib's default origin is not ours, we need to use 'lower'
        origin = 'lower'

        if extent is not None:
            plot.imshow(image, aspect='equal', vmin=vmin, vmax=vmax, cmap=plot.cm.jet,
                        extent=extent, origin=origin,
                        interpolation=interpolation)
            plot.axhline(0,color='k',lw=1,alpha=0.5)
            plot.axvline(0,color='k',lw=1,alpha=0.5)
            if contour is not None:
                cmax = bn.nanmax(contour)
                plot.contour(contour, extent=extent, color='k',
                             levels=[cmax / 10., cmax / 5., cmax / 2.],
                             origin=origin)
        else:
            plot.imshow(image, aspect='equal', vmin=vmin, vmax=vmax, cmap=plot.cm.jet,
                        origin=origin)
            plot.axhline(0,color='k',lw=1,alpha=0.5)
            plot.axvline(0,color='k',lw=1,alpha=0.5)
            if contour is not None:
                cmax = bn.nanmax(contour)
                plot.contour(contour, levels=[cmax / 10., cmax / 5., cmax / 2.],
                             color='k', origin=origin)
        if title is not None:
            plot.title(title)
        ax = plot.gca()
        v = ax.axis()
        if pos is not None:
            plot.plot(pos[0], pos[1], 'k+', ms=25, mew=3)
        plot.axis(v)

        if xlabel is not None:
            plot.xlabel(xlabel)
        if ylabel is not None:
            plot.ylabel(ylabel)
            #ax=p.gca()

        # Add colorbar
        cax = inl.inset_axes(
            ax,
            width="80%",  # width = 10% of parent_bbox width
            height="10%",  # height : 50%
            #borderpad=1,
            #    bbox_to_anchor=(1,0,1,2),
            # bbox_transform=ax.transAxes,
            loc=1)
        norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
        if vmax > 1:
            tick_range = np.rint(np.r_[vmin:vmax:5j])
        else:
            tick_range = (np.r_[vmin:vmax:5j])

        # matplotlib will crash and burn if ticks are not unique
        tick_range = np.unique(tick_range)

        cb = mpl.colorbar.ColorbarBase(cax, cmap=plot.cm.jet,
                                       norm=norm, orientation='horizontal',
                                       ticks=tick_range[1:-1])

        #cax.xaxis.set_major_locator( MaxNLocator(nbins = 6) )
        return ax

    def _slit(self, mapdata, slit_width, reshape=False, ax=None):
        """
        Create 1d profile along the major axis.
        Note that PA = 0 is vertical, anti-clockwise from y-axis.
        """

        #orig code
        #ang=np.radians(PA)
        #prof=np.where(s<=(slit_width/2.0+0.5),data,0.)
        #profile=ndimage.rotate(prof,PA,mode='constant',order=1).sum(1)
        #profile=profile/np.max(profile)

        y, x = np.indices(mapdata.shape)
        ang = -np.radians(self.galaxy.pa - 90)
        if (mapdata.shape[0] % 2) == 0:  #even
            dx = x - self.galaxy.x - 0.5  #half pixel shift
        else:
            dx = x - self.galaxy.x
        if (mapdata.shape[0] % 2) == 0: #even
            dy = y - self.galaxy.y - 0.5
        else:
            dy = y - self.galaxy.y

        dx_p = dx * np.cos(ang) - dy * np.sin(ang)
        dy_p = dx * np.sin(ang) + dy * np.cos(ang)

        if (ax!=None):
            #plot slit
            #axis labels in arcsec
            xlim=ax.get_xlim()
            ylim=ax.get_ylim()
            pixscale = self.instrument.xy_step
            xar= (x[0] - self.galaxy.x) * pixscale
            ang = np.radians(self.galaxy.pa + 90.)
            xx= xar * np.cos(ang) - (slit_width/2.) * pixscale * np.sin(ang)
            yy= xar * np.sin(ang) + (slit_width/2.) * pixscale * np.cos(ang)
            ax.plot(xx,yy,'-',lw=2,c='grey',alpha=0.6)
            xx= xar * np.cos(ang) + (slit_width/2.) * pixscale * np.sin(ang)
            yy= xar * np.sin(ang) - (slit_width/2.) * pixscale * np.cos(ang)
            ax.plot(xx,yy,'-',lw=2,c='grey',alpha=0.6)
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)

        slit_vert = np.abs(dy_p)  # used for PA=0
        slit_horiz = dx_p  # distance along the slit

        slit_data     =  np.where(slit_vert <= (slit_width / 2.0 ), mapdata, 0.)
        slit_distance =  np.where(slit_vert <= (slit_width / 2.0 ), slit_horiz,0.)
        # PA is anti-clockwise, rotate is clockwise
        rot_ang = self.galaxy.pa + 90  # to have horizontal slit image
        slit_rot = ndimage.rotate(slit_data, rot_ang, mode='constant', order=0,reshape=reshape)  # 0 because spline introduces errors!
        dist_rot = ndimage.rotate(slit_distance, rot_ang, mode='constant', order=0,reshape=reshape)


        a =  np.sum(slit_rot != 0,axis=(0)) #nansum returns a bool with bottelneck; not with numpy!!
        profile = np.where(a!=0, bn.nansum(slit_rot, axis=(0)) / a, 0.)  #mean of the slit

        b =  np.sum(dist_rot != 0,axis=(0))  # pixels not zero and not nan
        xaxis =  np.where(b!=0, bn.nansum(dist_rot, axis=(0)) / b, 0.)

        return xaxis, profile

    def _make_maps_Epinat(self, cube=None, mask=False, cut_level=50, use_conv='other'):
        """
        make observed maps from true maps using formulas in Epinat 2010

        :param cube: input cube for computing masking
        :param mask: boolean [default: None] to apply masking
        :param use_conv: astropy [default] | scipy
        :param cut_level: 50 [default] cut used if mask=True
        :return:
        """

        if (cube is None):
                cube = self.convolved_cube

        if mask is True:
            # default mask is flux>max(flux)/30.
            mask = (bn.nansum(cube.data,0) > bn.nanmax(cube.data.sum(0)) / cut_level )
        else:
            mask = np.ones_like(cube.data[1,:,:])

        #Eq A15 Epinat
        psf2d = self.instrument.psf3d.sum(axis=0)
        if use_conv is 'scipy' :
            logger.debug("Using scipy %s for convolution" % (scipy.__version__))
            Fmap = conv2d_scipy(self.true_flux_map.data, psf2d, mode='same')
        elif use_conv is 'astropy':
            logger.debug("Using astropy %s for convolution" % (astropy.__version__))
            Fmap = conv2d_astro(self.true_flux_map.data, psf2d)
        else:
            Fmap, psf2d_fft = conv2d_intern(self.true_flux_map.data, psf2d, compute_fourier=True)

        #Eq A16 Epinat
        V1 = self.true_velocity_map.data * self.true_flux_map.data          # V.M
        if use_conv is 'scipy':
            Vtemp = conv2d_scipy(V1, psf2d, mode='same')
        elif use_conv is 'astropy':
            Vtemp = conv2d_astro(V1, psf2d)
        else:
            Vtemp, psf2d_fft = conv2d_intern(V1, psf2d, compute_fourier=True)
        Vmap = Vtemp / Fmap

        #Eq A17 Epinat
        S1 = self.true_disp_map.data**2 * self.true_flux_map.data
        if use_conv is 'scipy':
            Stemp = conv2d_scipy(S1, psf2d, mode='same')
        elif use_conv is 'astropy':
            Stemp = conv2d_astro(S1, psf2d)
        else:
            Stemp, psf2d_fft = conv2d_intern(S1, psf2d, compute_fourier=True)

        V2 = self.true_velocity_map.data**2 * self.true_flux_map.data
        if use_conv is 'scipy':
            Vtemp = conv2d_scipy(V2, psf2d, mode='same')
        elif use_conv is 'astropy':
            Vtemp = conv2d_astro(V2, psf2d)
        else:
            Vtemp, psf2d_fft = conv2d_intern(V2, psf2d, compute_fourier=True)

        Smap_sq = Stemp / Fmap + Vtemp / Fmap - Vmap**2
        Smap = np.sqrt(Smap_sq)

        self.obs_flux_map = HyperCube(Fmap * mask)
        self.obs_velocity_map = HyperCube(Vmap * mask)
        self.obs_disp_map = HyperCube(Smap * mask)

        return self.obs_flux_map, self.obs_velocity_map, self.obs_disp_map

    def _make_moment_maps(self, cube=None, mask=False, cut_level=50, parameters=None, instrument=None, remove_LSF_from_disp=False):
        """
        make moment maps from a noiseless cube
        assumes no continuum to be removed
        :param mask: boolean [default: None] to apply masking
        :param cube: HyperspectralCube
        :return:
        """

        if (cube is None):
                cube = self.convolved_cube

        if (instrument is None):
            vstep = self.instrument.z_step_kms
            lsf_vector = self.instrument.lsf.as_vector(cube)
            if remove_LSF_from_disp:
                lsf_fwhm = self.instrument.lsf.fwhm / self.instrument.z_step #in pixel  !
        else:
            vstep = instrument.z_step_kms
            lsf_vector = instrument.lsf.as_vector(cube)
            if remove_LSF_from_disp:
                x=np.arange(np.size(lsf_vector))
                sigma = np.sqrt(np.sum(x**2*lsf_vector)-np.sum(x*lsf_vector)**2) #in pixel !
                lsf_fwhm = sigma * 2.35

        zgrid, _, _ = np.indices(cube.shape)

        if parameters is None:
                zo = self.galaxy.z
        else:
                zo = parameters.z

        if mask is True:
            # default mask is flux>max(flux)/30.
            mask = (cube.data > bn.nanmax(cube.data) / cut_level )
        else:
            mask = np.ones_like(cube.data)

        #if the line is a doublet use a weighted average
        if self.model.line is not None:
                line = self.model.line
                delta = 3e5 * (line['wave'][1]-line['wave'][0])/(line['wave'][0]+line['wave'][1])*2
                r1 = line['ratio'][0]
                r2 = line['ratio'][1]
                p = r1 / (r1+r2) #weight of first/blue line
                # weighted averaged zo
                #zo_avg =  ((zo-delta/vstep) * r1 + zo * r2) / (r1 + r2)
                #print zo,zo-delta/vstep,zo_avg
                #zo = zo_avg

                #in km/s
                # M1 = p * mu1 + (1-p) * mu2 ; m1 = mu2-Delta
                # mu2 = (M1 - p mu1 ) / (1-p)
                # mu2 = M1 + p delta
                Fmap = bn.nansum(cube.data * mask,axis=0)
                cube_norm = np.where(np.isfinite(cube.data / Fmap), cube.data / Fmap, 0)
                M1map = bn.nansum(cube_norm * mask * (zgrid - zo), axis=0)   * vstep
                Vmap = (M1map + p * delta) # Vmap

                # M2 = p * (mu1^2+sig^2) + (1-p) * (mu2^2+sig^2); m1 = mu2-Delta
                # M2 = sig^2 + (p mu1^2 + (1-p) mu2^2)
                # M2 - p (mu2-delta)**2 - (1-p) mu2^2) = sig^2
                M2map = bn.nansum(cube.data / Fmap * mask * (zgrid -zo)**2, axis=0)  * vstep**2
                S2map = M2map - (Vmap-delta)**2 * p - (Vmap)**2 * (1-p)
                Smap = np.sqrt(S2map)

        else:
                Fmap = bn.nansum(cube.data * mask,axis=0)
                cube_norm = np.where(np.isfinite(cube.data / Fmap), cube.data / Fmap, 0)
                Vmap = bn.nansum(cube_norm * mask * (zgrid-zo), axis=0)  * vstep     # mu
                S2map = bn.nansum(cube_norm * mask *(zgrid-zo)**2, axis=0)  * vstep**2 # mu^2 + sigma^2
                Smap = np.sqrt(S2map-Vmap**2)

        #Remove instrument LSF
        if (remove_LSF_from_disp):
            self.logger.info('removing LSF from dispersion map in quadrature; with FWHM %.5f pix' % (lsf_fwhm) )
            Smap=np.sqrt(Smap**2 - (lsf_fwhm/2.35 * vstep)**2)


        self.obs_flux_map = HyperCube(Fmap)
        self.obs_velocity_map = HyperCube(Vmap)
        self.obs_disp_map = HyperCube(Smap)

        return self.obs_flux_map, self.obs_velocity_map, self.obs_disp_map

    def _geweke_score(self, x, first=.1, last=.5, intervals=20):
        """
        Return z-scores for convergence diagnostics.
        Compare the mean of the first % of series with the mean of the last % of
        series. x is divided into a number of segments for which this difference is
        computed. If the series is converged, this score should oscillate between
        -1 and 1.
        Parameters
        ----------
        x : array-like
          The trace of some stochastic parameter.
        first : float
          The fraction of series at the beginning of the trace.
        last : float
          The fraction of series at the end to be compared with the section
          at the beginning.
        intervals : int
          The number of segments.
        maxlag : int
          Maximum autocorrelation lag for estimation of spectral variance
        Returns
        -------
        scores : list [[]]
          Return a list of [i, score], where i is the starting index for each
          interval and score the Geweke score on the interval.
        Notes
        -----
        The Geweke score on some series x is computed by:
          .. math:: \frac{E[x_s] - E[x_e]}{\sqrt{V[x_s] + V[x_e]}}
        where :math:`E` stands for the mean, :math:`V` the variance,
        :math:`x_s` a section at the start of the series and
        :math:`x_e` a section at the end of the series.
        References
        ----------
        Geweke (1992)
        """
        if np.ndim(x) > 1:
            return [self._geweke_score(y, first, last, intervals) for y in np.transpose(x)]

        # Filter out invalid intervals
        if first + last >= 1:
            raise ValueError(
                "Invalid intervals for Geweke convergence analysis",
                (first, last))

        # Initialize list of z-scores
        zscores = [None] * intervals

        # Starting points for calculations
        starts = np.linspace(0, int(len(x)*(1.-last)), intervals).astype(int)

        # Loop over start indices
        for i,s in enumerate(starts):

            # Size of remaining array
            x_trunc = x[s:]
            n = len(x_trunc)

            # Calculate slices
            first_slice = x_trunc[:int(first * n)]
            last_slice = x_trunc[int(last * n):]

            z = (first_slice.mean() - last_slice.mean())
            #to avoid numerical errors
            if np.var(last_slice)>1e-6*last_slice.mean()**2:
                z /= np.sqrt(np.var(first_slice) +
                         np.var(last_slice))
            else:
                z = 0
            zscores[i] = len(x) - n, z

        return np.array(zscores)

        #@fixme: unsupported
        #def film_images(self, name, frames_skipped=0, fps=25):
        #    #"""
        #This is still a WiP.

        #TODO:
        #    - print => logging
        #    - heavily document how to solve ffmpeg issue (even if it's not our job)

        #Generates an video of the evolution of plot_images() through the chain,
        #skipping [frames_skipped] between each draw, at [fps] frames per second.

        #.. warning::
        #    The generated file may take up a lot of disk space.

        #Known issue with ffmpeg :
        #https://stackoverflow.com/questions/17887117/python-matplotlib-basemap-animation-with-ffmpegwriter-stops-after-820-frames
        #Fix :
        #sudo apt-add-repository ppa:jon-severinsson/ffmpeg
        #sudo apt-get update
        #sudo apt-get install ffmpeg
        #"""
        #import matplotlib.animation as animation

        # Initial plot
        #fig = self._plot_images(self.cube, self.galaxy, self.convolved_cube,
        #                        self.deconvolved_cube, self.residuals_cube)

        ## Convert the chain to a list of parameters
        #chain_list = np.array(self.chain.tolist())
        #params = chain_list[:, :-1]  # remove the reduced chi (last element)

        ## Sanity check (otherwise, divisions by 0 will happen)
        #if len(params) < 2:
        #    raise RuntimeError("Chain is not long enough for video.")

        #self.logger.info("Encoding video...")

        #def animate(i, skipped, count, me, chain):
        #    """
        #    animation.FuncAnimation requires a function to generate the figure
        #    on each frame. This is the bottleneck of our film generation.

        #    i: int
        #        0 0 1 2 3 ... up to [count]
        #    skipped: int
        #        Between each frame, skip [skipped] parameters in the chain
        #    count: int
        #        The total [count] of frames to show.
        #    me: GalPaK3D
        #        Our local self.
        #    chain: ndarray
        #        The list of parameters, as long as the MCMC chain.
        #    """
        #    # Get the parameters from the chain
        #    index = int(math.floor(i / (1 + skipped)))
        #    galaxy = ModelParameters.from_ndarray(chain[index])
        #    # Print the progression in %
        #    sys.stdout.write("\r%d: %2.2f%%" % (i, 100. * i / (count - 1)))
        #    sys.stdout.flush()
        #    # Compute the cubes
        #    deconvolved_cube = me.create_clean_cube(galaxy, me.cube.shape)
        #    convolved_cube = me.instrument.convolve(deconvolved_cube.copy())
        #    residuals_cube = (me.cube - convolved_cube) / me.error_cube
        #    # Plot and return the plot
        #    # (this is the expensive step, and it can be optimized further)
        #    return me._plot_images(me.cube, galaxy, convolved_cube,
        #                          deconvolved_cube, residuals_cube)

        #if frames_skipped < 0:
        #    frames_skipped *= -1
        #frames_count = int(math.floor(len(params) / (1. + frames_skipped)))
        #ani = animation.FuncAnimation(fig, animate, frames_count,
        #                              fargs=(int(frames_skipped), frames_count,
        #                                     self, params),
        #                              repeat=False)

        ## Still unsure if that metadata is really written in the file
        #metadata = {
        #    'title': 'GalPaK\'s cubes timelapse',
        #    'author': 'galpak',
        #}
        #writer = animation.FFMpegWriter(fps=fps)
        #ani.save(name + '_images.avi', writer=writer, metadata=metadata)
