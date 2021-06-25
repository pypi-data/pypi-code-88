"""
@File    :   __main__.py
@Path    :   agrothon_client/
@Time    :   2021/05/28
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.8
@Contact :   ckvbalusu@gmail.com
@Desc    :   Main Module for Agrothon
"""
from .utils import serial_sensor_in, pump_status, motion_intruder_detect
import multiprocessing
import os
import signal
import logging

LOGGER = logging.getLogger(__name__)

# def handler(signalname):
#     def f(signal_received, frame):
#         pass
#     return f

# signal.signal(signal.SIGINT, handler("SIGINT"))
# signal.signal(signal.SIGTERM, handler("SIGTERM"))


def main():
    try:
        pool = multiprocessing.Pool()
        sen_result = pool.apply_async(serial_sensor_in)
        pump_result = pool.apply_async(pump_status)
        intruder_checker = multiprocessing.Process(motion_intruder_detect(), daemon=True)
        intruder_checker.start()
        sen_result.wait()
        pump_result.wait()
    except (KeyboardInterrupt,  SystemExit):
        LOGGER.info("Keyboard interrupt given, exiting ...")
    finally:
        LOGGER.info("Exiting all Programs")
        pool.terminate()
        pool.join()
        pool.close()
        intruder_checker.terminate()
        intruder_checker.join()
        intruder_checker.close()
        os._exit(0)

if __name__ == '__main__':
    main()