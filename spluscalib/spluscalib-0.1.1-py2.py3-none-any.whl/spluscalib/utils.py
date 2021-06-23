# -*- coding: utf-8 -*-

# ******************************************************************************
#                          S-PLUS CALIBRATION PIPELINE
#                                     Utils
# ******************************************************************************


"""
This file includes all the functions used by the different scripts of the
calibration pipeline.

--------------------------------------------------------------------------------
   FUNCTIONS:
--------------------------------------------------------------------------------

general
    makedir()
    load_field_list()
    fz2fits()
    load_data()
    concat_data
    mean_robust()

pipeline configuration file
    pipeline_conf()
    load_conf()
    convert_param_to_pipeline_types()
    convert_to_system_path()

pipeline log file
    printlog()
    gen_logfile_name()
    get_time_stamp()

aperture photometry
    get_sex_config()
    splus_image_satur_level()
    splus_image_gain()
    splus_image_seeing()
    get_swarp_config()
    update_detection_header()
    get_sexconf_fwhm()
    plot_sex_diagnostic()

psf photometry
    get_dophot_config()
    psf_flagstar()
    format_dophot_catalog()
    plot_dophot_diagnostic()

xy inhomogeneities correction
    intersection_2lines()
    align_splus_xy()
    apply_xy_correction()

aperture correction
    get_apertures_from_sexconf()
    obtain_aperture_correction()
    star_selector()
    growth_curve()
    growth_curve_plotter()

master photometry
    extract_sex_photometry()
    extract_psf_photometry()
    format_master_photometry()

crossmatch
    download_vizier_catalog_for_splus_field()
    download_galex()
    download_refcat2()
    download_ivezic()
    download_sdss()
    download_gaia()
    download_reference()
    crossmatch_catalog_name()

extinction_correction
    correct_extinction_schlegel()
    correct_extinction_gorski()
    correct_extinction()

calibration
    zp_write()
    zp_read()
    zp_add()
    calibration_suffix()
    sed_fitting()
    get_filter_zeropoint()
    zp_estimate()
    zp_apply()
    plot_zp_fitting()
    zp_estimate_stlocus()

catalog_preparation

diagnostics

--------------------------------------------------------------------------------
   COMMENTS:
--------------------------------------------------------------------------------
A casual user of the spluscalib package should never have to worry about the
content of this file.

--------------------------------------------------------------------------------
   USAGE:
--------------------------------------------------------------------------------
in python:
from spluscalib import utils

----------------
"""

################################################################################
# Import external packages

import os
import sys
import datetime
import warnings

# Astropy
from astropy import units as u
from astropy.io import fits
from astropy.wcs import WCS
from astropy.wcs.utils import pixel_to_skycoord
from astropy.time import Time
from astropy.table import Table
from astropy.coordinates import SkyCoord, Distance

# Astroquery
from astroquery.vizier import Vizier

# sfdmap
import sfdmap

# Numpy
import numpy as np

# Pandas
import pandas as pd

# Scipy
from scipy.stats import linregress
from scipy.interpolate import interp2d

# Sklearn
from sklearn.neighbors import KernelDensity

# Matplotlib
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

# Shapely
from shapely.geometry import Point, Polygon


################################################################################
# Setup pipeline directories

pipeline_path = os.path.split(__file__)[0]
spluscalib_path = os.path.split(pipeline_path)[0]

sys.path.append(spluscalib_path)

################################################################################
# Import splucalib packages

from spluscalib import dust_laws
from spluscalib import sed_fitting as sf

################################################################################
# General


def makedir(directory):
    """
    Checks if a directory exists and, if not, creates it.

    Parameters
    ----------
    directory : str
        Directory to be created
    """

    if not os.path.exists(directory):
        print(directory)
        os.mkdir(directory)


def load_field_list(data_file):
    """
    Loads a list of fields in a file (one per line)

    Parameters
    ----------
    data_file : str
        Location with field list file

    Returns
    -------
    Sized
        list of fields
    """

    fields = []
    with open(data_file, 'r') as f:
        file_lines = f.readlines()

    for i in range(len(file_lines)):
        fields.append(file_lines[i].replace("\n", ""))

    return fields


def fz2fits(image):
    """
    Converts S-PLUS images from .fz to .fits

    Parameters
    ----------
    image : str
        Location of S-PLUS .fz image

    Returns
    -------
    Saves S-PLUS fits image in the same location
    """

    data = fits.open(image)[1].data
    header = fits.open(image)[1].header
    imageout = image[:-2] + 'fits'

    fits.writeto(imageout, data, header, overwrite=True)


def load_data(data_file):
    """
    Loads a catalog that is either in fits format, or can be read as a pandas
    dataframe, and returns a dataframe

    Parameters
    ----------
    data_file : str
        Location of the catalog

    Returns
    -------
    pd.DataFrame
        Catalog's dataframe
    """

    # If necessary, transform from fits table to data frame
    if os.path.splitext(data_file)[1] == '.fits':
        fits_data = Table.read(data_file, format='fits')
        ref_data  = fits_data.to_pandas()

    else:
        ref_data = pd.read_csv(data_file, delim_whitespace=True, escapechar='#',
                               skipinitialspace=True)

    ref_data.columns = ref_data.columns.str.replace(' ', '')

    return ref_data


def concat_data(files_list, save_file):
    """
    Concatenates a list of catalogs (can be both .fits or .cat [ascii])

    Parameters
    ----------
    files_list : list
        List of location of the catalogs to be concatenated
    save_file : str
        Location to save the result

    Returns
    -------
    Saves the concatenated catalog in .cat [ascii] format
    """

    df_list = []

    for cat_file in files_list:
        print(cat_file)
        df_list.append(load_data(cat_file))

    df_all = pd.concat(df_list)

    with open(save_file, 'w') as f:
        f.write("# ")
        df_all.to_csv(f, index = False, sep = " ")


def mean_robust(x, low=3, high=3):
    """
    Estimates the mean using a sigma clip between 'low'-sigma and 'high'-sigma

    Parameters
    ----------
    x : list
        Array-like unidimensional data
    low : float
        Lower cut [units of sdev]
    high : float
        Top cut [units of sdev]

    Returns
    -------
    float
        mean of the distribution after a sigma-clip
    """

    x = np.array(x)

    mean_x = np.nanmean(x)
    std_x = np.nanstd(x)

    x = x[(x > (mean_x - low * std_x)) & (x < (mean_x + high * std_x))]

    return np.mean(x)

################################################################################
# Configuration file


def pipeline_conf(conf_file):
    """
    Reads the configuration file including the default configuration

    Parameters
    ----------
    conf_file : str
        The location of the configuration file

    Returns
    -------
    dict
        a dictionary containing the parameters given in the configuration file.
        Parameter names are dict keys, and values are dict values.
    """

    # Load default configuration
    default_conf_file = os.path.join(pipeline_path,
                                     'steps',
                                     'resources',
                                     'default_config.conf')

    default_conf = load_conf(default_conf_file)

    # Load user configuration
    conf = load_conf(conf_file, default_conf)

    # Convert defaults to system path format
    conf = convert_to_system_path(conf)

    return conf


def load_conf(conf_file, default_conf=None):
    """
    Reads the configuration file and returns a dictionary with the parameters

    Parameters
    ----------
    conf_file : str
        The location of the configuration file

    default_conf : dict
        dictionary containing previously loaded parameters given in
        another (usually default) configuration file.

    Returns
    -------
    dict
        a dictionary containing the parameters given in the configuration file.
        Parameter names are dict keys, and values are dict values.
    """

    # Open the file
    with open(conf_file, 'r') as c:

        # Read the file
        raw_file = c.readlines()

    if default_conf is not None:
        conf = default_conf
    else:
        conf = {}

    for line in raw_file:

        # Ignore empty lines
        if line == '\n':
            continue

        # Ignore comment line
        if line[0] == '#':
            continue

        # Remove inline comment
        line = line.split("#")[0]

        # Remove extra spaces, tabs and linebreak
        line = " ".join(line.split())

        # Get parameter name
        param = line.split(" ")[0]

        # Get value
        value = "".join(line.split(" ")[1:])

        # Transform multiple values into list
        if ',' in value:
            value = value.split(',')

        # Assign param and value to dictionary
        conf[param] = value

    # Add run path if not given.
    if 'run_path' not in list(conf.keys()):
        try:
            conf['run_path'] = conf['save_path']
        except KeyError:
            pass

    # Convert parameters to expected types
    conf = convert_param_to_pipeline_types(conf)

    return conf


def convert_param_to_pipeline_types(conf):
    """
    Converts the parameters in the configuration file to the right python type

    Parameters
    ----------
    conf : dict
        pipeline config dictionary read in load_conf

    Returns
    -------
    dict
        dictionary with values converted to the expected type
    """

    ints = ['reference_flag',
            'stellar_locus_N_bins']

    floats = ['inst_zp',
              'apercorr_max_aperture',
              'apercorr_diameter',
              'apercorr_starcut']

    bools = ['use_weight',
             'remove_fits',
             'sex_XY_correction',
             'reference_in_individual_files']

    list_of_floats = ['XY_correction_xbins',
                      'XY_correction_ybins',
                      'apercorr_s2ncut',
                      'zp_fitting_mag_cut',
                      'stellar_locus_color_range',
                      'gaia_zp_fitting_mag_cut']

    list_of_strings = ['run_steps',
                       'filters',
                       'detection_image',
                       'reference_catalog',
                       'external_sed_fit',
                       'external_sed_pred',
                       'stellar_locus_fit',
                       'stellar_locus_color_ref',
                       'internal_sed_fit',
                       'internal_sed_pred',
                       'gaia_model_pred']

    for key in conf.keys():

        # Convert int type
        if key in ints:
            if not isinstance(conf[key], int):
                conf[key] = int(conf[key])

        # Convert float type
        elif key in floats:
            if not isinstance(conf[key], float):
                conf[key] = float(conf[key])

        # Convert boolean type
        elif key in bools:

            if not isinstance(conf[key], bool):
                if conf[key].lower() == 'true':
                    conf[key] = True

                elif conf[key].lower() == 'false':
                    conf[key] = False

                else:
                    raise ValueError("Invalid configuration for %s" % key)

        # Convert list of floats
        elif key in list_of_floats:
            if isinstance(conf[key], list):
                for i in range(len(conf[key])):
                    conf[key][i] = float(conf[key][i])

            else:
                raise ValueError("Invalid configuration for %s" % key)

        # Convert list of strings
        elif key in list_of_strings:
            if not isinstance(conf[key], list):
                conf[key] = [conf[key]]

    return conf


def convert_to_system_path(conf):
    """
    Convert paths to system path format and include path to the pipeline

    Parameters
    ----------
    conf : dict
        pipeline config dictionary read in load_conf

    Returns
    -------
    dict
        dictionary with formated paths
    """

    paths = ['save_path',
             'run_path',
             'path_to_sex',
             'path_to_swarp',
             'path_to_stilts',
             'path_to_dophot',
             'path_to_images',
             'sex_config',
             'sex_param',
             'swarp_config',
             'dophot_config',
             'XY_correction_maps_path',
             'extinction_maps_path',
             'path_to_reference',
             'path_to_models',
             'offset_to_splus_refcalib',
             'stellar_locus_reference',
             'path_to_gaia']

    for key in conf.keys():

        if key in paths:

            # Convert to system path format
            path_list = conf[key].split('/')

            if path_list[0] == '.':
                path_sys = os.path.join(pipeline_path, *path_list[1:])

            elif path_list[0] == '..':
                path_sys = os.path.join(spluscalib_path, *path_list[1:])

            else:
                path_sys = os.path.join(*path_list)

            # Replace default pipeline path to user pipeline path
            if "{pipeline_path}" in path_sys:
                path_sys = path_sys.format(pipeline_path=pipeline_path)

            # Replace default spluscalib path to user spluscalib path
            if "{spluscalib_path}" in path_sys:
                path_sys = path_sys.format(spluscalib_path=spluscalib_path)

            # Add initial /
            if path_sys[0] != '/':
                path_sys = '/' + path_sys

            # Remove double /
            path_sys = path_sys.replace("//", "/")

            # Update path to system path
            conf[key] = path_sys

    return conf


################################################################################
# Log

def printlog(message, log_file):
    """
    Prints message to console and save it to the log file

    Parameters
    ----------
    message : str
        message to print and save to log file

    log_file : str
        the location of the log file
    """

    print(message)

    # Get time stamp
    stamp = get_time_stamp()

    with open(log_file, 'a') as log:
        log.write(stamp + message)
        log.write('\n')


def gen_logfile_name(log_file, first_run = True):
    """
    Generates the name of the log file. If desired file already exists,
    adds _*number* in the end of the file name.
    Used to not overwrite existing log files.

    Parameters
    ----------
    log_file : str
        Desired log file location. Must end in .log

    first_run : bool
        Used internally to control recursivity

    Returns
    -------
    str
        Log file location.
    """

    if log_file[-4:] != '.log':
        raise NameError("log file must end in .log")

    if not os.path.exists(log_file):
        return log_file

    else:
        if first_run:
            new_file = log_file.replace(".log", "_1.log")
            return gen_logfile_name(new_file, first_run=False)

        else:
            log_number = int(log_file.split("_")[-1][:-4])
            new_file = log_file.replace(f"{log_number}.log",
                                        f"{log_number+1}.log")

            return gen_logfile_name(new_file, first_run = False)


def get_time_stamp():
    """
    Generates a time stamp

    Returns
    ----------
    str
        current time stamp
    """

    ct = datetime.datetime.now()

    stamp = "[{year}/{mon:02d}/{day:02d} {hh:02d}:{mm:02d}:{ss:02d}] ".format(
        year=ct.year,
        mon=ct.month,
        day=ct.day,
        hh=ct.hour,
        mm=ct.minute,
        ss=ct.second)

    return stamp


################################################################################
# Photometry

###############################
# Single / Dual mode photometry

