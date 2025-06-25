import numpy as np
from PIL import Image
import math

def clamp(x, a, b):
    return max(a, min(b, x))

def distort(u0, v0):
    cx, cy = 0.5, 0.5
    dx = u0 - cx
    dy = v0 - cy
    dist = math.sqrt(dx * dx + dy * dy)
    distortX = dx * dist * 0.5
    distortY = dy * dist * 0.5
    noise1 = math.sin(u0 * 25 + v0 * 20) * 0.1
    noise2 = math.cos(u0 * 20 + v0 * 25) * 0.1
    u_distorted = u0 + distortX + noise1
    v_distorted = v0 + distortY + noise2
    return u_distorted, v_distorted

def numerical_jacobian(u0, v0, eps=1e-5):
    # Partial derivatives wrt u0
    u_dx1, v_dx1 = distort(u0 + eps, v0)
    u_dx0, v_dx0 = distort(u0 - eps, v0)
    du_du = (u_dx1 - u_dx0) / (2 * eps)
    dv_du = (v_dx1 - v_dx0) / (2 * eps)

    # Partial derivatives wrt v0
    u_dy1, v_dy1 = distort(u0, v0 + eps)
    u_dy0, v_dy0 = distort(u0, v0 - eps)
    du_dv = (u_dy1 - u_dy0) / (2 * eps)
    dv_dv = (v_dy1 - v_dy0) / (2 * eps)

    J = np.array([[du_du, du_dv],
                  [dv_du, dv_dv]])
    return J

def invert_pixel(u, v, max_iter=30, tol=1e-7):
    u0, v0 = u, v  # Initial guess
    for _ in range(max_iter):
        u_dist, v_dist = distort(u0, v0)
        error = np.array([u_dist - u, v_dist - v])
        if abs(error[0]) < tol and abs(error[1]) < tol:
            break
        J = numerical_jacobian(u0, v0, eps=1e-6)
        if np.linalg.cond(J) > 1e12:
            break
        delta = np.linalg.solve(J, error)
        u0, v0 = u0 - delta[0], v0 - delta[1]
    # clamp only after iterations
    u0 = clamp(u0, 0, 1)
    v0 = clamp(v0, 0, 1)
    return u0, v0

def bilinear_interpolate(img_arr, x, y):
    h, w, c = img_arr.shape
    x0 = int(np.floor(x))
    x1 = min(x0 + 1, w - 1)
    y0 = int(np.floor(y))
    y1 = min(y0 + 1, h - 1)

    dx = x - x0
    dy = y - y0

    top = (1 - dx) * img_arr[y0, x0] + dx * img_arr[y0, x1]
    bottom = (1 - dx) * img_arr[y1, x0] + dx * img_arr[y1, x1]
    pixel = (1 - dy) * top + dy * bottom

    return pixel.astype(np.uint8)

def reverse_liquid_glass(in_path="out.png", out_path="reversed.png"):
    img = Image.open(in_path).convert("RGBA")
    w, h = img.size
    src_pixels = np.array(img)
    dst_pixels = np.zeros_like(src_pixels)

    for y in range(h):
        for x in range(w):
            u = x / (w - 1)
            v = y / (h - 1)
            u0, v0 = invert_pixel(u, v)
            dst_pixels[y, x] = bilinear_interpolate(src_pixels, u0 * (w - 1), v0 * (h - 1))

        if y % 50 == 0:
            print(f"Processed {y}/{h} rows...")

    out_img = Image.fromarray(dst_pixels, mode="RGBA")
    out_img.save(out_path)
    print(f"Saved reversed image as {out_path}")

# Run it
reverse_liquid_glass('output.png', 'original.png')
