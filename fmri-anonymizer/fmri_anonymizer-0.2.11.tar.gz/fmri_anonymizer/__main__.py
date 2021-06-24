import argparse
import traceback

import logging
import json
import nibabel
import numpy as np
import os
import pydeface.utils as pdu
import SimpleITK as sitk
import time

from alive_progress import alive_bar
from ttictoc import Timer
from fmri_anonymizer.directory_replicator import replicate_structure
from fmri_anonymizer.file_searcher import walk_through
from fmri_anonymizer.deidentifier import de_identifier

from nipype.interfaces.dcm2nii import Dcm2niix

__author__ = "Hugo Angulo"
__copyright__ = "Copyright 2021, CaosLab"
__credits__ = ["Hugo Angulo"]
__license__ = "MIT"
__version__ = "0.2.11"
__maintainer__ = "Hugo Angulo"
__email__ = "hugoanda@andrew.cmu.edu"
__status__ = "Production"


def str2bool(arg):
    if isinstance(arg, bool):
        return arg
    if arg.lower() in ('YES', 'Yes', 'yes', 'Y', 'y', 'TRUE', 'True', 'true', 'T', 't', '1', ' '):
        return True
    elif arg.lower in ('NO', 'No', 'no', 'N', 'n', 'FALSE', 'False', 'false', 'F', 'f', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value not recognized.')


def get_parser():
    """
    This is the parser for the arguments coming from STDIN. It parses all the input.
    :return: parser
    """

    docstr = ("""Example:
                 python -m fmri_anonymizer -i <root_input_path> -d <flag_for_dicoms> -n <flag_for_nifti> 
                 -a <flag_for_anonymization> -f <flag_for_defacing> -o <output_path>""")
    epilog = (f"This is a wrapper project created to de-identify DICOM and NIFTI files. Also, (if you want) it can \n"
              f"perform defacing on the MRI data.\n"
              f"It uses the best-effort approach. So, don't take for granted that all the files had been \n"
              f"de-identified and/or defaced. Please verify some of the files that were problematic or were detected \n"
              f"as an error during the process. You will find the log file with all of this information \n"
              f"in your current working directory. \n"
              f"Powered by: CAOsLab @ CMU \n"
              f"Author: {__author__} \n"
              f"Email: {__email__}")
    parser = argparse.ArgumentParser(prog='fmri_anonymizer', description=docstr, epilog=epilog, allow_abbrev=False,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-i', '--input', type=str, help='Path where all the DICOM files can be found.',
                        required=True)
    parser.add_argument('-d', '--dicom', type=str2bool, nargs='?', help='Flag to enable DICOM files discovery.',
                        const=True, default=False, required=True)
    parser.add_argument('-n', '--nifti', type=str2bool, nargs='?', help='Flag to enable NIFTI files discovery',
                        const=True, default=False, required=False)
    parser.add_argument('-a', '--anonymize', type=str2bool, nargs='?', help='Flag to enable PHI metadata scrubbing.',
                        const=True, default=True, required=True)
    parser.add_argument('-f', '--deface', type=str2bool, nargs='?', help='Flag to enable defacing on MRI data',
                        const=True, default=False, required=False)
    parser.add_argument('-o', '--output', type=str, help='Folder to put the converted files.',
                        required=True)
    return parser


def main(argv=None):
    # This section adds logging capabilities to this script.
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - PID[%(process)d] - [%(levelname)s]: %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_log = "fmri_anonymizer" + time.strftime("%Y-%m-%d__%H_%M_%S") + ".log"
    file_handler = logging.FileHandler(file_log)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    dicom_formats = ['.dcm', '.ima', '.IMA']
    nifti_formats = ['nii', 'nii.gz']
    t = Timer()
    t.start()
    parser = get_parser()
    args = parser.parse_args(argv)
    input_path = args.input
    output_path = args.output
    dcm_flag = args.dicom
    nii_flag = args.nifti
    deid_flag = args.anonymize
    deface_flag = args.deface
    dcm_files = list()
    nii_files = list()

    # Defining some variables
    current_path = os.path.abspath(os.path.dirname(__file__))

    if not dcm_flag and not nii_flag:
        logger.info(f'You have not enabled DICOM and/or NIFTI files recognition. You have to enable one of them.')
        return None
    if not os.path.isdir(input_path):
        logger.info(f'The input folder does not exists. Please try again with the proper root folder.')
        return None
    if not deid_flag and not deface_flag:
        logger.info(f'You have not enabled the de-identification nor the defacing.\n Process finished!')
        return None
    logger.info(f'Starting the process...')
    logger.info(f'Creating a replica folder structure of the input in the output path...')
    # This has to create a replica of the input in the output
    directory_map = replicate_structure(input_path=input_path, output_path=output_path)

    # We have to look for dicom and or nifti files
    if dcm_flag:
        logger.info(f'Searching DICOM files...')
        dcm_files = walk_through(input_path, '.dcm', '.ima', '.IMA')
        logger.info(f'Total dicom files discovered: {len(dcm_files)}')

    if nii_flag:
        logger.info(f'Searching NIFTI files...')
        nii_files = walk_through(input_path, 'nii', 'nii.gz')
        logger.info(f'Total NIFTI files discovered: {len(nii_files)}')

    dcm_folders = dict()
    if deid_flag:
        logger.info(f'Now, the system will de-identify all the files found...')
        dcm_cleaned = list()
        if dcm_files.__len__() > 0:
            dcm_recipe = os.path.join(current_path, "util/deid.dicom")
            with alive_bar(len(dcm_files)) as bar:
                for dcm_file in dcm_files:
                    _path, _file = os.path.split(dcm_file)
                    if directory_map[_path] not in dcm_folders:
                        list_cleaned, percentage_clean = de_identifier(input_folder=_path, recipe_file=dcm_recipe,
                                                                       output_folder=directory_map[_path])
                        dcm_cleaned.append(list_cleaned)
                        dcm_folders[directory_map[_path]] = True
                        logger.info(f'The current directory has been de-identified {percentage_clean:.2f}%')
                    bar()

    logger.info(f'The De-Identification process is done!')
    if deface_flag:
        # TODO: Transform all the DICOM cleaned into nifti files.
        nii_de_identified = dict()
        nii_defaced = dict()
        converter = Dcm2niix()
        converter.inputs.compression = 5

        for k, v in dcm_folders.items():
            try:
                converter.inputs.source_dir = k
                converter.inputs.output_dir = k
                converter.run()
            except:
                logger.error(f'An error has been detected while transforming the dcm files in: {k}')
                traceback.print_exc()
                pass
            nii_de_identified[k] = walk_through(k, 'nii', 'nii.gz')
            if len(nii_de_identified[k]) > 0:
                for nifti in nii_de_identified[k]:
                    if nifti.endswith(tuple(nifti_formats)):
                        nii_defaced[nifti] = False
        '''
        Deface the niftis.
        '''
        for k, v in nii_de_identified.items():
            for each in v:
                try:
                    pdu.deface_image(infile=each, forcecleanup=True, force=True)
                    pdu.cleanup_files()
                    if each in nii_defaced:
                        nii_defaced[each] = True
                except:
                    logger.error(f'An error has been detected while defacing the file: {v}')
                    traceback.print_exc()
                    pass
        try:
            logger.info(f'Percentage files defaced: {sum(nii_defaced.values()) / len(nii_defaced):.3f}%')
        except:
            logger.error(f'An error has been found while calculating the total number of defaced items.')
            traceback.print_stack()
        logger.info(f'The defacing process has finished!')

        '''
        Here goes the section related to transforming the nifti defaced into dicoms again.
        '''
        logger.info('Starting transformation back to DICOM from NIFTI defaced!')
        logger.info(f'Finding defaced NIFTI files...')
        nifti_defaced = walk_through(output_path, 'nii', 'nii.gz')
        _tmp_nifti = [nifti for nifti in nifti_defaced]
        logger.info(f'Elements found: {len(nifti_defaced)}')
        nifti_defaced = list(filter(lambda each: 'defaced' in each, nifti_defaced))
        logger.info(f'Total defaced NIFTI files discovered: {len(nifti_defaced)}')
        '''
        Here, we proceed to get only the nifti files that do not contain the 'defaced' keyword.
        '''
        _to_remove = np.setdiff1d(_tmp_nifti, nifti_defaced)
        for _nifti in _to_remove:
            if os.path.isfile(_nifti):
                os.remove(_nifti)
        '''
        Here is the section to create all the DICOM.
        '''
        writer = sitk.ImageFileWriter()
        for k in nifti_defaced:
            nifti_image = nibabel.load(k)
            nifti_data = nifti_image.get_fdata()
            number_slices = nifti_data.shape[3]
            logger.info(f'Path of the file to transform: {k}')
            logger.info(f'Number of slices detected: {number_slices}')
            path, filename = os.path.split(k)
            # Here, remove all the current DICOM files
            dcm_files_anon = walk_through(path, 'dcm')
            logger.info(f'Now removing initial dicom files found in the path: {path}')
            logger.info(f'Number of files to remove: {len(dcm_files)}')
            logger.info(f'Removing now...')
            with alive_bar(len(dcm_files_anon)) as bar:
                for each in dcm_files_anon:
                    os.remove(each)
                    bar()
            # Getting all the headers for the DCM
            json_meta = walk_through(path, 'json')
            with open(json_meta[0]) as f:
                metadata = json.load(f)
            with alive_bar(number_slices) as bar:
                for slice in range(number_slices):
                    dicom_filename = path + '/' + filename.split('.nii.gz')[0] + '_' + f'{slice + 1:04}' + '.dcm'
                    logger.info(f'File to write: {dicom_filename}')
                    filtered_image = sitk.GetImageFromArray(
                        np.swapaxes(nifti_data[:, :, :, slice], 0, 2).astype(np.uint16))
                    for k, v in metadata.items():
                        filtered_image.SetMetaData(str(k), str(v))
                    writer.SetFileName(dicom_filename)
                    writer.Execute(filtered_image)
                    logger.info(f'File written!')
                    bar()

    logger.info(f'Process finished. Time elapsed: {t.stop():.6f}s')


if __name__ == '__main__':
    main()
