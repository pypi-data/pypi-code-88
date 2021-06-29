from cloudplatform_sdks.tencentcloud_models import TencentCfs
# from cloudplatform_sdks.alicloud_models import AliCdnDomain

if __name__ == '__main__':
    # resp = TencentCfs.create(Zone="ap-shanghai-2", NetInterface="VPC", PGroupId="pgroupbasic", Protocol="NFS",
    #                   FsName="CYAN_test", VpcId="vpc-lo3ingay", SubnetId="subnet-gmow4lhv")
    # print(resp)
    # resp = TencentCfs.list()
    # print(resp)
    # print(resp[0].delete())
    # TencentCfs.create()
    cfs_list = TencentCfs.list()
    print(cfs_list[0])