from io import BytesIO
from PIL import Image
from typing import Tuple
import shades
import random
import string
import math
import os

SIDE = 200 # Scale 10x10 to 200x200 for drawing purposes

class RandomGrey(shades.Shade):
    def determine_shade(self, xy):
        mono = random.randint(0, 255)
        return (mono, mono, mono)

def img_to_data_url(img: Image) -> bytes:
    f = BytesIO()
    img.save(f, format="PNG")
    # img_base64 = base64.b64encode(f.getvalue()).decode("utf-8")
    # return f"data:image/png;base64,{img_base64}"
    return f.getvalue()

def gen_circle_point() -> Tuple[Tuple[float, float], float]:
    '''
    Generates center and radius for a circle inside the square
    '''
    # need to make sure radius is not too big
    max_radius = 0
    while max_radius < SIDE // 4:
        center = (random.uniform(SIDE//6, 5*SIDE//6), random.uniform(SIDE//6, 5*SIDE//6))
        max_radius = min(SIDE-center[0], SIDE-center[1], center[0], center[1])
    radius = random.uniform(max_radius // 2, max_radius)
    return tuple([center, radius])

def gen_inside_point(corner: int) -> Tuple[float, float]:
    '''
    Generates a point inside the square. We want the point to be close to side
    '''
    x, y = random.uniform(0, SIDE//4), random.uniform(0, SIDE//4)
    if corner == 0:
        # top left
        return tuple([x, SIDE - y])
    elif corner == 1:
        # top right
        return tuple([SIDE - x, SIDE - y])
    elif corner == 2:
        # bottom right
        return tuple([SIDE - x, y])
    else:
        # bottom left
        return tuple([x, y])

def calc_triangle_area(pts) -> float:
    x1, y1, x2, y2, x3, y3 = pts[0][0], pts[0][1], pts[1][0], pts[1][1], pts[2][0], pts[2][1]
    return abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1))))

def calc_circle_area(radius) -> float:
    return math.pi * radius ** 2

def calc_quadrilateral_area(pts) -> float:
    # sides of quadrilateral
    a = math.sqrt((pts[0][0] - pts[1][0]) ** 2 + (pts[0][1] - pts[1][1]) ** 2)
    b = math.sqrt((pts[1][0] - pts[2][0]) ** 2 + (pts[1][1] - pts[2][1]) ** 2)
    c = math.sqrt((pts[2][0] - pts[3][0]) ** 2 + (pts[2][1] - pts[3][1]) ** 2)
    d = math.sqrt((pts[3][0] - pts[0][0]) ** 2 + (pts[3][1] - pts[0][1]) ** 2)
    # semiperimeter
    s = (a + b + c + d) / 2
    # Brahmagupta's formula
    return math.sqrt((s-a)*(s-b)*(s-c)*(s-d))

def stage_one() -> Tuple[bytes, float]:
    '''
    Stage 1 of the challenge (50 images)
    One simple shape of sides 3-4 or a circle
    Returns the image data and correct answer (float number out of scale of 100)
    '''
    try:
        canvas = shades.Canvas(SIDE, SIDE)
        my_shade = RandomGrey()
        sides = random.randint(3, 5)
        # print(f"Generating image with {sides} sides.")
        if sides == 3:
            corners = [random.randint(0, 3) for _ in range(sides)]
            pts = [gen_inside_point(c) for c in corners]
            res = calc_triangle_area(pts) / SIDE / SIDE * 100.0
            # print(f"Area of triangle: {res}")
            my_shade.shape(canvas, pts)
        elif sides == 4:
            pts = [gen_inside_point(i) for i in range(sides)]
            res = calc_quadrilateral_area(pts) / SIDE / SIDE * 100.0
            # print(f"Area of quadrilateral: {res}")
            my_shade.shape(canvas, pts)
        else:
            center, radius = gen_circle_point()
            res = calc_circle_area(radius) / SIDE / SIDE * 100.0
            # print(f"Area of circle: {res}")
            my_shade.circle(canvas, center, radius)

        rand_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        canvas.save(f"{rand_name}.png")
        im = Image.open(f"{rand_name}.png")
        # res = calc_area(im) <- To be used in random shape
        data = img_to_data_url(im)
        os.unlink(f"{rand_name}.png")
        return tuple([data, res])
    except Exception as e:
        raise