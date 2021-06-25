from localstack.utils.aws import aws_models
kxwId=super
kxwIv=None
kxwIE=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  kxwId(LambdaLayer,self).__init__(arn)
  self.cwd=kxwIv
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.kxwIE.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(RDSDatabase,self).__init__(kxwIE,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(RDSCluster,self).__init__(kxwIE,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(AppSyncAPI,self).__init__(kxwIE,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(AmplifyApp,self).__init__(kxwIE,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(ElastiCacheCluster,self).__init__(kxwIE,env=env)
class TransferServer(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(TransferServer,self).__init__(kxwIE,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(CloudFrontDistribution,self).__init__(kxwIE,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,kxwIE,env=kxwIv):
  kxwId(CodeCommitRepository,self).__init__(kxwIE,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
