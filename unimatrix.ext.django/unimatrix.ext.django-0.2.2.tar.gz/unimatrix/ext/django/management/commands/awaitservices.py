"""Blocks until all services required by the application are available."""
#pylint: disable=undefined-loop-variable
import logging
import time

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Exposes a public API for the Django command framework to run the
    ``awaitservices`` command.
    """
    help = "Waits for services to become ready."
    logger = logging.getLogger('django')
    default_interval = 6.0
    max_attempts = 100

    def handle(self, *args, **options): #pylint: disable=unused-argument
        """Called when the ``awaitservices`` command is issued through
        ``manage.py``.
        """
        self.await_databases()

    def await_databases(self, interval=5.0):
        """Blocks until all databases are available.

        Args:
            interval (:obj:`float`): specifies the interval between checks,
                in seconds.

        Returns:
            :obj:`NoneType`
        """
        attempts = 0
        awaiting = {str(x) for x in connections}
        connected = set()
        while awaiting != connected:
            attempts += 1
            for alias in connections:
                connection = connections[alias]
                try:
                    cursor = connection.cursor()
                except OperationalError as exc:
                    msg = str.split(exc.args[0], '\n')[0]
                    self.logger.error(
                        "Database connection '%s' not ready (%s)",
                        alias, msg
                    )
                    continue
                self.logger.info("Database connection '%s' is operational",
                    alias)
                connected.add(alias)

            if attempts > self.max_attempts:
                raise CommandError("Connection '%s' not available after %s attempts"
                    % (alias, self.max_attempts))

            # If the databases were already up, check again here
            # so we don't wait unnecessarily.
            if awaiting == connected:
                break
            time.sleep(interval)
