from PIL import Image
import numpy as np

def scale_image_nearest(filename, s):
    img = Image.open(filename)
    data = np.array(img)

    H, W = data.shape[0], data.shape[1]  

    new_H = int(H * s)
    new_W = int(W * s)

    
    result = np.zeros((new_H, new_W, 3), dtype=np.uint8)

    for y_new in range(new_H):
        for x_new in range(new_W):
            x_old = int(x_new / s)
            y_old = int(y_new / s)

            if x_old < W and y_old < H:
                result[y_new, x_new] = data[y_old, x_old]

    result_img = Image.fromarray(result)
    result_img.save("C:/Users/miju/media/day10/result_nearest.png")
    result_img.show()

scale_image_nearest("C:/Users/miju/media/day10/8_lena24b_512x512.bmp", 1.7)