# Generate Configuration file
def get_sex_config(save_file, default_sexconfig, default_sexparam,
                   catalog_file, image_file, inst_zp, path_to_sex,
                   use_weight=False, mode=None, check_aperima=None,
                   check_segima=None, detection_file=None):

    # Read general configuration file
    with open(default_sexconfig, 'r') as f:
        sex_config = f.readlines()
        sex_config = "".join(sex_config)

    # Read parameters from image header
    satur = splus_image_satur_level(image_file)
    seeing = splus_image_seeing(image_file)
    gain = splus_image_gain(image_file)

    # Update sexconfig
    sex_config = sex_config.format(catalog_file=catalog_file,
                                   param_file=default_sexparam,
                                   path_to_sex=path_to_sex,
                                   inst_zp=inst_zp,
                                   satur=satur,
                                   seeing=seeing,
                                   gain=gain)

    # Include weight image
    if use_weight:
        wimage_file = image_file.replace(".fits", "weight.fits")

        if mode == 'single':
            sex_config += ("WEIGHT_TYPE MAP_WEIGHT\n"
                           "WEIGHT_IMAGE {wimage}").format(wimage=wimage_file)

        elif mode == 'dual':

            wdetection_file = detection_file.replace(".fits", "weight.fits")

            sex_config += ("WEIGHT_TYPE MAP_WEIGHT, MAP_WEIGHT\n"
                           "WEIGHT_IMAGE {wdetection}, {wimage}"
                           "").format(wimage=wimage_file,
                                      wdetection=wdetection_file)

    # Add aper and segm image
    if check_aperima is not None:
        sex_config += ("\nCHECKIMAGE_TYPE APERTURES,SEGMENTATION\n"
                       "CHECKIMAGE_NAME {aperima}, {segima}"
                       "").format(aperima=check_aperima,
                                  segima=check_segima)

    # Save config file
    with open(save_file, 'w') as f:
        f.write(sex_config)


def splus_image_satur_level(image_file):
    """
    Reads the S-PLUS image header and returns the saturation level

    Parameters
    ----------
    image_file : str
        Location of S-PLUS image (fits or fz)

    Returns
    -------
    float
        Value of saturation level ('SATURATE')
    """

    # Get file extension
    extension = os.path.splitext(image_file)[1][1:]

    if extension == 'fz':
        head = fits.open(image_file)[1].header

    elif extension == 'fits':
        head = fits.open(image_file)[0].header

    else:
        raise ValueError("Image extension must be 'fits' or 'fz'")

    satur = float(head['SATURATE'])

    return satur


def splus_image_gain(image_file):
    """
    Reads the S-PLUS image header and returns the gain

    Parameters
    ----------
    image_file : str
        Location of S-PLUS image (fits or fz)

    Returns
    -------
    float
        Value of gain ('GAIN')
    """

    # Get file extension
    extension = os.path.splitext(image_file)[1][1:]

    if extension == 'fz':
        head = fits.open(image_file)[1].header

    elif extension == 'fits':
        head = fits.open(image_file)[0].header

    else:
        raise ValueError("Image extension must be 'fits' or 'fz'")

    gain = float(head['GAIN'])

    return gain


def splus_image_seeing(image_file):
    """
    Reads the S-PLUS image header and returns the observation seeing

    Parameters
    ----------
    image_file : str
        Location of S-PLUS image (fits or fz)

    Returns
    -------
    float
        Value of gain ('HIERARCH OAJ PRO FWHMSEXT')
    """

    # Get file extension
    extension = os.path.splitext(image_file)[1][1:]

    if extension == 'fz':
        head = fits.open(image_file)[1].header

    elif extension == 'fits':
        head = fits.open(image_file)[0].header

    else:
        raise ValueError("Image extension must be 'fits' or 'fz'")

    seeing = float(head['HIERARCH OAJ PRO FWHMSEXT'])

    return seeing


def get_swarp_config(save_file, default_swarpconfig, detection_image_out,
                     detection_weight_out, resample_dir, xml_output,
                     combine_type, weight_type):

    """
    Generates the swarp configuration file, including field specific paths

    Parameters
    ----------
    save_file : str
        Location to save the swarp configuration file
    default_swarpconfig : str
        Location of the general swarp splus configuration file
    detection_image_out : str
        Location to save the generated detection image
    detection_weight_out : str
        Location to save the generated detection image weight
    resample_dir : str
        Directory to save the resampled fits images
    xml_output : str
        Location to save the swarp xml output
    combine_type : str
        swarp configuration parameter COMBINE_TYPE
    weight_type : str
        swarp configuration parameter WEIGHT_TYPE

    Returns
    -------

    """
    # Read general configuration file
    with open(default_swarpconfig, 'r') as f:
        swarp_config = f.readlines()
        swarp_config = "".join(swarp_config)

    # Update swarp_config
    swarp_config = swarp_config.format(image_out    = detection_image_out,
                                       weight_out   = detection_weight_out,
                                       resample_dir = resample_dir,
                                       xml_output   = xml_output,
                                       combine_type = combine_type,
                                       weight_type  = weight_type)

    # Save config file
    with open(save_file, 'w') as f:
        f.write(swarp_config)


def update_detection_header(detection_image, image_list_file):
    """
    Updates detection image header

    Parameters
    ----------
    detection_image : str
        Location of the detection image file
    image_list_file : str
        Location of the file listing the combined images
    """

    # Read list of images
    with open(image_list_file, 'r') as im_list:
        image_list = im_list.readlines()

    # Remove linebreaks
    for i in range(len(image_list)):
        image_list[i] = image_list[i].replace("\n", "")

    # Load images
    images = []

    for i in range(len(image_list)):
        images.append(fits.open(image_list[i]))

    # Load detection image
    det_image = fits.open(detection_image)

    # Update parameters
    det_image[0].header['AUTHOR'] = 'spluscalib'

    # Add new parameters
    FILTER   = ''
    NCOMBINE = 0
    TEXPOSED = 0.
    EFECTIME = 0.

    for i in range(len(image_list)):
        filter_i = images[i][0].header['FILTER'].split("_swp.fits")[0]
        filter_i = filter_i.split("_")[-1]

        FILTER += filter_i+','

        NCOMBINE += int(images[i][0].header['NCOMBINE'])
        TEXPOSED += float(images[i][0].header['TEXPOSED'])
        EFECTIME += float(images[i][0].header['EFECTIME'])

    # Remove last comma from FILTER
    FILTER = FILTER[:-1]

    # Add to the header
    det_image[0].header['FILTER'] = FILTER
    det_image[0].header['NCOMBINE'] = NCOMBINE
    det_image[0].header['TEXPOSED'] = TEXPOSED
    det_image[0].header['EFECTIME'] = EFECTIME

    det_image[0].header['FILENAME'] = os.path.split(detection_image)[1]

    # Add image list
    for i in range(len(image_list)):
        image_i = os.path.split(image_list[i])[1]
        param_name = f'IMAGE{i:.0f}'
        det_image[0].header[param_name] = image_i

    # List of params to take from image0
    inherit_params = ['HIERARCH OAJ QC NCMODE',
                      'HIERARCH OAJ QC NCMIDPT',
                      'HIERARCH OAJ QC NCMIDRMS',
                      'HIERARCH OAJ QC NCNOISE',
                      'HIERARCH OAJ QC NCNOIRMS',
                      'HIERARCH OAJ PRO FWHMSEXT',
                      'HIERARCH OAJ PRO FWHMSRMS',
                      'HIERARCH OAJ PRO FWHMMEAN',
                      'HIERARCH OAJ PRO FWHMBETA',
                      'HIERARCH OAJ PRO FWHMnstars',
                      'HIERARCH OAJ PRO Ellipmean',
                      'HIERARCH OAJ PRO PIPVERS',
                      'HIERARCH OAJ PRO REFIMAGE',
                      'HIERARCH OAJ PRO REFAIRMASS',
                      'HIERARCH OAJ PRO REFDATEOBS',
                      'HIERARCH OAJ PRO SWCMB1',
                      'HIERARCH OAJ PRO SWSCALE1',
                      'HIERARCH OAJ PRO SWCMB2',
                      'HIERARCH OAJ PRO SWSCALE2',
                      'HIERARCH OAJ PRO SWCMB3',
                      'HIERARCH OAJ PRO SWSCALE3']

    for param in inherit_params:
        det_image[0].header[param] = images[0][0].header[param]

    # Adding comments to the header
    det_image[0].header.add_comment(" Updated Header Keywords", after="PSCALET2")
    det_image[0].header.add_comment("", after="PSCALET2")

    det_image[0].header.add_comment(" List of combined images", after="EFECTIME")
    det_image[0].header.add_comment("", after="EFECTIME")

    det_image[0].header.add_comment(" Params from IMAGE0",
                                    after=inherit_params[-1])
    det_image[0].header.add_comment("", after=inherit_params[-1])

    # Save updated detection image
    det_image.writeto(detection_image, overwrite=True)


