from localstack.utils.aws import aws_models
AWiEp=super
AWiEo=None
AWiEK=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  AWiEp(LambdaLayer,self).__init__(arn)
  self.cwd=AWiEo
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.AWiEK.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(RDSDatabase,self).__init__(AWiEK,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(RDSCluster,self).__init__(AWiEK,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(AppSyncAPI,self).__init__(AWiEK,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(AmplifyApp,self).__init__(AWiEK,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(ElastiCacheCluster,self).__init__(AWiEK,env=env)
class TransferServer(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(TransferServer,self).__init__(AWiEK,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(CloudFrontDistribution,self).__init__(AWiEK,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,AWiEK,env=AWiEo):
  AWiEp(CodeCommitRepository,self).__init__(AWiEK,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
