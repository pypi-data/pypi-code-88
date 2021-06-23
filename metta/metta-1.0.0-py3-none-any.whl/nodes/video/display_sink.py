import typer
import asyncio
import cv2

from typing import Dict, List, Optional

from metta.nodes.sink_node import SinkNode
from metta.topics.topics import Topic, Message


class DisplaySink(SinkNode):
    def __init__(
        self,
        *,
        source_topic: Topic,
        kafka_brokers: List[str],
        zookeeper_hosts: List[str],
        event_loop: Optional[asyncio.unix_events._UnixSelectorEventLoop] = None,
        fps: Optional[int] = None,
        source_filters: List[str] = [],
    ):
        super().__init__(
            source_topic=source_topic,
            kafka_brokers=kafka_brokers,
            zookeeper_hosts=zookeeper_hosts,
            event_loop=event_loop,
        )
        self.display_ns = int(1000 / fps) if fps is not None else 1
        self.source_filters = source_filters
        self.open_windows: List[str] = []

    async def add_window(self, window_name):
        cv2.namedWindow(s)
        self.open_windows.append(s)

    async def __aenter__(self):
        for s in self.source_filter:
            self.add_window(s)
        return await super().__aenter__()

    async def __aexit__(self, exc_type, exc, tb):
        cv2.destroyAllWindows()
        self.open_windows = []
        return await super().__aexit__(exc_type, exc, tb)

    async def process(self, input_msg: Message):
        if not self.source_filter or input_msg.msg.source in self.source_filter:
            if input_msg.msg.source not in self.open_windows:
                self.add_window(input_msg.msg.source)
            cv2.imshow(input_msg.msg.source, input_msg.data)
            cv2.waitKey(self.display_ns)


def main(
    source_topic: str = typer.Argument(None, envvar="SOURCE_TOPIC"),
    brokers: List[str] = typer.Argument(None, envvar="BROKERS"),
    zk_hosts: List[str] = typer.Argument(None, envvar="ZOOKEEPER_HOSTS"),
    fps: Optional[int] = typer.Option(None, envvar="FPS"),
    source_filters: List[str] = typer.Option([], envvar="SOURCE_FILTER"),
    profile: bool = typer.Option(False, envvar="PROFILE"),
):
    """
    Run a DisplaySink node.
    """

    node = DisplaySink(
        fps=fps,
        source_topic=source_topic,
        kafka_brokers=brokers,
        zookeeper_hosts=zk_hosts,
        source_filters=source_filters,
    )
    node.mainloop(profile=profile)


if __name__ == "__main__":

    typer.run(main)