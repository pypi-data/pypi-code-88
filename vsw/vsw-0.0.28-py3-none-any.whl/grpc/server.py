from concurrent import futures
import logging
import grpc

import sys

from vsw.grpc import vsw_pb2_grpc, vsw_pb2

sys.path.append("vsw")


class Vsw(vsw_pb2_grpc.VswServicer):

    def Notification(self, request, context):
        print(f"grpc status: {request.state}")
        return vsw_pb2.Reply(code=0, msg='ok')


def serve():
    logging.basicConfig()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    vsw_pb2_grpc.add_VswServicer_to_server(Vsw(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

