from localstack.utils.aws import aws_models
tjeHX=super
tjeHA=None
tjeHO=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  tjeHX(LambdaLayer,self).__init__(arn)
  self.cwd=tjeHA
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.tjeHO.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(RDSDatabase,self).__init__(tjeHO,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(RDSCluster,self).__init__(tjeHO,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(AppSyncAPI,self).__init__(tjeHO,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(AmplifyApp,self).__init__(tjeHO,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(ElastiCacheCluster,self).__init__(tjeHO,env=env)
class TransferServer(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(TransferServer,self).__init__(tjeHO,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(CloudFrontDistribution,self).__init__(tjeHO,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,tjeHO,env=tjeHA):
  tjeHX(CodeCommitRepository,self).__init__(tjeHO,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
