from localstack.utils.aws import aws_models
gLPmX=super
gLPmE=None
gLPmH=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  gLPmX(LambdaLayer,self).__init__(arn)
  self.cwd=gLPmE
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.gLPmH.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(RDSDatabase,self).__init__(gLPmH,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(RDSCluster,self).__init__(gLPmH,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(AppSyncAPI,self).__init__(gLPmH,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(AmplifyApp,self).__init__(gLPmH,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(ElastiCacheCluster,self).__init__(gLPmH,env=env)
class TransferServer(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(TransferServer,self).__init__(gLPmH,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(CloudFrontDistribution,self).__init__(gLPmH,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,gLPmH,env=gLPmE):
  gLPmX(CodeCommitRepository,self).__init__(gLPmH,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
