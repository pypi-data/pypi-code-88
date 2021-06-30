from enum import Enum


class CfnResourceType(Enum):
    VPC = 'AWS::EC2::VPC'
    EC2_INSTANCE = 'AWS::EC2::Instance'
    SUBNET = 'AWS::EC2::Subnet'
    SECURITY_GROUP = 'AWS::EC2::SecurityGroup'
