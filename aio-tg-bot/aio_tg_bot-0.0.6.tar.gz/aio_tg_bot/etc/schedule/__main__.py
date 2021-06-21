import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from . import broadcast
from aio_tg_bot.etc.conf import settings


def setup(broadcast_runner=False):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    scheduler = AsyncIOScheduler(loop=loop)
    if broadcast_runner:
        scheduler.add_job(broadcast.broadcast_runner, "interval", minutes=1)

    scheduler.start()
