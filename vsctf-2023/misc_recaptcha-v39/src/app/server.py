import aiohttp
from aiohttp import web
import asyncio
import utils
import math

routes = web.RouteTableDef()
loop = asyncio.get_event_loop()

@routes.get("/")
async def hello_world(request):
    return web.FileResponse('./index.html')

@routes.get('/echo')
async def echo(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    try:
        counter = -1
        wrong_ans = 0
        timeout = None
        result = 0
        while True:
            msg = await ws.receive(timeout=timeout)
            timeout = 5
            if msg.type != aiohttp.WSMsgType.TEXT:
                await ws.send_str("ERR")
                return ws
            input_txt = msg.data
            # if input_txt is not a float type, increase wrong_ans
            try:
                input_txt = float(input_txt)
            except:
                wrong_ans += 1
                await ws.send_str(f"{counter}/100 correct, {wrong_ans}/10 wrong (+1)")
            if math.fabs(input_txt - result) > 1.0:
                wrong_ans += 1
                await ws.send_str(f"{counter}/100 correct, {wrong_ans}/10 wrong (+1)")
            else:
                counter += 1
                await ws.send_str(f"{counter}/100 correct (+1), {wrong_ans}/10 wrong")
            if wrong_ans >= 10:
                return ws
            if counter >= 100:
                break
            data, result = utils.stage_one()
            # print(result)
            await ws.send_bytes(data)
        with open("flag.txt", "r") as f:
            flag = f.read()
        await ws.send_str(flag)
        return ws
    except Exception as e:
        return ws


def init(argv):
    app = web.Application()
    app.add_routes(routes)
    return app

if __name__ == "__main__":
    app = init(None)
    web.run_app(app)