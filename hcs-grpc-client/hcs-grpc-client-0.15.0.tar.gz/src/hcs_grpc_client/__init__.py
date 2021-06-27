import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from ConsensusService_pb2 import (
    ConsensusTopicQuery,
    ConsensusTopicResponse,
    )
from BasicTypes_pb2 import TopicID
from Timestamp_pb2 import Timestamp, TimestampSeconds
from ConsensusService_pb2_grpc import ConsensusServiceStub
