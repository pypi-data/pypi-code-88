# -*- coding: utf-8 -*-

# ******************************************************************************
#                          S-PLUS CALIBRATION PIPELINE
#                                 pipeline.py
#             Runs all the steps of the S-PLUS calibration pipeline
# ******************************************************************************


"""
This scripts runs the steps of the calibration pipeline

--------------------------------------------------------------------------------
   INPUTS:
--------------------------------------------------------------------------------
All inputs are taken from the config_file

--------------------------------------------------------------------------------
   COMMENTS:
--------------------------------------------------------------------------------
User must not change anything in this code. Changes to choose which steps to
run should be made in the config_file

config_file.py
    run_steps        = [*list of stepś*]

    possible steps are:
        The following steps are necessary to complete the calibration
        'photometry_single': obtain aperture photometry in single mode
        'photometry_dual'  : obtain aperture photometry in dual mode
        'photometry_psf'   : obtain psf photometry
        'correction_xy'    : corrects XY position zero-points inhomogeneities
        'aper_corretion'   : applies aperture correction to fixed aperture

--------------------------------------------------------------------------------
   USAGE:
--------------------------------------------------------------------------------
$ python pipeline_final *field_list_file* *config_file*

the field_list_file should be an ascii file where each line is the name of one
field to calibrate.
----------------
"""

################################################################################
# Import external packages

import os
import sys

pipeline_path = os.path.split(__file__)[0]

sys.path.append(pipeline_path)

################################################################################
# Import spluscalib packages

import utils as ut

################################################################################
# Read parameters

print("""
************************************************************************
*                                                                      *
*                   Starting the calibration pipeline                  *
*                                                                      *
************************************************************************
""")

cwd = os.getcwd()

field_list_file = os.path.join(cwd, sys.argv[1])
conf_file = os.path.join(cwd, sys.argv[2])

pipeline_path = os.path.split(__file__)[0]

print(conf_file)
print("reading the configuration file")
conf = ut.pipeline_conf(conf_file)

################################################################################
# Create save path directory

ut.makedir(conf['save_path'])
ut.makedir(conf['run_path'])

logs_path = os.path.join(conf['save_path'], 'logs')
ut.makedir(logs_path)

################################################################################
# Initiate log file

log_file_name = os.path.join(logs_path, 'pipeline.log')
log_file_name = ut.gen_logfile_name(log_file_name)
log_file = os.path.join(conf['run_path'], log_file_name)

with open(log_file, "w") as log:
    log.write("")

################################################################################
# Reading parameters

print("\n\n")

ut.printlog("*********** Reading configuratrion file **********", log_file)

for param in list(conf.keys()):
    ut.printlog(f"{param}: {conf[param]}", log_file)

print("\n\n")

################################################################################
# Reading field list

ut.printlog("*********** Reading field list **********", log_file)

if '--onefield' in sys.argv:
    fields = [sys.argv[1]]
else:
    fields = ut.load_field_list(field_list_file)

ut.printlog(f"Running the pipeline for fields:", log_file)
ut.printlog(f"{fields}", log_file)

################################################################################
# Running pipeline for each field

