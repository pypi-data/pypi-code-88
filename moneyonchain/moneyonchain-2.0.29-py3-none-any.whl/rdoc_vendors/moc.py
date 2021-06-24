"""
        GNU AFFERO GENERAL PUBLIC LICENSE
           Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN
 @2020
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import os
from decimal import Decimal
from web3 import Web3
from web3.types import BlockIdentifier
import math

from moneyonchain.contract import ContractBase
from moneyonchain.rdoc import RDOCMoC
from moneyonchain.transaction import receipt_to_log

from .mocconnector import VENDORSRDOCMoCConnector
from .mocinrate import VENDORSRDOCMoCInrate
from .mocstate import VENDORSRDOCMoCState
from .mocexchange import VENDORSRDOCMoCExchange
from .mocsettlement import VENDORSRDOCMoCSettlement
from .mocvendors import VENDORSRDOCMoCVendors

from moneyonchain.tokens import RIFPro, RIFDoC, RIF, MoCToken


STATE_LIQUIDATED = 0
STATE_BPRO_DISCOUNT = 1
STATE_BELOW_COBJ = 2
STATE_ABOVE_COBJ = 3

BUCKET_X2 = '0x5832000000000000000000000000000000000000000000000000000000000000'
BUCKET_C0 = '0x4330000000000000000000000000000000000000000000000000000000000000'

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'


class VENDORSRDOCMoC(RDOCMoC):
    contract_name = 'MoC'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoC.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoC.bin'))

    precision = 10 ** 18
    mode = 'RRC20'
    project = 'RDoC'
    minimum_amount = Decimal(0.00000001)

    def __init__(self,
                 network_manager,
                 contract_name=None,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None,
                 contract_address_moc_state=None,
                 contract_address_moc_inrate=None,
                 contract_address_moc_exchange=None,
                 contract_address_moc_connector=None,
                 contract_address_moc_settlement=None,
                 contract_address_moc_bpro_token=None,
                 contract_address_moc_doc_token=None,
                 contract_address_reserve_token=None,
                 contract_address_moc_moc_token=None,
                 contract_address_moc_vendors=None,
                 load_sub_contract=True):

        config_network = network_manager.config_network
        if not contract_address:
            contract_address = network_manager.options['networks'][config_network]['addresses']['MoC']

        super().__init__(network_manager,
                         contract_name=contract_name,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin,
                         contract_address_moc_state=contract_address_moc_state,
                         contract_address_moc_inrate=contract_address_moc_inrate,
                         contract_address_moc_exchange=contract_address_moc_exchange,
                         contract_address_moc_connector=contract_address_moc_connector,
                         contract_address_moc_settlement=contract_address_moc_settlement,
                         contract_address_moc_bpro_token=contract_address_moc_bpro_token,
                         contract_address_moc_doc_token=contract_address_moc_doc_token,
                         load_sub_contract=False
                         )

        if load_sub_contract:
            contract_addresses = dict()
            contract_addresses['MoCState'] = contract_address_moc_state
            contract_addresses['MoCInrate'] = contract_address_moc_inrate
            contract_addresses['MoCExchange'] = contract_address_moc_exchange
            contract_addresses['MoCConnector'] = contract_address_moc_connector
            contract_addresses['MoCSettlement'] = contract_address_moc_settlement
            contract_addresses['BProToken'] = contract_address_moc_bpro_token
            contract_addresses['DoCToken'] = contract_address_moc_doc_token
            contract_addresses['ReserveToken'] = contract_address_reserve_token
            contract_addresses['MoCToken'] = contract_address_moc_moc_token
            contract_addresses['MoCVendors'] = contract_address_moc_vendors

            # load contract addresses
            self.load_sub_contracts(contract_addresses)

    def load_sub_contracts(self, contract_addresses):

        # load contract moc connector
        self.sc_moc_connector = self.load_moc_connector_contract(contract_addresses['MoCConnector'])

        # load contract moc state
        self.sc_moc_state = self.load_moc_state_contract(contract_addresses['MoCState'])

        # load contract moc inrate
        self.sc_moc_inrate = self.load_moc_inrate_contract(contract_addresses['MoCInrate'])

        # load contract moc exchange
        self.sc_moc_exchange = self.load_moc_exchange_contract(contract_addresses['MoCExchange'])

        # load contract moc settlement
        self.sc_moc_settlement = self.load_moc_settlement_contract(contract_addresses['MoCSettlement'])

        # load contract moc bpro_token
        self.sc_moc_bpro_token = self.load_moc_bpro_token_contract(contract_addresses['BProToken'])

        # load contract moc doc_token
        self.sc_moc_doc_token = self.load_moc_doc_token_contract(contract_addresses['DoCToken'])

        # load_reserve_token_contract
        self.sc_reserve_token = self.load_reserve_token_contract(contract_addresses['ReserveToken'])

        # load contract moc moc_token
        if contract_addresses['MoCToken']:
            self.sc_moc_moc_token = self.load_moc_moc_token_contract(contract_addresses['MoCToken'])
        else:
            self.sc_moc_moc_token = self.load_moc_moc_token_contract(self.sc_moc_state.moc_token())

        # load contract moc vendors
        if contract_addresses['MoCVendors']:
            self.sc_moc_vendors = self.load_moc_vendors_contract(contract_addresses['MoCVendors'])
        else:
            self.sc_moc_vendors = self.load_moc_vendors_contract(self.sc_moc_state.moc_vendors())

    def contracts_discovery(self):
        """ This implementation get sub contracts only with MoC Contract address"""

        contract_addresses = dict()
        contract_addresses['MoCConnector'] = self.connector()
        self.sc_moc_connector = self.load_moc_connector_contract(contract_addresses['MoCConnector'])
        connector_addresses = self.connector_addresses()
        contract_addresses['MoCState'] = connector_addresses['MoCState']
        contract_addresses['MoCInrate'] = connector_addresses['MoCInrate']
        contract_addresses['MoCExchange'] = connector_addresses['MoCExchange']
        contract_addresses['MoCSettlement'] = connector_addresses['MoCSettlement']
        contract_addresses['BProToken'] = connector_addresses['BProToken']
        contract_addresses['DoCToken'] = connector_addresses['DoCToken']
        contract_addresses['ReserveToken'] = connector_addresses['ReserveToken']
        contract_addresses['MoCToken'] = None
        contract_addresses['MoCVendors'] = None

        self.load_sub_contracts(contract_addresses)

        return self

    def load_moc_inrate_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCInrate']

        sc = VENDORSRDOCMoCInrate(self.network_manager,
                              contract_address=contract_address).from_abi()

        return sc

    def load_moc_state_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCState']

        sc = VENDORSRDOCMoCState(self.network_manager,
                             contract_address=contract_address).from_abi()

        return sc

    def load_moc_exchange_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCExchange']

        sc = VENDORSRDOCMoCExchange(self.network_manager,
                                contract_address=contract_address).from_abi()

        return sc

    def load_moc_connector_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCConnector']

        sc = VENDORSRDOCMoCConnector(self.network_manager,
                          contract_address=contract_address).from_abi()

        return sc

    def load_moc_settlement_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCSettlement']

        sc = VENDORSRDOCMoCSettlement(self.network_manager,
                                  contract_address=contract_address).from_abi()

        return sc

    def load_moc_bpro_token_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['BProToken']

        sc = RIFPro(self.network_manager,
                    contract_address=contract_address).from_abi()

        return sc

    def load_moc_doc_token_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['DoCToken']

        sc = RIFDoC(self.network_manager,
                    contract_address=contract_address).from_abi()

        return sc

    def load_reserve_token_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['ReserveToken']

        sc = RIF(self.network_manager,
                 contract_address=contract_address).from_abi()

        return sc

    def load_moc_moc_token_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCToken']

        sc = MoCToken(self.network_manager,
                      contract_address=contract_address).from_abi()

        return sc

    def load_moc_vendors_contract(self, contract_address):

        config_network = self.network_manager.config_network
        if not contract_address:
            contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCVendors']

        sc = VENDORSRDOCMoCVendors(self.network_manager,
                               contract_address=contract_address).from_abi()

        return sc

    def moc_price(self,
                  formatted: bool = True,
                  block_identifier: BlockIdentifier = 'latest'):
        """MoC price in USD"""

        result = self.sc_moc_state.moc_price(
            formatted=formatted,
            block_identifier=block_identifier)

        return result

    def moc_balance_of(self,
                       account_address,
                       formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):

        return self.sc_moc_moc_token.balance_of(
            account_address,
            formatted=formatted,
            block_identifier=block_identifier)

    def moc_allowance(self,
                      account_address,
                      contract_address,
                      formatted: bool = True,
                      block_identifier: BlockIdentifier = 'latest'):

        return self.sc_moc_moc_token.allowance(
            account_address,
            contract_address,
            formatted=formatted,
            block_identifier=block_identifier)