def get_sexconf_fwhm(sexconf):
    """
    Reads a SExtractor config file and extracts the FWHM value

    Parameters
    ----------
    sexconf : str
        Location of SExtractor config file

    Returns
    -------
    float
        FWHM used in SExtractor configuration
    """


    fwhm = None

    with open(sexconf, 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = line.split()

            if line[0] == 'SEEING_FWHM':
                fwhm = float(line[1])
                break

    return fwhm


def plot_sex_diagnostic(catalog, save_file, s2ncut, starcut, sexconf, filt,
                        mag_cut = (10, 25)):
    """
    Makes diagnostic plots of the photometry in a given SExtractor output

    Parameters
    ----------
    catalog : str
        Location of SExtractor output catalog
    save_file : str
        Location to save plots
    s2ncut : list
        [min, max] values of the s2n calibration cut
    starcut : float
        min value of the class_star calibration cut
    sexconf : str
        Location of SExtractor configuration file
    filt : str
        Name of the photometric filter

    Returns
    -------
    Saves diagnostic plots
    """

    sexcat = Table.read(catalog)

    select, medianFWHM = star_selector(catalog       = sexcat,
                                       s2ncut        = s2ncut,
                                       starcut       = starcut,
                                       mag_partition = 2,
                                       verbose       = False)

    fig, axs = plt.subplots(3, figsize = [5,15])

    #################
    # Plot class star

    # Plot all points
    axs[0].scatter(sexcat['MAG_AUTO'], sexcat['CLASS_STAR'],
                   c="#AAAAAA", s=10, alpha=0.1)

    # Plot selection
    axs[0].scatter(select['MAG_AUTO'], select['CLASS_STAR'],
                   c="#2266FF", s=10, alpha=0.3,
                   label=f"s2ncut: {s2ncut}\n& starcut: {starcut}")

    # Plot cut line
    axs[0].hlines(starcut, mag_cut[0], mag_cut[1],
                  colors="#2266FF", zorder=1)

    # Plot grid lines
    axs[0].hlines(np.arange(-0.1, 1.1, 0.1), mag_cut[0], mag_cut[1],
                  colors="#EEEEEE", zorder=-1)

    axs[0].legend(loc=1)
    axs[0].set_xlim(mag_cut)
    axs[0].set_ylim([-0.1, 1.1])
    axs[0].set_ylabel('CLASS_STAR')
    axs[0].minorticks_on()

    ##########
    # Plot s2n

    # Plot all points
    s2n_cat = sexcat['FLUX_AUTO'] / sexcat['FLUXERR_AUTO']
    axs[1].scatter(sexcat['MAG_AUTO'], s2n_cat,
                   c="#AAAAAA", s=10, alpha=0.1)

    # Plot selection
    s2n_sel = select['FLUX_AUTO'] / select['FLUXERR_AUTO']
    axs[1].scatter(select['MAG_AUTO'], s2n_sel,
                   c="#2266FF", s=10, alpha=0.3)

    # Plot cut line
    axs[1].hlines(s2ncut, mag_cut[0], mag_cut[1],
                  colors="#2266FF", zorder=1)

    # Plot grid lines
    axs[1].hlines([0.1, 1, 10, 100, 1000, 10000], mag_cut[0], mag_cut[1],
                  colors="#EEEEEE", zorder=-1)

    axs[1].set_xlim(mag_cut)
    axs[1].set_yscale('log')
    axs[1].set_ylim([0.1, 2 * s2ncut[1]])
    axs[1].set_ylabel('S/N')
    axs[1].minorticks_on()

    ###########
    # Plot FWHM

    # Plot all points
    axs[2].scatter(sexcat['MAG_AUTO'], sexcat['FWHM_WORLD'] * 3600,
                   c="#AAAAAA", s=10, alpha=0.1)

    # Plot selection
    axs[2].scatter(select['MAG_AUTO'], select['FWHM_WORLD'] * 3600,
                   c="#2266FF", s=10, alpha=0.3, zorder=2)

    # Plot cut line
    fwhm_config = get_sexconf_fwhm(sexconf=sexconf)
    fwhm_estimated = medianFWHM * 3600

    axs[2].plot([mag_cut[0], mag_cut[1]], [fwhm_config, fwhm_config],
                color="#FF6622", zorder=1,
                label=r"FWHM$_{\mathrm{config}}$" + f": {fwhm_config:.3f}")

    axs[2].plot([mag_cut[0], mag_cut[1]], [fwhm_estimated, fwhm_estimated],
                color="#22AA66", zorder=1,
                label=r"FWHM$_{\mathrm{estimated}}$" + f": {fwhm_estimated:.3f}")

    # Plot grid lines
    axs[2].hlines(np.arange(0, 15, 2), mag_cut[0], mag_cut[1],
                  colors="#EEEEEE", zorder=-1)

    axs[2].legend(loc=2)
    axs[2].set_xlim(mag_cut)
    axs[2].set_ylim([0, 15])
    axs[2].set_ylabel('FWHM [arcsec]')
    axs[2].minorticks_on()

    axs[2].set_xlabel(f"{filt}_AUTO [inst]")

    plt.subplots_adjust(left=0.14, right=0.98, top=0.98, bottom=0.06, hspace=0.1)

    plt.savefig(save_file)
    plt.close(fig)


###############################
# PSF photometry


def get_dophot_config(image_in, objects_out, config_file,
                      apercorr_max_aperture):
    """
    Returns the dophot tuneup file for a given S-PLUS image

    Parameters
    ----------
    image_in : str
        Location of S-PLUS image to run dophot
    objects_out : str
        Location of desired dophot output file
    config_file : str
        Location to save dophot tuneup file for this image
    apercorr_max_aperture : float
        Diameter [pixels] considered for the aperture correction

    Returns
    -------
    saves dophot tuneup file in the param:config_file location

    """

    # Load S-PLUS image
    head = fits.open(image_in)[0].header

    # Get image and catalog names
    image_name   = os.path.split(image_in)[1]
    objects_name = os.path.split(objects_out)[1]

    # Calculating dophot parameters
    # Reference: Javier Alonso - Private Communication

    FWHM = float(head['HIERARCH OAJ PRO FWHMMEAN']) / float(head['PIXSCALE'])

    SKY = float(head['HIERARCH OAJ QC NCMIDPT'])

    TEXPOSED = float(head['TEXPOSED']) / float(head['NCOMBINE'])

    SIGSKY = float(head['HIERARCH OAJ QC NCNOISE']) * TEXPOSED

    EPERDN = float(head['GAIN']) / TEXPOSED

    RDNOISE = 3.43 * np.sqrt(float(head['NCOMBINE']))

    TOP = float(head['SATURATE']) * TEXPOSED

    SCALEAPRADIUS = np.around((apercorr_max_aperture/2) / FWHM,3)

    # Generating config file
    config = (f"FWHM =     {FWHM}\n"
              f"SKY =      {SKY}\n"
              f"SIGSKY =   {SIGSKY}\n"
              f"EPERDN =   {EPERDN}\n"
              f"RDNOISE =  {RDNOISE}\n"
              f"TOP =      {TOP}\n"
              f"TEXPOSED = {TEXPOSED}\n"
              f"IMAGE_IN = '{image_name}'\n"
              f"OBJECTS_OUT = '{objects_name}'\n"
              "PARAMS_DEFAULT = paramdefault")

    # Saving config file
    with open(config_file, "w") as f:
        f.write(config)

def psf_flagstar(fitmag, fitsky, err_fitmag, max_err = 0.02, upper_limit = 0.5):
    """
    Create a star flag (1 classified as star, 0 not classified) for the dophot
    output catalog using the columns fitmag, fitsky and err_fitmag.

    Parameters
    ----------
    fitmag : np.array
        dophot catalog fitmag column
    fitsky : np.array
        dophot catalog fitsky column
    err_fitmag : np.array
        dophot catalog err_fitmag column
    max_err : float
        max value of err_fitmag selected for linear regression
    upper_limit : float
        value above linear regression limiting the star classification

    Returns
    -------
    np.array
        starflag array (1 classified as star, 0 not classified)
    """

    nrows = len(fitmag)

    # Create flag_star array
    flagstar = np.zeros(nrows)

    # select points for fit
    f0 = fitsky > 0
    ferr = err_fitmag < max_err

    y = np.log10(fitsky[f0 & ferr])
    x = fitmag[f0 & ferr]

    # Linear fit: log10(fitsky) = a * fitmag + b
    a, b = np.polyfit(x, y, 1)

    # Star classification
    selection = np.log10(fitsky[f0]) < (upper_limit + a*fitmag[f0] + b)

    flagstar[f0] = selection.astype(int)

    # Alse set points with fitsky < 0 as stars
    flagstar[~f0] = 1

    return flagstar.astype(int)


def format_dophot_catalog(catalog_in, catalog_out, image):
    """
    Formats dophot output catalog into an ascii table, adding RA, DEC columns
    and also classifing stars (column STAR_FLAG = 1)

    It's also necessary to input the location of the field's .fz
    image. The WCS data from the header is used to convert x, y coordinates to
    RA and DEC.

    Parameters
    ----------
    catalog_in : str
        Location of dophot .sum catalog
    catalog_out : str
        Desired location of the formated catalog
    image : str
        Location of S-PLUS field image

    Returns
    -------
    Saves formated catalog to the param:catalog_out location
    """

    dophot_column_names = ["Star_number", "xpos", "ypos", "fitmag",
                           "err_fitmag", "fitsky", "objtype", "chi", "apcorr"]

    dophot_data_types = {'Star_number': int, 'xpos': float, 'ypos': float,
                         'fitmag': float, 'err_fitmag': float, 'fitsky': float,
                         'objtype': int, 'chi': float, 'apcorr': float}

    cat_data = pd.read_csv(catalog_in,
                           skiprows = 3,
                           delim_whitespace = True,
                           names = dophot_column_names,
                           dtype = dophot_data_types)

    # Include RA and DEC
    x = cat_data.loc[:, 'xpos'].array
    y = cat_data.loc[:, 'ypos'].array

    # Extract field WCS from image header
    head = fits.open(image)[1].header
    coord_wcs = WCS(head)

    skycoords = pixel_to_skycoord(x, y, coord_wcs, origin=1)

    # Get ra and dec in degrees
    ra = np.array(skycoords.ra)
    dec = np.array(skycoords.dec)

    cat_data['RAJ2000'] = ra
    cat_data['DEJ2000'] = dec

    flagstar = psf_flagstar(fitmag = cat_data.loc[:,'fitmag'].values,
                            fitsky = cat_data.loc[:,'fitsky'].values,
                            err_fitmag = cat_data.loc[:, 'err_fitmag'].values)

    cat_data['FLAG_STAR'] = flagstar

    with open(catalog_out, 'w') as f:
        f.write("# ")
        cat_data.to_csv(f, index = False, sep = " ")


def plot_dophot_diagnostic(catalog, save_file, filt, mag_cut = (8, 22)):
    """
    Makes diagnostic plots of the photometry in a given DOPHOT output

    Parameters
    ----------
    catalog : str
        Location of SExtractor output catalog
    save_file : str
        Location to save plots
    filt : str
        Name of the photometric filter
    mag_cut : list
        Limiting magnitudes (min, max)

    Returns
    -------
    Saves diagnostic plots
    """

    psfcat = load_data(catalog)

    fig, axs = plt.subplots(2, figsize = [5,10])

    #############
    # Plot fitsky

    # Plot all points
    axs[0].scatter(psfcat['fitmag'], psfcat['fitsky'],
                   c="#AAAAAA", s=10, alpha=0.1)

    # Plot selection
    f = psfcat['FLAG_STAR'] == 1
    axs[0].scatter(psfcat['fitmag'][f], psfcat['fitsky'][f],
                   c="#2266FF", s=10, alpha=0.3,
                   label=f"FLAG_STAR = 1")

    # Plot grid lines
    axs[0].hlines(np.arange(0, 10000, 100), mag_cut[0], mag_cut[1],
                  colors="#EEEEEE", zorder=-1)

    axs[0].legend(loc=1)
    axs[0].set_xlim(mag_cut)
    axs[0].set_ylim([-50, 500])
    axs[0].set_ylabel('fitsky')
    axs[0].minorticks_on()

    #############
    # Plot fitmag

    # Plot all points
    axs[1].scatter(psfcat['fitmag'], psfcat['err_fitmag'],
                   c="#AAAAAA", s=10, alpha=0.1)

    # Plot selection
    f = psfcat['FLAG_STAR'] == 1
    axs[1].scatter(psfcat['fitmag'][f], psfcat['err_fitmag'][f],
                   c="#2266FF", s=10, alpha=0.3,
                   label=f"err_fitmag < 0.02")

    # Plot cut line
    axs[1].hlines(0.02, mag_cut[0], mag_cut[1],
                  colors="#2266FF", zorder=1)

    # Plot grid lines
    axs[1].hlines(np.arange(0, 0.2, 0.02), mag_cut[0], mag_cut[1],
                  colors="#EEEEEE", zorder=-1)

    axs[1].set_xlim(mag_cut)
    axs[1].set_ylim([0, 0.2])
    axs[1].set_ylabel('err_fitmag')
    axs[1].minorticks_on()

    axs[1].set_xlabel(f"{filt}_fitmag [inst]")

    plt.subplots_adjust(left=0.14, right=0.98, top=0.98, bottom=0.06, hspace=0.1)

    plt.savefig(save_file)
    plt.close(fig)

###############################
# Correction xy


def intersection_2lines(x1, y1, x2, y2, x3, y3, x4, y4):

    """
    Returns the intersection of line L1 defined by points (x1,y1), (x2,y2), and
    line L2 defined by points (x3,y3), (x4,y4)

    see https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    """

    D = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    x = ( (x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4) ) / D

    y = ( (x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4) ) / D

    return np.array([x, y])


def align_splus_xy(x, y, center = None, margin = 10):
    """
    Aligns S-PLUS X,Y coordinates by moving origin to bottom left vertice and
    rotating to fit x and y directions

    Parameters
    ----------
    x : array
        array of X_IMAGE values
    y : array
        array of Y_IMAGE values
    center : list
        center value in the format [xcenter, ycenter]. If None, center is
        calculated from the average x and y values
    margin : int
        margin, in pixels, added to the origin

    Returns
    -------
    array
        array of square vertices in the format:
         [[x_bottomleft,  y_bottomleft],
          [x_bottomright, y_bottomright],
          [x_topright,    y_topright],
          [x_topleft,     y_topleft]]

    """
    # Center coordinates
    if center is None:
        x0 = np.nanmean(x)
        y0 = np.nanmean(y)
    else:
        x0 = center[0]
        y0 = center[1]

    # Defining quadrants:   Q4 | Q3
    #                       -------
    #                       Q1 | Q2

    Q1 = (x < x0) & (y < y0)
    Q2 = (x > x0) & (y < y0)
    Q3 = (x > x0) & (y > y0)
    Q4 = (x < x0) & (y > y0)

    # Finding points in left and right sides and bottom

    x1l = x[Q1][ x[Q1] == np.nanmin(x[Q1]) ][0]  # x of left most point in Q1
    y1l = y[Q1][ x[Q1] == np.nanmin(x[Q1]) ][0]  # y of left most point in Q1

    x1b = x[Q1][ y[Q1] == np.nanmin(y[Q1]) ][0]
    y1b = y[Q1][ y[Q1] == np.nanmin(y[Q1]) ][0]

    x2r = x[Q2][ x[Q2] == np.nanmax(x[Q2]) ][0]
    y2r = y[Q2][ x[Q2] == np.nanmax(x[Q2]) ][0]

    x2b = x[Q2][ y[Q2] == np.nanmin(y[Q2]) ][0]
    y2b = y[Q2][ y[Q2] == np.nanmin(y[Q2]) ][0]

    x3r = x[Q3][ x[Q3] == np.nanmax(x[Q3]) ][0]
    y3r = y[Q3][ x[Q3] == np.nanmax(x[Q3]) ][0]

    x4l = x[Q4][ x[Q4] == np.nanmin(x[Q4]) ][0]
    y4l = y[Q4][ x[Q4] == np.nanmin(x[Q4]) ][0]

    # bottom-left vertice
    vbl = intersection_2lines(x1=x1b, y1=y1b, x2=x2b, y2=y2b,
                              x3=x1l, y3=y1l, x4=x4l, y4=y4l)

    # bottom-right vertice
    vbr = intersection_2lines(x1=x1b, y1=y1b, x2=x2b, y2=y2b,
                              x3=x3r, y3=y3r, x4=x2r, y4=y2r)

    # Bottom vector
    vb = vbr - vbl

    # Unit vector
    unit_vb = vb / np.sqrt(np.sum((vb**2)))

    # Angle
    dot_product = np.dot(unit_vb, np.array([1, 0]))
    angle = np.arccos(dot_product)

    # Move origin to bottom left vertice
    x_temp = x - vbl[0] - margin
    y_temp = y - vbl[1] - margin

    # Rotate to align
    x_align = x_temp * np.cos(angle) - y_temp * np.sin(angle)
    y_align = x_temp * np.sin(angle) + y_temp * np.cos(angle)

    return x_align, y_align


def apply_xy_correction(catalog, save_file, map_file, xbins, ybins):
    """
    Applies XY corrections to the S-PLUS photometry catalogs.

    Correction are applied to all fixed aperture, auto, petro and iso magnitudes
    and fluxes (if present in the catalogs).

    Two additional columns are created: X_ALIGN and Y_ALIGN, corresponding to
    normalized X_IMAGE and Y_IMAGE positions (origin moved to bottom left
    corner, and coordinates rotate to match X and Y axis).

    Parameters
    ----------
    catalog : str
        Location to the SExtractor photometry output catalog

    save_file : str
        Desired location to save the XY corrected catalog

    map_file : str
        Location of the xy correction map (must be numpy npy file)

    xbins : list
        xbins of the correction map (start, end, Nbins) [in pixels]

    ybins : list
        ybins of the correction map (start, end, Nbins) [in pixels]

    Returns
    -------
    Saves XY corrected catalog in the desired location (param:save_file)
    """

    cat = fits.open(catalog)
    cat_data = cat[1].data

    x = cat_data.columns['X_IMAGE'].array
    y = cat_data.columns['Y_IMAGE'].array

    # Normalize X and Y
    x_align, y_align = align_splus_xy(x, y)

    # Create new fits catalog with new columns
    corr_data = cat_data.columns

    corr_data += fits.Column(name='X_ALIGN',
                             format='1E',
                             array=x_align)

    corr_data += fits.Column(name='Y_ALIGN',
                             format='1E',
                             array=y_align)

    # Prepare bins
    xbins_grid = np.linspace(xbins[0], xbins[1], int(xbins[2]) + 1)
    ybins_grid = np.linspace(ybins[0], ybins[1], int(ybins[2]) + 1)

    xbins_id = np.array(range(int(xbins[2]) + 1))
    ybins_id = np.array(range(int(ybins[2]) + 1))

    # Load corrections
    corrections = np.load(map_file)

    # Apply corrections
    for k in range(len(cat_data)):
        x_source = x_align[k]
        y_source = y_align[k]

        # Get delta mag (if given on the correction map for this position)
        try:
            # Find ids of the bin that contains the source
            bin_source_i = xbins_id[xbins_grid <= x_source][-1]
            bin_source_j = ybins_id[ybins_grid <= y_source][-1]

            delta_mag = corrections[bin_source_i, bin_source_j]
            delta_flux_frac = 10.0 ** (-(delta_mag / 2.5))

        except IndexError:
            delta_mag = 0
            delta_flux_frac = 1

        try:
            if corr_data['MAG_AUTO'].array[k] != 99:
                corr_data['MAG_AUTO'].array[k] += delta_mag
            corr_data['FLUX_AUTO'].array[k] *= delta_flux_frac
        except KeyError:
            pass

        try:
            if corr_data['MAG_ISO'].array[k] != 99:
                corr_data['MAG_ISO'].array[k] += delta_mag
            corr_data['FLUX_ISO'].array[k] *= delta_flux_frac
        except KeyError:
            pass

        try:
            if corr_data['MAG_PETRO'].array[k] != 99:
                corr_data['MAG_PETRO'].array[k] += delta_mag
            corr_data['FLUX_PETRO'].array[k] *= delta_flux_frac
        except KeyError:
            pass

        try:
            f = corr_data['MAG_APER'].array[k] != 99
            corr_data['MAG_APER'].array[k][f] += delta_mag
            corr_data['FLUX_APER'].array[k] *= delta_flux_frac
        except KeyError:
            pass

    # Save corrected data to save_file fits catalog
    hdu = fits.BinTableHDU.from_columns(corr_data)
    hdu.writeto(save_file)


################################################################################
# Aperture correction

# Aperture Photometry Functions for the S-PLUS Collaboration
# Author: André Zamorano Vitorelli - andrezvitorelli@gmail.com
# 2020-07-07
# """
#
# Editions: Felipe Almeida-Fernandes - felipefer42@gmail.com
# 2021-05-26
# __license__ = "GPL"
# __version__ = "0.1"

def get_apertures_from_sexconf(sexconf):
    """
    Reads the PHOT_APERTURES parameter in the sexconf file

    Parameters
    ----------
    sexconf : str
        Location of sexconf file

    Returns
    -------
    np.ndarray
        list of apertures
    """

    with open(sexconf) as f:
        lines = f.readlines()

    for line in lines:
        # remove comment from line
        line = line.split("#")[0]

        # Get param name
        param = line.split()[0]

        # If param is "PHOT_APERTURES", return list of values
        if param == "PHOT_APERTURES":
            value = "".join(line.split()[1:])
            value = np.array(value.split(","), dtype = float)

            return value

    # If param "PHOT_APERTURES" is not found
    return None


def obtain_aperture_correction(catalog, filt, sexconf, save_file, aperture,
                               s2ncut, starcut, max_aperture = 72.72727,
                               mag_partition = 2, convergence_slope = 1e-2,
                               check_convergence = True, verbose = False):
    """
    Calculates the aperture correction from a certain "aperture" to the another
    aperture "max_aperture" (which must be big enought to represent the
    total emission of the source)

    Parameters
    ----------
    catalog : str
        Location of SExtractor output catalog with the measured fixed apertures
    filt : str
        Name of the filter
    sexconf : str
        Location of sexconfig file for this filter's photometry
    save_file : str
        Desired location to save calculated aperture corrections
    aperture : float
        Base aperture which will have the correction estimated, in pixels
    s2ncut : list
        Min and max values of signal-to-noise to consider
    starcut : float
        Min value of SExtractor CLASS_STAR to consider
    max_aperture : str
        The maximum aperture in pixels
    mag_partition : float
        out of the stars selected with criteria above, get the 1/mag_partition
        sample with lower magnitudes
    convergence_slope : str
        the slope of the growth curve at the maximum aperture
    check_convergence : bool
        use slope to evaluate the confidence in the correction
    verbose : bool
        print details of the process

    Returns
    -------
    Saves estimated aperture correction and bounds in 3 columns to save_file,
    identified by filters by line
    """

    sextractor_table = Table.read(catalog)

    if verbose:
        catalog_name = os.path.split(catalog)[1]
        print(f"Filter {filt}")
        print(f"Calculating aperture correction from table {catalog_name}")
        print(f"Total objects: {len(sextractor_table)}\n")

    # Get aperture list
    apertures_list = get_apertures_from_sexconf(sexconf)  # type: np.ndarray

    if apertures_list is None:
        raise ValueError(f"Could not find param PHOT_APERTURES in {sexconf}.")

    # Get base aperture ID (allowing a rounding error up to the third decimal)
    round_list = np.around(apertures_list, 3)
    round_aper = np.around(aperture, 3)
    aperture_id = np.where(round_list == round_aper)[0][0]

    # Apply selection criteria
    select, medianFWHM = star_selector(catalog = sextractor_table,
                                       s2ncut        = s2ncut,
                                       starcut       = starcut,
                                       mag_partition = mag_partition,
                                       verbose       = verbose)

    magnitude_corr_list = []
    # individual aperture corrections
    for star in select:
        mags = star['MAG_APER'] - star['MAG_APER'][aperture_id]
        magnitude_corr_list.append(mags)

    mincorr, mediancorr, maxcorr = np.percentile(magnitude_corr_list,
                                                 [16, 50, 84], axis=0)

    correction = np.nan
    correction_low = np.nan
    correction_up = np.nan
    final_radius = np.nan
    slope = np.nan

    for i in range(len(apertures_list)):
        if verbose:
            SNR = np.sqrt(mediancorr[i] ** 2 / (maxcorr[i] - mincorr[i]) ** 2)

            msg  = "Radius: {:.2f} single aper. ".format(apertures_list[i])
            msg += "correction: {:.4f} ".format(mediancorr[i])
            msg += "[{:.4f} - {:.4f}](CL68) ".format(mincorr[i], maxcorr[i])
            msg += "SNR: {}".format(SNR)

            print(msg)

        if apertures_list[i] <= max_aperture:

            correction     = mediancorr[i]
            correction_low = mincorr[i]
            correction_up  = maxcorr[i]
            final_radius   = apertures_list[i]

            # Check convergence
            j = len(apertures_list) - i
            if check_convergence and i > 2:
                slope_radii = apertures_list[-(j + 3):-j]
                slope_corrs = mediancorr[-(j + 3):-j]
                slope = linregress(slope_radii, slope_corrs)[0]

    if verbose:
        print((f"low-median-high: [{correction_low:.4f} "
               f"{correction:.4f} {correction_up:.4f}]"))

        print(f'Nearest aperture: {final_radius}')

        if check_convergence:
            print(f'Slope of last 3 apertures: {slope:.2e}\n')

    convergence = None

    if check_convergence:
        if abs(slope) > convergence_slope:
            convergence = "Not_converged"
            print((f'Warning: aperture correction is not stable at the selected'
                   f' aperture for filter {filt}. Slope: {slope:.2e}'))
        else:
            convergence = "Converged"

    # Write to file
    with open(save_file, 'a') as f:
        f.write(f'SPLUS_{filt} {correction} {correction_low} {correction_up}')

        if check_convergence:
            f.write(f' {convergence}')

        f.write('\n')

    del select


def star_selector(catalog, s2ncut = (30, 1000), starcut = 0.9,
                  mag_partition = 2, verbose = False):
    """
    Selects the stars for the aperture correction

    Parameters
    ----------
    catalog : astropy Table
        Loaded fits catalog as an astropy table
    s2ncut : list
        Min and max values of signal-to-noise to consider
    starcut : float
        Min value of SExtractor CLASS_STAR to consider
    mag_partition : float
        out of the stars selected with criteria above, get the 1/mag_partition
        sample with lower magnitudes
    verbose : bool
        print details of the process

    Returns
    -------
    astropy Table
        Selected stars data
    """

    # Calculate the s2n
    s2n = catalog['FLUX_AUTO'] / catalog['FLUXERR_AUTO']

    # Apply selection conditions
    conditions = ((catalog['CLASS_STAR'] > starcut) &
                  (s2n > s2ncut[0]) &
                  (s2n < s2ncut[1]) &
                  (catalog['FLAGS'] == 0))

    select = catalog[conditions]

    if verbose:
        print(f"Selected stars: {len(select)}")

    # Select well behaved FWHM
    inferior, medianFWHM, superior = np.percentile(select['FWHM_WORLD'],
                                                   [16, 50, 84])

    conditions2 = ((select['FWHM_WORLD'] > inferior) &
                   (select['FWHM_WORLD'] < superior))

    select = select[conditions2]

    if verbose:
        print(f"Median FWHM for field: {medianFWHM:.4f}")
        print(f"After FWHM cut: {len(select)}")

    # Brightest of the best:
    select.sort('MAG_AUTO')
    select = select[0:int(len(select) / mag_partition)]

    if verbose:
        print(f"After brightest 1/{mag_partition} cut: {len(select)}\n")

    return select, medianFWHM


def growth_curve(catalog, s2ncut = (30, 1000), starcut = 0.9,
                 mag_partition=2, verbose = False):
    """
    Calculates the growth curve (magnitude in radius K+1 - magnitude in
    radius K) for a filter in a field from a sextractor catalogue

    Parameters
    ----------
    catalog : astropy Table
        Loaded fits catalog as an astropy table
    s2ncut : list
        Min and max values of signal-to-noise to consider
    starcut : float
        Min value of SExtractor CLASS_STAR to consider
    mag_partition : float
        out of the stars selected with criteria above, get the 1/mag_partition
        sample with lower magnitudes
    verbose : bool
        print details of the process

    Returns
    -------
    np.ndarray
        numpy array of shape (5, len(aperture_radii)-1) containing, in order:
            lower bound of the 95% confidence region of the growth curve
            lower bound of the 68% confidence region of the growth curve
            median of the growth curve
            higher bound of the 68% confidence region of the growth curve
            higher bound of the 95% confidence region of the growth curve
    float
        median FWHM of stars
    int
        number of selected stars
    """

    sextractor_table = Table.read(catalog)

    select, medianFWHM = star_selector(catalog = sextractor_table,
                                       s2ncut        = s2ncut,
                                       starcut       = starcut,
                                       mag_partition = mag_partition,
                                       verbose       = verbose)

    mlist = []
    for star in select:
        mags = np.diff(star['MAG_APER'])
        mlist.append(mags)

    percentile = np.percentile(mlist, [2.5, 16, 50, 84, 97.5], axis=0)
    minmag2, minmag, medianmag, maxmag, maxmag2 = percentile

    result = np.array([minmag2, minmag, medianmag, maxmag, maxmag2])

    return result, medianFWHM, len(select)


def growth_curve_plotter(catalog, filt, sexconf, save_file, aperture,
                         max_aperture = 72.72727, starcut=.9, s2ncut=(30, 1000),
                         mag_partition=2, verbose = False):
    """
    Generates and plots the field's growth curve for a given filter

    Parameters
    ----------
    catalog : str
        Location of SExtractor output catalog with the measured fixed apertures
    filt : str
        Name of the filter
    sexconf : str
        Location of sexconfig file for this filter's photometry
    save_file : str
        Desired location to save the plot of the growth curve
    aperture : float
        Base aperture diameter (pixels) which will have the correction estimated
    max_aperture : str
        The maximum aperture diameter in pixels
    s2ncut : list
        Min and max values of signal-to-noise to consider
    starcut : float
        Min value of SExtractor CLASS_STAR to consider
    mag_partition : float
        out of the stars selected with criteria above, get the 1/mag_partition
        sample with lower magnitudes
    verbose : bool
        print details of the process


    Returns
    -------
    Saves plot of the growth curve
    """

    # Get aperture list
    # Diameters (in pixels)
    apertures_list = get_apertures_from_sexconf(sexconf)  # type: np.ndarray

    if apertures_list is None:
        raise ValueError(f"Could not find param PHOT_APERTURES in {sexconf}.")

    result, medianFWHM, starcount = growth_curve(catalog = catalog,
                                                 s2ncut  = s2ncut,
                                                 starcut = starcut,
                                                 mag_partition = mag_partition,
                                                 verbose = verbose)

    minmag2, minmag, medianmag, maxmag, maxmag2 = [x for x in result]

    diameter = [(a + b) / 2 for a, b in zip(apertures_list[:],
                                            apertures_list[1:])]

    # Plot growth curve
    plt.figure(figsize=(5, 4))

    maxy = 0.1
    miny = -0.5

    # medians
    plt.plot(diameter, medianmag, color='red')

    # CL68 & CL95
    plt.fill_between(diameter, minmag, maxmag, color='orange', alpha=0.7)
    plt.fill_between(diameter, minmag2, maxmag2, color='orange', alpha=0.3)

    # plot median FWHM
    plt.plot([medianFWHM, medianFWHM], [miny, maxy], color='darkslategray',
             label='Median FWHM')

    # plot aperture
    plt.plot([max_aperture, max_aperture], [miny, maxy], '-', color='purple',
             label="{} pix".format(max_aperture))

    # base aperture
    plt.plot([aperture, aperture], [miny, maxy], '-', color='blue',
             label=f'{aperture:.3f}-diameter')

    # region around zero
    plt.plot([0, max(diameter)], [0, 0], color='blue')
    plt.fill_between([0, max(diameter)], [-1e-2, -1e-2], [1e-2, 1e-2],
                     color='blue', alpha=0.3)

    # Plot parameters
    plt.ylim(miny, maxy)
    plt.xlim(0, max(diameter))

    # Labels
    plt.legend()
    plt.xlabel("Aperture Diameter (pix)")
    plt.ylabel("$m_{k+1} - m_{k}$")
    plt.title(f"Magnitude growth curve in {filt}, {starcount} stars")
    plt.savefig(save_file, bbox_inches='tight')
    plt.close()


def apply_aperture_correction(catalog,
                              filt,
                              sexconf,
                              aperture,
                              apercorr_file,
                              save_file,
                              aper_names = ('3', '6'),
                              aper_ids   = (2, 4)):

    """
    Applies aperture correction to SExtractor photometry.
    This function removes the APER column from SExtractor catalogs and adds the
    PStotal column and other desired apertures defined in aper_names and
    aper_ids

    Parameters
    ----------
    catalog : str
        Location of SExtractor photometry catalog
    filt : str
        Name of the filter
    sexconf : str
        SExtractor configuration file for this filter photometry
    aperture : float
        Base aperture to apply aperture correction
    apercorr_file : str
        Location of the aperture correction file
    save_file : str
        Desired location to save new catalog
    aper_names : list
        List of names of fixed apertures to keep in the catalog
    aper_ids : list
        List of ids of these fixed magnitudes in the SExconf aperture list

    Returns
    -------
    Saves new catalog with aperture corrected apertures (PStotal)

    """

    # Read catalog
    cat = fits.open(catalog)
    cat_data = cat[1].data

    # Read aper correction
    aper_corr_dict = zp_read(apercorr_file)

    # Create new fits catalog with new columns
    new_data = []

    aper_columns = ["MAG_APER",  "MAGERR_APER", "FLUX_APER", "FLUXERR_APER"]
    for col in cat_data.columns:
        if not col.name in aper_columns:
            new_data.append(col)

    # Add 3" and 6" columns
    for aper, k in zip(aper_names, aper_ids):
        for colname in aper_columns:
            col = cat_data.columns[colname]
            new_data.append(fits.Column(name=f'{colname}_{aper}',
                                        format='1E',
                                        array=col.array[:, k]))

    # Get aperture list
    apertures_list = get_apertures_from_sexconf(sexconf)  # type: np.ndarray

    if apertures_list is None:
        raise ValueError(f"Could not find param PHOT_APERTURES in {sexconf}.")

    # Get base aperture ID (allowing a rounding error up to the third decimal)
    round_list = np.around(apertures_list, 3)
    round_aper = np.around(aperture, 3)
    aper_id    = np.where(round_list == round_aper)[0][0]

    # Apply aperture correction
    aper_corr = aper_corr_dict[f"SPLUS_{filt}"]
    flux_corr = 10**(-aper_corr/2.5)

    col = cat_data.columns['MAG_APER'].array[:, aper_id]
    f = col != 99
    col[f] = col[f] + aper_corr
    new_data.append(fits.Column(name=f'MAG_PStotal',
                                format='1E',
                                array=col))

    col = cat_data.columns['MAGERR_APER'].array[:, aper_id]
    new_data.append(fits.Column(name=f'MAGERR_PStotal',
                                format='1E',
                                array=col))

    col = cat_data.columns['FLUX_APER'].array[:, aper_id] * flux_corr
    new_data.append(fits.Column(name=f'FLUX_PStotal',
                                format='1E',
                                array=col))

    col = cat_data.columns['FLUXERR_APER'].array[:, aper_id]
    new_data.append(fits.Column(name=f'FLUXERR_PStotal',
                                format='1E',
                                array=col))

    # Save corrected data to save_file fits catalog
    hdu = fits.BinTableHDU.from_columns(new_data)
    hdu.writeto(save_file)


################################################################################
# Master photometry

#############################################
# Extract photometry from SExtractor catalogs

def extract_sex_photometry(catalog, save_file, filt):
    """
    Loads a SExtractor catalog and extracts only the PStotal photometry,
    renaming the columns to the format used by the pipeline

    Parameters
    ----------
    catalog : str
        Location of SExtractor output fits catalog
    save_file : str
        Location to save catalog with photometry only
    filt : str
        Name of the catalog's filter

    Returns
    -------
    Saves file with only the photometry

    """

    photometry_data = []

    # Load data from filter catalog
    cat      = fits.open(catalog)
    cat_data = cat[1].data

    photometry_data.append(cat_data.columns['NUMBER'])

    photometry_data.append(cat_data.columns['ALPHA_J2000'])
    photometry_data[-1].name = 'RA'

    photometry_data.append(cat_data.columns['DELTA_J2000'])
    photometry_data[-1].name = 'DEC'

    photometry_data.append(cat_data.columns['X_IMAGE'])
    photometry_data[-1].name = 'X'

    photometry_data.append(cat_data.columns['Y_IMAGE'])
    photometry_data[-1].name = 'Y'

    photometry_data.append(cat_data.columns['MAG_PStotal'])
    photometry_data[-1].name = f'SPLUS_{filt}'

    photometry_data.append(cat_data.columns['MAGERR_PStotal'])
    photometry_data[-1].name = f'SPLUS_{filt}_err'

    photometry_data.append(cat_data.columns['CLASS_STAR'])
    photometry_data[-1].name = f'CLASS_STAR'

    # Generate HDU from columns
    hdu = fits.BinTableHDU.from_columns(photometry_data)

    # Save master HDU
    hdu.writeto(save_file)
    print('Created file %s' % save_file)


def extract_psf_photometry(catalog, save_file, filt):
    """
    Loads a DOPHOT catalog and extracts only the photometry, renaming the
    columns to the format used by the pipeline.

    Parameters
    ----------
    catalog : str
        Location of dophot output ascii catalog
    save_file : str
        Location to save catalog with photometry only
    filt : str
        Name of the catalog's filter

    Returns
    -------
    Saves file with only the photometry

    """

    photometry_data = []

    # Load data from filter catalog
    cat_data = pd.read_csv(catalog,
                           delim_whitespace=True,
                           escapechar = "#")

    # Get x,y coordinates
    x = cat_data.loc[:, 'xpos'].array
    y = cat_data.loc[:, 'ypos'].array

    # Get ra,dec coordinates
    ra = cat_data.loc[:, 'RAJ2000'].array
    dec = cat_data.loc[:, 'DEJ2000'].array

    # Add number
    col_array = cat_data.loc[:, ' Star_number'].array
    photometry_data.append(fits.Column(name=f'NUMBER',
                                       format='1J',
                                       array=col_array))

    # Add RA
    photometry_data.append(fits.Column(name=f'RA',
                                       format='1E',
                                       array=ra))

    # Add DEC
    photometry_data.append(fits.Column(name=f'DEC',
                                       format='1E',
                                       array=dec))

    # Add x
    photometry_data.append(fits.Column(name=f'X',
                                       format='1E',
                                       array=x))

    # Add y
    photometry_data.append(fits.Column(name=f'Y',
                                       format='1E',
                                       array=y))

    # Add mag
    col_array = cat_data.loc[:, 'fitmag'].array
    photometry_data.append(fits.Column(name=f'SPLUS_{filt}',
                                       format='1E',
                                       array=col_array))

    # Add mag error
    col_array = cat_data.loc[:, 'err_fitmag'].array
    photometry_data.append(fits.Column(name=f'SPLUS_{filt}_err',
                                       format='1E',
                                       array=col_array))

    # Add flag_star
    col_array = cat_data.loc[:, 'FLAG_STAR'].array
    photometry_data.append(fits.Column(name=f'CLASS_STAR',
                                       format='1E',
                                       array=col_array))

    # Generate HDU from columns
    hdu = fits.BinTableHDU.from_columns(photometry_data)

    # Save master HDU
    hdu.writeto(save_file)
    print('Created file %s' % save_file)


def format_master_photometry(catalog, save_file, filters):

    """
    Reads the previously created master catalog and formats it removing
    multiple columns and filling nan values with 99.

    RA, DEC, X, Y columns are selected from the reddest filter in which the
    source was detected

    Parameters
    ----------
    catalog : str
        Location of unformated master photometry file
    save_file : str
        Location to save formated master photometry file
    filters : sized
        List of filters, from bluest to reddest

    Returns
    -------
    Saves formated master photometry file
    """

    photometry_data = []

    # Load data from filter catalog
    cat      = fits.open(catalog)
    cat_data = cat[1].data

    N = cat_data.shape[0]

    number = range(1, N+1)

    ra  = np.full(N, np.nan)
    dec = np.full(N, np.nan)

    x = np.full(N, np.nan)
    y = np.full(N, np.nan)

    class_star = np.full(N, np.nan)

    # Add new number column to new fits catalog
    photometry_data.append(fits.Column(name   = 'NUMBER',
                                       format = '1J',
                                       array  = np.array(number)))

    # Iteratively fill coords and class_star
    for i in range(len(filters), 0, -1):
        ra_i = cat_data.columns[f'RA_{i}'].array
        ra[np.isnan(ra)] = ra_i[np.isnan(ra)]

        dec_i = cat_data.columns[f'DEC_{i}'].array
        dec[np.isnan(dec)] = dec_i[np.isnan(dec)]

        x_i = cat_data.columns[f'X_{i}'].array
        x[np.isnan(x)] = x_i[np.isnan(x)]

        y_i = cat_data.columns[f'Y_{i}'].array
        y[np.isnan(y)] = y_i[np.isnan(y)]

        class_star_i = cat_data.columns[f'CLASS_STAR_{i}'].array
        class_star[np.isnan(class_star)] = class_star_i[np.isnan(class_star)]

    # Add to new fits catalog
    photometry_data.append(fits.Column(name   = 'RAJ2000',
                                       format = '1E',
                                       array  = ra))

    photometry_data.append(fits.Column(name   = 'DEJ2000',
                                       format = '1E',
                                       array  = dec))

    photometry_data.append(fits.Column(name   = 'X',
                                       format = '1E',
                                       array  = x))

    photometry_data.append(fits.Column(name   = 'Y',
                                       format = '1E',
                                       array  = y))

    photometry_data.append(fits.Column(name   = 'CLASS_STAR',
                                       format = '1E',
                                       array  = class_star))

    # Ndetections
    ndet = np.zeros(N)

    # Add magnitudes
    for i in range(len(filters)):
        filt = filters[i]

        mag     = cat_data.columns[f'SPLUS_{filt}'].array
        mag_err = cat_data.columns[f'SPLUS_{filt}_err'].array

        # Add detections
        ndet[~np.isnan(mag)] += 1

        # Fill nan values
        mag[np.isnan(mag)] = 99
        mag_err[np.isnan(mag_err)] = 99

        # Add to new fits catalog
        photometry_data.append(fits.Column(name=f'SPLUS_{filt}',
                                           format='1E',
                                           array=mag))

        photometry_data.append(fits.Column(name=f'SPLUS_{filt}_err',
                                           format='1E',
                                           array=mag_err))

    # Count detections
    photometry_data.append(fits.Column(name=f'NDET',
                                       format='1I',
                                       array=ndet))
    # Generate HDU from columns
    hdu = fits.BinTableHDU.from_columns(photometry_data)

    # Save master HDU
    hdu.writeto(save_file)
    print('Created file %s' % save_file)


################################################################################
# Crossmatch


def download_vizier_catalog_for_splus_field(splus_image, vizier_catalog_id,
                                            columns, column_filters = None,
                                            pixscale = 0.55):
    """
    Downloads a catalog from vizier in the region covered by an splus_image

    Parameters
    ----------
    splus_image : str
        Location of the S-PLUS image .fz file
    vizier_catalog_id : str
        ID of the catalog in the vizier database
    columns: list
        List of columns to download
    column_filters: dictionary
        Column filters, see astroquery.Vizier documentation
    pixscale : float
        Pixel scale in arcsec/pixel. Only used if image has no PIXSCALE
        parameter in the header

    Returns
    -------
    astropy.table.table.Table
        Catalog obtained from the VIZIER database
    """

    v = Vizier()

    # Change row limit to get whole catalog
    v.ROW_LIMIT = -1

    # List of columns to download
    v.columns = columns

    if column_filters is not None:
        v.column_filters = column_filters

    # Extract field ra and dec from image header
    head = fits.open(splus_image)[1].header
    ra = head['CRVAL1']   # degrees
    dec = head['CRVAL2']  # degrees
    c = SkyCoord(ra=ra, dec=dec, unit=(u.deg, u.deg))

    try:
        width = head['NAXIS1'] * head['PIXSCALE'] / 3600.  # degrees
        height = head['NAXIS2'] * head['PIXSCALE'] / 3600.  # degrees

    except KeyError:
        warnings.warn(('No PIXSCALE value in image header. Using default value '
                      f'of {pixscale} for S-PLUS'))

        width = head['NAXIS1'] * pixscale / 3600.  # degrees
        height = head['NAXIS2'] * pixscale / 3600.  # degrees

    print(f"width: {width}")
    print(f"height: {height}")
    print(f"coord: {c}")
    print(f"cat_id: {vizier_catalog_id}")
    # Retrieve catalog data in the field
    query = v.query_region(c, width = width*u.deg, height = height*u.deg,
                           catalog = vizier_catalog_id)
    print(query)
    input()
    catalog = query[vizier_catalog_id]

    return catalog


def download_galex(image, save_file):
    """
    Downloads the GALEX DR6/7 catalog from the vizier database in the region
    covered by an splus image. Changes column names for the format used by the
    pipeline, deletes unnecessary columns and saves results to a fits file

    Parameters
    ----------
    image : str
        Location of the splus image (must be .fz)
    save_file : str
        Location to save the retrieved catalog (must be .fits)

    Returns
    -------
    Saves catalog in the desired location
    """

    # Vizier Table
    cat_id = "II/335/galex_ais"

    columns = ['Name', 'RAJ2000', 'DEJ2000', 'FUVmag', 'e_FUVmag', 'NUVmag',
               'e_NUVmag']

    # Download catalog
    catalog = download_vizier_catalog_for_splus_field(splus_image = image,
                                               vizier_catalog_id = cat_id,
                                               columns = columns)

    # Rename columns
    catalog.columns['Name'].name = 'GALEX_ID'
    catalog.columns['RAJ2000'].name = 'GALEX_RAJ2000'
    catalog.columns['DEJ2000'].name = 'GALEX_DEJ2000'
    catalog.columns['FUVmag'].name = 'GALEX_FUV'
    catalog.columns['e_FUVmag'].name = 'GALEX_FUV_err'
    catalog.columns['NUVmag'].name = 'GALEX_NUV'
    catalog.columns['e_NUVmag'].name = 'GALEX_NUV_err'

    # Truncate description (usually to big to save as fits)
    catalog.meta['description'] = catalog.meta['description'][:55]

    # Save table as fits
    catalog.write(save_file, overwrite = True)


def download_refcat2(image, save_file):

    """
    Downloads the ATLAS REFCAT2 catalog from the vizier database in the region
    covered by an splus image. Changes column names for the format used by the
    pipeline, deletes unnecessary columns and saves results to a fits file

    Parameters
    ----------
    image : str
        Location of the splus image (must be .fz)
    save_file : str
        Location to save the retrieved catalog (must be .fits)

    Returns
    -------
    Saves catalog in the desired location
    """

    # Vizier Table
    cat_id = "J/ApJ/867/105/refcat2"

    columns = ['RA_ICRS', 'DE_ICRS', 'pmRA', 'pmDE', 'Plx', 'gmag',
               'e_gmag', 'rmag', 'e_rmag', 'imag', 'e_imag', 'zmag', 'e_zmag',
               'gcontrib', 'rcontrib', 'icontrib', 'zcontrib']

    column_filters = {'Plx': '>0'}

    # Download catalog
    catalog = download_vizier_catalog_for_splus_field(splus_image = image,
                                               vizier_catalog_id = cat_id,
                                               columns = columns,
                                               column_filters = column_filters)

    ###############################################
    # Covert coordinates from EPOCH 2015.5 to J2000
    ra_icrs = catalog.columns['RA_ICRS']
    de_icrs = catalog.columns['DE_ICRS']
    pmra    = catalog.columns['pmRA']
    pmde    = catalog.columns['pmDE']
    plx     = np.array(catalog.columns['Plx'])

    c = SkyCoord(ra=ra_icrs, dec=de_icrs, frame='icrs',
                 pm_ra_cosdec= pmra, pm_dec = pmde,
                 distance = Distance(parallax=plx*u.mas, allow_negative=True),
                 obstime = Time(2015.5, format='jyear'))

    # Convert epoch from 2015.5 to J2000
    c_j2000 = c.apply_space_motion(Time(2000.0, format='jyear'))

    # Get RA and DEC
    ra = np.array(c_j2000.ra)
    de = np.array(c_j2000.dec)

    ##############################
    # Add RA and DEC J2000 columns
    catalog['REFCAT2_RAJ2000'] = ra
    catalog['REFCAT2_DEJ2000'] = de

    ################
    # Rename columns
    catalog.columns['gmag'].name = 'PS_G'
    catalog.columns['e_gmag'].name = 'PS_G_err'
    catalog.columns['rmag'].name = 'PS_R'
    catalog.columns['e_rmag'].name = 'PS_R_err'
    catalog.columns['imag'].name = 'PS_I'
    catalog.columns['e_imag'].name = 'PS_I_err'
    catalog.columns['zmag'].name = 'PS_Z'
    catalog.columns['e_zmag'].name = 'PS_Z_err'

    # Truncate description (usually to big to save as fits)
    catalog.meta['description'] = catalog.meta['description'][:55]

    ##############################
    # Remove unreliable magnitudes
    # (PS mag estimated from an insuficient number of references)
    f = np.full(len(ra), True)
    for mag in ['g', 'r', 'i', 'z']:
        contrib = np.array(catalog.columns[f'{mag}contrib'])
        f = f & (contrib != '00') & (contrib != '01')

    catalog = catalog[f]

    ####################
    # Save table as fits
    catalog.write(save_file, overwrite = True)


def download_ivezic(image, save_file):
    """
    Downloads the Ivezic catalog from the vizier database in the region
    covered by an splus image. Changes column names for the format used by the
    pipeline, deletes unnecessary columns and saves results to a fits file

    Parameters
    ----------
    image : str
        Location of the splus image (must be .fz)
    save_file : str
        Location to save the retrieved catalog (must be .fits)

    Returns
    -------
    Saves catalog in the desired location
    """

    # Vizier Table
    cat_id = "J/AJ/134/973/stdcat"

    columns = ['RAJ2000', 'DEJ2000', 'umag', 'e_umag', 'gmag', 'e_gmag',
               'rmag', 'e_rmag', 'imag', 'e_imag', 'zmag', 'e_zmag']

    # Download catalog
    catalog = download_vizier_catalog_for_splus_field(splus_image = image,
                                               vizier_catalog_id = cat_id,
                                               columns = columns)

    # Rename columns
    catalog.columns['RAJ2000'].name = 'IVEZIC_RAJ2000'
    catalog.columns['DEJ2000'].name = 'IVEZIC_DEJ2000'

    catalog.columns['umag'].name = 'SDSS_U'
    catalog.columns['e_umag'].name = 'SDSS_U_err'
    catalog.columns['gmag'].name = 'SDSS_G'
    catalog.columns['e_gmag'].name = 'SDSS_G_err'
    catalog.columns['rmag'].name = 'SDSS_R'
    catalog.columns['e_rmag'].name = 'SDSS_R_err'
    catalog.columns['imag'].name = 'SDSS_I'
    catalog.columns['e_imag'].name = 'SDSS_I_err'
    catalog.columns['zmag'].name = 'SDSS_Z'
    catalog.columns['e_zmag'].name = 'SDSS_Z_err'

    ###################
    # Remove nan values
    Nrows = np.array(catalog.columns['IVEZIC_RAJ2000']).shape[0]
    f = np.full(Nrows, True)

    for mag in ['U', 'G', 'R', 'I', 'Z']:
        f = f & (np.array(catalog.columns[f'SDSS_{mag}']) < 90)

    catalog = catalog[f]

    # Truncate description (usually to big to save as fits)
    catalog.meta['description'] = catalog.meta['description'][:55]

    # Save table as fits
    catalog.write(save_file, overwrite = True)


def download_sdss(image, save_file):
    """
    Downloads the SDSS DR12 catalog from the vizier database in the region
    covered by an splus image. Changes column names for the format used by the
    pipeline, deletes unnecessary columns and saves results to a fits file

    Parameters
    ----------
    image : str
        Location of the splus image (must be .fz)
    save_file : str
        Location to save the retrieved catalog (must be .fits)

    Returns
    -------
    Saves catalog in the desired location
    """

    # Vizier Table
    cat_id = "V/147/sdss12"

    columns = ['RA_ICRS', 'DE_ICRS', 'SDSS12', 'umag', 'e_umag', 'gmag',
               'e_gmag', 'rmag', 'e_rmag', 'imag', 'e_imag', 'zmag', 'e_zmag']

    column_filters = {'class': '=6'}

    # Download catalog
    catalog = download_vizier_catalog_for_splus_field(splus_image = image,
                                               vizier_catalog_id = cat_id,
                                               columns = columns,
                                               column_filters = column_filters)

    # Rename columns
    catalog.columns['RA_ICRS'].name = 'SDSS_RAJ2000'
    catalog.columns['DE_ICRS'].name = 'SDSS_DEJ2000'

    catalog.columns['umag'].name = 'SDSS_U'
    catalog.columns['e_umag'].name = 'SDSS_U_err'
    catalog.columns['gmag'].name = 'SDSS_G'
    catalog.columns['e_gmag'].name = 'SDSS_G_err'
    catalog.columns['rmag'].name = 'SDSS_R'
    catalog.columns['e_rmag'].name = 'SDSS_R_err'
    catalog.columns['imag'].name = 'SDSS_I'
    catalog.columns['e_imag'].name = 'SDSS_I_err'
    catalog.columns['zmag'].name = 'SDSS_Z'
    catalog.columns['e_zmag'].name = 'SDSS_Z_err'

    # Truncate description (usually to big to save as fits)
    catalog.meta['description'] = catalog.meta['description'][:55]

    # Save table as fits
    catalog.write(save_file, overwrite = True)


def download_gaia(image, save_file):
    """
    Downloads the Gaia EDR3 catalog from the vizier database in the region
    covered by an splus image. Changes column names for the format used by the
    pipeline, deletes unnecessary columns and saves results to a fits file

    Parameters
    ----------
    image : str
        Location of the splus image (must be .fz)
    save_file : str
        Location to save the retrieved catalog (must be .fits)

    Returns
    -------
    Saves catalog in the desired location
    """

    # Vizier Table
    cat_id = "I/350/gaiaedr3"

    columns = ['RA_ICRS', 'DE_ICRS', 'Source', 'Plx', 'pmRA', 'pmDE',
               'Gmag', 'e_Gmag', 'BPmag', 'e_BPmag', 'RPmag', 'e_RPmag']

    column_filters = {'Plx': '>0'}

    # Download catalog
    catalog = download_vizier_catalog_for_splus_field(splus_image = image,
                                               vizier_catalog_id = cat_id,
                                               columns = columns,
                                               column_filters = column_filters)

    ###############################################
    # Covert coordinates from EPOCH 2016 to J2000
    ra_icrs = catalog.columns['RA_ICRS']
    de_icrs = catalog.columns['DE_ICRS']
    pmra    = catalog.columns['pmRA']
    pmde    = catalog.columns['pmDE']
    plx     = np.array(catalog.columns['Plx'])

    c = SkyCoord(ra=ra_icrs, dec=de_icrs, frame='icrs',
                 pm_ra_cosdec= pmra, pm_dec = pmde,
                 distance = Distance(parallax=plx*u.mas, allow_negative=True),
                 obstime = Time(2016, format='jyear'))

    # Convert epoch from 2015.5 to J2000
    c_j2000 = c.apply_space_motion(Time(2000.0, format='jyear'))

    # Get RA and DEC
    ra = np.array(c_j2000.ra)
    de = np.array(c_j2000.dec)

    ##############################
    # Add RA and DEC J2000 columns
    catalog['GAIA_RAJ2000'] = ra
    catalog['GAIA_DEJ2000'] = de

    # Rename columns
    catalog.columns['Source'].name = 'GAIA_ID'

    catalog.columns['Gmag'].name = 'GAIA_G'
    catalog.columns['e_Gmag'].name = 'GAIA_G_err'
    catalog.columns['BPmag'].name = 'GAIA_BP'
    catalog.columns['e_BPmag'].name = 'GAIA_BP_err'
    catalog.columns['RPmag'].name = 'GAIA_RP'
    catalog.columns['e_RPmag'].name = 'GAIA_RP_err'

    # Truncate description (usually to big to save as fits)
    catalog.meta['description'] = catalog.meta['description'][:55]

    # Save table as fits
    catalog.write(save_file, overwrite = True)


def download_reference(image, reference, save_file):
    """
    General function to download a specific reference catalog

    Parameters
    ----------
    image : str
        Location of the splus image (must be .fz)
    reference : str
        Indiciates the reference catalog to download
    save_file : str
        Location to save the retrieved catalog (must be .fits)

    Returns
    -------
    Saves catalog in the desired location
    """

    if reference == 'GALEX':
        download_galex(image, save_file)

    elif reference == 'REFCAT2':
        download_refcat2(image, save_file)

    elif reference == 'IVEZIC':
        download_ivezic(image, save_file)

    elif reference == 'SDSS':
        download_sdss(image, save_file)

    elif reference == 'GAIA':
        download_gaia(image, save_file)

    else:
        raise ValueError((f"Reference {reference} is not supported. Currently "
                          "supported values are 'GALEX', 'REFCAT2', 'IVEZIC', "
                          "'SDSS', and 'GAIA'"))


def crossmatch_catalog_name(field, conf):
    """
    Generates the name of the S-PLUS/references crossmatched catalog taking
    into account the photometry mode and the reference catalog(s) used for
    calibration

    Parameters
    ----------
    field : str
        Name of the S-PLUS field
    conf : dict
        Dictionary loaded from the configuration file

    Returns
    -------
    str
        Name of the crossmatched catalog
    """

    calib_phot = conf['calibration_photometry']
    cmatch_name = f"{field}_SPLUS_{calib_phot}"

    nref = len(conf['reference_catalog'])
    for i in range(nref):
        cmatch_name += f"_{conf['reference_catalog'][i]}"

    cmatch_name += ".fits"

    return cmatch_name


################################################################################
# Extinction Correction

# http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php?mode=browse
_lambda_eff = {  'SPLUS_U': 3542.07, 'SPLUS_F378': 3783.69,
              'SPLUS_F395': 3940.17, 'SPLUS_F410': 4094.63,
              'SPLUS_F430': 4286.52,    'SPLUS_G': 4715.83,
              'SPLUS_F515': 5131.93,    'SPLUS_R': 6202.57,
              'SPLUS_F660': 6616.95,    'SPLUS_I': 7627.01,
              'SPLUS_F861': 8607.17,    'SPLUS_Z': 8913.47,
               'GALEX_FUV': 1549.02,  'GALEX_NUV': 2304.74,
                  'SDSS_U': 3608.04,     'SDSS_G': 4671.78,
                  'SDSS_R': 6141.12,     'SDSS_I': 7457.89,
                  'SDSS_Z': 8922.78,       'PS_G': 4810.88,
                    'PS_R': 4900.12,       'PS_I': 7503.68,
                    'PS_Z': 8668.56,    'GAIA_BP': 5035.75,
                  'GAIA_G': 5822.39,    'GAIA_RP': 7619.96,
                    'SM_U': 3498.15,       'SM_V': 3870.92,
                    'SM_G': 4968.46,       'SM_R': 6040.07,
                    'SM_I': 7712.95,       'SM_Z': 9091.50}


def correct_extinction_schlegel(catalog, save_file, ebv_maps_path,
                                filters_lambda=None):
    """
    Corrects ISM extinction in the given catalog using Schelegel EB-V maps

    Parameters
    ----------
    catalog : str
        Location of the catalog which will have exctinction corrected
    save_file : str
        Location of file to save the results
    ebv_maps_path : str
        Path to directory containing extinction maps
    filters_lambda : dict
        Dictionary with values of lambda eff for each filter to be corrected

    Returns
    -------
    Saves catalog with corrected extinctions
    """

    if filters_lambda is None:
        filters_lambda = _lambda_eff

    m = sfdmap.SFDMap(ebv_maps_path)

    # Reading Catalog data
    cat = fits.open(catalog)
    cat_data = cat[1].data

    ##############
    # Obtaining AV
    RA = cat_data['RAJ2000']
    DEC = cat_data['DEJ2000']

    EBV = m.ebv(RA, DEC)
    Av = EBV * 3.1

    ####################################
    # Correct extinction for each filter
    for filt in list(filters_lambda.keys()):
        if filt in cat_data.columns.names:

            l_eff = filters_lambda[filt]
            Alambda = Av * dust_laws.CCM(l_eff)

            not_nan = cat_data.columns[filt].array != 99
            cat_data.columns[filt].array[not_nan] -= Alambda[not_nan]

    # Save output data
    cat.writeto(save_file)
    print('Created file %s' % save_file)


def correct_extinction_gorski(catalog, save_file, ebv_maps_path,
                              filters_lambda=None):
    """
    Corrects ISM extinction in the given catalog using Gorski et al. 2020
    EB-V maps for the small and large magellanic clouds

    Parameters
    ----------
    catalog : str
        Location of the catalog which will have exctinction corrected
    save_file : str
        Location of file to save the results
    ebv_maps_path : str
        Path to directory containing extinction maps
    filters_lambda : dict
        Dictionary with values of lambda eff for each filter to be corrected

    Returns
    -------
    Saves catalog with corrected extinctions
    """

    # Add on a later date for proper calibration of the MCs
    # Extinction maps are already in the /stes/Resources/Extinction path
    if filters_lambda is None:
        filters_lambda = _lambda_eff

    # SMC and LMC grid coverage
    # Made by hand using topcat
    smc_polygon = Polygon([[13.398,-71.201], [20.481,-71.201], [22.029,-74.197],
                           [13.770,-74.272], [13.559,-74.693], [12.321,-74.569],
                           [12.222,-74.730], [11.627,-74.643], [11.553,-74.854],
                           [4.891,-74.817],  [5.708,-72.315],  [11.392,-72.377],
                           [11.516,-71.609], [13.299,-71.585]])

    lmc_polygon = Polygon([[68.89, -66.51], [79.10, -66.51], [79.08, -67.67],
                           [86.66, -67.71], [86.75, -68.25], [91.55, -68.32],
                           [91.74, -68.87], [93.52, -68.90], [94.82, -71.31],
                           [93.48, -71.43], [93.99, -73.08], [89.85, -73.15],
                           [89.79, -72.57], [84.21, -72.53], [84.16, -71.98],
                           [78.71, -71.93], [78.75, -71.38], [73.45, -71.38],
                           [73.49, -70.85], [66.78, -70.67]])

    # Reading Catalog data
    cat = fits.open(catalog)
    cat_data = cat[1].data

    ##################################
    # Choose between LMC and SMC grids

    RA = cat_data['RAJ2000']
    DEC = cat_data['DEJ2000']

    within_smc = np.full(len(RA), False)
    within_lmc = np.full(len(RA), False)

    # Checking if points are within lmc or smc
    for i in range(len(RA)):
        p = Point(RA[i], DEC[i])
        within_smc[i] = p.within(smc_polygon)
        within_lmc[i] = p.within(lmc_polygon)

    if within_smc.sum() > 0:
        grid = os.path.join(ebv_maps_path, 'Gorski_EBV_res3_smc.txt')

    elif within_lmc.sum() > 0:
        grid = os.path.join(ebv_maps_path, 'Gorski_EBV_res3_lmc.txt')

    else:
        raise ValueError("Cannot calibrate field using Gorski EBV maps")

    #################
    # Interpolate EBV

    ebv_map = pd.read_csv(grid, delim_whitespace=True, comment = "#",
                    names = ['RA', 'DEC', 'EBV', 'e_EBV', 'sigma_RC', 'N_RC'])

    print("Interpolating extinction map")
    ebv_interp = interp2d(ebv_map['RA'], ebv_map['DEC'], ebv_map['EBV'])

    # Get EB-V
    EBV = np.full(len(RA), np.nan)

    for i in range(len(RA)):
        EBV[i] = ebv_interp(RA[i],DEC[i])

    Av = EBV * 3.1

    ####################################
    # Correct extinction for each filter
    for filt in list(filters_lambda.keys()):
        if filt in cat_data.columns.names:
            l_eff = filters_lambda[filt]

            Alambda = Av * dust_laws.CCM(l_eff)

            not_nan = cat_data.columns[filt].array != 99
            cat_data.columns[filt].array[not_nan] -= Alambda[not_nan]

    # Save output data
    cat.writeto(save_file)
    print('Created file %s' % save_file)


def correct_extinction(catalog, save_file, correction,
                       filters_lambda=None, **kwargs):

    """
    General function to correct extinction using a specific map

    Parameters
    ----------
    catalog : str
        Location of the catalog which will have exctinction corrected
    save_file : str
        Location of file to save the results
    correction : str
        Which correction map should be applied: SCHLEIGEL, GORSKI
    filters_lambda : dict
        Dictionary with values of lambda eff for each filter to be corrected

    Returns
    -------
    Saves catalog with corrected extinctions
    """

    if filters_lambda is None:
        filters_lambda = _lambda_eff

    if correction.lower() == 'schlegel':
        correct_extinction_schlegel(catalog=catalog, save_file=save_file,
                                    filters_lambda=filters_lambda, **kwargs)

    elif correction.lower() == 'gorski':
        correct_extinction_gorski(catalog=catalog, save_file=save_file,
                                  filters_lambda=filters_lambda, **kwargs)

    else:
        raise ValueError(f"Extinction {correction} is not supported.")

################################################################################
# Calibration

# \todo ADD uncertainty estimation to the SED fitted zero-points


def zp_write(zp_dict, save_file, filters_list=None):
    """
    writes a .zp file

    Parameters
    ----------
    zp_dict : dict
        Dictionary of zero points (keys: filter name, value: filter zero-point)
    save_file : str
        Location to save the zp file
    filters_list : list
        List of filters to save zero-points. If None, all filters in zp_dict are
        saved

    Returns
    -------
    Saves a zp file
    """

    print('\nSaving results to file %s' % save_file)

    if filters_list is None:
        filters_list = zp_dict.keys()

    with open(save_file, 'w') as f:

        if type(filters_list) is str:
            f.write("{:s} {:.5f}\n".format(filters_list, zp_dict[filters_list]))

        else:
            for filt in filters_list:
                f.write("{:s} {:.5f}\n".format(filt, zp_dict[filt]))

    print('Results are saved in file %s' % save_file)


def zp_read(load_file, zp_col = 1):
    """
    Reads a .zp file
    Parameters
    ----------
    load_file : str
        Location of the .zp file
    zp_col : int
        Column where zero-point is saved

    Returns
    -------
    dict
        Dictionary of zero-points (keys: filter name, value: filter zero-point)
    """

    filters = np.genfromtxt(load_file, dtype=str, usecols=[0])
    ZPs = np.genfromtxt(load_file, dtype=float, usecols=[zp_col])

    zp_dict = {}

    try:
        for i in range(len(filters)):
            zp_dict[filters[i]] = ZPs[i]

    except TypeError:
        zp_dict[str(filters)] = float(ZPs)

    return zp_dict


def zp_add(zp_file_list, save_file, filters, inst_zp=None):
    """
    Adds the zero-points for the same filters in multiple .zp files

    Can also be used to combine multiple .zp files featuring different filters

    Parameters
    ----------
    zp_file_list : list
        List of .zp files to add
    save_file : str
        Location to save the resulting .zp file
    filters : list
        List of filters to add zps and save in the save_file
    inst_zp : float
        A zero-point value to be added for all filters. Default = None

    Returns
    -------
    Saves the resulting .zp file
    """

    zp_dict_sum = {}
    zp_dict_list = []

    for zp_file in zp_file_list:
        zp_dict_list.append(zp_read(zp_file))

    for filt in filters:
        zp_sum = 0
        for zp_dict in zp_dict_list:
            if filt in zp_dict.keys():
                zp_sum += zp_dict[filt]

        zp_dict_sum[filt] = zp_sum

        if inst_zp is not None:
            zp_dict_sum[filt] = zp_dict_sum[filt] + inst_zp

    zp_write(zp_dict=zp_dict_sum,
             save_file=save_file,
             filters_list=filters)


def calibration_suffix(conf):
    """
    Generates the suffix to apply to a given calibration configuration taking
    into account the photometry mode and the reference catalog(s) used for
    calibration

    Parameters
    ----------
    conf : dict
        Dictionary loaded from the configuration file

    Returns
    -------
    str
        Suffix to apply to calibration and catalogs for a given calibration
        configuration
    """

    # Photometry mode
    suffix = f"{conf['calibration_photometry']}_"

    # Reference catalogs
    for i in range(len(conf['reference_catalog'])):
        if i != 0:
            suffix += '+'

        suffix += f"{conf['reference_catalog'][i]}"

    return suffix


def sed_fitting(models, catalog, save_file, ref_mag_cols,
                pred_mag_cols = None):
    """

    Parameters
    ----------
    models : str
        Location of the model's file with synthetic SEDs convolved to the
        pipeline supported filters
    catalog : str
        Location of the catalog with the filters data to fit the SEDs
    save_file : str
        Location of the desired save file where model predicted magnitudes will
        be saved
    ref_mag_cols : list
        List of magnitudes used to fit the SEDs
    pred_mag_cols : list
        List of magnitudes predicted by the fitted SEDs. If none, the code
        predicts magnitudes for ref_mag_cols only.

    Returns
    -------
    Saves predicted magnitudes to the save_file location.
    """

    sf.get_model_mags(models_file   = models,
                      data_file     = catalog,
                      save_file     = save_file,
                      ref_mag_cols  = ref_mag_cols,
                      pred_mag_cols = pred_mag_cols)


def get_filter_zeropoint(obs_mag_array, model_mag_array, cut=(14,19)):
    """
    Estimate the zero point of a particular filter by comparing observed
    magnitudes and model predicted magnitudes.

    Parameters
    ----------
    obs_mag_array : np.array
        array of observed zero-points
    model_mag_array : np.array
        array of model predicted zero-points
    cut : list
        Interval [min,max] of magnitudes to be considered for the estimation
        of the zero-points

    Returns
    -------
    float
        The value of the zero-point
    """

    f = (model_mag_array >= cut[0]) & (model_mag_array <= cut[1])

    delta_array = model_mag_array[f] - obs_mag_array[f]

    delta_array = delta_array.values.reshape(-1, 1)

    kde_dens = KernelDensity(kernel='gaussian', bandwidth=0.05).fit(delta_array)

    # Transform to kde
    x = np.arange(-10, 10, 0.001)
    y = np.exp(kde_dens.score_samples(x.reshape(-1, 1)))

    # get mode
    mode = x[y == np.max(y)][0]

    return mode


def zp_estimate(catalog, save_file, filters_list, mag_cut=(14, 19)):
    """
    Obtain zero-points for a given catalog by comparing the observed and model
    predicted magnitudes in this catalog. Input catalog must be the output of
    sed_fitting.get_model_mags

    Parameters
    ----------
    catalog : str
        Location of the input catalog. Must be the output
        of sed_fitting.get_model_mags
    save_file : str
        Location to save the estimated zero-points
    filters_list : list
        List of filters to estimate the zero-points
    mag_cut : list
        Interval [min,max] of magnitudes to be considered for the estimation
        of the zero-points

    Returns
    -------
    Saves the zero-points in a .zp file
    """

    data = load_data(catalog)
    print("\n\nStarting to apply ZeroPoints\n\n")

    print("Obtaining zero point for magnitudes:")
    print(filters_list)

    print("Using {0} stars to estimate ZPs".format(data.shape[0]))

    # Estimating and applying ZP
    zp_dict = {}

    for filt in filters_list:
        print("\nEstimating ZP for mag {0}".format(filt))

        # Cut logg
        dwarfs = data.loc[:, 'logg'].values > 3

        obs_mag_array = data.loc[dwarfs, f"{filt}"]
        mod_mag_array = data.loc[dwarfs, f"{filt}_mod"]

        filt_zp = get_filter_zeropoint(obs_mag_array=obs_mag_array,
                                      model_mag_array=mod_mag_array,
                                      cut=mag_cut)

        zp_dict[filt] = filt_zp

        data.loc[:, f"{filt}"] = data.loc[:, f"{filt}"] + filt_zp

        print("{} ZP = {:.3f}".format(f"{filt}", filt_zp))

    # Saving data
    zp_write(zp_dict=zp_dict, save_file=save_file, filters_list=filters_list)


def zp_apply(catalog, save_file, zp_file, fmt = "ascii", zp_inst = None):
    """
    Applies the zero-points to the magnitudes catalog

    Parameters
    ----------
    catalog : str
        Location of the catalog
    save_file : str
        Location to save the catalog with zero-points applied
    zp_file : str
        Location to the .zp file with the zero-points
    fmt : str
        Output format
    zp_inst : float
        Constant zp to be added to all filters. Default = None

    Returns
    -------
    Saves new catalog with zero-points applied
    """

    ZPs = zp_read(zp_file)
    cat_data = load_data(catalog)

    # Apply Zero Points
    for filt in ZPs.keys():

        if zp_inst is None:
            zp_i = ZPs[filt]
        else:
            zp_i = ZPs[filt] + zp_inst

        no_nan = cat_data.loc[:, filt] != 99

        cat_data.loc[no_nan, filt] = cat_data.loc[no_nan, filt] + zp_i

    with open(catalog, 'r') as f:
        first_line = f.readline()

    if fmt == 'ascii':
        with open(save_file, 'w') as f:
            f.write(first_line)
            np.savetxt(f, cat_data, fmt='%.5f')

    elif fmt == 'fits':
        t = Table.from_pandas(cat_data)
        t.write(save_file)


def plot_zp_fitting(sed_fit_file, save_file, filt, mag_cut = (14, 19),
                    zp_file = None, label = 'mag_inst', color = "#2266ff"):

    """
    Makes a plot of the zero-point estimation process

    Parameters
    ----------
    sed_fit_file : str
        Location of the catalog with fitted and model-predicted magnitudes
    zp_file : str
        Location of the obtained zp file
    save_file : str
        Location to save the plot
    filt : str
        Name of the filter to plot
    mag_cut : list
        Limits of magnitudes [min,max] selected for zero-point estimation
    label : str
        Identify the step in the calibration process
    color : str
        Color of the points in the scatter plot and line of density plot

    Returns
    -------
    Saves the plot
    """

    ###########
    # Load data

    cat_data = load_data(sed_fit_file)

    # Remove 99
    data_selection = np.abs(cat_data.loc[:, filt] < 50)
    cat_data = cat_data[data_selection]

    ##############
    # Prepare data

    x = cat_data.loc[:, f'{filt}_mod']
    y = x - cat_data.loc[:, f'{filt}']

    dwarfs = cat_data.loc[:, 'logg'].values > 3
    selection = (x >= mag_cut[0]) & (x <= mag_cut[1]) & dwarfs

    ############################
    # Apply different estimators

    delta = y[selection]
    delta = delta.values.reshape(-1, 1)

    kde_dens = KernelDensity(kernel='gaussian', bandwidth=0.05).fit(delta)

    y_dens = np.arange(-10, 10, 0.001)
    x_dens = np.exp(kde_dens.score_samples(y_dens.reshape(-1, 1)))

    mode = y_dens[x_dens == np.max(x_dens)][0]

    mu = np.mean(y[selection])
    mu_robust = mean_robust(y[selection])

    ################
    # Make the plots

    fig = plt.figure(figsize=(8, 5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])

    ax1 = plt.subplot(gs[0])

    ax1.scatter(x[selection], y[selection],
                c=color, s=20, alpha=0.5, zorder=1)

    ax1.scatter(x[~selection], y[~selection],
                c=color, s=20, alpha=0.05, zorder=2)

    ax1.plot([mag_cut[0], mag_cut[1]], [mode, mode],
             color='#FF3219', linestyle='-', zorder=6)

    ####
    # Limits of the plot
    ####
    xlim = [mag_cut[0] - 2, mag_cut[1] + 4]
    ylim = [mode - 1.5, mode + 1.5]

    ax1.text(mag_cut[0] - 1.5, mode + 1.3, f"{filt}", fontsize=14)

    ax1.set_xlim(xlim)
    ax1.set_ylim(ylim)

    ax1.set_xlabel("mag_model")
    ax1.set_ylabel(f"mag_model - {label}")

    ###
    # Plot KDE distribution
    ###

    ax2 = plt.subplot(gs[1])

    ax2.plot(x_dens / np.max(x_dens), y_dens, zorder=3, color = color)

    if zp_file is not None:
        zp_data = zp_read(zp_file)
        zp = zp_data[filt]

        ax2.plot([0, 2], [zp, zp], color='#000000', linestyle='--',
                 zorder=3, label='zp: {:.4f}'.format(mode))

    ax2.plot([0, 2], [mode, mode], color='#FF3219', linestyle='-',
             zorder=2, label='mode: {:.4f}'.format(mode))

    ax2.plot([0, 2], [mu, mu], color='#1932FF', linestyle='--',
             zorder=1, label='mean: {:.4f}'.format(mu))

    ax2.plot([0, 2], [mu_robust, mu_robust], color='#19DD32', linestyle=':',
             zorder=1,
             label='mean_robust: {:.4f}'.format(mu_robust))

    ax2.set_xlim([0, 1.1])
    ax2.set_ylim(ylim)

    ax2.legend(fontsize=7)

    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)
    ax2.set_ylabel("Density")

    ############
    # Plot grids

    for i in np.arange(-10, 10, 0.5):

        ax1.plot([0, 30], [i, i],
                 color="#666666", alpha=0.3,
                 linewidth=0.5, zorder=-5)

        ax2.plot([0, 30], [i, i],
                 color="#666666", alpha=0.3,
                 linewidth=0.5, zorder=-5)

    for i in np.arange(-10, 10, 0.1):

        ax1.plot([0, 30], [i, i],
                 color="#666666", alpha=0.1,
                 linewidth=0.5, zorder=-5)

        ax2.plot([0, 30], [i, i],
                 color="#666666", alpha=0.1,
                 linewidth=0.5, zorder=-5)

    for i in np.arange(1, 30, 1):

        ax1.plot([i, i], [-10, 10],
                 color="#666666", linewidth=0.5,
                 alpha=0.1, zorder=-5)

    for i in np.arange(2, 30, 2):

        ax1.plot([i, i], [-10, 10],
                 color="#666666", linewidth=0.5,
                 alpha=0.3, zorder=-5)

    plt.subplots_adjust(top=0.98, left=0.1, right=0.98, wspace=0)

    plt.savefig(save_file)
    plt.clf()
    plt.close()


