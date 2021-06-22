import asyncio.subprocess as aio_subprocess
from contextlib import asynccontextmanager
import uuid


async def subprocess_exec(*args, **kwargs):
    kwargs.setdefault("stderr", aio_subprocess.DEVNULL)
    kwargs.setdefault("stdout", aio_subprocess.DEVNULL)

    proc = await aio_subprocess.create_subprocess_exec(
        *args,
        **kwargs,
    )
    return await proc.wait()


@asynccontextmanager
async def check_subprocess_exec(*args, **kwargs) -> aio_subprocess.Process:
    proc = await aio_subprocess.create_subprocess_exec(*args, **kwargs)
    try:
        yield proc
    finally:
        await proc.wait()


def generate_unique_name() -> str:
    return str(uuid.uuid4())
