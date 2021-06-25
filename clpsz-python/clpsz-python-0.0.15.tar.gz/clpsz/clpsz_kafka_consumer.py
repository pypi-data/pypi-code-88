import os
import sys
import json
import click
from confluent_kafka import Consumer, KafkaError


@click.command()
@click.option('-b', '--brokers', 'brokers', required=True, help='kafka brokers')
@click.option('-t', '--topic', 'topic', required=True, help='kafka topic to consume from')
@click.option('-c', '--consumer-group', 'consumer_group', required=True, help='consumer group')
def main(brokers, topic, consumer_group):
    main1(brokers, topic, consumer_group)


def main1(brokers, topic, consumer_group):
    settings = {
        'bootstrap.servers': brokers,
        'group.id': consumer_group,
        'client.id': 'client-1',
        'enable.auto.commit': True,
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'latest'} # latest, none, earliest
    }
    c = Consumer(settings)
    c.subscribe([topic])

    try:
        while True:
            msg = c.poll(0.1)
            if msg is None:
                continue
            elif not msg.error():
                print(msg.value())
            elif msg.error().code() == KafkaError._PARTITION_EOF:
                print('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
            else:
                print('Error occured: {0}'.format(msg.error().str()))

    except KeyboardInterrupt:
        pass

    finally:
        c.close()


if __name__ == '__main__':
    main1('sz.vm2:9094', 'test', 'my-consumer')
