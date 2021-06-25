# -*- coding: utf-8 -*-

import numpy as np, time
from .galpak3d import GalPaK3D
from .model_sersic3d import ModelSersic as DefaultModel

# LOGGING CONFIGURATION
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('GalPaK API')

def run(cube,
        variance=None,
        seeing=None, line=None, instrument=None,
        verbose=True,
        model=None,
        crval3=None, crpix3=None, cunit3=None, cdelt3=None, ctype3=None, cunit1=None,
        force_header_update=False,
        max_iterations=15000,
        method_chain='last',
        last_chain_fraction=60,
        percentile=95,
        mcmc_method='galpak',
        chi_stat = 'gaussian',
        min_boundaries=None,
        max_boundaries=None,
        known_parameters=None,
        initial_parameters=None,
        min_acceptance_rate=5.0,
        random_scale=None, **kwargs):
    """
    Creates a GalPaK3D instance and runs it on provided cube.
    Refer to documentations of GalPaK3D and GalPaK3D.run_mcmc().

    model: Model Class
        default: DefaultModel

    Use like this: ::

        import galpak
        g = galpak.run(cube='my.fits', instrument=myinstrument, model=mymodel)

        print g.galaxy
        g.save('my_run')
        # etc.
    """
    g = GalPaK3D(cube, variance=variance,
               instrument=instrument,  seeing=seeing,
               crval3=crval3, crpix3=crpix3, cunit3=cunit3, cdelt3=cdelt3, ctype3=ctype3, cunit1=cunit1,
               force_header_update=force_header_update)
    #default model
    if model is None:
        model = DefaultModel(line=line)
    g.run_mcmc(verbose=verbose,
               model=model,
               method_chain=method_chain,
               last_chain_fraction=last_chain_fraction,
               percentile=percentile,
               chi_stat=chi_stat,
               mcmc_method=mcmc_method,
               min_boundaries=min_boundaries,
               max_boundaries=max_boundaries,
               known_parameters=known_parameters,
               initial_parameters=initial_parameters,
               min_acceptance_rate=min_acceptance_rate,
               random_scale=random_scale,
               max_iterations=max_iterations, **kwargs)

    return g

def autorun(cube,
        variance=None,
        instrument=None,
        verbose=True,
        seeing=None,
        model=None,
        crval3=None, crpix3=None, cunit3=None, cdelt3=None, ctype3=None, cunit1=None,
        force_header_update=False,
        max_iterations=5000,
        method_chain='last',
        last_chain_fraction=60,
        percentile=95,
        chi_stat = 'gaussian',
        mcmc_method='galpak',
        min_boundaries=None,
        max_boundaries=None,
        known_parameters=None,
        initial_parameters=None,
        random_scale=1,
        MaxIter=25,
        target_acceptance = 40,
        target_tolerance = 5, **kwargs):
    """
    Creates a GalPaK3D instance and runs it on provided cube.
    Refer to documentations of GalPaK3D and GalPaK3D.run_mcmc().

    model: Model Class
        default: ModelSersic

    MaxIter: int
        default: 25
        maximum number of iterations for searching rscale
    target_acceptance : float
        default: 40
        target acceptance rate

    Use like this: ::

        import galpak
        g = galpak.autorun(cube='my.fits', instrument=myinstrument, model=mymodel)

        print g.galaxy
        g.save('my_run')
        # etc.
    """
    g = GalPaK3D(cube, variance=variance,
                instrument=instrument, seeing=seeing,
                quiet=True,
                crval3=crval3, crpix3=crpix3, cunit3=cunit3, cdelt3=cdelt3, ctype3=ctype3, cunit1=cunit1,
                force_header_update=force_header_update)
    #default model
    if model is None:
        model = DefaultModel()

    #first quick run
    logger.info("First quick run")
    g.run_mcmc(verbose=None,
               model=model,
               method_chain=method_chain,
               mcmc_method='galpak',
               last_chain_fraction=last_chain_fraction,
               percentile=percentile,
               chi_stat=chi_stat,
               min_boundaries=min_boundaries,
               max_boundaries=max_boundaries,
               known_parameters=known_parameters,
               initial_parameters=initial_parameters,
               random_scale=random_scale,
               max_iterations=250)
    #iterate to calibrate random_scale
    logger.info("Initial Acceptance %.2f" % (g.acceptance_rate))

    if g.acceptance_rate>80:
        g.random_scale = 15

    i=0
    f=1
    new_rscale=1.0
    if isinstance(g.random_scale,np.ndarray):
        raise NotImplementedError("Random Scale must be float for autorun")

    while (i<5) or ((np.abs(g.acceptance_rate-target_acceptance)>target_tolerance) and (i<MaxIter)):

        new_rscale= g.random_scale+f*np.log10(g.acceptance_rate/target_acceptance)

        if i>10 and new_rscale>1:
            f=2 #adapt faster
        if new_rscale<0:
            f=0.25
            new_rscale = g.random_scale + f * np.log10(g.acceptance_rate / target_acceptance)
        #if new_rscale<0.5:
        #    f / 2
        if new_rscale>15:
            f=5

        #@fixme check if random_scale becomes <0
        if new_rscale<0:
            new_rscale=0.5 #minimum
            i = MaxIter
        g.run_mcmc(verbose=None,
               model=model,
               method_chain=method_chain,
               mcmc_method='galpak',
               last_chain_fraction=last_chain_fraction,
               percentile=percentile,
               chi_stat=chi_stat,
               min_boundaries=min_boundaries,
               max_boundaries=max_boundaries,
               known_parameters=known_parameters,
               initial_parameters=g.galaxy,
               random_scale=new_rscale,
               max_iterations=150);
        logger.info("%d Rscale %.2f Acceptance %.2f%% Target: %d%%" \
                             % (i,g.random_scale, g.acceptance_rate, target_acceptance))
        logger.info(" Parameters : " + g.galaxy.short_info())
        i+=1
    #save rscale
    tuned_rscale = g.random_scale
    logger.info("Using best Rscale %.2f" % (tuned_rscale))    #reusing g.galaxy
    time.sleep(5)#wait 5sec
    #then run everything
    if i<MaxIter:
        g.run_mcmc(verbose=verbose,
               model=model,
               method_chain=method_chain,
               mcmc_method=mcmc_method,
               last_chain_fraction=last_chain_fraction,
               percentile=percentile,
               chi_stat=chi_stat,
               min_boundaries=min_boundaries,
               max_boundaries=max_boundaries,
               known_parameters=known_parameters,
               initial_parameters=g.galaxy,
               random_scale=tuned_rscale,
               max_iterations=max_iterations, **kwargs)
        logger.info(" Parameters : " + g.galaxy.short_info())
        return g
    else:
        logger.error("AutoRandomScale Failed")

        return None
