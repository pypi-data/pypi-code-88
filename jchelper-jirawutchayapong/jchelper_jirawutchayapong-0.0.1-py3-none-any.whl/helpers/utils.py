import json
import random
import string
import datetime as dt

class ReturnDict:
    def __init__(self, message="", statusCode=400, data={}):
        self.message = message
        self.statusCode = statusCode
        self.data = data
        
    def toReturnCommon(self)->dict:
        return Utils.returnCommon(
            statusCode = self.statusCode,
            message = self.message,
            data = self.data
        )
    
class ModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'attribute_values'):
            return obj.attribute_values
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

class Utils:
    @staticmethod
    def returnCommon(message, statusCode=400, data={})->dict:
        return {
            "statusCode": statusCode,
            "message": message,
            "data": json.dumps(data, ensure_ascii=False)
        }
    
    @staticmethod
    def returnCommonDict(message, statusCode=400, data={})->dict:
        return ReturnDict(message=message, statusCode=statusCode, data=data)
    
    @staticmethod
    def assignDictToDict(fromDict, toDict)->dict:
        result = {key: fromDict.get(key, toDict[key]) for key in toDict}
        return result
    
    @staticmethod
    def assignValueIsEmpty(value, valueAssign):
        return valueAssign if (not value or len(value.strip()) == 0) else value.strip()
    
    @staticmethod
    def get_random_string(length):
        letters = string.ascii_uppercase + string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
    
    @staticmethod
    def removeNone(data):
        return { k:v for k, v in data.items() if v is not None }
    
#     @staticmethod
#     def apiParseEvent(event)->dict:
#         return json.loads(event)
    
    @staticmethod
    def apiGetBody(event)->dict:
        if "body" not in event.keys():
            raise Exception("body not found")
        return json.loads(event["body"])

    @staticmethod
    def apiGetResponse(statusCode=400, headers={}, body={})->dict:
        return {
            "statusCode": statusCode,
            "headers": headers,
            "body": json.dumps(body, ensure_ascii=False)
        }
    
    @staticmethod
    def datetimeToUnix(value, format_datetime="%Y-%m-%d %H:%M:%S.%f"):
        if not value or value.strip() == "":
            return 0
        else:
            result = dt.datetime.strptime(value, format_datetime)
            if result.year >= 1970:
                return result.timestamp()
            else:
                return (result - dt.datetime(1970, 1, 1)).total_seconds()

    @staticmethod
    def unixToDatetime(value, format_datetime="%Y-%m-%d %H:%M:%S.%f", removeCount=None):
        if not value or value == 0:
            return ""
        else:
            if value >= 0:
                result = dt.datetime.fromtimestamp(value)
            else:
                result = dt.datetime(1970, 1, 1) + dt.timedelta(seconds=value)
            return result.strftime(format_datetime)[:removeCount]

    @staticmethod
    def dateToUnix(value, format_date="%Y-%m-%d"):
        return Utils.datetimeToUnix(value=value, format_datetime=format_date)

    @staticmethod
    def unixToDate(value, format_date="%Y-%m-%d"):
        return Utils.unixToDatetime(value=value, format_datetime=format_date)