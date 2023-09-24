from websocket import create_connection
from PIL import Image
from io import BytesIO

def calc_area(im: Image) -> float:
    '''
    Calculates the area of the shaded area in the image
    '''
    pixels = im.load()
    # count number of non-white pixels
    count, total = 0, 0
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if pixels[i, j] != (240, 240, 240):
                count += 1
            total += 1
    return float(100) * count / total

ws = create_connection("ws://172.86.96.174:8000/echo")
ws.send("0")

while True:
    d = ws.recv()
    if type(d) == str:
        print("PROMPT:", d)
        if "vsctf" in d:
            ws.close()
            break
        continue
    if not d:
        break
    assert type(d) == bytes
    im = Image.open(BytesIO(d))
    res = calc_area(im)
    ws.send(str(res))