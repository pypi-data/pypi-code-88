from localstack.utils.aws import aws_models
vIWCl=super
vIWCm=None
vIWCL=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  vIWCl(LambdaLayer,self).__init__(arn)
  self.cwd=vIWCm
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.vIWCL.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(RDSDatabase,self).__init__(vIWCL,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(RDSCluster,self).__init__(vIWCL,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(AppSyncAPI,self).__init__(vIWCL,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(AmplifyApp,self).__init__(vIWCL,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(ElastiCacheCluster,self).__init__(vIWCL,env=env)
class TransferServer(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(TransferServer,self).__init__(vIWCL,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(CloudFrontDistribution,self).__init__(vIWCL,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,vIWCL,env=vIWCm):
  vIWCl(CodeCommitRepository,self).__init__(vIWCL,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
