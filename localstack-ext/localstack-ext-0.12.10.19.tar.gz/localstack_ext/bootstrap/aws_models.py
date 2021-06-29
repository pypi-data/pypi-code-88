from localstack.utils.aws import aws_models
kbtmj=super
kbtma=None
kbtmO=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  kbtmj(LambdaLayer,self).__init__(arn)
  self.cwd=kbtma
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.kbtmO.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(RDSDatabase,self).__init__(kbtmO,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(RDSCluster,self).__init__(kbtmO,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(AppSyncAPI,self).__init__(kbtmO,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(AmplifyApp,self).__init__(kbtmO,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(ElastiCacheCluster,self).__init__(kbtmO,env=env)
class TransferServer(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(TransferServer,self).__init__(kbtmO,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(CloudFrontDistribution,self).__init__(kbtmO,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,kbtmO,env=kbtma):
  kbtmj(CodeCommitRepository,self).__init__(kbtmO,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
