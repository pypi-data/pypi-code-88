import datetime
import logging
import time
from .abstract_model_object import *

logger = logging.getLogger('microgue')


class AbstractExpiringModelObject(AbstractModelObject):
    expiration_seconds = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.expires_in and self.expires_in < int(time.mktime(datetime.datetime.now().timetuple())):
            logger.debug("########## {} Expired ##########".format(self.__class__.__name__))
            raise GetFailed('item expired')

    def insert(self):
        # add expires_in
        expires_in = datetime.datetime.now() + datetime.timedelta(seconds=self.expiration_seconds)
        self.expires_in = int(time.mktime(expires_in.timetuple()))
        super().insert()

    def update(self, *args, **kwargs):
        # add expires_in
        expires_in = datetime.datetime.now() + datetime.timedelta(seconds=self.expiration_seconds)
        self.expires_in = int(time.mktime(expires_in.timetuple()))
        super().update()
