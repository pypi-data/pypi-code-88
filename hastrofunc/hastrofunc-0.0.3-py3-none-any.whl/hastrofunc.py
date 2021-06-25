import numpy as np
import matplotlib as mpl
import matplotlib.colors as colors
from PyAstronomy.pyasl.asl.astroTimeLegacy import precess
from astropy.io import fits
from astropy import constants as const
import gc

######
### Calculates v_LSR given RA and Dec (in degrees)
######
def lsr_vel(RA_deg, Dec_deg, equinox=2000):
    ## Precess the given RA, Dec to 1900
    ra1900_deg, dec1900 = precess(RA_deg, Dec_deg, equinox, 1900)
    ra1900 = ra1900_deg/15.
    
    ## Convert RA, Dec to radians
    ra = np.deg2rad(ra1900_deg)
    dec = np.deg2rad(dec1900)
    
    ## Get the X,Y,Z vector of the source at equinox 1900...
    xx = np.empty(3)
    xx[0] = np.cos(dec) * np.cos(ra)
    xx[1] = np.cos(dec) * np.sin(ra)
    xx[2] = np.sin(dec)
    
    ## Get the conventional LSR solar motion.
    ##	LSR MOVES WITH 20.000 KM/S TOWARDS ra1900, dec1900 = 18.000, 30.000
    ralsr = np.pi * 18./12.
    declsr = np.pi * 30./180.
    
    xxlsr = np.empty(3)
    xxlsr[0] = np.cos(declsr) * np.cos(ralsr)
    xxlsr[1] = np.cos(declsr) * np.sin(ralsr)
    xxlsr[2] = np.sin(declsr)
    
    vvlsr = xxlsr * 20.
    vvlsrsrc = np.sum(np.multiply(xx,vvlsr))
    delvlsr = -vvlsrsrc
    
    return delvlsr

######
### Calculates v_GSR given v_LSR, Galactic latitude, and Galactic longitude
######
def convert_lsr2gsr(v_LSR, Glat, Glon, MW_rot=220.):
    # v_LSR = LSR velocity (km/s)
    # Glat, Glon = Galactic latitude and longitude (degrees)
    # MW_rot = Assumed rotation velocity for the Milky Way (km/s)
    return v_LSR + (MW_rot*np.sin(np.deg2rad(Glon))*np.cos(np.deg2rad(Glat)))


######
### Create a gradient between two colors and return a color on that gradient determined by the mix parameter (a value between 0 and 1)
######
def mix_colors(c1, c2, mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)
    
    ### Example:
    #c1='red'
    #c2='white'
    #n=10
    #fig, ax = plt.subplots(figsize=(8, 5))
    #for x in range(n+1):
    #    ax.axvline(x, color=colorFader(c1,c2,x/n), linewidth=4) 
    #ax.scatter(0,0.5,s=500,marker='o',edgecolor='grey',color=colorFader(c1,c2,mix=0.))
    #ax.scatter(5,0.5,s=500,marker='o',edgecolor='grey',color=colorFader(c1,c2,mix=0.5))
    #ax.scatter(10,0.5,s=500,marker='o',edgecolor='grey',color=colorFader(c1,c2,mix=1.))
    #plt.show()
    


######
### Return a truncated version of an existing colormap
######
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

    ### Example:
    # new_cmap = truncate_colormap(plt.get_cmap('viridis'), 0., 0.98)
    
    
######
### Stack QuaStar spectra from table
######  
def stack_quastar_spectra(input_table, objtype='',line='', stacktype='median'): # 'line' parameter is integer wavelength in Angstroms
    ### Check for valid input parameters
    if objtype == 'BHB':
        vel_key = 'BHB_vels_'+line+'A'
        flux_key = 'BHB_normflux'
    elif objtype == 'QSO':
        vel_key = 'QSO_binned_vels_'+line+'A'
        flux_key = 'QSO_binned_normflux'
    else:
        raise ValueError("Must specify objtype: 'BHB' or 'QSO'")
    if not any(line == validline for validline in ['1548','1550','1393','1402','1526','1608','1611','1670']):
    #if line == !('1548' or '1550' or '1393' or '1402' or '1526' or '1608' or '1611' or '1670'):
        raise ValueError("Must specify line parameter (integer wavelength in Angstroms) \n" + \
                        "Available ions: \n" + \
                         "C IV (1548, 1550) \n" + \
                         "Si IV (1393, 1402) \n" + \
                         "Si II (1526) \n" + \
                         "Fe II (1608, 1611) \n" + \
                         "Al II (1670)")
    ### Combine velocity arrays so they are the same for both lines, then use interpolation get the flux values and stack them
    # Create array that contains velocity values for all rows of the input table
    combined_vels = np.unique(np.concatenate([row[vel_key] for row in input_table]))
    # Initialize array for summing fluxes
    interpflux_sum = np.zeros(len(combined_vels))
    for row in input_table:
            # Interpolate so the line has corresponding flux values at every velocity
            interpflux_obj = np.interp(combined_vels, row[vel_key], row[flux_key], left=0, right=0) # Perform interpolation on this object using combined velocity array
            # Add the interpolated flux values to running sum
            interpflux_sum = np.vstack([interpflux_sum, interpflux_obj])
    if stacktype == 'mean':
        flux_stack = np.mean(interpflux_sum[1:],axis=0)
    elif stacktype == 'median':
        flux_stack = np.median(interpflux_sum[1:],axis=0)
    return combined_vels, flux_stack