###########################
# Stellar Locus calibration

def zp_estimate_stlocus(catalog, save_file, stlocus_ref_cat,
                        filts_color_ref, filt_ref, filts_to_get_zp,
                        color_range, nbins, plot_path = None, field = None):

    """
    Applies the stellar locus technique to derive the zero-points of a list
    of filters yet to be calibrated.

    Parameters
    ----------
    catalog : str
        Location of the catalog with filter columns to be calibrated
    save_file : str
        Location of the .zp output file
    stlocus_ref_cat : str
        Location of the catalog used as the reference for the calibration
    filts_color_ref : list
        color filt1 - filt2 is calculated from the columns [filt1, filt2]
    filt_ref : str
        filter that completes the color in the y axis
    filts_to_get_zp : list
        List of filters to obtain zp using the stellar locus technique
    color_range : list
        x-axis color range considered in the zp fitting [min, max]
    nbins : int
        Number of bins to divide the color_range interval
    plot_path : str
        Location of the directory to save plots (can be None)
    field : str
        Name of the field (used only for the plots file names)

    Returns
    -------
    Saves a .zp file with the zero points and, optionally, saves plots of the
    process
    """

    # Load Reference and data
    reference = load_data(stlocus_ref_cat)
    cat_data = load_data(catalog)

    # define x axis => color = filt_x0 - filt_x1
    filt_x0 = filts_color_ref[0]
    filt_x1 = filts_color_ref[1]

    # Calculate colors from reference and from catalog to calibrate
    reference_x = reference.loc[:, filt_x0] - reference.loc[:, filt_x1]
    cat_data_x  = cat_data.loc[:, filt_x0] - cat_data.loc[:, filt_x1]

    zp_dict = {}

    bins = np.linspace(color_range[0], color_range[1], nbins)
    delta_bin = bins[1] - bins[0]

    # Obtain zero points
    for filt in filts_to_get_zp:
        print(f"Estimating ZP for filter {filt} using the stellar locus")

        delta_mag = []

        ####
        reference_bin_y_list = []
        data_bin_y_list = []
        ####

        # Remove mag = 99 or -99
        remove_bad_data = (cat_data.loc[:, filt].values != -99) & \
                          (cat_data.loc[:, filt].values != 99) & \
                          (cat_data.loc[:, filt_ref].values != -99) & \
                          (cat_data.loc[:, filt_ref].values != 99) & \
                          (cat_data.loc[:, filt_x0].values != -99) & \
                          (cat_data.loc[:, filt_x0].values != 99) & \
                          (cat_data.loc[:, filt_x1].values != -99) & \
                          (cat_data.loc[:, filt_x1].values != 99)

        for bin_i in bins[:-1]:

            reference_bin_cut = (reference_x >= bin_i) & \
                                (reference_x < bin_i + delta_bin)

            data_bin_cut = (cat_data_x >= bin_i) & \
                           (cat_data_x < bin_i + delta_bin) & \
                           remove_bad_data

            reference_bin_y = reference.loc[reference_bin_cut, filt] - \
                              reference.loc[reference_bin_cut, filt_ref]

            data_bin_y = cat_data.loc[data_bin_cut, filt] - \
                         cat_data.loc[data_bin_cut, filt_ref]

            mean_reference_bin_y = mean_robust(reference_bin_y)

            cut_outliers = (data_bin_y > -5) & (data_bin_y < 5)
            mean_data_bin_y = mean_robust(data_bin_y[cut_outliers], 0.5, 0.5)

            delta_mag.append(mean_reference_bin_y - mean_data_bin_y)

            ####
            reference_bin_y_list.append(mean_reference_bin_y)
            data_bin_y_list.append(mean_data_bin_y)
            ####

        # Calculate ZP
        delta_mag = np.array(delta_mag)

        reference_bin_y_list = np.array(reference_bin_y_list)
        data_bin_y_list = np.array(data_bin_y_list)

        # Get order to remove max and min values
        o = np.argsort(delta_mag)

        zp_dict[filt] = mean_robust(delta_mag[o][1:-1])
        print(f"{filt} ZP = {zp_dict[filt]:.3f}")

        #######
        save_fig_name = f"{field}_{filt}_stlocus.png"
        save_fig_file = os.path.join(plot_path, save_fig_name)

        if (plot_path is not None) and (not os.path.exists(save_fig_file)):

            x = np.array(bins[:-1]) + delta_bin/2

            plt.scatter(reference_x,
                        reference.loc[:, filt] - reference.loc[:, filt_ref],
                        zorder = 1, alpha = 0.02, color = "#444444")

            plt.scatter(x[o][1:-1], reference_bin_y_list[o][1:-1],
                        s = 100, c = "#000000", zorder = 3)

            plt.scatter(x[o][0], reference_bin_y_list[o][0],
                        s = 100, c = "#000000", marker = 'x', zorder = 3)

            plt.scatter(x[o][-1], reference_bin_y_list[o][-1],
                        s = 100, c = "#000000", marker = 'x', zorder = 3)

            plt.plot(x, reference_bin_y_list, color = "#000000", zorder = 4)

            x_data = cat_data_x[remove_bad_data]
            y_data = cat_data.loc[remove_bad_data, filt] - \
                     cat_data.loc[remove_bad_data, filt_ref]

            plt.scatter(x_data, y_data, c = "#AA8800", zorder=2, alpha=0.2)

            plt.scatter(x[o][1:-1], data_bin_y_list[o][1:-1],
                        s = 100, c = "#664400", zorder = 5)

            plt.scatter(x[o][0], data_bin_y_list[o][0],
                        s = 100, c = "#000000", marker = 'x', zorder = 5)

            plt.scatter(x[o][-1], data_bin_y_list[o][-1],
                        s = 100, c = "#000000", marker = 'x', zorder = 5)

            plt.plot(x, data_bin_y_list, color = "#664400", zorder = 6)

            ymax = np.max((np.max(reference_bin_y_list),
                          np.max(data_bin_y_list))) + 1
            ymin = np.min((np.min(reference_bin_y_list),
                          np.min(data_bin_y_list))) - 1

            plt.gca().set_xlabel(f"{filt_x0} - {filt_x1}")
            plt.gca().set_ylabel(f"{filt} - {filt_ref}")
            plt.gca().set_ylim((ymin, ymax))
            plt.gca().set_xlim(color_range)
            plt.savefig(save_fig_file)
            plt.clf()
            plt.close()
            #######

    # Write zero-points to .zp file
    zp_write(zp_dict=zp_dict,
             save_file=save_file,
             filters_list=filts_to_get_zp)


