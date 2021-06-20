
from radware.sdk.beans_common import *


class EnumSecurityModel(BaseBeanEnum):
    SNMPv1 = 1
    SNMPv2c = 2
    UserBased = 3


class vacmSecurityToGroupTable(DeviceBean):
    def __init__(self, **kwargs):
        self.Model = EnumSecurityModel.enum(kwargs.get('Model', None))
        self.UsmUserName = kwargs.get('UsmUserName', None)
        self.GroupName = kwargs.get('GroupName', None)
        self.GroupStorageType = kwargs.get('GroupStorageType', None)
        self.GroupStatus = kwargs.get('GroupStatus', None)

    def get_indexes(self):
        return self.Index,
    
    @classmethod
    def get_index_names(cls):
        return 'Index',

