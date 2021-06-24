# import pandas
import boto3

from bin.connector import create_client

client = create_client('kinesis', 'eu-west-3')


def deleteStream(stream_name):
    client.delete_stream(
        StreamName=stream_name,
        EnforceConsumerDeletion=True
    )


def send_data_kinesis():
    kinesisRecords = []


if __name__ == '__main__':
    deleteStream('test_kinesis_stream')
