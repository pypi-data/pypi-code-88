from cloudrail.knowledge.context.aws.cfn.cfn_resource_status import CfnResourceStatus


class CfnResourceInfo:

    def __init__(self,
                 account: str,
                 region: str,
                 stack_id: str,
                 stack_name: str,
                 logical_resource_id: str,
                 physical_resource_id: str,
                 resource_type: str,
                 resource_status: CfnResourceStatus):
        self.account: str = account
        self.region: str = region
        self.stack_name: str = stack_name
        self.stack_id: str = stack_id
        self.logical_resource_id: str = logical_resource_id
        self.physical_resource_id: str = physical_resource_id
        self.resource_type: str = resource_type
        self.resource_status: CfnResourceStatus = resource_status
