
from sqlalchemy import engine_from_config
from sqlalchemy.exc import DisconnectionError,InvalidRequestError,OperationalError

import time
from datetime import datetime,timedelta
import queue,threading


from .sessionhandling import (engineFromSettings,factoryFormSettings,session_scope)

import logging
l = logging.getLogger(__name__)


#from pyramid.threadlocal import get_current_registry
#from pyramid.request import Request


def threaded_jobs(settings,threadqueue,mynumber,callback):
  factory = factoryFormSettings(settings)
  while True:
    l.debug("executor is looping")
    try:
      job = threadqueue.get(timeout=120.0)

      try:
        with session_scope(factory) as dbsession:
          callback(job,dbsession,factory)
      except (DisconnectionError, InvalidRequestError,OperationalError) as dbconnerror:
        l.exception("db connection died of unexpected violent death. Trying to revive it...")
        if job is not None:
          __incomingjobsqueue.put(job)
          l.info("putting the job back in queue {}".format(job))
        time.sleep(60)
        factory = factoryFormSettings(settings)
        raise dbconnerror
    except queue.Empty as nojob:
      l.debug("no job received")
    except Exception as e:
      l.exception("Exception, but still runing!")


__queuelock = threading.Semaphore()
__allqueues = {}
__defaultqueue = None

def getQueue(name=None):
  with __queuelock:
    if name is None:
      return __defaultqueue
    else:
      return __allqueues.get(name)

def __addQueue(queue,name):
  with __queuelock:
    global __defaultqueue
    if __defaultqueue is None:
      __defaultqueue = queue
    if name in __allqueues:
      raise Exception("Name {name} already assigned in queues".format(name=name))
    __allqueues[name] = queue


def startThread(settings,callback,name="executor",concurrent=1):
  threadqueue = queue.Queue()
  __addQueue  (threadqueue,name)
  for i in range(concurrent):
    x = threading.Thread(name=name,target=threaded_jobs, args=( settings,threadqueue,i,callback ) )
    x.setDaemon(True)
    x.start()
  return threadqueue


