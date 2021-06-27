from __future__ import print_function
import logging
import numpy

import grpc

from . import uda_pb2
from . import uda_pb2_grpc

class UDA(object):
    def __init__(self, host='127.0.0.1', port=50051) -> None:
        super().__init__()
        logging.basicConfig()
        self._host = host
        self._port = str(port)
        self.channel = grpc.insecure_channel(target = self._host + ':' + self._port,
                                             options=[('grpc.lb_policy_name', 'pick_first'),
                                                      ('grpc.enable_retries', 0),
                                                      ('grpc.keepalive_timeout_ms', 10000)
                                                      ])
        self.experiment_stub = uda_pb2_grpc.ExperimentStub(self.channel)
        self.meta_stub = uda_pb2_grpc.MetaStub(self.channel)
        self.user_stub = uda_pb2_grpc.UserStub(self.channel)
        self.project_stub = uda_pb2_grpc.ProjectStub(self.channel)
        self.token = ''
    
    def Signal(self, exp, path, shot):
        signalrequest = uda_pb2.SignalRequest()
        signalrequest.experiment = exp
        signalrequest.path = path
        signalrequest.shot = shot
        signalresponse = self.experiment_stub.Signal(signalrequest, timeout = 30)
        return numpy.frombuffer(signalresponse.data, dtype=numpy.float32)

    def SignalByTime(self, exp, path, shot, start, end):
        sginaldatabytimerequest = uda_pb2.SignalByTimeRequest()
        sginaldatabytimerequest.experiment = exp
        sginaldatabytimerequest.path = path
        sginaldatabytimerequest.shot = shot
        sginaldatabytimerequest.start = start
        sginaldatabytimerequest.end = end
        signaldatabytimeresponse = self.experiment_stub.SignalByTime(sginaldatabytimerequest, timeout=30)
        return numpy.frombuffer(signaldatabytimeresponse.data, dtype=numpy.float32)

    def SignalList(self, exp):
        signallistrequest = uda_pb2.SignalListRequest()
        signallistrequest.experiment = exp;
        signallistresponse = self.meta_stub.SignalList(signallistrequest, timeout = 30)
        return signallistresponse.item

    def SignalMeta(self, exp, path, shot):
        singalmetarequest = uda_pb2.SignalMetaRequest()
        singalmetarequest.experiment = exp
        singalmetarequest.path = path
        singalmetarequest.shot = shot
        signalmetaresponse = self.meta_stub.SingalMeta(singalmetarequest, timeout = 30)
        return signalmetaresponse.details

    def SignalMonitor(self):
        empty = uda_pb2.Empty()
        signalmonitorresponse = self.project_stub.SignalMonitor(empty, timeout = 30)
        return signalmonitorresponse

    def SignalMonitorByTime(self, system, name, start, end):
        signalmonitorbytimerequest = uda_pb2.SignalMonitorByTimeRequest()
        signalmonitorbytimerequest.system = system;
        signalmonitorbytimerequest.name = name
        signalmonitorbytimerequest.start = start
        signalmonitorbytimerequest.end = end
        signalmonitorbytimeresponse = self.project_stub.SignalMonitorByTime(signalmonitorbytimerequest, timeout = 30)
        return signalmonitorbytimeresponse.data

    def SignalMonitorStruct(self):
        empty = uda_pb2.Empty()
        signalmonitorrequest = self.project_stub.SignalMonitorStruct(empty, timeout = 30)
        return signalmonitorrequest.item

    def Login(self, username, password) -> bool:
        loginrequest = uda_pb2.LoginRequest()
        loginrequest.username = username
        loginrequest.password = password
        loginreponse = self.user_stub.Login(loginrequest, timeout=30)
        self.token = loginreponse.token
        if self.token == '' or self.token.uda_pb2.Empty():
            return False
        return True


