import atexit
import logging
import numbers
from datetime import date, datetime
from uuid import uuid4

from dateutil.tz import tzutc
from filum_analytics.consumer import Consumer
from filum_analytics.request import post
from filum_analytics.utils import guess_timezone, clean
from filum_analytics.version import VERSION
from six import string_types

try:
    import queue
except:
    import Queue as queue

ID_TYPES = (numbers.Number, string_types)


def is_datetime_valid_isoformat(dt_str):
    try:
        datetime.fromisoformat(dt_str)
    except:
        return False
    return True


class Client(object):
    """Create a new analytics client."""
    log = logging.getLogger('filum')

    def __init__(self, write_key=None, host=None, debug=False, max_queue_size=10000,
                 send=True, on_error=None, upload_size=100, upload_interval=0.5,
                 gzip=False, max_retries=10, sync_mode=False):
        require('write_key', write_key, string_types)

        self.queue = queue.Queue(max_queue_size)
        self.write_key = write_key
        self.on_error = on_error
        self.debug = debug
        self.send = send
        self.sync_mode = sync_mode
        self.host = host
        self.gzip = gzip

        if debug:
            self.log.setLevel(logging.DEBUG)

        if sync_mode:
            self.consumer = None
        else:
            self.consumer = Consumer(self.queue, write_key, host=host, on_error=on_error,
                                     upload_size=upload_size, upload_interval=upload_interval,
                                     gzip=gzip, retries=max_retries)

            # if we've disabled sending, just don't start the consumer
            if send:
                # On program exit, allow the consumer thread to exit cleanly.
                # This prevents exceptions and a messy shutdown when the interpreter is
                # destroyed before the daemon thread finishes execution. However, it
                # is *not* the same as flushing the queue! To guarantee all messages
                # have been delivered, you'll still need to call flush().
                atexit.register(self.join)
                self.consumer.start()

    def eventify(self, user_id=None, event_name="DefaultFilumEventName", event_type="DefaultFilumEventType",
                 event_params=None, context=None, timestamp=None, original_timestamp=None, anonymous_id=None,
                 origin=None):
        event_params = event_params or {}
        event_params = convert_dict_to_filum_event_format(event_params)
        context = context or {}
        require('user_id or anonymous_id', user_id or anonymous_id, ID_TYPES)
        if user_id is None and anonymous_id is None:
            raise ValueError("Either User ID or Anonymous ID must be set.")

        require('event_params', event_params, list)

        if original_timestamp is None:
            original_timestamp = datetime.utcnow().replace(tzinfo=tzutc())
        if timestamp is None:
            timestamp = original_timestamp

        sent_at = datetime.utcnow().replace(tzinfo=tzutc())
        received_at = datetime.utcnow().replace(tzinfo=tzutc())
        msg = {
            'anonymous_id': anonymous_id,
            'user_id': user_id,
            'context': context,
            'timestamp': timestamp,
            'original_timestamp': original_timestamp,
            'sent_at': sent_at,
            'received_at': received_at,
            'event_name': event_name,
            'event_type': event_type,
            'event_params': event_params,
            'origin': origin
        }
        return self._enqueue(msg)

    def identify(self, user_id=None, event_params=None, context=None, timestamp=None, original_timestamp=None,
                 anonymous_id=None, origin=None):
        event_params = event_params or {}
        context = context or {}
        require('user_id or anonymous_id', user_id or anonymous_id, ID_TYPES)
        return self.eventify(user_id=user_id, event_name="Identify", event_type="identify", event_params=event_params,
                      context=context, anonymous_id=anonymous_id, timestamp=timestamp,
                      original_timestamp=original_timestamp, origin=origin)

    def track(self, user_id=None, event_name=None, event_params=None, context=None,
              timestamp=None, original_timestamp=None, anonymous_id=None):
        event_params = event_params or {}
        context = context or {}
        require('user_id or anonymous_id', user_id or anonymous_id, ID_TYPES)
        return self.eventify(user_id=user_id, event_name=event_name, event_type="track", event_params=event_params,
                      context=context, timestamp=timestamp, original_timestamp=original_timestamp,
                      anonymous_id=anonymous_id)

    def _enqueue(self, msg):
        """Push a new `msg` onto the queue, return `(success, msg)`"""
        timestamp = msg['timestamp']
        if timestamp is None:
            timestamp = datetime.utcnow().replace(tzinfo=tzutc())

        original_timestamp = msg['original_timestamp']
        if original_timestamp is None:
            original_timestamp = datetime.utcnow().replace(tzinfo=tzutc())

        event_id = msg.get('eventId')
        if event_id is None:
            event_id = uuid4()

        # require('integrations', msg['integrations'], dict)
        require('timestamp', timestamp, datetime)
        require('original_timestamp', original_timestamp, datetime)

        require('context', msg['context'], dict)

        # add common
        timestamp = guess_timezone(timestamp)

        msg['original_timestamp'] = original_timestamp.isoformat()
        msg['timestamp'] = timestamp.isoformat()
        msg['sent_at'] = msg['sent_at'].isoformat()
        msg['received_at'] = msg['received_at'].isoformat()

        msg['event_id'] = stringify_id(event_id)

        # handle Context to follow Filum Event Schema
        _context = process_context_data()
        msg['context'] = _context

        msg['user_id'] = stringify_id(msg.get('user_id', ''))
        msg['anonymous_id'] = stringify_id(msg.get('anonymous_id', ''))

        msg = clean(msg)
        self.log.debug('queueing: %s', msg)

        # if send is False, return msg as if it was successfully queued
        if not self.send:
            return True, msg

        if self.sync_mode:
            # self.log.debug('enqueued with blocking %s.', msg['type'])
            post(self.write_key, self.host, gzip=self.gzip, data=[msg])

            return True, msg

        try:
            self.queue.put(msg, block=False)
            # self.log.debug('enqueued %s.', msg['type'])
            return True, msg
        except queue.Full:
            self.log.warning('analytics-python queue is full')
            return False, msg

    def flush(self):
        """Forces a flush from the internal queue to the server"""
        queue = self.queue
        size = queue.qsize()
        queue.join()
        # Note that this message may not be precise, because of threading.
        self.log.debug('successfully flushed about %s items.', size)

    def join(self):
        """Ends the consumer thread once the queue is empty. Blocks execution until finished"""
        self.consumer.pause()
        try:
            self.consumer.join()
        except RuntimeError:
            # consumer thread has not started
            pass

    def shutdown(self):
        """Flush all messages and cleanly shutdown the client"""
        self.flush()
        self.join()


