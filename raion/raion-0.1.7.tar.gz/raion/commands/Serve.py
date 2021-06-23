from raion.commands import raion, typer
import uvicorn

@raion.command(name="serve")
def handle():
    """
    Serve the application on the development server
    """
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)