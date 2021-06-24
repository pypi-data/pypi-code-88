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

from moneyonchain.contract import ContractBase
from moneyonchain.moc import CommissionSplitter


class VENDORSCommissionSplitter(CommissionSplitter):
    contract_name = 'CommissionSplitter'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/CommissionSplitter.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/CommissionSplitter.bin'))

    mode = 'MoC'
    precision = 10 ** 18

    def moc_token(self, block_identifier: BlockIdentifier = 'latest'):
        """the address of MoC Token contract"""

        result = self.sc.mocToken(block_identifier=block_identifier)

        return result

    def moc_token_commission_address(self, block_identifier: BlockIdentifier = 'latest'):
        """the address in which the Moc Token commissions are sent"""

        result = self.sc.mocTokenCommissionsAddress(block_identifier=block_identifier)

        return result
