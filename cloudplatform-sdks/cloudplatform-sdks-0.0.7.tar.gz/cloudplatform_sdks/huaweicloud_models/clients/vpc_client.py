from .client import HuaweiClient
from huaweicloudsdkvpc.v2 import VpcClient, ListVpcsRequest, ListSubnetsRequest, CreateSubnetRequest, \
    DeleteSubnetRequest
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion


class HuaweiVpcClient(HuaweiClient):
    def __init__(self, *args, **kwargs):
        super(HuaweiVpcClient, self).__init__(*args, **kwargs)

    @property
    def vpc_client(self):
        return self.generate_client(VpcClient, VpcRegion)

    def list_vpc(self, vpc_id=None):
        request = ListVpcsRequest(id=vpc_id)
        return self.vpc_client.list_vpcs(request).vpcs

    def list_subnet(self, vpc_id=None):
        request = ListSubnetsRequest(vpc_id=vpc_id)
        return self.vpc_client.list_subnets(request).subnets

    def create_subnet(self, body_params=None):
        request = CreateSubnetRequest(body=body_params)
        return self.vpc_client.create_subnet(request)

    def delete_subnet(self, vpc_id=None, subnet_id=None):
        request = DeleteSubnetRequest(vpc_id=vpc_id, subnet_id=subnet_id)
        return self.vpc_client.delete_subnet(request)
