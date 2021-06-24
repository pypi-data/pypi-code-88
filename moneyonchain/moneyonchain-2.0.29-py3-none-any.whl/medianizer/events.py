"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

from web3 import Web3
from web3.exceptions import BlockNotFound
import datetime

from moneyonchain.events import BaseEvent


# FeedFactory.sol


class EventCreated(BaseEvent):

    name = "Created"

    def __init__(self, event):

        self.blockNumber = event['blockNumber']
        self.transactionHash = event['transactionHash']
        self.timestamp = event['timestamp']
        self.event = event['event'][self.name]

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Sender', 'Price Feeder']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['sender'] = self.event['sender']
        d_event['feed'] = self.event['feed']

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['sender'],
                d_event['feed']]
