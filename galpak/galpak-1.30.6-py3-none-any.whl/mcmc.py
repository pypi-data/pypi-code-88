# coding=utf-8

from __future__ import division

import numpy as np, sys
from astropy.table import Table

from .galaxy_parameters import  GalaxyParameters
from .hyperspectral_cube import HyperspectralCube as HyperCube
from .math_utils import merge_where_nan, median_clip, safe_exp

class MCMC:
    """
        An extension of the galpak class with the galpak MH algorithm (myMCMC class)
        and method used for emcee and external algorithm

        the following methods are for external samplers such as emcee:
            - lnprob: returned by __call__ / the full log-probability function: Ln = Priors x L(p)
            - loglike: the log L(p)
            - logpriors: the log priors with  uniform priors.
        the following methods are for multinest:
            - pyloglike: the log L(p)
            - pycube: transforms unit cube to uniform priors.
        the following methods are for dynesty:
            - loglike: the log L(p)
            - ptforms: transforms unit cube to uniform priors.
        the following methods are for the internal galpak MH algorithm
            - myMCMC

    """
    CHISTAT_VALID = ['gaussian', 'Mighell', 'Cstat', 'Neyman', 'Pearson']

    SAMPLING_VALID = ['Cauchy', 'Normal', 'AdaptiveCauchy',\
                      'DE', 'Snooker', 'walkers', 'walkersCauchy']

    MCMC_VALID = ['galpak', 'emcee_MH', 'emcee_walkers', 'dynesty', 'multinest']

    def __call__(self, x):
        """
            call for instance ()
        used for emcee
        """
        return self.lnprob(x)

    #For EMCEE
    def lnprob(self, params):
        """
            the full log-probability function: Ln = Priors x L(p)
        """

        #convert ndarray to Parameter class {for emcee}
        if not isinstance(params, GalaxyParameters):
            if isinstance(params, np.ndarray):
                params = self.model.Parameters().from_ndarray(params)
            else:
                self.logger.error("Param is not ModelParameter nor a ndarray")

        lp = self.logpriors(params)
        if not np.isfinite(lp):
            return -np.inf
        return lp+self.loglike(params)

    def loglike(self, params):
        """
            The log-likelihood function.
            log L ~ log Pi_i [1/Vi^0.5 exp(-0.5 (xi-m)^/Vi]
            log L ~ -0.5 * sum_i Vi - 0.5 sum_i (xi-m)^2/Vi
        """
        #return -0.5*self.compute_chi(params)
        #adding a constant
        return -0.5*self.compute_chi(params)

    def logpriors(self, params):
        """
        Define  uniform prior.
        Make sure we're inside the preset boundaries

        :param params:
        :return:
        """
        if params is None:
            self.logger.error("Param is None " )

        in_boundaries = (params >= self.min_boundaries) * (params <= self.max_boundaries)
        if (in_boundaries==False).as_vector().any():
            return -np.inf
        else:
            self.model.sanitize_parameters(params)
            return 0.0
    #for PyMultinest
    def pyloglike(self, cube, ndim, nparams):
        """
        wrap for pymultinest
        """
        vect = [cube[i] for i in range(ndim)]
        params = self.model.Parameters().from_ndarray(vect)
        self.model.sanitize_parameters(params)

        return self.loglike(params)

    def pycube(self, cube, ndim, nparams):
        """
        Transforms samples `u` drawn from the unit cube to samples to those
        from our uniform prior

        for pymultinest
        """
        for i in range(ndim):
            cube[i] = (self.max_boundaries - self.min_boundaries)[i] * cube[i] + self.min_boundaries[i]

    #For Dynesty
    def ptform(self, u):
        """Transforms samples `u` drawn from the unit cube to samples to those
        from our uniform prior

        for Dynesty
        """
        return (self.max_boundaries - self.min_boundaries) * u + self.min_boundaries

    def compute_chi(self, params):
        # Sanitize the parameters
        #
        if not isinstance(params, GalaxyParameters):
            if isinstance(params, np.ndarray):
                params = self.model.Parameters().from_ndarray(params)

        self.model.sanitize_parameters(params) # to deal with circularity

        #dim_d = np.size(self.cube.data)
        ones = self.cube**2/self.variance_cube   #
        dim_d = np.isfinite(ones.data).sum() #count only data with finite values

        dim_p_free = dim_p = len(params)
        #already taken care
        #if self.model.flux_profile is not 'sersic':
        #    dim_p_free = dim_p -1
        if self.known_parameters is not None:
            fixed = np.where(np.isfinite(self.known_parameters),1,0).sum()
        else:
            _snr = self.galaxy.stdev / np.abs(self.galaxy)
            fixed = np.where(_snr<1e-6,1,0).sum()
        self.dim_p_free = dim_p_free - fixed

        self.Ndegree = (dim_d - self.dim_p_free -1)

        return self.chisq(self.chi_stat)(params)

    def chisq(self, chi_stat):

        # Chi2 satistics, default
        if (chi_stat == 'gaussian'):
            compute_chi_fct = lambda g: \
            np.nansum(self._compute_error_gauss(g)
            )
        # https://heasarc.gsfc.nasa.gov/xanadu/xspec/manual/XSappendixStatistics.html
        # Mighell http://adsabs.harvard.edu/abs/1999ApJ...518..380M
        # Humphrey 2009, http://adsabs.harvard.edu/abs/2009ApJ...693..822H
        # Mighell
        elif (chi_stat == 'Mighell'):
            compute_chi_fct = lambda g: \
            np.nansum(self._compute_error_Mighell(g)
            )
        # C-statistique
        elif (chi_stat == 'Cstat'):
            compute_chi_fct = lambda g: \
            np.nansum(self._compute_error_cstat(g)
            )
        # Neyman
        elif (chi_stat == 'Neyman'):
            compute_chi_fct = lambda g: \
            np.nansum(self._compute_error_Neyman(g)
            )
        # Pearson
        elif (chi_stat == 'Pearson'):
            compute_chi_fct = lambda g: \
            np.nansum(self._compute_error_Pearson(g)
            )
        else:
            raise Exception("chi_stat is not Valid, should be %s" %(str(self.CHISTAT_VALID)))
        #returns function
        return compute_chi_fct

    def myMCMC(self, max_iterations, random_amplitude, sampling_method='Cauchy', min_acceptance_rate=10 ):
        """

        :param max_iterations:
        :param random_scale:
        :param should_guess_flags:
        :param sampling_method:
        :param  min_acceptance_rate: float [defailt = 5]
            In %, the acceptance rate is the number of useful iterations divided
            by the total number of iterations.
            If it gets below the `failure_rate` treshold, iterations stop.

        :return:
        """


        self.logger.info("Random amplitude : %s", str(random_amplitude))


        # Some useful vars

        count_alpha_ok = 0
        count_min = 0
        total_iterations = 0
        ki_min = sys.maxsize  # that way, it can only go down

        galaxy = self.initial_parameters
        galaxy_old = galaxy.copy()
        galaxy_new = galaxy_old.copy()
        chi_old = self.compute_chi(galaxy)
        #lnprob = self.lnprob(galaxy)

        self.logger.critical("Running GalPak MHSampler with Sampling %s" % (sampling_method))

        names_param = list(galaxy.names)
        names_param.append('reduced_chi')
        # names_param = [
        #   'x', 'y', 'z', 'flux', 'radius', 'inclination', 'pa',
        #   'turnover_radius', 'maximum_velocity', 'velocity_dispersion',
        #   'reduced_chi',
        # ]
        # types_param = ['float32' for i in range(dim_p + 1)]
        #dt = zip(names_param, types_param)
        #chain = np.zeros(max_iterations, dtype=dt)  # intensive operation !
        # chain = Table(names=names_param,dtype=types_param)
        self.chain_rows = []

        rate = 100.
        while (rate > min_acceptance_rate) and (count_alpha_ok < max_iterations):

            # Update loop conditions
            total_iterations += 1

            # Cauchy jumping
            galaxy_new = self._sampling_method(sampling_method, galaxy_old, random_amplitude)


            #new way: from emceee
            #newlnprob = self.lnprob(galaxy_new)
            #diff = 0.5 * (newlnprob - lnprob)

            #if diff < 0:
            #    diff = np.exp(diff) - np.random.rand()

            #if diff > 0:
            #    lnprob = newlnprob
            #    galaxy = galaxy_new

            # Make sure we're inside the preset boundaries
            in_boundaries = (galaxy_new >= self.min_boundaries) * (galaxy_new <= self.max_boundaries)
            if in_boundaries.all():

                # Computing convolved model with new parameters
                chi_new = self.compute_chi(galaxy_new)
                if chi_new<1e-3:
                    #print chi_new,galaxy_new
                    self.logger.error('Chi2 is 0, quit')
                    exit()

                # Compute ratio of likelihood a posteriori
                # exp( old-new / 2 )
                likelihood =  safe_exp(-0.5 * (chi_new - chi_old))

                # likelihood > 1 => new is better
                # likelihood < 1 => accept or reject
                alpha = np.random.rand()

                # Conservation test
                if alpha < likelihood:
                    count_alpha_ok += 1
                    rate = count_alpha_ok * 100. / total_iterations

                    # Save minimum
                    if ki_min > chi_new:
                        ki_min = chi_new
                        count_min = count_alpha_ok

                    galaxy_old = galaxy_new
                    chi_old = chi_new

                    # vect = np.append(galaxy_new, chi_new / self.Ndegree)
                    #chain[count_alpha_ok - 1] = np.float32(vect)
                    # chain.add_row(vect)
                    self.chain_rows.append(list(galaxy_new) +
                                      [chi_new / self.Ndegree])

                    if self.verbose:
                        # Check that parameters are not too close to the boundaries
                        too_close_to_max = np.abs((galaxy_new - self.max_boundaries) / self.max_boundaries) < self.eps
                        too_close_to_min = np.abs((galaxy_new - self.min_boundaries) / self.min_boundaries) < self.eps
                        too_close_to_boundaries = too_close_to_min + too_close_to_max
                        #
                        info = "{count:5d} MIN={count_min:5d} {rate:2.0f}% " \
                               "χ²={ki:3.6f}>{ki_min:3.6f} {params:s}"
                        info = info.format(
                            count=count_alpha_ok,
                            count_min=count_min,
                            ki=chi_new / self.Ndegree,
                            ki_min=ki_min / self.Ndegree,
                            rate=rate,
                            params=galaxy_new.colored_info(too_close_to_boundaries)
                        )
                        if self.model.redshift is not None:
                            mdyn = self.model.compute_Mdyn_at_Rhalf(galaxy_new)
                            info += "log_mdyn={mass:.2f} "
                            info = info.format(mass=np.log10(mdyn))
                        info += "lnlog={lnlog:6.4f} "
                        info = info.format(lnlog=self.loglike(galaxy_new))
                        print(info)

        if len(self.chain_rows)>0:
            chain = Table(names=names_param, rows=self.chain_rows)
        else:
            raise Exception("No useful iterations")

        # Raise if no useful iteration was run
        if rate == 0.:
            self.logger.debug("Last Galaxy Parameters : %s", galaxy_new)
            raise RuntimeError("No useful iteration was run. "
                               "Try with higher max_iterations?")


        # Report
        self.logger.info("Iterations report : %d Total, %d OK, %d%% Rate",
                         total_iterations, count_alpha_ok, rate)
        self.logger.info("Storing results as parameters...")

        # Acceptance Rate
        self.acceptance_rate = rate
        self.logger.info("self.acceptance_rate : useful iterations count / total iterations count : %s " % (self.acceptance_rate) )

        return chain


    #PRIVATE METHODS
    def _sampling_method(self, sampling, params, scale):
        """
        set proposal distribution with sampling
        sampling: 'Cauchy' [default] | 'Normal'
            Cauchy: Lorentz proposal
            Normal: Gaussian proposal
        """
        if sampling == 'Cauchy':
            random_uniforms = np.random.uniform(-np.pi / 2., np.pi / 2., size=len(params))
            galaxy_new = params + scale * np.tan(random_uniforms)
        elif sampling == 'Normal':
            galaxy_new = np.random.normal(params, scale, size=len(params))
        elif sampling == 'AdaptiveCauchy':
            random_uniforms = np.random.uniform(-np.pi / 2., np.pi / 2., size=len(params))
            #@fixme should be covariance
            if len(self.chain_rows)>1500:
                scale = np.sqrt(np.std(np.array(self.chain_rows)[-750:,:-1], axis=0) )**2 / len(params)
            elif len(self.chain_rows) > 500:
                scale = np.sqrt(np.std(np.array(self.chain_rows)[-250:, :-1], axis=0) * 1.25 ) ** 2 / len(params)
            elif len(self.chain_rows) > 50:
                scale = np.sqrt(np.std(np.array(self.chain_rows)[-50:, :-1], axis=0) * 1.5) ** 2 / len(params)

            galaxy_new = params + scale * np.tan(random_uniforms)
        else:
            raise Exception("Not implemented. Should be %s" %(self.SAMPLING_VALID))

        return galaxy_new

    def _init_sampling_scale(self, random_scale, should_guess_flags):
        dim_d = np.size(self.cube.data)
        dim_p = len(self.galaxy)

        # Tweak the random amplitude vector (Kp coeff, as pid)
        # that we can document Model.setup_random_amplitude() adequately
        random_amplitude = np.sqrt(
            (self.min_boundaries - self.max_boundaries) ** 2 / 12.
        ) * dim_p / dim_d

        # Let the model adjust the random amplitude of the parameter jump
        self.model.setup_random_amplitude(random_amplitude)

        # Scale MCMC if needed // allowing vectors
        if random_scale is not None:
            if np.size(random_scale) != 1:
                merge_where_nan(random_scale, np.ones_like(random_amplitude))
            random_amplitude = random_amplitude * random_scale

        # Zero random amplitude where parameters are known
        random_amplitude = random_amplitude * should_guess_flags

        return random_amplitude

    def _compute_error_gauss(self, galaxy):
        """
        It computes the difference between the measured cube
        and the computed cube from given galaxy parameters.
        returns ( D - M ) / stdev
        """

        # Compute convolved cube for given galaxy parameters
        cube_convolved = self.create_convolved_cube(galaxy, self.cube.shape)

        # Diff. between measured cube and convolved cube, scaled by the error
        self.variance_chi = self.variance_cube
        difference = (self.cube - cube_convolved)**2 / self.variance_chi

        return np.ndarray.flatten(difference.data)

    def _compute_error_Mighell(self, galaxy):
        """
            Modified Statistic Mighell 1998
            Sum ( D + min(1,D) - M)^2 / D + 1
        """

        # Compute convolved cube for given galaxy parameters
        cube_convolved = self.create_convolved_cube(galaxy, self.cube.shape)

        tmp_cube = HyperCube(np.where(self.cube.data >= 1, 1., self.cube.data))
        self.variance_chi = self.cube + 1.0
        difference = (self.cube + tmp_cube - cube_convolved ) **2 \
                     / self.variance_chi


        return np.ndarray.flatten(difference.data)

    def _compute_error_Neyman(self, galaxy):
        """
            Modified Neyman statistic
            Humphrey 2009, http://adsabs.harvard.edu/abs/2009ApJ...693..822H
            Sum ( M - D )^2 / max(D,1)
        """

        # Compute convolved cube for given galaxy parameters
        cube_convolved = self.create_convolved_cube(galaxy, self.cube.shape)

        self.variance_chi = HyperCube(np.where(self.cube.data <= 1, 1., self.cube.data))
        difference = (cube_convolved - self.cube)**2 / self.variance_chi

        return np.ndarray.flatten(difference.data)

    def _compute_error_Pearson(self, galaxy):
        """
            Pearson statistic
            Humphrey 2009, http://adsabs.harvard.edu/abs/2009ApJ...693..822H
            Sum ( M - D )^2 / M
         """

        # Compute convolved cube for given galaxy parameters
        cube_convolved = self.create_convolved_cube(galaxy, self.cube.shape)
        difference = (cube_convolved - self.cube)**2 / (cube_convolved)
        self.variance_chi = cube_convolved

        return np.ndarray.flatten(difference.data)

    def _compute_error_cstat(self, galaxy):
        """
         Cash statistique for Poisson noise
         Humphrey 2009, http://adsabs.harvard.edu/abs/2009ApJ...693..822H
         Sum ( M - D + D * log(D/M) )
        """

        # Compute convolved cube for given galaxy parameters
        cube_convolved = self.create_convolved_cube(galaxy, self.cube.shape)

        tmp_cube = np.log(self.cube.data/cube_convolved)
        difference = (cube_convolved - self.cube) + self.cube * tmp_cube
        self.variance_chi = np.ones_like(self.cube.data)

        return np.ndarray.flatten(difference.data)

