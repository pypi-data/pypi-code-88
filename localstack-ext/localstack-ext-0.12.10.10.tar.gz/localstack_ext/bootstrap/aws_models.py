from localstack.utils.aws import aws_models
dcLGI=super
dcLGN=None
dcLGf=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  dcLGI(LambdaLayer,self).__init__(arn)
  self.cwd=dcLGN
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.dcLGf.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(RDSDatabase,self).__init__(dcLGf,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(RDSCluster,self).__init__(dcLGf,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(AppSyncAPI,self).__init__(dcLGf,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(AmplifyApp,self).__init__(dcLGf,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(ElastiCacheCluster,self).__init__(dcLGf,env=env)
class TransferServer(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(TransferServer,self).__init__(dcLGf,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(CloudFrontDistribution,self).__init__(dcLGf,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,dcLGf,env=dcLGN):
  dcLGI(CodeCommitRepository,self).__init__(dcLGf,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
