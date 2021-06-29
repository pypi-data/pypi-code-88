
from .clients import hw_vpc_client


class HuaweiVpc:

    def __init__(self, object):
        self.object = object

    @property
    def id(self):
        return self.object.id

    @property
    def name(self):
        return self.object.name

    @property
    def cidr(self):
        return self.object.cidr

    @classmethod
    def get(cls, vpc_id=None):
        vpcs = hw_vpc_client.list_vpc(vpc_id)
        if not vpcs:
            return
        return cls(vpcs[0])


class HuaweiSubnet:

    def __init__(self, object):
        self.object = object

    @property
    def id(self):
        return self.object.id

    @property
    def name(self):
        return self.object.name

    @property
    def vpc_id(self):
        return self.object.vpc_id

    @property
    def availability_zone(self):
        return self.object.availability_zone

    @property
    def cidr(self):
        return self.object.cidr

    @property
    def dns_list(self):
        return self.object.dns_list

    @classmethod
    def get(cls, vpc_id=None, subnet_id=None):
        subnets = hw_vpc_client.list_subnet(vpc_id)
        if not subnets:
            return
        for subnet in subnets:
            if subnet.id == subnet_id:
                return cls(subnet)

    @classmethod
    def create(cls, params=None):
        create_response = hw_vpc_client.create_subnet(body_params=params)
        if not create_response:
            return
        return create_response.subnet

    def delete(self):
        return hw_vpc_client.delete_subnet(vpc_id=self.vpc_id, subnet_id=self.id)
