from typing import Union, List

import os
import json
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pipeline.pipeline import generatedProjectNamePipeline
from pipeline.schema.inputs import generatedProjectNameInputs
from pipeline.schema.outputs import generatedProjectNameOutputs

def load_allowed_cors_origins():
    allowed_origins = []
    cors_origin_list_path = 'cors_allowed_origins.json'
    if os.path.exists(cors_origin_list_path):
        with open(cors_origin_list_path) as f:
            allowed_origins = json.load(f)

    return allowed_origins


app = FastAPI()

origins = load_allowed_cors_origins()
methods = ["*"]
headers = ["*"]
credentials = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=credentials,
    allow_methods=methods,
    allow_headers=headers,
)

@app.post('/predict')
def predict(body: generatedProjectNameInputs) -> List[generatedProjectNameOutputs]:
    '''
    predict api
    '''
    data = body.dict()
    print('data', data)

    # call model here
    p = generatedProjectNamePipeline()
    output: List[generatedProjectNameOutputs] = p.execute(**data)
    # call model here
    return output

@app.post('/parse')
def parse(body: generatedProjectNameInputs) -> List[generatedProjectNameOutputs]:
    '''
    parse api
    '''
    data = body.dict()
    print('data', data)

    # call model here
    p = generatedProjectNamePipeline()
    output: List[generatedProjectNameOutputs] = p.execute(**data)
    # call model here
    return output

@app.post('/test')
def test(body: List[generatedProjectNameInputs]) -> List[generatedProjectNameOutputs]:
    '''
    test api
    '''
    print('body',body)

    # call model here
    p = generatedProjectNamePipeline()
    output: List[generatedProjectNameOutputs] = []
    for item in body:
        output.extend(p.execute(**item.dict()))
    # output: List[generatedProjectNameOutputs] = p.execute(**body)
    # call model here
    return output

@app.get("/livenessprobe")
def liveness_probe():
    return {"alive": True}


@app.get("/readinessprobe")
def readiness_probe():
    return {"ready": True}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)

