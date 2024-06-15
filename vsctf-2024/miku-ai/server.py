import aiohttp
from aiohttp import web
import asyncio
from checker import *

routes = web.RouteTableDef()
loop = asyncio.get_event_loop()

@routes.get("/")
async def hello_world(request):
    return web.FileResponse('./index.html')

@routes.get('/echo')
async def echo(request):
    ws = web.WebSocketResponse(timeout=100)
    await ws.prepare(request)
    try:
        result = "start"
        while True:
            msg = await ws.receive(timeout=15)
            if not (msg.type == aiohttp.WSMsgType.BINARY or (msg.type == aiohttp.WSMsgType.TEXT and msg.data == "start")):
                await ws.send_str("ERR")
                return ws
            if str(msg.data) != result:
                passed, message = check(msg.data, result)
                if passed:
                    break
                await ws.send_str(message)
                return ws
            else:
                await ws.send_str("Starting...")
            result, data = generate_challenge()
            await ws.send_bytes(data)
        with open("flag.txt", "r") as f:
            flag = f.read()
        await ws.send_str(flag)
        return ws
    except Exception as e:
        print(e)
        return ws

def init(argv):
    app = web.Application()
    app.add_routes(routes)
    return app

if __name__ == "__main__":
    app = init(None)
    web.run_app(app)