def require(name, field, data_type):
    """Require that the named `field` has the right `data_type`"""
    if not isinstance(field, data_type):
        msg = '{0} must have {1}, got: {2}'.format(name, data_type, field)
        raise AssertionError(msg)


def stringify_id(val):
    if val is None:
        return None
    if isinstance(val, string_types):
        return val
    return str(val)


def convert_dict_to_filum_event_format(event_params):
    event_params_server_format = []
    for k, v in event_params.items():
        new_item = dict()
        new_item['key'] = k
        new_item['value'] = {}
        if isinstance(v, int):
            new_item['value'].update({'int_value': v})
        elif isinstance(v, float):
            new_item['value'].update({'double_value': v})
        elif isinstance(v, datetime):
            new_item['value'].update({'datetime_value': v})
        else:
            if v is None:
                new_item['value'].update({'string_value': None})
            else:
                new_item['value'].update({'string_value': str(v)})
        event_params_server_format.append(new_item)
    return event_params_server_format


def process_context_data():
    _context = dict()
    _context['active'] = 0
    _context['app'] = {}
    _context['campaign'] = {}
    _context['device'] = {}
    _context['ip'] = ''
    _context['library'] = {
        'name': 'filum-python-sdk',
        'version': VERSION
    }
    _context['locale'] = 'vi-VN'
    _context['location'] = {}
    _context['network'] = {}
    _context['os'] = {}
    _context['page'] = {}
    _context['referrer'] = {}
    _context['screen'] = {}
    _context['user_agent'] = ''
    return _context
