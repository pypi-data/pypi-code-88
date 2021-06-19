import os
import logging

from subprocess import call

from django.core.files.move import file_move_safe

from ...settings import (BACKUP_FILE_PREFIX,
                         EXCLUDED_MODELS,
                         BACKUP_DESTINATION_FOLDER,
                         DUMPDATA_JSON_FILENAME,
                         PUBLIC_ASSETS_FOLDERS,
                         PRIVATE_ASSETS_FOLDERS)

logger = logging.getLogger('django_project_backup.utils.filesystem')


def get_backup_name_by_path(path):
    return str(path).split(os.sep)[-1:][0]


# DB

def run_dumpdata_backup():
    excluded_models_string = ' -e '.join(EXCLUDED_MODELS)

    cmd = 'python manage.py dumpdata --indent=4 --natural-foreign -e {} > {}'.format(
               excluded_models_string,
               DUMPDATA_JSON_FILENAME)

    logger.debug('Running: {}'.format(cmd))

    exit_code = call(cmd, shell=True)

    return exit_code


def move_dumpdata_backup(now, compress=False):
    file_path = os.path.abspath(DUMPDATA_JSON_FILENAME)
    file_name = DUMPDATA_JSON_FILENAME

    if not os.path.exists(BACKUP_DESTINATION_FOLDER):
        os.mkdir(BACKUP_DESTINATION_FOLDER)

    new_file_path = os.path.join(BACKUP_DESTINATION_FOLDER, file_name)

    file_move_safe(file_path, new_file_path, allow_overwrite=True)


# assets

def move_assets_backup(file_name):
    file_path = os.path.abspath(os.path.join(file_name))

    if not os.path.exists(BACKUP_DESTINATION_FOLDER):
        os.mkdir(BACKUP_DESTINATION_FOLDER)

    new_file_path = os.path.join(BACKUP_DESTINATION_FOLDER, file_name)

    file_move_safe(file_path, new_file_path, allow_overwrite=True)


def run_public_assets_backup(now):
    for folder in PUBLIC_ASSETS_FOLDERS:
        public_backup_filename = '{}.{}.public.gz'.format(BACKUP_FILE_PREFIX, now)

        cmd = 'tar --exclude="{2}{0}media{0}filer_public_thumbnails" --exclude="{2}{0}static" -cvjf {1} {2}'.format(
            os.path.sep,
            public_backup_filename,
            os.path.abspath(folder))

        exit_code = call(cmd, shell=True)

        if exit_code == 0:
            move_assets_backup(public_backup_filename)

        return exit_code


def run_private_assets_backup(now):
    for folder in PRIVATE_ASSETS_FOLDERS:
        private_backup_filename = '{}.{}.private.gz'.format(BACKUP_FILE_PREFIX, now)

        cmd = 'tar -cvjf {1} {2}'.format(
            os.path.sep,
            private_backup_filename,
            os.path.abspath(folder))

        exit_code = call(cmd, shell=True)

        if exit_code == 0:
            move_assets_backup(private_backup_filename)

        return exit_code