#########################
######EMCEE 3.0
########################
try:
    from emcee.moves import MHMove

    class CauchyMove(MHMove):
        """A Metropolis step with a Gaussian proposal function.

        Args:
            cov: The covariance of the proposal function. This can be a scalar,
                vector, or matrix and the proposal will be assumed isotropic,
                axis-aligned, or general respectively.
            mode (Optional): Select the method used for updating parameters. This
                can be one of ``"vector"``, ``"random"``, or ``"sequential"``. The
                ``"vector"`` mode updates all dimensions simultaneously,
                ``"random"`` randomly selects a dimension and only updates that
                one, and ``"sequential"`` loops over dimensions and updates each
                one in turn.
            factor (Optional[float]): If provided the proposal will be made with a
                standard deviation uniformly selected from the range
                ``exp(U(-log(factor), log(factor))) * cov``. This is invalid for
                the ``"vector"`` mode.

        Raises:
            ValueError: If the proposal dimensions are invalid or if any of any of
                the other arguments are inconsistent.

        """
        def __init__(self, cov, mode="vector", factor=None):
            # Parse the proposal type.
            try:
                float(cov)

            except TypeError:
                cov = np.atleast_1d(cov)
                if len(cov.shape) == 1:
                    # A diagonal proposal was given.
                    ndim = len(cov)
                    proposal = _diagonal_proposal(np.sqrt(cov), factor, mode)

                elif len(cov.shape) == 2 and cov.shape[0] == cov.shape[1]:
                    # The full, square covariance matrix was given.
                    ndim = cov.shape[0]
                    proposal = _proposal(cov, factor, mode)

                else:
                    raise ValueError("Invalid proposal scale dimensions")

            else:
                # This was a scalar proposal.
                ndim = None
                proposal = _isotropic_proposal(np.sqrt(cov), factor, mode)

            super(CauchyMove, self).__init__(proposal, ndim=ndim)


    class _isotropic_proposal(object):

        allowed_modes = ["vector", "random", "sequential"]

        def __init__(self, scale, factor, mode):
            self.index = 0
            self.scale = scale
            if factor is None:
                self._log_factor = None
            else:
                if factor < 1.0:
                    raise ValueError("'factor' must be >= 1.0")
                self._log_factor = np.log(factor)

            if mode not in self.allowed_modes:
                raise ValueError(("'{0}' is not a recognized mode. "
                                  "Please select from: {1}")
                                 .format(mode, self.allowed_modes))
            self.mode = mode

        def get_factor(self, rng):
            if self._log_factor is None:
                return 1.0
            return np.exp(rng.uniform(-self._log_factor, self._log_factor))

        def get_updated_vector(self, rng, x0):
            return x0 + self.get_factor(rng) * self.scale * rng.randn(*(x0.shape))

        def __call__(self, x0, rng):
            nw, nd = x0.shape
            xnew = self.get_updated_vector(rng, x0)
            if self.mode == "random":
                m = (range(nw), rng.randint(x0.shape[-1], size=nw))
            elif self.mode == "sequential":
                m = (range(nw), self.index % nd + np.zeros(nw, dtype=int))
                self.index = (self.index + 1) % nd
            else:
                return xnew, np.zeros(nw)
            x = np.array(x0)
            x[m] = xnew[m]
            return x, np.zeros(nw)


    class _diagonal_proposal(_isotropic_proposal):

        def get_updated_vector(self, rng, x0):
            random_uniforms = np.random.uniform(-np.pi / 2., np.pi / 2., size=len(self.scale))
            return x0 + self.get_factor(rng) * self.scale * np.tan(random_uniforms)
            #return x0 + self.get_factor(rng) * self.scale * rng.randn(*(x0.shape))

    class _proposal(_isotropic_proposal):

        allowed_modes = ["vector"]

        def get_updated_vector(self, rng, x0):
            random_uniforms = np.random.uniform(-np.pi / 2., np.pi / 2., size=len(self.scale))
            return x0 + self.get_factor(rng) * self.scale * np.tan(random_uniforms)
            #return x0 + self.get_factor(rng) * rng.multivariate_normal(
            #    np.zeros(len(self.scale)), self.scale)

except:
    pass
