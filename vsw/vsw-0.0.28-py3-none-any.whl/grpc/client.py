from __future__ import print_function
import logging
import grpc

import sys

from vsw.grpc import vsw_pb2_grpc, vsw_pb2

sys.path.append("vsw")


def run():
    logging.basicConfig()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = vsw_pb2_grpc.VswStub(channel)
        response = stub.Notification(vsw_pb2.Request(
            state='Verified'
        ))
    print(f'code: {response.code}, msg:{response.msg}')
