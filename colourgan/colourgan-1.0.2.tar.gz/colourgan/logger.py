'''Logger for Complete Project.'''
import logging
import os

logging.basicConfig(
    format='%(asctime)s - ColourGAN - %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)
logger = logging.getLogger(__name__)

# if not os.path.exists('logs'):
#     os.mkdir('logs')
#
# file = open(os.path.join('logs','log_history.txt') , 'w')

def log(message, info = 'ColourGAN'):
    # Something Else
    logger.info(message)
    # file.write(info + ' : ' +  message + '\n')
    return
