from localstack.utils.aws import aws_models
OGgNu=super
OGgNj=None
OGgNm=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  OGgNu(LambdaLayer,self).__init__(arn)
  self.cwd=OGgNj
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.OGgNm.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(RDSDatabase,self).__init__(OGgNm,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(RDSCluster,self).__init__(OGgNm,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(AppSyncAPI,self).__init__(OGgNm,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(AmplifyApp,self).__init__(OGgNm,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(ElastiCacheCluster,self).__init__(OGgNm,env=env)
class TransferServer(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(TransferServer,self).__init__(OGgNm,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(CloudFrontDistribution,self).__init__(OGgNm,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,OGgNm,env=OGgNj):
  OGgNu(CodeCommitRepository,self).__init__(OGgNm,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
