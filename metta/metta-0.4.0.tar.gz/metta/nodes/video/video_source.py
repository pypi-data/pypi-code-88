import typer
import asyncio
import uvloop
import ffmpeg
import numpy as np

from typing import List, Optional
from nptyping import NDArray

from metta.common.time_utils import time_ms
from metta.common.topics import Topic, NewMessage
from metta.nodes.source_node import SourceNode


class VideoSource(SourceNode):
    def __init__(
        self,
        *,
        source_name: str,
        input_path: str,
        height: int,
        width: int,
        publish_topic: Topic,
        kafka_brokers: List[str],
        zookeeper_hosts: List[str],
        event_loop: Optional[asyncio.unix_events._UnixSelectorEventLoop] = None,
        hwaccel: bool = False,
    ):
        super().__init__(
            publish_topic=publish_topic,
            kafka_brokers=kafka_brokers,
            zookeeper_hosts=zookeeper_hosts,
            event_loop=event_loop,
        )
        self.source_name = source_name
        self.input_path = input_path
        self.height = height
        self.width = width
        self.hwaccel = hwaccel

    async def __aenter__(self):
        self.loop = asyncio.get_running_loop()

        input_args = {}
        if self.hwaccel:
            input_args["hwaccel"] = "cuda"

        self.frame_stream = (
            ffmpeg.input(self.input_path, **input_args)
            .output("pipe:", format="rawvideo", pix_fmt="rgb24")
            .run_async(pipe_stdout=True)
        )
        return await super().__aenter__()

    async def __aexit__(self, exc_type, exc, tb):
        self.frame_stream.stdout.close()
        self.frame_stream.wait()
        return await super().__aexit__(exc_type, exc, tb)

    def read_next(self) -> Optional[NDArray[np.uint8]]:
        in_bytes = self.frame_stream.stdout.read(self.height * self.width * 3)
        if in_bytes:
            return np.frombuffer(in_bytes, np.uint8).reshape(
                [self.height, self.width, 3]
            )
        return None

    async def process(self) -> List[NewMessage]:
        frame = await self.loop.run_in_executor(None, self.read_next)
        if frame is not None:
            return [
                NewMessage(source=self.source_name, data=frame, timestamp=time_ms())
            ]
        return []


def main(
    source_name: str = typer.Argument(None, envvar="SOURCE_NAME"),
    input_path: str = typer.Argument(None, envvar="INPUT_PATH"),
    height: int = typer.Argument(None, envvar="HEIGHT"),
    width: int = typer.Argument(None, envvar="WIDTH"),
    publish_topic: str = typer.Argument(None, envvar="PUBLISH_TOPIC"),
    brokers: List[str] = typer.Argument(None, envvar="BROKERS"),
    profile: bool = typer.Option(False, envvar="PROFILE"),
    hwaccel: bool = typer.Option(False, envvar="HWACCEL"),
):
    """
    Run a VideoSource node.
    """

    async def run():
        async with VideoSource(
            source_name=source_name,
            input_path=input_path,
            height=height,
            width=width,
            publish_topic=publish_topic,
            kafka_brokers=brokers,
            event_loop=asyncio.get_event_loop(),
            hwaccel=hwaccel,
        ) as display:
            await display.run(profile=profile)

    uvloop.install()
    asyncio.run(run())


if __name__ == "__main__":

    typer.run(main)