for field in fields:

    ut.printlog(f"""
    ************************************************************************
    *                                                                      *
    *                Working on field {field:37}*
    *                                                                      *
    ************************************************************************
    """, log_file)

    #################
    # Make field path
    field_path = os.path.join(conf['run_path'], field)
    logs_path = os.path.join(field_path, 'logs')

    field_images_path = os.path.join(field_path, 'Images')

    if not os.path.exists(field_path):
        ut.makedir(field_path)
        ut.printlog(f"Created directory {field_path}.", log_file)

        ut.makedir(logs_path)
        ut.printlog(f"Created directory {logs_path}.", log_file)

        ut.makedir(field_images_path)
        ut.printlog(f"Created directory {field_images_path}.", log_file)

    else:
        ut.printlog(f"Directory {field_path} already exists.", log_file)

    print("")
    ###################
    # Prepare field log

    log_field_name = os.path.join(logs_path, f'{field}.log')
    log_field_name = ut.gen_logfile_name(log_field_name)
    log_field_file = os.path.join(conf['run_path'], log_field_name)

    with open(log_file, "w") as log:
        log.write("")

    # Make backup of config file
    cmd = f"cp {conf_file} {field_path}"
    ut.printlog(cmd, log_field_file)
    os.system(cmd)

    # Run steps

    ############################################################################
    # Copy fz images and unpack, if necessary

    run_photometry = 'photometry_single' in conf['run_steps']
    run_photometry = run_photometry or ('photometry_dual' in conf['run_steps'])
    run_photometry = run_photometry or ('photometry_psf' in conf['run_steps'])

    if run_photometry and not ('--nofits' in sys.argv):

        for filt in conf['filters']:
            image_name  = f'{field}_{filt}_swp.fz'
            image_db_fz = os.path.join(conf['path_to_images'], field,
                                       image_name)
            image_fz    = os.path.join(field_images_path, image_name)

            ##############################################
            # Copying fz from path_to_images to field path

            if not os.path.exists(image_fz):

                ut.printlog(f"Copying image {image_name}", log_field_file)

                cmd = f"cp {image_db_fz} {field_images_path}"
                ut.printlog(cmd, log_field_file)
                os.system(cmd)

                if conf['use_weight']:

                    weight_db_fz = image_db_fz.replace(".fz", "weight.fz")

                    cmd = f"cp {weight_db_fz} {field_images_path}"
                    ut.printlog(cmd, log_field_file)
                    os.system(cmd)

            else:
                ut.printlog(f"Image {image_fz} already exists",
                            log_field_file)

            #######################
            # Unpacking fits images

            image_fits = image_fz.replace(".fz", ".fits")

            if not os.path.exists(image_fits):

                ut.printlog(f"Unpacking image {image_fz}", log_field_file)
                ut.fz2fits(image_fz)

                if conf['use_weight']:
                    weight_fz = image_fz.replace(".fz", "weight.fz")
                    ut.printlog(f"Unpacking weight {weight_fz}",
                                log_field_file)
                    ut.fz2fits(weight_fz)

            else:
                ut.printlog(f"Image {image_fits} already exists",
                            log_field_file)

            print("")

    ############################################################################

    ############################################################################
    # Run the photometry

    if 'photometry_single' in conf['run_steps']:

        final_file = os.path.join(field_path, 'Photometry', 'single', 'master',
                                  f"{field}_master_photometry_only_single.fits")

        if not os.path.exists(final_file):
            script = os.path.join(pipeline_path,'steps','photometry_single.py')
            cmd = f'python3 {script} {field} {conf_file}'
            ut.printlog(cmd, log_field_file)
            os.system(cmd)

            print("\n\n")

    if 'photometry_dual' in conf['run_steps']:

        final_file = os.path.join(field_path, 'Photometry', 'dual', 'master',
                                  f"{field}_master_photometry_only_dual.fits")

        if not os.path.exists(final_file):
            script = os.path.join(pipeline_path, 'steps', 'photometry_dual.py')
            cmd = f'python3 {script} {field} {conf_file}'
            ut.printlog(cmd, log_field_file)
            os.system(cmd)

            print("\n\n")

    if 'photometry_psf' in conf['run_steps']:

        final_file = os.path.join(field_path, 'Photometry', 'psf', 'master',
                                  f"{field}_master_photometry_only_psf.fits")

        if not os.path.exists(final_file):
            script = os.path.join(pipeline_path, 'steps', 'photometry_psf.py')
            cmd = f'python3 {script} {field} {conf_file}'
            ut.printlog(cmd, log_field_file)
            os.system(cmd)

            print("\n\n")

    if 'correction_xy' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'correction_xy.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    if 'correction_aper' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'correction_aper.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    if run_photometry:

        script = os.path.join(pipeline_path, 'steps', 'photometry_master.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    if 'crossmatch' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'crossmatch.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    if 'calibration_external' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'calibration_external.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    if 'calibration_stloc' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'calibration_stloc.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    if 'calibration_internal' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'calibration_internal.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    # It only needs to check for calibration_external to know if any calibration
    # is being run.
    if 'calibration_external' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'calibration_finalzp.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")

    if 'calibration_catalog' in conf['run_steps']:

        script = os.path.join(pipeline_path, 'steps', 'calibration_catalog.py')
        cmd = f'python3 {script} {field} {conf_file}'
        ut.printlog(cmd, log_field_file)
        os.system(cmd)

        print("\n\n")
    ############################################################################

    ###################
    # Remove fits files

    if run_photometry and conf['remove_fits'] and not ('--nofits' in sys.argv):

        for filt in conf['filters']:
            image_name = f'{field}_{filt}_swp.fz'
            image_fz = os.path.join(field_images_path, image_name)
            image_fits = image_fz.replace(".fz", ".fits")

            # Only remove .fits if .fz exists:
            if os.path.exists(image_fz):

                ut.printlog(f"Removing image {image_fits}", log_field_file)

                cmd = f"rm {image_fits}"
                ut.printlog(cmd, log_field_file)
                os.system(cmd)

            if conf['use_weight']:

                weight_fz = image_fz.replace(".fz", "weight.fz")
                weight_fits = weight_fz.replace(".fz", ".fits")

                if os.path.exists(weight_fz):
                    ut.printlog(f"Removing weight {weight_fits}",
                                log_field_file)

                    cmd = f"rm {weight_fits}"
                    ut.printlog(cmd, log_field_file)
                    os.system(cmd)

    #########################
    # Move field to save_path

    if conf['save_path'] != conf['run_path']:
        cmd = f"mv {field_path} {conf['save_path']}"
        ut.printlog(cmd, log_field_file)

        os.system(cmd)