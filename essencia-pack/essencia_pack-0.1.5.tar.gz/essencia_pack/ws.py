from starlette.websockets import WebSocket


async def app(scope, receive, send):
    websocket = WebSocket(scope=scope, receive=receive, send=send)
    await websocket.accept()
    await websocket.send_text('Hello, world!')
    await websocket.close()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('ws:app', reload=True)