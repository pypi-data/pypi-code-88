import os
import pathlib
import aiogram

from . import filters
from . import handlers
from . import middlewares
from . import fsm_storage
from .etc.database import models
from .etc import schedule as _schedule
from .etc.database.migrations import Router


def setup(dispatcher, filter=True, handler=False, middleware=True, schedule=False, use_django=False):
    dispatcher.storage = fsm_storage.PeeweeORMStorage()

    if filter:
        filters.setup(dispatcher)

    if handler:
        handlers.setup(dispatcher)

    if middleware:
        middlewares.setup(dispatcher)

    if schedule:
        _schedule.setup()

    if use_django:
        import django
        django.setup()
