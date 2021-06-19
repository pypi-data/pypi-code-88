import os

from django.conf import settings

SERIALIZATION_MODULE = 'dpb_couchdb_datastore'

_EXCLUDED_MODELS = [
    # 'migrations',
    'auth.permission',
    'contenttypes.contenttype',
]
EXCLUDED_MODELS = _EXCLUDED_MODELS + getattr(settings, 'DJANGO_PROJECT_BACKUP_EXCLUDED_MODELS', [])

COUCHDB_DATASTORE_URL = getattr(settings, 'DJANGO_PROJECT_BACKUP_COUCHDB_DATASTORE_URL', 'http://127.0.0.1:5984')
COUCHDB_DATASTORE_USER = getattr(settings, 'DJANGO_PROJECT_BACKUP_COUCHDB_DATASTORE_USER', 'admin')
COUCHDB_DATASTORE_PASSWORD = getattr(settings, 'DJANGO_PROJECT_BACKUP_COUCHDB_DATASTORE_PASSWORD', 'couchdb')
# couchdb db index
COUCHDB_DATASTORE_DATABASE_NAME = getattr(settings, 'DJANGO_PROJECT_BACKUP_COUCHDB_DATASTORE_DATABASE_NAME',
                                          'django_project_backup')

DUMPDATA_JSON_FILENAME = 'dump_all.json'
BACKUP_FILE_PREFIX = 'backup'

_PUBLIC_ASSETS_FOLDERS = ['media']
PUBLIC_ASSETS_FOLDERS = getattr(settings, 'DJANGO_PROJECT_BACKUP_PUBLIC_ASSETS_FOLDERS',
                                _PUBLIC_ASSETS_FOLDERS)
_PRIVATE_ASSETS_FOLDERS = []
PRIVATE_ASSETS_FOLDERS = getattr(settings, 'DJANGO_PROJECT_BACKUP_PRIVATE_ASSETS_FOLDERS',
                                _PRIVATE_ASSETS_FOLDERS)

_BACKUP_DESTINATION_FOLDER = os.path.abspath('backups')
BACKUP_DESTINATION_FOLDER = getattr(settings, 'DJANGO_PROJECT_BACKUP_DESTINATION_FOLDER',
                                    _BACKUP_DESTINATION_FOLDER)

_BACKUP_MODES = ('incremental', 'full')
BACKUP_MODE = getattr(settings, 'DJANGO_PROJECT_BACKUP_MODE', 'incremental')
if BACKUP_MODE not in _BACKUP_MODES:
    raise Exception('BACKUP_MODE "{}" not in {}'.format(BACKUP_MODE, _BACKUP_MODES))

REALTIME_BACKUP = getattr(settings, 'DJANGO_PROJECT_BACKUP_REALTIME', False)

DO_FAILSAFE_BACKUP = getattr(settings,
                            'DJANGO_PROJECT_BACKUP_DO_FAILSAFE_BACKUP',
                            True)
FAILSAFE_BACKUP_PATH = getattr(settings,
                               'DJANGO_PROJECT_BACKUP_FAILSAFE_BACKUP_PATH',
                               os.path.join(BACKUP_DESTINATION_FOLDER, 'failed'))
FAILSAFE_BACKUP_PATH_UPDATE = os.path.join(FAILSAFE_BACKUP_PATH, 'update')
FAILSAFE_BACKUP_PATH_DELETE = os.path.join(FAILSAFE_BACKUP_PATH, 'delete')
