from localstack.utils.aws import aws_models
eiNVW=super
eiNVq=None
eiNVR=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  eiNVW(LambdaLayer,self).__init__(arn)
  self.cwd=eiNVq
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.eiNVR.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(RDSDatabase,self).__init__(eiNVR,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(RDSCluster,self).__init__(eiNVR,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(AppSyncAPI,self).__init__(eiNVR,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(AmplifyApp,self).__init__(eiNVR,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(ElastiCacheCluster,self).__init__(eiNVR,env=env)
class TransferServer(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(TransferServer,self).__init__(eiNVR,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(CloudFrontDistribution,self).__init__(eiNVR,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,eiNVR,env=eiNVq):
  eiNVW(CodeCommitRepository,self).__init__(eiNVR,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
