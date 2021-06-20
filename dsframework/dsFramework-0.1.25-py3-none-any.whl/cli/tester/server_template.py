from typing import Union, List

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dsframework.pipeline import generatedProjectNamePipeline
from dsframework.schema.inputs import generatedProjectNameInputs
from dsframework.schema.outputs import generatedProjectNameOutputs

app = FastAPI()

origins = ["*"]
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
def predict(body: generatedProjectNameInputs) -> generatedProjectNameOutputs:
    '''
    predict api
    '''
    data = body.dict()
    print('data', data)

    # call model here
    p = generatedProjectNamePipeline()
    output = p.execute(data=data)
    # call model here
    if output == None:
        output = {}
    return generatedProjectNameOutputs(**output)

@app.post('/parse')
def parse(body: generatedProjectNameInputs) -> generatedProjectNameOutputs:
    '''
    parse api
    '''
    data = body.dict()
    print('data', data)

    # call model here
    p = generatedProjectNamePipeline()
    output = p.execute(data=data)
    # call model here
    if output == None:
        output = {}
    return generatedProjectNameOutputs(**output)

@app.post('/test')
def test(body: List[generatedProjectNameInputs]) -> List[generatedProjectNameOutputs]:
    '''
    test api
    '''
    print('body',body)

    # call model here
    test_output = []
    output = []
    for item in test_output:
        output.append(generatedProjectNameOutputs(**item))
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

