import sys
import os

from django.apps import AppConfig


class DjangoProjectBackupConfig(AppConfig):
    name = 'django_project_backup'
    verbose_name = 'Django Project Backup'
    excluded_management_commands = ('migrate', 'flush', 'dpb_couchdb_loaddata')

    def ready(self):
        from .settings import REALTIME_BACKUP

        if REALTIME_BACKUP:
            # disabled while running django "migrate" and "flush" commands
            load_signals = True
            for c in self.excluded_management_commands:
                if c in sys.argv:
                    load_signals = False
                    break
            if load_signals:
                try:
                    from . import signals  # noqa F401

                    # create failsafe backup folders
                    from .settings import FAILSAFE_BACKUP_PATH, FAILSAFE_BACKUP_PATH_UPDATE, FAILSAFE_BACKUP_PATH_DELETE

                    if not os.path.exists(FAILSAFE_BACKUP_PATH):
                        os.mkdir(FAILSAFE_BACKUP_PATH)
                    if not os.path.exists(FAILSAFE_BACKUP_PATH_UPDATE):
                        os.mkdir(FAILSAFE_BACKUP_PATH_UPDATE)
                    if not os.path.exists(FAILSAFE_BACKUP_PATH_DELETE):
                        os.mkdir(FAILSAFE_BACKUP_PATH_DELETE)

                except ImportError:
                    pass
