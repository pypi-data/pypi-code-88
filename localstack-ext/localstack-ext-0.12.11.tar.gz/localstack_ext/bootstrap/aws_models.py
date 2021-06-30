from localstack.utils.aws import aws_models
ydjqT=super
ydjqC=None
ydjqk=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ydjqT(LambdaLayer,self).__init__(arn)
  self.cwd=ydjqC
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.ydjqk.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(RDSDatabase,self).__init__(ydjqk,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(RDSCluster,self).__init__(ydjqk,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(AppSyncAPI,self).__init__(ydjqk,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(AmplifyApp,self).__init__(ydjqk,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(ElastiCacheCluster,self).__init__(ydjqk,env=env)
class TransferServer(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(TransferServer,self).__init__(ydjqk,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(CloudFrontDistribution,self).__init__(ydjqk,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,ydjqk,env=ydjqC):
  ydjqT(CodeCommitRepository,self).__init__(ydjqk,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
