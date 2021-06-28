# -*- coding: utf-8 -*-
"""
Services for customerdataapi.
"""
from datetime import datetime

class ChangePlanService:
    """ Use case change of plan """
    FREE = 'free'
    BASIC = 'basic'
    PREMIUM = 'premium'

    def __init__(self, data, current_plan):
        self.data = data
        self.current_plan = current_plan
        self.new_plan = self.data['data']['SUBSCRIPTION']

    def execute(self):
        """ Entrypoint method """

        if self.current_plan == self.new_plan:
            return self.data

        if self.__upgrade_plan():
            return self.data

        if self.__downgrade_plan():
            return self.data

        return self.data

    def __upgrade_plan(self):
        """ Upgrade a plan """
        if self.__is_upgrade(self.current_plan, self.new_plan):

            self.data['data']['UPGRADE_DATE'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            if 'DOWNGRADE_DATE' in self.data['data']:
                del self.data['data']['DOWNGRADE_DATE']

            return True

        return False

    def __downgrade_plan(self):
        """ Downgrade a plan """
        if self.__is_downgrade(self.current_plan, self.new_plan):

            self.data['data']['DOWNGRADE_DATE'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            for key in self.data['data']['ENABLED_FEATURES']:
                self.data['data']['ENABLED_FEATURES'][key] = False

            if 'UPGRADE_DATE' in self.data['data']:
                del self.data['data']['UPGRADE_DATE']

            return True

        return False

    def __is_upgrade(self, current_plan, new_plan):
        """ Ensure upgrade is valid """
        if self.__upgrade_free_to_basic(current_plan, new_plan):
            return True
        if self.__upgrade_free_to_premium(current_plan, new_plan):
            return True
        return self.__upgrade_basic_to_premium(current_plan, new_plan)

    def __upgrade_free_to_basic(self, current_plan, new_plan):
        """  Ensure upgrade is valid from free to basic """
        return current_plan == self.FREE and new_plan == self.BASIC

    def __upgrade_free_to_premium(self, current_plan, new_plan):
        """  Ensure upgrade is valid from free to premium """
        return current_plan == self.FREE and new_plan == self.PREMIUM

    def __upgrade_basic_to_premium(self, current_plan, new_plan):
        """  Ensure upgrade is valid from basic to premium """
        return current_plan == self.BASIC and new_plan == self.PREMIUM

    def __is_downgrade(self, current_plan, new_plan):
        """ Ensure downgrade is valid """
        if self.__downgrade_basic_to_free(current_plan, new_plan):
            return True
        if self.__downgrade_premium_to_basic(current_plan, new_plan):
            return True
        return self.__downgrade_premium_to_free(current_plan, new_plan)

    def __downgrade_basic_to_free(self, current_plan, new_plan):
        """  Ensure downgrade is valid from basic to free """
        return current_plan == self.BASIC and new_plan == self.FREE

    def __downgrade_premium_to_basic(self, current_plan, new_plan):
        """  Ensure downgrade is valid from premium to basic """
        return current_plan == self.PREMIUM and new_plan == self.BASIC

    def __downgrade_premium_to_free(self, current_plan, new_plan):
        """  Ensure downgrade is valid from premium to free """
        return current_plan == self.PREMIUM and new_plan == self.FREE
