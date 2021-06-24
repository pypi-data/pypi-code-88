import asyncio
from typing import Awaitable

def run(loop: asyncio.AbstractEventLoop = None, main_task: Awaitable = None):
    try:
        loop = loop or asyncio.get_event_loop()
        if main_task:
            loop.run_until_complete(main_task)
        else:
            loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        for task in asyncio.Task.all_tasks(loop):
            task.cancel()
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
