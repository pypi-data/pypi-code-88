import asyncio
import base64
import concurrent.futures
import json
import logging
import ssl
import time
import traceback
from functools import partial
from uuid import uuid4

import aioredis
import boto3
import snappy
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from botocore.config import Config

logger = logging.getLogger("aiokafkadaemon")

OPTS_REDIS_QUEUE_KEY = "redis_queue"
OPTS_REDIS_URL = "redis_url"
OPTS_REDIS_NAME = "redis_name"
OPTS_SQS_QUEUE_URL = "sqs_queue_url"

CONTEXT_REDIS_CHANNEL = "redis_channel"
CONTEXT_REDIS_QUEUE = "redis_queue"
CONTEXT_SQS_URL = "sqs_queue_url"

SQS_COMPRESSION_SNAPPY = "snappy"


class Worker:

    _sf_client = None
    _sqs_clients = {}

    def __init__(
        self,
        kafka_broker_addr=None,
        kafka_group_id="",
        consumer_topic="",
        producer_topic="",
        create_consumer=True,
        create_producer=False,
        on_run=None,
        sasl_opts={},
        consumer_opts={},
        producer_opts={},
        redis_opts={},
        sqs_opts={},
    ):
        self._uuid = str(uuid4())
        try:
            # only called in async func when the worker is created
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.get_event_loop()

        self._kafka_broker_addr = kafka_broker_addr
        self._kafka_group_id = kafka_group_id
        self._consumer_topic = consumer_topic
        self._producer_topic = producer_topic
        if not producer_topic:
            self._producer_topic = consumer_topic
        self._consumer = None
        self._producer = None
        self._sqs_opts = sqs_opts
        self._exit = False

        # Automatically reads environment variables
        #       AWS_ACCESS_KEY_ID
        #       AWS_SECRET_ACCESS_KEY
        #       AWS_SESSION_TOKEN (optional)
        #       AWS_DEFAULT_REGION
        # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#environment-variables
        try:
            self._sf_client = boto3.client("stepfunctions")
        except Exception as e:
            logger.warning(f"Unable to connect to boto3 client: {e}")

        # optional redis
        self._redis_opts = redis_opts
        self._redis = None
        self._redis_retry = 0
        self._redis_reconnecting = False

        if (
            create_consumer
            and not sqs_opts.get(OPTS_SQS_QUEUE_URL)
            and not redis_opts.get(OPTS_REDIS_QUEUE_KEY)
        ):
            self._consumer = Worker.make_consumer(
                loop, kafka_broker_addr, kafka_group_id, sasl_opts, consumer_opts
            )
        if create_producer:
            self._producer = Worker.make_producer(
                loop, kafka_broker_addr, sasl_opts, producer_opts
            )

        # legacy code, to be removed in future releases
        if on_run:
            logger.warning(
                f"DEPRECIATED: on_run should not be passed as param. Subclass the Worker"
            )
        self._on_run = on_run

    @classmethod
    def make_consumer(cls, loop, broker_addr, group_id, sasl_opts={}, consumer_opts={}):
        """
        Creates and connects Kafka  consumer to the broker
        :param loop:
        :param broker_addr:
        :return:
        """
        logger.debug("Creating instance of kafka consumer")

        if not sasl_opts:
            consumer = AIOKafkaConsumer(
                loop=loop,
                bootstrap_servers=broker_addr,
                group_id=group_id,
                **consumer_opts,
            )
        else:
            consumer = AIOKafkaConsumer(
                loop=loop,
                bootstrap_servers=broker_addr,
                group_id=group_id,
                sasl_mechanism="PLAIN",
                sasl_plain_username=sasl_opts["username"],
                sasl_plain_password=sasl_opts["password"],
                security_protocol="SASL_SSL",
                ssl_context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2),
                **consumer_opts,
            )

        logger.info("Connected consumer to kafka on {}".format(broker_addr))
        return consumer

    @classmethod
    def make_producer(cls, loop, broker_addr, sasl_opts={}, producer_opts={}):
        """
        Creates an instance of the AIOKafka producer
        :param loop:
        :param broker_addr:
        :return:
        """
        logger.debug("Creating instance of producer")
        if not sasl_opts:
            producer = AIOKafkaProducer(
                loop=loop,
                bootstrap_servers=broker_addr,
                compression_type="snappy",
                **producer_opts,
            )
        else:
            producer = AIOKafkaProducer(
                loop=loop,
                bootstrap_servers=broker_addr,
                compression_type="snappy",
                sasl_mechanism="PLAIN",
                sasl_plain_username=sasl_opts["username"],
                sasl_plain_password=sasl_opts["password"],
                security_protocol="SASL_SSL",
                ssl_context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2),
                **producer_opts,
            )

        logger.info("Producer connected to kafka on {}".format(broker_addr))
        return producer

    async def create_redis(self):
        """
        Keep retrying until succeed every 5 * retry seconds, max 1 minute interval
        """
        self._redis_reconnecting = True
        while True:
            try:
                if self._redis_opts:
                    self._redis = await aioredis.create_redis_pool(
                        self._redis_opts[OPTS_REDIS_URL], timeout=5
                    )
                    asyncio.ensure_future(self.redis_setname_loop())
                else:
                    logger.warning("Redis opts not supplied")
                break
            except Exception as e:
                # failed to create, just retry
                logger.error(e)
            self._redis_retry += 1
            await asyncio.sleep(min(60, 5 * self._redis_retry))
            logger.warning(f"Retry connecting redis {self._redis_retry}")

        # reset counters and flags after connection
        self._redis_retry = 0
        self._redis_reconnecting = False

    async def redis_setname_loop(self):
        # during reconnection, the name will not be reset
        if self._redis_opts.get(OPTS_REDIS_NAME) is not None:
            name_to_set = f"{self._redis_opts.get(OPTS_REDIS_NAME)}-{self._uuid}"
            while not self.should_exit():
                try:
                    existing_name = await self._redis.client_getname()
                    try:
                        existing_name = existing_name.decode()  # byte
                    except Exception:
                        pass
                    if existing_name != name_to_set:
                        await self._redis.client_setname(name_to_set)
                        logger.warning(
                            f"redis client name set from: '{existing_name}' to: '{name_to_set}'"
                        )
                    await asyncio.sleep(60)
                except Exception as e:
                    logger.error(e)

    async def destroy_redis(self):
        """
        Don't care if the close fails or timeout
        """
        if self._redis is not None and not self._redis_reconnecting:
            try:
                self._redis.close()
                await asyncio.wait_for(self._redis.wait_closed(), timeout=3)
            except Exception as e:
                logger.error(e)
            finally:
                self._redis = None
                logger.warning("Redis destoryed")

    def sqs_client(self, queue_url):
        if not queue_url:
            return None

        region = queue_url.split(".")[1]
        client = self._sqs_clients.get(region)
        if not client:
            config = Config(region_name=region)

            client = boto3.client("sqs", config=config)
            self._sqs_clients[region] = client

            logger.info(f"new sqs client {region} created")

        return client

    async def __aenter__(self):
        """
        Async iterator-enter coroutine
        :return:
        """
        return self

    async def __aexit__(self):
        """
        Async iterator-exit coroutine
        :return:
        """
        return await self.stop()

    def should_exit(self):
        return self._exit

    async def start(self):
        await self.create_redis()

        if self._consumer:
            if self._consumer_topic:
                self._consumer.subscribe([self._consumer_topic])

            logger.info("Kafka consumer started")
            await self._consumer.start()
        if self._producer:
            logger.info("Kafka producer started")
            await self._producer.start()

    async def stop_kafka(self, stop_producer=False):
        if self._consumer:
            await self._consumer.stop()
            logger.warning("Consumer has been stopped")

        if stop_producer and self._producer:
            await self._producer.stop()
            logger.warning("Producer has been stopped")

    async def stop(self):
        logger.warning("System stopping, stopping consumer first")
        self._exit = True
        await self.stop_kafka(False)

    async def clean_up_after_run(self):
        logger.warning("clean up after run")
        self._exit = True
        await self.stop_kafka(True)
        await self.destroy_redis()

    async def run(self):
        """
        Main method for the worker. Any child class can either
        overload it, or just implement on_run async callback,
        to perform specific tasks.
        :return:
        """
        try:
            await self.start()
            on_run = getattr(self, "on_run", None)
            if on_run and callable(on_run):
                await on_run()
        except Exception as exc:
            # Only deadling with generic and Kafka critical
            # errors here. ie, UnknownMemberIdError and any
            # heartbeat error, like RequestTimedOutError, is
            # logged only, not raised again
            # https://bit.ly/2IWG8Mn
            # https://bit.ly/2ZCNCtE
            logger.error(
                "Error causing system failure, "
                "{}:\n{}".format(exc, traceback.format_exc())
            )
        finally:
            await self.clean_up_after_run()

    async def send_heartbeat(self, step_functions_task_id):
        """
        If being processed as part of an AWS Step Functions pipeline
        then send a regular heartbeat when processing to let Step Functions
        know and not kill the process.
        """
        if self._sf_client is None or step_functions_task_id is None:
            return
        try:
            logger.info(
                f"Sending step functions heartbeat for {step_functions_task_id}"
            )
            with concurrent.futures.ThreadPoolExecutor() as pool:
                await asyncio.get_running_loop().run_in_executor(
                    pool,
                    partial(
                        self._sf_client.send_task_heartbeat,
                        taskToken=step_functions_task_id,
                    ),
                )
        except Exception as e:
            logger.error(f"Unable to send heartbeat {e}")
            return

    async def send_step_functions_result(
        self, step_functions_task_id, result, result_data
    ):
        """
        If being processed as part of an AWS Step Functions pipeline
        then send back a relevant result (success or failure) with useful
        data for processing.
        """
        if self._sf_client is None or step_functions_task_id is None:
            return
        try:
            with concurrent.futures.ThreadPoolExecutor() as pool:
                if result.get("error") is not None:
                    logger.info(
                        f"Sending step functions task failure for {step_functions_task_id}"
                    )

                    await asyncio.get_running_loop().run_in_executor(
                        pool,
                        partial(
                            self._sf_client.send_task_failure,
                            taskToken=step_functions_task_id,
                            error=str(result.get("code")),
                            cause=str(result.get("error")),
                        ),
                    )
                else:
                    logger.info(
                        f"Sending step functions task success for {step_functions_task_id}"
                    )
                    await asyncio.get_running_loop().run_in_executor(
                        pool,
                        partial(
                            self._sf_client.send_task_success,
                            taskToken=step_functions_task_id,
                            output=result_data,
                        ),
                    )
        except Exception as e:
            logger.error(f"Unable to send step functions response: {e}")
            return

    async def send_sqs_message(
        self,
        queue_url,
        message,
        wait=True,
        high_throughput=True,
        compression=SQS_COMPRESSION_SNAPPY,
    ):
        client = self.sqs_client(queue_url)

        message_attributes = None
        if compression == SQS_COMPRESSION_SNAPPY:
            # message to keep as a string instead of bytes
            message = base64.b64encode(snappy.compress(message)).decode()
            message_attributes = {
                "compression": {"StringValue": f"{compression}", "DataType": "String"}
            }

        if queue_url.endswith(".fifo"):
            did = f"{time.time()}"
            coro = asyncio.get_running_loop().run_in_executor(
                None,
                partial(
                    client.send_message,
                    QueueUrl=queue_url,
                    MessageAttributes=message_attributes,
                    MessageBody=message,
                    MessageDeduplicationId=did,
                    MessageGroupId=did if high_throughput else self._uuid,
                ),
            )
        else:
            coro = asyncio.get_running_loop().run_in_executor(
                None,
                partial(
                    client.send_message,
                    QueueUrl=queue_url,
                    MessageAttributes=message_attributes,
                    MessageBody=message,
                ),
            )

        if wait:
            await coro
        else:
            asyncio.ensure_future(coro)

    async def receive_sqs_message(self, num_message=1):
        queue_url = self._sqs_opts[OPTS_SQS_QUEUE_URL]
        client = self.sqs_client(queue_url)

        response = await asyncio.get_running_loop().run_in_executor(
            None,
            partial(
                client.receive_message,
                QueueUrl=queue_url,
                MessageAttributeNames=["compression"],
                MaxNumberOfMessages=num_message,
                WaitTimeSeconds=15,
            ),
        )

        for message in response.get("Messages", []):
            compression = message.get("MessageAttributes", {}).get("compression")
            if compression and compression.get("StringValue") == SQS_COMPRESSION_SNAPPY:
                message["Body"] = snappy.uncompress(
                    base64.b64decode(message["Body"])
                ).decode()

        return response

    async def delete_sqs_message(self, receipt_handle):
        queue_url = self._sqs_opts[OPTS_SQS_QUEUE_URL]
        client = self.sqs_client(queue_url)

        return await asyncio.get_running_loop().run_in_executor(
            None,
            partial(
                client.delete_message, QueueUrl=queue_url, ReceiptHandle=receipt_handle,
            ),
        )

    async def receive_redis_queue(self, timeout=0):
        queue_key = self._redis_opts[OPTS_REDIS_QUEUE_KEY]
        return await self._redis.blpop(queue_key, timeout=timeout)

    async def send_result(
        self, result, context=None, result_channel=None, wait_for_sqs=True
    ):
        context_topic = None
        result_data = json.dumps(result)

        if context:
            if context.get("step_functions_task_id") is not None:
                await self.send_step_functions_result(
                    context.get("step_functions_task_id"), result, result_data
                )

            # step function and kafka callback topic don't need to be mutually exclusive
            if context.get("topic") and self._producer:
                context_topic = context.get("topic")
                partition = context.get("partition")
                headers = context.get("headers")
                if headers:
                    headers = [(k, v.encode("utf-8")) for k, v in headers.items()]

                await self._producer.send(
                    context_topic,
                    result_data.encode("utf-8"),
                    partition=partition,
                    headers=headers,
                )

                logger.info(
                    "pushing result with code {} "
                    'to topic "{}"'.format(result.get("code", None), context_topic)
                )

            if self._redis:
                if context.get(CONTEXT_REDIS_CHANNEL):
                    # can be redis pubsub
                    redis_channel = context.get(CONTEXT_REDIS_CHANNEL)

                    await self._redis.publish(redis_channel, result_data)

                    logger.info(
                        "pushing result with code {} "
                        'to redis "{}"'.format(result.get("code", None), redis_channel)
                    )

                if context.get(CONTEXT_REDIS_QUEUE):
                    redis_queue = context.get(CONTEXT_REDIS_QUEUE)
                    await self._redis.rpush(redis_queue, result_data)

                    logger.info(
                        "pushing result with code {} "
                        'to redis queue "{}"'.format(
                            result.get("code", None), redis_queue
                        )
                    )

            if context.get(CONTEXT_SQS_URL):
                sqs_queue = context.get(CONTEXT_SQS_URL)
                await self.send_sqs_message(sqs_queue, result_data, wait=wait_for_sqs)

                logger.info(
                    "pushing result with code {} "
                    'to sqs "{}"'.format(result.get("code", None), sqs_queue)
                )

        # always check the result_channel as it is usually used for data persistence
        if result_channel:
            for rc in result_channel.split(","):
                if rc.startswith("https://sqs"):
                    await self.send_sqs_message(rc, result_data, wait=wait_for_sqs)
                elif rc.startswith("redis://"):
                    channel = rc.split("redis://")[1]
                    await self._redis.rpush(channel, result_data)
                elif self._producer and context_topic != result_channel:
                    await self._producer.send(rc, result_data)
                else:
                    logger.error(f"{rc} result channel cannot be understood")

        # unify error logging
        self.capture_error(result=result)

    def capture_error(
        self, result=None, min_code_as_error=500, delete_error_detail=True
    ):
        """Capture error, can be overwritten by subclass
        logger.error will be captured by Sentry if initialized
        logger.warning will just log it, without triggering Sentry
        """
        if not isinstance(result, dict) or not result.get("error"):
            return None

        # only log errors whose code >= min_code_as_error
        # the rest are warning
        # logger.error triggers sentry and needs attention
        # if code is undefined or other values, then log it as error
        error_code = result.get("code", 500)
        error = result["error"]

        if not isinstance(error_code, int) or error_code >= min_code_as_error:
            # error_detail is for trace stack or other verbose details
            # self-defined convention
            error_detail = result.get("error_detail", error)
            logger.error(error_detail)
        else:
            logger.warning(error)

        # avoid large payload to be sent back to frontend
        if delete_error_detail and "error_detail" in result:
            del result["error_detail"]
