from typing import Union, List

import logging

if __name__ == "main":
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)  # TODO read from config

from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

formatter = jsonlogger.JsonFormatter()

for handler in logger.handlers:
    handler.setFormatter(formatter)

import os
import json
import uvicorn
from fastapi import FastAPI, Depends, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pipeline.pipeline import generatedProjectNamePipeline
from pipeline.schema.inputs import generatedProjectNameInputs
from pipeline.schema.outputs import generatedProjectNameOutputs

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token": # todo: please replace with realistic token
        raise HTTPException(status_code=400, detail="X-Token header invalid")

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

@app.post('/predict', dependencies=[Depends(get_token_header)])
def predict(body: generatedProjectNameInputs) -> List[generatedProjectNameOutputs]:
    '''
    predict api
    '''
    data = body.dict()
    logger.info({"message": "predict invoked", "data": json.dumps(data)})
    print('data', data)

    # call model here
    try:
        p = generatedProjectNamePipeline()
        output: List[generatedProjectNameOutputs] = p.execute(**data)
    except Exception as ex:
        logger.exception(msg=data, exc_info=True)
        output = {'error': {'request': data}}
    # call model here
    return output

@app.post('/parse', dependencies=[Depends(get_token_header)])
def parse(body: generatedProjectNameInputs) -> List[generatedProjectNameOutputs]:
    '''
    parse api
    '''
    data = body.dict()
    logger.info({"message": "parse invoked", "data": json.dumps(data)})
    print('data', data)

    # call model here
    try:
        p = generatedProjectNamePipeline()
        output: List[generatedProjectNameOutputs] = p.execute(**data)
    except Exception as ex:
        logger.exception(msg=data, exc_info=True)
        output = {'error': {'request': data}}
    # call model here
    return output

@app.post('/test', dependencies=[Depends(get_token_header)])
def test(body: List) -> List[generatedProjectNameOutputs]:
    '''
    test api
    '''
    logger.info({"message": "test invoked", "test": json.dumps(body)})
    print('body',body)

    # call model here
    try:
        p = generatedProjectNamePipeline()
        output: List[generatedProjectNameOutputs] = []
        for item in body:
            output.append(p.execute(**item))
    except Exception as ex:
        logger.exception(msg=body, exc_info=True)
        output = {'error': {'request': body}}
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

