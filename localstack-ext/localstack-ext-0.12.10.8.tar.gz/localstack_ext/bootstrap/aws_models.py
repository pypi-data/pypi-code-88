from localstack.utils.aws import aws_models
eUJuT=super
eUJuo=None
eUJut=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  eUJuT(LambdaLayer,self).__init__(arn)
  self.cwd=eUJuo
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.eUJut.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(RDSDatabase,self).__init__(eUJut,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(RDSCluster,self).__init__(eUJut,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(AppSyncAPI,self).__init__(eUJut,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(AmplifyApp,self).__init__(eUJut,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(ElastiCacheCluster,self).__init__(eUJut,env=env)
class TransferServer(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(TransferServer,self).__init__(eUJut,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(CloudFrontDistribution,self).__init__(eUJut,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,eUJut,env=eUJuo):
  eUJuT(CodeCommitRepository,self).__init__(eUJut,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
