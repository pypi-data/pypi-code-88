from localstack.utils.aws import aws_models
xzLSr=super
xzLSe=None
xzLSR=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  xzLSr(LambdaLayer,self).__init__(arn)
  self.cwd=xzLSe
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.xzLSR.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(RDSDatabase,self).__init__(xzLSR,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(RDSCluster,self).__init__(xzLSR,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(AppSyncAPI,self).__init__(xzLSR,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(AmplifyApp,self).__init__(xzLSR,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(ElastiCacheCluster,self).__init__(xzLSR,env=env)
class TransferServer(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(TransferServer,self).__init__(xzLSR,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(CloudFrontDistribution,self).__init__(xzLSR,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,xzLSR,env=xzLSe):
  xzLSr(CodeCommitRepository,self).__init__(xzLSR,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
