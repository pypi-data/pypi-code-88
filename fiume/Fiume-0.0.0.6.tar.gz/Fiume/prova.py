import unittest
from unittest.mock import Mock, MagicMock

import random
import time
import random

import Fiume.utils as utils
# import Fiume.metainfo_decoder as md
# import Fiume.state_machine as sm

import logging
logging.disable(logging.WARNING)

###############

metainfo = Mock(piece_size=10)
peer = Mock(address=("localhost", 50154))

# mcu = MasterControlUnit(global_bitmap=[])
# mcu.connected(peer_mock)

# mcu_queue_in  = self.mcu.queue_in
# mcu_queue_out = self.mcu.out_queues[peer_mock.address]

# mcu_queue_in.put(utils.M_PEER_HAS([1,2,3,4,5]))

        
class BasicsTestCase(unittest.TestCase):
    def test_bitmap_conversion(self):
        metainfo = Mock(piece_size=10)
        peer = Mock(address=("localhost", 50154))

        self.mcu = MasterControlUnit(global_bitmap=[])
        self.mcu.add_connection_to(peer_mock)

        master_queue  = self.mcu.master_queue
        queue_to_peer = self.mcu.get_queue(peer.address)

        master_queue.put(utils.M_PEER_HAS([1,2,3,4,5]))
        
