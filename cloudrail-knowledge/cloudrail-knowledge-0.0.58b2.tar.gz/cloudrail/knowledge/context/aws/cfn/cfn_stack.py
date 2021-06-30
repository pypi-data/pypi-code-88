from typing import List, Tuple
from cloudrail.knowledge.context.aws.aws_resource import AwsResource
from cloudrail.knowledge.context.aws.service_name import AwsServiceAttributes, AwsServiceType, AwsServiceName


class CfnStack(AwsResource):
    """
        Attributes:
            arn: The ARN of the cfn stack resource.
            stack_name: The name of the cfn stack.
            stack_id: The id of the cfn stack.
            stack_parameters: The parameters key/value lists of the cfn stack.
    """
    def __init__(self,
                 account: str,
                 region: str,
                 arn: str,
                 stack_name: str,
                 stack_parameters: List[Tuple[str, str]]):
        super().__init__(account=account, region=region, tf_resource_type=AwsServiceName.NONE,
                         aws_service_attributes=AwsServiceAttributes(AwsServiceType.CLOUDFORMATION.value))
        self.arn: str = arn
        self.stack_name: str = stack_name
        self.stack_id: str = arn
        self.stack_parameters: List[Tuple[str, str]] = stack_parameters
        self.with_aliases(stack_name, arn)

    def get_keys(self) -> List[str]:
        return [self.stack_id]

    def get_name(self) -> str:
        return self.stack_name

    def get_id(self) -> str:
        return self.stack_id

    def get_arn(self) -> str:
        return self.arn

    def get_cloud_resource_url(self) -> str:
        return '{0}cloudformation/home?region={1}#/stacks/stackinfo?stackId={2}'\
            .format(self.AWS_CONSOLE_URL, self.region, self.stack_id)

    @property
    def is_tagable(self) -> bool:
        return False  # todo - stack resources tags or stack tags?
