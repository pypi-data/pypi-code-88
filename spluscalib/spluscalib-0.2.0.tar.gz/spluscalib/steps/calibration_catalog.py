# -*- coding: utf-8 -*-

# ******************************************************************************
#                          S-PLUS CALIBRATION PIPELINE
#                             calibration_catalog.py
#            Applies the final zero-point to the photometry catalogs
# ******************************************************************************

"""
Generates photometric calibrated catalogs from the final zero-points and the
photometry output tables

The S-PLUS field is given as the first command line argument. Configurations
are set in the config file, given as the second command line argument.

--------------------------------------------------------------------------------
   FUNCTIONS:
--------------------------------------------------------------------------------
copy_splus_psf_inst_catalog()
apply_final_zero_points_to_psf()

--------------------------------------------------------------------------------
   COMMENTS:
--------------------------------------------------------------------------------
Ideally this script should only be run through the pipeline.py script.

Assumes that at least calibration_finalzp.py has already been run for this field

--------------------------------------------------------------------------------
   USAGE:
--------------------------------------------------------------------------------
$python3 calibration_catalog.py *field_name* *config_file*

----------------
"""

################################################################################
# Import external packages

import os
import sys

steps_path = os.path.split(__file__)[0]
pipeline_path = os.path.split(steps_path)[0]
spluscalib_path = os.path.split(pipeline_path)[0]

sys.path.append(spluscalib_path)

################################################################################
# Import spluscalib packages

from spluscalib import utils as ut

################################################################################
# Read parameters

field     = sys.argv[1]
conf_file = sys.argv[2]

conf = ut.pipeline_conf(conf_file)

################################################################################
# Get directories

field_path       = os.path.join(conf['run_path'], field)
crossmatch_path  = os.path.join(field_path, 'Crossmatch')

suffix = ut.calibration_suffix(conf)
calibration_path  = os.path.join(field_path, f'Calibration_{suffix}')

catalogs_path = os.path.join(calibration_path, 'catalogs')

photometry_path = os.path.join(field_path, 'Photometry')

psf_path         = os.path.join(photometry_path, 'psf')
psf_catalog_path = os.path.join(psf_path, 'catalogs')
psf_master_path  = os.path.join(psf_path, 'master')

log_path = os.path.join(calibration_path, 'logs')


################################################################################
# Initiate log file

ut.makedir(catalogs_path)
ut.makedir(log_path)

log_file_name = os.path.join(log_path, 'catalog.log')
log_file_name = ut.gen_logfile_name(log_file_name)
log_file = os.path.join(calibration_path, log_file_name)

with open(log_file, "w") as log:
    log.write("")

################################################################################
# Begin script

# ***************************************************
#    Copy splus PSF instrumental catalog
# ***************************************************


def copy_splus_psf_inst_catalog():

    """
    Copy S-PLUS PSF instrumental magnitudes to catalogs path
    """

    print("")
    ut.printlog(('********** '
                 'Copying S-PLUS PSF instrumental magnitudes catalog '
                 '**********'),
                 log_file)
    print("")

    catalog_name = f"{field}_master_photometry_only_psf.fits"
    catalog_file = os.path.join(psf_master_path, catalog_name)

    save_name = f'{field}_psf_inst.cat'
    save_file = os.path.join(catalogs_path, save_name)

    if not os.path.exists(save_file) or True:

        cmd = f"java -jar {conf['path_to_stilts']} tcopy "
        cmd += f"in={catalog_file} ifmt=fits "
        cmd += f"out={save_file} ofmt=ascii"
        ut.printlog(cmd, log_file)
        os.system(cmd)

    else:
        ut.printlog(f"Catalog {save_name} already exists", log_file)


if 'photometry_psf' in conf['run_steps']:
    copy_splus_psf_inst_catalog()


# ***************************************************
#    Apply final zero points to PSF inst catalog
# ***************************************************


def apply_final_zero_points_to_psf():

    """
    Applies final zero-points to psf mag_inst catalog
    """

    print("")
    ut.printlog(('********** '
                 'Applying final zero-points to PSF mag_inst catalog '
                 '**********'),
                 log_file)
    print("")

    catalog_name = f'{field}_psf_inst.cat'
    catalog_file = os.path.join(catalogs_path, catalog_name)

    zp_name = f"{field}_final.zp"
    zp_file = os.path.join(calibration_path, zp_name)

    save_name = f"{field}_psf_calibrated.cat"
    save_file = os.path.join(catalogs_path, save_name)

    if not os.path.exists(save_file) or True:
        ut.zp_apply(catalog   = catalog_file,
                    save_file = save_file,
                    zp_file   = zp_file,
                    fmt = 'ascii',
                    zp_inst = -conf['inst_zp'])

        ut.printlog(f"Created file {save_file}", log_file)

    else:
        ut.printlog(f"Catalog {save_name} already exists", log_file)


if 'photometry_psf' in conf['run_steps']:
    apply_final_zero_points_to_psf()
