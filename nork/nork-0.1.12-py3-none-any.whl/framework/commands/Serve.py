from nork.commands import nork
from nork import config
import fnc
import uvicorn


@nork.command(name="serve")
def handle(host: str = "0.0.0.0", port: int = 8080, reload: bool = True):
    """
    Serve the application on the development server
    """
    host = fnc.get("server.host", config, default=host)
    port = fnc.get("server.port", config, default=port)
    reload = fnc.get("server.reload", config, default=reload)

    if fnc.get("server.custom", config):
        uvicorn.run(fnc.get("server.module", config,
                    default="server:app"), host=host, port=port, reload=reload)
    else:
        uvicorn.run("nork.framework.server:app",
                    host=host, port=port, reload=reload)
