from nork.core.logging import Log
from ..application import Application
import importlib

app = Application()
app.bootstrap()

try:
    server = importlib.import_module(f"server")
except Exception as exception:
    if type(exception).__name__ != "ModuleNotFoundError":
        Log.error(f"server.py :: {exception}")
    server = None


@app.on_event("startup")
async def on_startup():
    try:
        getattr(server, 'on_startup')(app)
    except Exception as exception:
        if type(exception).__name__ != "AttributeError":
            Log.error(f"Event Startup :: {exception}")


@app.on_event("shutdown")
async def on_shutdown():
    try:
        getattr(server, 'on_shutdown')(app)
    except Exception as exception:
        if type(exception).__name__ != "AttributeError":
            Log.error(f"Event Shutdown :: {exception}")
