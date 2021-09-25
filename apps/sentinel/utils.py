import asyncio

def loop(func):
    loop = asyncio.get_event_loop()
    def decorated(*args, **kwargs):
        loop.run_until_complete(func(*args, **kwargs))
    return decorated
