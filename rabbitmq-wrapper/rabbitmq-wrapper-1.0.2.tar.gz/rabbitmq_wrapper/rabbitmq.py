from json import JSONDecodeError, dumps, loads
from pydoc import locate

from pika import BlockingConnection, ConnectionParameters, PlainCredentials, URLParameters


class RabbitWrapper:
    CONFIG = {}

    def __init__(self, name=None, config=None, channel=None) -> None:
        if name is None and config is None:
            raise AssertionError('The "config" or "name" parameter is required.')

        if isinstance(name, str) and isinstance(config, dict):
            raise TypeError('Invalid type of parameters received.')

        self.NAME = name
        self.mount_settings(name, config)

        if self.get_enabled():
            self.create_connection(channel)
            self.create_queue()

    def mount_settings(self, name, config):
        if config:
            self.CONFIG = config

        else:
            try:
                from django.conf import settings
                self.CONFIG = getattr(settings, f'RABBIT_{name}')
            except ModuleNotFoundError:
                raise RuntimeError(
                    "Couldn't locate configuration, run passing with RabbitMqWrapper(config={...}),"
                    "if you use django, just pass a name to this wrapper and declare config in settings "
                    "using name on variable RABBIT_NameHere, Ex: RabbitMqWrapper(name='TEST'), in settings.py:"
                    "RABBIT_TEST = {...}."
                )

    ###
    # Connection and Queues
    ###
    def create_credentials(self):
        credentials = self.get_credentials()
        if credentials['username'] and credentials['password']:
            return {'credentials': PlainCredentials(**credentials)}
        return {}

    def create_connection(self, channel):
        conn_url = self.get_connection_url()
        if conn_url:
            connect = BlockingConnection(URLParameters(conn_url))
        else:
            connect = BlockingConnection(
                ConnectionParameters(
                    **self.get_connection_settings(),
                    **self.create_credentials()
                )
            )
        self.channel = channel or connect.channel()

    def create_queue(self):
        for queue in self.get_allowed_queues():
            self.channel.queue_declare(queue=queue)

    def set_receiver(self, **kwargs):
        if self.get_enabled():
            self.channel.basic_consume(**kwargs)

    ###
    # Getters
    ###
    def get_enabled(self):
        return self.CONFIG.get('ENABLED', False)

    def get_exchange(self):
        return self.CONFIG.get('USE_EXCHANGE', '')

    def get_credentials_keys(self):
        return ('username', 'password', 'erase_on_connect')

    def get_credentials(self):
        connect_data = self.CONFIG.get('CONNECTION', {})
        return {k: connect_data.get(k.upper()) for k in self.get_credentials_keys()}

    def get_connection_keys(self):
        return ('host', 'port', 'virtual_host', 'channel_max', 'frame_max', 'heartbeat', 'ssl_options',
                'connection_attempts', 'retry_delay', 'socket_timeout', 'stack_timeout', 'locale',
                'blocked_connection_timeout', 'client_properties', 'tcp_options')

    def get_connection_settings(self):
        connect_data = self.CONFIG.get('CONNECTION')
        if not connect_data:
            raise AssertionError('The "CONNECTION" parameter, is not present in config.')

        default = ConnectionParameters._DEFAULT
        return {k: connect_data.get(k.upper(), default) for k in self.get_connection_keys()}

    def get_connection_url(self):
        connect_data = self.CONFIG.get('CONNECTION')
        if not connect_data:
            raise AssertionError('The "CONNECTION" parameter, is not present in config.')

        return connect_data.get('URL', None)

    def get_default_queue(self):
        default_queue = self.CONFIG.get('DEFAULT_QUEUE')
        if not default_queue:
            raise AssertionError('The "DEFAULT_QUEUE" parameter, is not present in config.')
        return default_queue

    def get_deadletter(self):
        return self.CONFIG.get('DEADLETTER_QUEUE', f"{self.CONFIG['DEFAULT_QUEUE']}_deadletter")

    def get_allowed_queues(self):
        return self.CONFIG.get('ALLOWED_QUEUES') or [self.get_default_queue(), self.get_deadletter()]

    def get_consumers(self):
        return self.CONFIG.get('CONSUMERS')

    ###
    # Operations
    ###
    def msg_raw_send(self, **kwargs):
        if self.get_enabled():
            self.channel.basic_publish(**kwargs)
        else:
            print(kwargs)

    def msg_send(self, data, queue=None, json=True):
        queue = queue if queue else self.get_default_queue()
        data = dumps(data) if json else data
        if self.get_enabled():
            self.channel.basic_publish(exchange=self.get_exchange(), routing_key=queue, body=data)
        else:
            print(data)

    def mount_receivers(self):
        for receiver in self.get_consumers():
            receiver['on_message_callback'] = locate(receiver.pop('callback'))
            self.set_receiver(**receiver)

    def start_consuming(self):
        if self.get_enabled():
            self.mount_receivers()
            print(' [*] Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()
        else:
            raise RuntimeError("Couldn't run broker without enabled rabbit in config.")


class CallbackWrapper:
    NAME = None
    CONFIG = None
    WRAPPER = None

    def __init__(self, channel, method, properties, body):
        self.channel = channel
        self.method = method
        self.properties = properties
        self.body = body
        self.get_rabbit_instance()
        self.consume_data(raw_msg=body)

    def msg_ack(self):
        self.channel.basic_ack(delivery_tag=self.method.delivery_tag)

    def msg_resend(self, data, queue=None, json=True):
        self.validate_wrapper_started("msg_resend")
        self.WRAPPER.msg_send(data, queue, json=json)

    def msg_deadletter(self, data, queue=None, json=True):
        self.validate_wrapper_started("msg_deadletter")
        deadletter = queue or self.WRAPPER.get_deadletter()
        self.WRAPPER.msg_send(data, queue=deadletter, json=json)

    def consume_data(self, raw_msg):
        raise Exception('Implement your owner "consume_data" function')

    ###
    # Utils
    ###
    def validate_wrapper_started(self, func_name):
        if not self.WRAPPER:
            raise RuntimeError(
                f'To use "{func_name}" function you need to set "NAME" or "CONFIG" in the class variables.'
                'Use "CONFIG" if it`s using with python standalone or "NAME" if using django framework'
            )

    def msg_json_parser(self, data, deadletter_on_error=False, ack_on_error=False):
        try:
            return loads(data)
        except (TypeError, JSONDecodeError) as e:
            if deadletter_on_error:
                self.msg_deadletter(data=data, json=False)
            if ack_on_error:
                self.msg_ack()

    ###
    # Getters
    ###
    def get_rabbit_instance(self):
        if bool(self.NAME) or bool(self.CONFIG):
            self.wrapper = RabbitWrapper(name=self.NAME, config=self.CONFIG, channel=self.channel)
