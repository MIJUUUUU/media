from PIL import Image
import numpy as np
import math

def rotate_image(filename, degree):
    img = Image.open(filename)
    data = np.array(img)

    H, W = data.shape[0], data.shape[1]
    cx, cy = W // 2, H // 2 

    rad = math.radians(degree) 
    cos_r = math.cos(rad)
    sin_r = math.sin(rad)

    result = np.zeros_like(data)

    for y_new in range(H):
        for x_new in range(W):
            x_origin = (x_new - cx) * cos_r + (y_new - cy) * sin_r + cx
            y_origin = -(x_new - cx) * sin_r + (y_new - cy) * cos_r + cy

            x_origin = int(round(x_origin))
            y_origin = int(round(y_origin))

            if 0 <= x_origin < W and 0 <= y_origin < H:
                result[y_new, x_new] = data[y_origin, x_origin]

    result_img = Image.fromarray(result)
    result_img.save("C:/Users/miju/media/day10/result_rotated.png")
    result_img.show()

rotate_image("C:/Users/miju/media/day10/8_lena24b_512x512.bmp", 45)
