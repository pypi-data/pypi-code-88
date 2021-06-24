import uvicorn

from request_listener.app import app
from pyngrok import ngrok

http_tunnel = ngrok.connect(8000)
print(f"listening to: {http_tunnel.public_url}")
uvicorn.run(app, host="0.0.0.0", port=8000, access_log=False, log_level="warning")