def zp_comparison(fields_zps, save_file, fields_list):
    """
    Creates a comparison file between two zero points calibrations for a list
    of fields

    Parameters
    ----------
    fields_zps : dict
        Dictionary formated as fields_zps[*field*] = [zp_file1, zp_file2],
        where zp_file corresponds to the .zp file of each calibration to
        compare
    fields_list : list
        List of filters. If None the list is taking from fields_zps.keys(),
        although in this case the order of the fields will be randomized
    save_file : str
        Location to save the resulting comparison file

    Returns
    -------
    Saves a .cat table with zero points from both calibrations and their
    differences
    """

    #########################################
    # Get list of filters from first .zp file
    field0   = list(fields_zps.keys())[0]
    zp_file0 = fields_zps[field0][0]

    filters = np.genfromtxt(zp_file0, dtype=str, usecols=[0])

    ##############################
    # Create comparison data frame
    if fields_list is None:
        fields = fields_zps.keys()
    else:
        fields = fields_list

    zp_data = pd.DataFrame()

    zp_data['field'] = fields
    for filt in filters:
        zp_data[f'zp_{filt}_1'] = np.full(len(fields), np.nan)
        zp_data[f'zp_{filt}_2'] = np.full(len(fields), np.nan)
        zp_data[f'zp_{filt}_diff'] = np.full(len(fields), np.nan)

    ############################
    # Fill comparison data frame
    for i in range(len(fields)):

        field = fields[i]
        try:
            zp1 = zp_read(fields_zps[field][0])
        except OSError:
            zp1 = None

        try:
            zp2 = zp_read(fields_zps[field][1])
        except OSError:
            zp2 = None

        for filt in filters:

            try:
                zp_data.loc[i, f'zp_{filt}_1'] = zp1[filt]
            except KeyError:
                pass
            except TypeError:
                pass

            try:
                zp_data.loc[i, f'zp_{filt}_2'] = zp2[filt]
            except KeyError:
                pass
            except TypeError:
                pass

            try:
                diff = zp1[filt] - zp2[filt]
                zp_data.loc[i, f'zp_{filt}_diff'] = np.around(diff, 5)
            except KeyError:
                pass
            except TypeError:
                pass

    #################
    # Save data frame
    with open(save_file, 'w') as f:
        f.write("# ")
        zp_data.to_csv(f, index = False, sep = " ")


def zp_fit_offsets(zp_comparison_file, save_file, filters):
    """
    fit offsets between the zero-points obtained from two different calibrations

    Parameters
    ----------
    zp_comparison_file : str
        Location of the .cat zero-point comparison catalog
        (output of func:zp_comparison)

    save_file : str
        Location to save offset zp file

    filters : list
        List of filters to estimate offsets

    Returns
    -------
    Saves .zp file with the offsets to be applied
    """

    offsets = {}
    zp_diff = load_data(zp_comparison_file)

    for filt in filters:
        diff_array = np.array(zp_diff[f'zp_{filt}_diff'])
        diff_array = diff_array.reshape(-1, 1)

        kde_dens = KernelDensity(kernel='gaussian', bandwidth=0.05)
        kde_dens = kde_dens.fit(diff_array)

        # Transform to kde
        x = np.arange(-1, 1, 0.001)
        y = np.exp(kde_dens.score_samples(x.reshape(-1, 1)))

        # get mode
        mode = x[y == np.max(y)][0]

        offsets[filt] = mode

    zp_write(zp_dict=offsets,
             save_file=save_file,
             filters_list=filters)