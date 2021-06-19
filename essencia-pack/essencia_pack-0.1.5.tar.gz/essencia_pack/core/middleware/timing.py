import time


class TimingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        start_time = time.time()
        await self.app(scope, receive, send)
        end_time = time.time()
        print(f"Took {end_time - start_time:.2f} seconds")