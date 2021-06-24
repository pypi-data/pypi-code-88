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
from web3 import Web3
from web3.types import BlockIdentifier

from moneyonchain.contract import ContractBase
from moneyonchain.governance import GovernedInterface, ProxyAdminInterface


BUCKET_X2 = '0x5832000000000000000000000000000000000000000000000000000000000000'
BUCKET_C0 = '0x4330000000000000000000000000000000000000000000000000000000000000'


class MoCBProxManagerBase(ProxyAdminInterface, GovernedInterface):
    contract_name = 'MoCBProxManager'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCBProxManager.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCBProxManager.bin'))

    precision = 10 ** 18
    mode = 'MoC'
    project = 'MoC'

    def __init__(self,
                 network_manager,
                 contract_name=None,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None):
        if not contract_address:
            config_network = network_manager.config_network
            contract_address = network_manager.options['networks'][config_network]['addresses']['MoCBProxManager']

        super().__init__(network_manager,
                         contract_name=contract_name,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

    def available_bucket(self,
                         bucket=None,
                         formatted: bool = True,
                         block_identifier: BlockIdentifier = 'latest'):
        """ available_bucket """

        if not bucket:
            bucket = BUCKET_X2

        result = self.sc.isAvailableBucket(bucket, block_identifier=block_identifier)

        return result

    def bprox_balanceof(self,
                        bucket,
                        account_address,
                        formatted: bool = True,
                        block_identifier: BlockIdentifier = 'latest'):
        """ returns user balance """

        if not bucket:
            bucket = BUCKET_X2

        result = self.sc.bproxBalanceOf(bucket,
                                        Web3.toChecksumAddress(account_address),
                                        block_identifier=block_identifier)

        return result

    def has_valid_balance(self,
                          bucket,
                          account_address,
                          index,
                          formatted: bool = True,
                          block_identifier: BlockIdentifier = 'latest'):
        """ verifies that this user has assigned balance for the given bucket """

        if not bucket:
            bucket = BUCKET_X2

        result = self.sc.hasValidBalance(
            bucket,
            Web3.toChecksumAddress(account_address),
            index,
            block_identifier=block_identifier)

        return result

    def active_address_count(self,
                             bucket=None,
                             formatted: bool = True,
                             block_identifier: BlockIdentifier = 'latest'):
        """ Returns all the address that currently have riskProx position for this bucket """

        if not bucket:
            bucket = BUCKET_X2

        result = self.sc.getActiveAddressesCount(bucket, block_identifier=block_identifier)

        return result
