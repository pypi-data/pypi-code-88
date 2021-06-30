import sys
from zipfile import ZipFile
from biolib.biolib_logging import logger


def validate_zip_file(zip_file_path, app_path):
    try:
        zip_file = ZipFile(zip_file_path)
    except Exception as e:
        logger.error('App could not be zipped')
        raise e

    files = [filename.strip('/') for filename in zip_file.namelist()]

    # Check if .biolib folder is present
    if f'.biolib' in files and f'biolib' in files:
        logger.error('You provided both a biolib and a .biolib folder. Please only provide the .biolib folder')
        sys.exit(1)

    elif f'.biolib' in files:
        biolib_folder_path = f'.biolib'

    elif f'biolib' in files:
        logger.error('Your biolib folder appears to be called "biolib" - it must be called ".biolib".')
        sys.exit(1)

    else:
        logger.error(f'Could not find a .biolib folder in provided app folder {app_path}')
        sys.exit(1)

    # Check if the config file is present
    if f'{biolib_folder_path}/config.yml' in files:
        # TODO: Changed to make sense in CLI. Rewrite this check at some point
        pass

    elif f'{biolib_folder_path}/config.yaml' in files:
        logger.error('Your biolib config file has the .yaml file extension - it must be .yml')
        sys.exit(1)

    else:
        logger.error(
            f'Could not find yaml config file  \
                 Please provide a yaml file named config.yml in the .biolib folder'
        )
