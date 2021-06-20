import json

from mobio.libs.kafka_lib.helpers.kafka_config_helper import KafkaConfigHelper


class KafkaProducerManager:
    def flush_message(self, topic: str, key: str, value):
        # SystemConfig().logger.info("kafka message data", extra={
        #     "key": "kafka",
        #     "topic": topic,
        #     "kafka_key": key,
        #     "value": value
        # })
        p = KafkaConfigHelper().get_producer_by_topic(topic=topic)
        p.produce(
            topic=topic,
            key=key,
            value=json.dumps(value).encode("utf-8"),
            on_delivery=self.kafka_delivery_report,
        )
        p.poll(0)

    def kafka_delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print("Message delivery failed: {}".format(err))
        else:
            print('message delivery to: {}, {}'.format(msg.topic(), msg.partition()))
