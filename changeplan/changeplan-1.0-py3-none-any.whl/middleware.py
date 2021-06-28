import json
import requests

from .change_plan_service import ChangePlanService

class ChangePlanMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.method == 'PUT' or request.method == 'PATCH':
            data = json.loads(request.body)
            response = requests.get(f'http://{request.get_host()}{request.path}', headers={'Content-Type': 'Application/json'})
            current_plan = response.json()['data']['SUBSCRIPTION']
            change_plan_service = ChangePlanService(data, current_plan)
            body = json.dumps(change_plan_service.execute(), indent=2).encode('utf-8')
            request._body = body

        return self.get_response(request)  
