"""
Main score worker class implementation
"""
import asyncio
import json
import logging
import tempfile

import aiofiles
from yarl import URL

from .errors import AudioUndecodableException
from .worker import Worker

logger = logging.getLogger("aiokafkadaemon.AdvancedWorker")


class AdvancedWorker(Worker):
    """
    Worker class runs the main worker for the scoring service
    """

    def __init__(
        self,
        testing=False,
        init_kafka=True,
        score_model=None,
        kafka_opts={},
        redis_opts={},
        sqs_opts={},
    ):
        """
        Lowering max_poll_interval_ms from 300s to 60s to be more responsive
        to rebalance error, reduce the impact of user timeouts
        Keep default auto_commit (5000ms) but list here for further tuning
        """
        if testing:
            init_kafka = False

        create_consumer = init_kafka
        create_producer = init_kafka

        super().__init__(
            kafka_broker_addr=kafka_opts.get("broker"),
            kafka_group_id=kafka_opts.get("group_id"),
            consumer_topic=kafka_opts.get("topic"),
            create_consumer=create_consumer,
            create_producer=create_producer,
            sasl_opts=kafka_opts.get("sasl_opts"),
            consumer_opts={
                "max_poll_interval_ms": 60000,
                "auto_commit_interval_ms": 5000,
            },
            producer_opts={"max_request_size": 3145728},  # 3mb
            redis_opts=redis_opts,
            sqs_opts=sqs_opts,
        )
        self._testing = testing
        self._audio_path = tempfile.mkdtemp()
        self._score_model = score_model
        self._versions = AdvancedWorker.get_worker_version()

    @staticmethod
    def get_worker_version():
        """
        Parses worker metadada and returns it
        :return:
        """
        metadata = None
        try:
            with open("metadata.json", "r") as f:
                data = f.read()
                metadata = json.loads(data)
        except Exception:
            logger.error("metadata does not exist")

        return metadata

    @staticmethod
    def is_binary_audio(audio):
        try:
            # Let's try forcing decode here to check it's ok
            if str(audio, "utf-8"):
                audio = None
        except UnicodeDecodeError:
            # This is ok
            pass
        return audio

    @staticmethod
    async def read_local(path):
        audio = None
        async with aiofiles.open(path, "rb") as f:
            audio = await f.read()

        return audio

    @staticmethod
    async def read_http_audio(url, session):
        audio = None
        encoded_url = URL(url, encoded=True)
        async with session.get(encoded_url, timeout=3) as response:
            audio = await response.read()

        return audio

    @staticmethod
    async def read_redis_audio(url, redis_client):
        audio = None
        if not redis_client:
            raise Exception("Redis not initiated")

        key = url.split("//")[1]
        audio = await asyncio.wait_for(redis_client.get(key), timeout=3)
        return audio

    @staticmethod
    async def fetch_and_write(audio_url, session, redis_client, file_path, retry=2):
        # It assumes the checking for allow local was already done.
        # Let's propagate any exception by the main function
        audio = None
        while retry:
            retry -= 1

            try:
                if audio_url.startswith("http"):
                    audio = await AdvancedWorker.read_http_audio(audio_url, session)
                elif audio_url.startswith("redis"):
                    audio = await AdvancedWorker.read_redis_audio(
                        audio_url, redis_client
                    )
                else:
                    audio = await AdvancedWorker.read_local(audio_url)

                audio = AdvancedWorker.is_binary_audio(audio)

                if audio:
                    break

                raise AudioUndecodableException()
            except Exception as e:
                # catch all kinds of error
                if retry == 0:
                    raise e

            await asyncio.sleep(0.5)

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(audio)
