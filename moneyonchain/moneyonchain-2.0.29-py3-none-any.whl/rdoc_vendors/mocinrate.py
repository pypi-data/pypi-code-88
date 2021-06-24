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
from moneyonchain.rdoc import RDOCMoCInrate


class VENDORSRDOCMoCInrate(RDOCMoCInrate):
    contract_name = 'MoCInrate'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.bin'))

    precision = 10 ** 18
    mode = 'RRC20'
    project = 'RDoC'

    def commision_rate(self,
                       formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):
        """Gets commision rate"""

        raise Exception('DEPRECATED')

    def commission_rate_by_transaction_type(
            self,
            tx_type,
            formatted: bool = True,
            block_identifier: BlockIdentifier = 'latest'):
        """Gets commision rate by transaction type from mapping"""

        result = self.sc.commissionRatesByTxType(tx_type, block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_commission_value(
            self,
            amount,
            tx_type,
            formatted: bool = True):
        """ Calc commission value amount in ether float"""

        result = self.sc.calcCommissionValue(int(amount * self.precision), tx_type)

        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calculate_vendor_markup(
            self,
            vendor_account,
            amount,
            formatted: bool = True):
        """ Calc vendor markup in ether float"""

        result = self.sc.calculateVendorMarkup(vendor_account, int(amount * self.precision))

        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def tx_type_mint_riskpro_fees_reserve(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.MINT_RISKPRO_FEES_RESERVE(block_identifier=block_identifier)

        return result

    def tx_type_redeem_riskpro_fees_reserve(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.REDEEM_RISKPRO_FEES_RESERVE(block_identifier=block_identifier)

        return result

    def tx_type_mint_stabletoken_fees_reserve(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.MINT_STABLETOKEN_FEES_RESERVE(block_identifier=block_identifier)

        return result

    def tx_type_redeem_stabletoken_fees_reserve(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.REDEEM_STABLETOKEN_FEES_RESERVE(block_identifier=block_identifier)

        return result

    def tx_type_mint_riskprox_fees_reserve(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.MINT_RISKPROX_FEES_RESERVE(block_identifier=block_identifier)

        return result

    def tx_type_redeem_riskprox_fees_reserve(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.REDEEM_RISKPROX_FEES_RESERVE(block_identifier=block_identifier)

        return result

    def tx_type_mint_riskpro_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.MINT_RISKPRO_FEES_MOC(block_identifier=block_identifier)

        return result

    def tx_type_redeem_riskpro_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.REDEEM_RISKPRO_FEES_MOC(block_identifier=block_identifier)

        return result

    def tx_type_mint_stabletoken_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.MINT_STABLETOKEN_FEES_MOC(block_identifier=block_identifier)

        return result

    def tx_type_redeem_stabletoken_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.REDEEM_STABLETOKEN_FEES_MOC(block_identifier=block_identifier)

        return result

    def tx_type_mint_riskprox_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.MINT_RISKPROX_FEES_MOC(block_identifier=block_identifier)

        return result

    def tx_type_redeem_riskprox_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):
        result = self.sc.REDEEM_RISKPROX_FEES_MOC(block_identifier=block_identifier)

        return result
