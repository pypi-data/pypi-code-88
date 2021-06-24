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
from web3.types import BlockIdentifier
from web3 import Web3

from moneyonchain.contract import ContractBase
from moneyonchain.changers import BaseChanger
from moneyonchain.governance import Governor


class UpgraderChanger(ContractBase):
    contract_name = 'UpgraderChanger'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/UpgraderChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/UpgraderChanger.bin'))

    mode = 'MoC'
    precision = 10 ** 18

    def __init__(self,
                 network_manager,
                 contract_name=None,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None):
        config_network = network_manager.config_network
        if not contract_address:
            raise ValueError("You need to pass contract address")

        super().__init__(network_manager,
                         contract_name=contract_name,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

    def new_implementation(self, block_identifier: BlockIdentifier = 'latest'):
        """Contract address output"""

        result = self.sc.newImplementation(block_identifier=block_identifier)

        return result

    def proxy(self, block_identifier: BlockIdentifier = 'latest'):
        """Contract address output"""

        result = self.sc.proxy(block_identifier=block_identifier)

        return result

    def upgrade_delegator(self, block_identifier: BlockIdentifier = 'latest'):
        """Contract address output"""

        result = self.sc.upgradeDelegator(block_identifier=block_identifier)

        return result


class RDOCUpgraderChanger(ContractBase):
    contract_name = 'RDOCUpgraderChanger'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/UpgraderChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/UpgraderChanger.bin'))

    mode = 'RDOC'
    precision = 10 ** 18

    def __init__(self,
                 network_manager,
                 contract_name=None,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None):
        config_network = network_manager.config_network
        if not contract_address:
            raise ValueError("You need to pass contract address")

        super().__init__(network_manager,
                         contract_name=contract_name,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

    def new_implementation(self, block_identifier: BlockIdentifier = 'latest'):
        """Contract address output"""

        result = self.sc.newImplementation(block_identifier=block_identifier)

        return result

    def proxy(self, block_identifier: BlockIdentifier = 'latest'):
        """Contract address output"""

        result = self.sc.proxy(block_identifier=block_identifier)

        return result

    def upgrade_delegator(self, block_identifier: BlockIdentifier = 'latest'):
        """Contract address output"""

        result = self.sc.upgradeDelegator(block_identifier=block_identifier)

        return result


class MoCIGovernorChanger(BaseChanger):
    contract_name = 'MoCIGovernorChanger'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCIGovernorChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCIGovernorChanger.bin'))

    mode = 'MoC'

    def constructor(self, contract_address, new_governor, execute_change=False, **tx_arguments):

        self.log.info("Deploying new contract...")

        tx_receipt = self.deploy(
            Web3.toChecksumAddress(contract_address),
            Web3.toChecksumAddress(new_governor),
            **tx_arguments)

        tx_receipt.info()
        tx_receipt.info_to_log()

        self.log.info("Deployed contract done!")
        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))

        if execute_change:
            self.log.info("Executing change....")
            governor = Governor(self.network_manager).from_abi()
            tx_receipt = governor.execute_change(tx_receipt.contract_address, **tx_arguments)
            self.log.info("Change successfull!")

        return tx_receipt


class SkipVotingProcessChange(BaseChanger):
    contract_name = 'SkipVotingProcessChange'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/SkipVotingProcessChange.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/SkipVotingProcessChange.bin'))

    mode = 'MoC'

    def constructor(self, voting_machine, i_governor, change_contract, execute_change=False, **tx_arguments):

        self.log.info("Deploying new contract...")

        tx_receipt = self.deploy(
            Web3.toChecksumAddress(voting_machine),
            Web3.toChecksumAddress(i_governor),
            Web3.toChecksumAddress(change_contract),
            **tx_arguments)

        tx_receipt.info()
        tx_receipt.info_to_log()

        self.log.info("Deployed contract done!")
        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))

        if execute_change:
            self.log.info("Executing change....")
            governor = Governor(self.network_manager).from_abi()
            tx_receipt = governor.execute_change(tx_receipt.contract_address, **tx_arguments)
            self.log.info("Change successfull!")

        return tx_receipt
