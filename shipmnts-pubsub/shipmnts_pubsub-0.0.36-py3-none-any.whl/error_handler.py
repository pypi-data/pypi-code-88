import logging
import os
import json
import hashlib
from redis import StrictRedis
from pb.error_event import publish_to_error
from rest_framework.response import Response
from django.db import connection
from rest_framework import status

redis_host = os.getenv('REDIS_HOST', 'redis://localhost')
redis = StrictRedis.from_url(redis_host)


def handle_error(data, counter, is_processed, project_id, topic_name=None):
    retry_limit_exceeded = False
    if is_processed:
        logging.info("Message is already processed")
        return True
    if counter >= 1:
        logging.info(
            "Retry limit exceeded. Currently Retry changed from 5 to 0")
        logging.info("data in handle error %s", data)
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE jobs set status = 'failed' WHERE id={0}".format(
                        data['job_id']
                    )
                )
                if data.get("child_document_id"):
                    cursor.execute("UPDATE child_documents set status = 'failed' WHERE id={0}".format(
                        data.get("child_document_id")))
            if topic_name:
                publish_to_error(data={'job_id': data['job_id'], 'tenant': data['tenant'],
                                       'service': data.get("service")}, project_id=project_id, topic_name=topic_name)
            retry_limit_exceeded = True
        except Exception as e:
            logging.info(
                "Job id or tenant is missing in data. Exception = {0}".format(e))
        finally:
            return retry_limit_exceeded


def create_key(request, data):
    # This helper function creates a unique key for a message
    str_data = json.dumps(data)
    sha256 = hashlib.sha256(str_data.encode('utf-8')).hexdigest()
    subscription = request['subscription'].split('/')[-1]
    message_id = request['message']['messageId']
    return ["%s_%s_%s" % (subscription, sha256, message_id), "%s_%s" % (subscription, message_id)]


def get_count(key):
    # In case you want to wait some arbitrary time before your message "fails"
    counter = redis.get(key)
    if counter:
        redis.incr(key)
        counter = redis.get(key)
    else:
        counter = 0
        redis.set(key, counter, 3600*6)
    return int(counter)


def check_message_processed(status_key):
    status = redis.get(status_key)
    if status:
        is_processed = True
    else:
        is_processed = False
    return is_processed


def set_message_status(request):
    subscription = request['subscription'].split('/')[-1]
    message_id = request['message']['messageId']
    key = "%s_%s" % (subscription, message_id)
    redis.set(key, "1", 3600*6)


def handle_pubsub_retry(request, data, project_id, topic_name=None):
    key, msg_status_key = create_key(request, data)
    counter = get_count(key)
    is_processed = check_message_processed(msg_status_key)
    logging.info("message key for retry %s, counter %s, is_processed: %s",
                 key, counter, is_processed)
    return handle_error(data, counter, is_processed, project_id, topic_name=topic_name)
