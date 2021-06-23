import logging
from datetime import datetime
import random
def setup_logging(file):
    logging.basicConfig(format="%(message)s",filename=file,level=logging.DEBUG)
    logging.warning(datetime.now())
def log(message):
    logging.warning(message)

def log_status(counter,size,debug):
    percentage=(float(counter)/size)*100
    if debug and random.randint(0,100) %13 ==0:
        logging.warning(f"finished {percentage:2.2f}")

def log_matches(id,topic_id,debug):
    if debug and random.randint(0,100) %13 ==0:
        logging.warning(f"matched ontology topic id {topic_id} for {id}")
def log_size(dataset,size):
    logging.warning(f"size of {dataset} is {size}")