from ibmcloud_python_sdk.vpc import vpc as icv

# Intentiate the class
vpc = icv.Vpc()

# Retrieve a complete VPC list
vpc.get_vpcs()

# Retrieve specific VPC (generic)
vpc.get_vpc("ibmcloud-vpc-baby")

# Retrieve address prefixes
vpc.get_address_prefixes()

# Retrieve address prefixes
vpc.get_address_prefixes("ibmcloud-vpc-baby")

vpc.get_address_prefix("ibmcloud-vpc-baby",
                       "ibmcloud-vpc-address-prefix-baby")

# Delete VPC
vpc.delete_vpc("ibmcloud-vpc-baby")
