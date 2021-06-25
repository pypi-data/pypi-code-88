from localstack.utils.aws import aws_models
Euqso=super
EuqsA=None
EuqsM=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  Euqso(LambdaLayer,self).__init__(arn)
  self.cwd=EuqsA
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.EuqsM.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(RDSDatabase,self).__init__(EuqsM,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(RDSCluster,self).__init__(EuqsM,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(AppSyncAPI,self).__init__(EuqsM,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(AmplifyApp,self).__init__(EuqsM,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(ElastiCacheCluster,self).__init__(EuqsM,env=env)
class TransferServer(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(TransferServer,self).__init__(EuqsM,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(CloudFrontDistribution,self).__init__(EuqsM,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,EuqsM,env=EuqsA):
  Euqso(CodeCommitRepository,self).__init__(EuqsM,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
