from django.core.management.base import BaseCommand

from ...tasks import untis_import_mysql_current_next_term


class Command(BaseCommand):
    def handle(self, *args, **options):
        untis_import_mysql_current_next_term.delay()
