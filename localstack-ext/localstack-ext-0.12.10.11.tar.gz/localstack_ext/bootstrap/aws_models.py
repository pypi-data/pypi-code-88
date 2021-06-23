from localstack.utils.aws import aws_models
yvuNT=super
yvuNV=None
yvuNL=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  yvuNT(LambdaLayer,self).__init__(arn)
  self.cwd=yvuNV
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.yvuNL.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(RDSDatabase,self).__init__(yvuNL,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(RDSCluster,self).__init__(yvuNL,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(AppSyncAPI,self).__init__(yvuNL,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(AmplifyApp,self).__init__(yvuNL,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(ElastiCacheCluster,self).__init__(yvuNL,env=env)
class TransferServer(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(TransferServer,self).__init__(yvuNL,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(CloudFrontDistribution,self).__init__(yvuNL,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,yvuNL,env=yvuNV):
  yvuNT(CodeCommitRepository,self).__init__(yvuNL,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
