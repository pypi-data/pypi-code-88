import asyncio
import os

from dotenv import load_dotenv

from SheriAPI import SheriAPI, FreeEndpoint, NSFWEndpoint

load_dotenv()


async def sheri_stuff():
    async with SheriAPI(token=os.environ['TOKEN'], allow_nsfw=True) as api:
        image = await api.get(FreeEndpoint.Snek, count=1)
        print(image)


def run():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sheri_stuff())


if __name__ == "__main__":
    run()
