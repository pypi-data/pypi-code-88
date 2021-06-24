import json
import logging

from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()


@app.post("/{path:path}")
async def parse_request(request: Request, path: str):
    print(
        logging.INFO,
        json.dumps(
            dict(
                hostname=str(request.url.hostname),
                path=str(request.url.path),
                query_params=dict(**request.query_params),
                body=(await request.body()).decode(),
                headers=dict(**request.headers),
            ),
            indent=2,
        ),
    )
    return {"status": "ok"}
