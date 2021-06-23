import boto3, json, logging
from awsSchema.apigateway import Event,Response
from jsonschema import ValidationError
from nicHelper.schema import validateUrl



def removeNone(data):
    return { k:v for k, v in data.items() if v is not None }

class LogFunction:
  def __init__(self, stackName= 'villa-wallet-log-master', user=None, pw=None, sessionToken=None, region='ap-southeast-1'):
    self.lambdaClient = boto3.client(
        'lambda',
        aws_access_key_id = user,
        aws_secret_access_key = pw ,
        aws_session_token = sessionToken,
        region_name = region
      )
    self.stackName = stackName

  def invoke(self, functionName, data:dict, invocationType:str = 'Event'):
    inputData=Event.getInput(data)
    response = self.lambdaClient.invoke(
        FunctionName = functionName,
        InvocationType = invocationType,
        Payload=json.dumps(inputData)
    )
    print(response)
    if invocationType == 'Event': return True
    return json.loads(response['Payload'].read())



  def getLog(self, data:dict):
    functionName = f'{self.stackName}-get'
    return self.invoke(functionName = functionName, data=data, invocationType = 'RequestResponse')
    
  def setLog(self, data:dict)->bool:
    error = ''
    url = 'https://raw.githubusercontent.com/thanakijwanavit/villaMasterSchema/master/wallet/log/log.yaml'
    try:
        validateUrl(url, data, format_='yaml')
        success = 1
    except ValidationError as e:
        print('wrong schema')
        error = f'wrong schema {e}'
    functionName = f'{self.stackName}-create'
    result =  self.invoke(functionName = functionName, data=data)
    if error:
        raise ValidationError(error)
    return result
