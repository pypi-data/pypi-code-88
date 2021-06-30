import logging
import time
import sys
import signal

from . import __version__
from .args import args
from .mqtt_task import mqttc_setup, mqttc_publish, mqttc_close
from .modbus_task import modbus_setup, modbus_poll, modbus_export, modbus_close

# global objects
run_loop = True

# config logging in main
LOG_SIMPLE = "%(asctime)s | %(levelname).1s | %(name)s | %(message)s"
LOG_PROCESS = "%(asctime)s | %(levelname).1s | %(processName)s | %(name)s | %(message)s"
LOG_THREAD = "%(asctime)s | %(levelname).1s | %(threadName)s | %(name)s | %(message)s"
logging.basicConfig(
    level="INFO",
    format=LOG_THREAD,
)
# get logger
log = logging.getLogger(__name__)


def _signal_handler(signal, frame):
    print('Exiting ' + sys.argv[0])
    _shutdown()


def app(name="modpoll"):
    log.info(f"Starting {name} v{__version__}")
    signal.signal(signal.SIGINT, _signal_handler)

    # setup mqtt
    if args.mqtt_host:
        log.info(f"Setup MQTT connection to {args.mqtt_host}")
        if not mqttc_setup(args.mqtt_host, port=args.mqtt_port, user=args.mqtt_user, password=args.mqtt_pass, qos=1):
            log.error("fail to setup MQTT client")
            mqttc_close()
            exit(1)
    else:
        log.info("No MQTT host specified, skip MQTT setup.")

    # setup modbus
    if not modbus_setup():
        log.error("fail to setup modbus client(master)")
        mqttc_close()
        exit(1)

    # main loop
    interval_s = 5.0
    last_check = 0
    while run_loop:
        now = time.time()
        if last_check == 0:
            last_check = now
            continue
        # Always run
        modbus_poll()
        # routine check
        if now > last_check + interval_s:
            log.debug(f"loop at {now}")
            if args.export:
                # export all current references
                modbus_export(args.export)
            # test mqtt
            # mqttc_publish("ysdtest/1", f"hello, {now}")
            last_check = now
    _shutdown()


def _shutdown():
    global run_loop
    run_loop = False
    modbus_close()
    mqttc_close()


if __name__ == "__main__":
    app()
