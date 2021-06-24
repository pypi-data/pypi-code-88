import requests
import json
from http import HTTPStatus
from pipeline.schema.inputs import generatedProjectNameInputs


def post(endPoint, data):
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    url = 'http://localhost:8080/' + endPoint
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        data = HTTPStatus.INTERNAL_SERVER_ERROR.description
    else:
        data = json.loads(response.content)
    return data

if __name__ == '__main__':
    # test - parse
    data = {}
    d = generatedProjectNameInputs(**data)
    results = post('parse', data)
    print('results', results)

    results = post('predict', data)
    print('results', results)

    # test - test
    batch = []
    batch.append(d.dict())
    results = post('test', batch)
    print('results', results)
