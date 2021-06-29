# Service 
from fastapi import FastAPI
from . import routers


# FastAPI app instance
app = FastAPI()


# Include all routers
app.include_router(routers.router, prefix='/admin', tags=[])