######
### Get continuum-fit spectrum from FITS file
######
def get_spectrum(filename):
    """
    flux_line = fits.getdata(filename, ext=0)
    flux_error = fits.getdata(filename, ext=1)
    lambda_data = fits.getdata(filename, ext=2)
    flux_cont = fits.getdata(filename, ext=3)
    #"""
    with fits.open(filename, memmap=False) as hdul:
        flux_line = hdul[0].data
        flux_error = hdul[1].data
        lambda_data = hdul[2].data
        flux_cont = hdul[3].data
        for hdu in hdul:
#             del hdu_data
            del hdu.data
#         print(hdu.closed)
        gc.collect()
    return lambda_data, flux_line, flux_error, flux_cont

######
### Convert wavelength to velocity for a specific line
######
def convert_wave2vel(obs_wave, rest_wave, LSR_vel=0.):
    # Define constants
    c = const.c.to('km/s').value
    return (((obs_wave - rest_wave)/rest_wave) * c) - LSR_vel

    #obs_wave = ((vel + LSR_vel) * rest_wave / c) + rest_wave
    #(vel + LSR_vel)*(rest_wave/c) = (obs_wave-rest_wave)
    #(vel + LSR_vel)/c = (obs_wave-rest_wave)/rest_wave
    #vel + LSR_vel = ((obs_wave-rest_wave)/rest_wave)*c
    #return vel = (((obs_wave-rest_wave)/rest_wave)*c) - LSR_vel

######
### Convert velocity to wavelength for a specific line
######
def convert_vel2wave(vel, rest_wave, LSR_vel=0.):
    # Define constants
    c = const.c.to('km/s').value
    return ((vel + LSR_vel) * rest_wave / c) + rest_wave

######
### Convert velocity to redshift (approximation)
######
def convert_vel2z(vel):
    return vel/c

######
### Convert redshift to velocity (approximation)
######
def convert_z2vel(z):
    return z*c

######
### Convert rest wavelength to observed wavelength
######
def convert_restwave2obswave(rest_wave,z):
    return (z*restwave) + restwave

######
### Convert column density to equivalent width for a specific line
######    
def convert_N2EW(N, lambda_0, f):
    # N: column density [cm^-2; not the log value!]
    # lambda_0: rest wavelength of the line being measured [Angstroms]
    # f: oscillator strength of the line [dimensionless; 0<f<1]
    #
    # This is for the optically thin case only!
    return N * lambda_0**2 * f / 1.13e20

###### !!!!!!BROKEN?
### Propogate errors for addition or subtraction
######
def propogate_error_addsub(err_array):
    # err_array: numpy array of integer values being added (you cannot give the function an array of error arrays)
    #if np.any([type(el) != float for el in err_array]):
    #    raise ValueError('The input error array must contain floats!')
    err_array = np.array(err_array)
    # dQ = sqrt((da)^2 + (db)^2 + ... + (dy)^2 + (dz)^2)
    errs_squared = err_array**2
    dQ = np.sqrt(np.sum(errs_squared))
    return dQ

######
### Propogate errors for multiplication or division
######
def propogate_error_multdiv(err_array, val_array, final_val):
    # val_array: numpy array of values being multiplied
    # err_array: numpy array of errors on those values (must be the same length as val_array)
    # final_val: the result of the multiplication/division, to which the fractional error will be applied (float)
    val_array = np.array(val_array)
    err_array = np.array(err_array)
    # dQ/Q = sqrt((da/a)^2 + (db/b)^2 + ... + (dy/y)^2 + (dz/z)^2)
    err_fracs = err_array/val_array
    errs_squared = err_fracs**2
    dQ = np.sqrt(np.sum(errs_squared)) * abs(final_val)
    return dQ

######
### Propogate errors for exponentials
######
def propogate_error_exp(power, base, base_err, final_val): # all integers
    # power: power of the exponential (float)
    # base: value in the base of the exponent (float)
    # base_err: error of the value in the base of the exponent (float)
    # final_val: the result of the exponential operation, to which the fractional error will be applied (float)
    # dQ/Q = abs(n) * dx/abs(x) where Q=x^n
    err_frac = abs(power) * (base_err / abs(base))
    dQ = err_frac * abs(final_val)
    return dQ

######
### Propogate errors for log10
######
def propogate_error_log10(arg, arg_err): # all integers
    # arg: value in the logarithm (float)
    # arg_err: error of the value in the logarithm (float)
    # dQ = 0.434 * dx/x where Q=log10(x)
    dQ = 0.434 * (arg_err/arg)
    return dQ

######
### Calculate column density for a specific line
######
# This was adapted from IDL code passed on by Jess, and last used in Python 2 - may need updating
# Used this to measure logN on absorption-free region near NaI, CaII lines (which will then give an upper limit on column density sensitivity)
def calc_N(wave, spec, error, vrange, w0, f0,limit=2):
    # wave: wavelength array
    # spec: flux array
    # error: flux error array
    # vrange: 2-element list or array with lower, upper limits of velocity range
    # w0: central wavelength for measurement
    # f0: oscillator strength
    # limit: ???
    # Returns logN and error
    vv = (wave-w0) / w0 * 2.9979e5
    iv = (vv[1:] >= vrange[0]) & (vv[1:]<= vrange[1])
    #
    tau = -1. *np.log(spec)
    nv = tau / 2.654e-15 / f0 / w0 # in units cm^-2 / (km s^-2) column density per unit velocity
    n = nv[1:] * np.diff(vv) # column density per bin obtained by multiplying differential Nv by bin width
    col = np.sum(n[iv])
    #
    tauerr = error/spec
    nerr = tauerr[1:] / 2.654e-15 / f0 / w0 * np.diff(vv)
    colerr = np.sum((nerr[iv])**2)**0.5
    #
    print('Limit N = (',   '%e'%col, ') +/- ', '%e' %(colerr))
    print('Limit N = (',   np.log10(abs(col)), ') +/- ', np.log10(colerr))
    #
    return col, colerr


