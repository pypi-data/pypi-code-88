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
import logging

from web3.types import BlockIdentifier
from web3 import Web3
from moneyonchain.contract import ContractBase
from moneyonchain.transaction import receipt_to_log


class OwnableInterface(ContractBase):

    def owner(self, block_identifier: BlockIdentifier = 'latest'):
        """the address of the owner"""

        result = self.sc.owner(block_identifier=block_identifier)

        return result

    def is_owner(self, block_identifier: BlockIdentifier = 'latest'):
        """true if `msg.sender` is the owner of the contract."""

        result = self.sc.isOwner(block_identifier=block_identifier)

        return result

    def transfer_ownership(self,
                           new_owner,
                           **tx_arguments):
        """
        Allows the current owner to transfer control of the contract to a newOwner.
        new_owner The address to transfer ownership to.
        """

        tx_args = self.tx_arguments(**tx_arguments)

        tx_receipt = self.sc.transferOwnership(Web3.toChecksumAddress(new_owner), tx_args)

        tx_receipt.info()
        receipt_to_log(tx_receipt, self.log)

        return tx_receipt

    def renounce_ownership(self,
                           **tx_arguments):
        """
        Allows the current owner to relinquish control of the contract.
        Renouncing to ownership will leave the contract without an owner.
        It will not be possible to call the functions with the `onlyOwner`
        """

        tx_args = self.tx_arguments(**tx_arguments)

        tx_receipt = self.sc.renounceOwnership(tx_args)

        tx_receipt.info()
        receipt_to_log(tx_receipt, self.log)

        return tx_receipt


class Governor(OwnableInterface):

    contract_name = 'Governor'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'
    precision = 10 ** 18

    def __init__(self,
                 network_manager,
                 contract_name=None,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None):

        if not contract_address:
            config_network = network_manager.config_network
            contract_address = network_manager.options['networks'][config_network]['addresses']['governor']

        super().__init__(network_manager,
                         contract_name=contract_name,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

    def execute_change(self,
                       contract_address,
                       **tx_arguments):
        """
        Function to be called to make the changes in changeContract
        changeContract Address of the contract that will execute the changes
        """

        tx_args = self.tx_arguments(**tx_arguments)

        tx_receipt = self.sc.executeChange(Web3.toChecksumAddress(contract_address), tx_args)

        tx_receipt.info()
        receipt_to_log(tx_receipt, self.log)

        return tx_receipt

    def is_authorized_changer(self,
                              contract_address,
                              block_identifier: BlockIdentifier = 'latest'):
        """
        Returns true if the _changer address is currently authorized to make
        changes within the system.
        contract_address Address of the contract that will be tested
        """

        result = self.sc.isAuthorizedChanger(Web3.toChecksumAddress(contract_address),
                                             block_identifier=block_identifier)

        return result


class BlockableGovernor(Governor):
    """
    Base contract to be able to define a blockable contract. The blocked contract
    is blocked until a certain date. That date cannot be changed while the contract is blocked so
    it is guaranteed that you will be blocked until that date
    """

    contract_name = 'Governor'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/BlockableGovernor.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/BlockableGovernor.bin'))

    mode = 'MoC'
    precision = 10 ** 18

    def unblock_date(self, block_identifier: BlockIdentifier = 'latest'):
        """Return unblock date"""

        result = self.sc.unblockDate(block_identifier=block_identifier)

        return result

    def is_blocked(self, block_identifier: BlockIdentifier = 'latest'):
        """Return bool"""

        result = self.sc.isBlocked(block_identifier=block_identifier)

        return result

    def is_authorized_to_block(self,
                               contract_address,
                               block_identifier: BlockIdentifier = 'latest'):
        """
        Blocks the governor until unblockAt
        @dev The new threshold should be big enough to block the governor after the tx and the contract should not be blocked, but that is enforced
        in the executeChange function which ALWAYS should be called before calling this function because it is the only one authorizing a changer
        newUnblockDate Timestamp of the next threshold that should be passed before the governor is active
        again
        """

        result = self.sc.isAuthorizedToBlock(Web3.toChecksumAddress(contract_address),
                                             block_identifier=block_identifier)

        return result

    def block_until(self,
                    new_unblock_date,
                    **tx_arguments):
        """
        Blocks the governor until unblockAt
        @dev The new threshold should be big enough to block the governor after the tx and the contract should not be blocked, but that is enforced
        in the executeChange function which ALWAYS should be called before calling this function because it is the only one authorizing a changer
         newUnblockDate Timestamp of the next threshold that should be passed before the governor is active
        again
        """

        tx_args = self.tx_arguments(**tx_arguments)

        tx_receipt = self.sc.blockUntil(new_unblock_date, tx_args)

        tx_receipt.info()
        receipt_to_log(tx_receipt, self.log)

        return tx_receipt


class DEXGovernor(Governor):

    contract_name = 'Governor'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'DEX'
    precision = 10 ** 18


class RDOCGovernor(Governor):

    contract_name = 'Governor'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'RDoC'
    precision = 10 ** 18
