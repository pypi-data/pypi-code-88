import os

from django.core.management.base import BaseCommand  # , CommandError
from django.utils import timezone

from ...utils.filesystem import run_dumpdata_backup, move_dumpdata_backup
from ...settings import DUMPDATA_JSON_FILENAME, BACKUP_DESTINATION_FOLDER


class Command(BaseCommand):
    help = 'Performs dumpdata JSON file backup'

    def add_arguments(self, parser):
        parser.add_argument(
            '--compress',
            action='store_true',
            help='Compress dump_data.json',
        )

    def handle(self, *args, **options):
        now = timezone.now().strftime('%Y_%m_%dT%H_%M')

        try:
            dump_all_filepath = os.path.abspath(os.path.join(BACKUP_DESTINATION_FOLDER,
                                                             DUMPDATA_JSON_FILENAME))
            exit_code = run_dumpdata_backup()

            if exit_code != 0:
                self.stdout.write(self.style.ERROR('Wrong exit code running manage.py dumpdata ({})'.format(exit_code)))
            else:
                self.stdout.write(
                    self.style.SUCCESS('Dumpdata backup done on "{}"'.format(os.path.abspath(dump_all_filepath))))

                move_dumpdata_backup(now, compress=options['compress'])

                self.stdout.write(
                    self.style.SUCCESS('Dumpdata backup moved into "{}"'.format(BACKUP_DESTINATION_FOLDER)))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Error executing dumpdata backup: {}'.format(e)))
            raise
