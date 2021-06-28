import json

import grpc

from cql import commons_pb2, find_command_pb2, get_command_pb2
from server import server_service_pb2_grpc


class Cranky:
    _channel = None
    _stub = None

    def __init__(self, host="localhost", port="9876"):
        self._channel = grpc.insecure_channel("localhost:9876")
        self._stub = server_service_pb2_grpc.CrankDBStub(self._channel)

    def set(self, key, value):
        valType = type(value)
        data = commons_pb2.DataPacket(key=key)
        if valType == int:
            data.s64intVal = value
            data.dataType = commons_pb2.LONG
        elif valType == float:
            data.doubleVal = value
            data.dataType = commons_pb2.DOUBLE
        elif valType == str:
            data.stringVal = value
            data.dataType = commons_pb2.STRING
        elif valType == bool:
            data.doubleVal = value
            data.dataType = commons_pb2.DOUBLE
        elif valType == bytes:
            data.doubleVal = value
            data.dataType = commons_pb2.BYTES
        else:
            try:
                jsonVal = json.dumps(value)
            except:
                raise Exception("unsupported type value")
            data.jsonVal = jsonVal.encode("utf-8")
            data.dataType = commons_pb2.JSON

        resp = self._stub.Set(data)
        return resp

    def get(self, key):

        query = get_command_pb2.GetCommandRequest(key=key)
        response = self._stub.Get(query)

        return response

    def find(self, query):
        if type(query) != dict:
            raise Exception("query object should be of type dict")

        queryObj = json.dumps(query).encode("utf-8")
        result = []

        data = find_command_pb2.FindCommandRequest(Query=queryObj)

        for doc in self._stub.Find(data):
            result.append(doc)
        return result
