from PIL import Image
import numpy as np

def translate_image(filename, x, y, w, h, tx, ty):
    img = Image.open(filename)
    data = np.array(img)

    H, W = data.shape[0], data.shape[1]  


    part = data[y:y+h, x:x+w].copy()

    data[y:y+h, x:x+w] = [0, 0, 0]

    new_x = x + tx
    new_y = y + ty

    copy_w = min(w, W - new_x)
    copy_h = min(h, H - new_y)

    if copy_w > 0 and copy_h > 0:
        data[new_y:new_y+copy_h, new_x:new_x+copy_w] = part[:copy_h, :copy_w]

    result = Image.fromarray(data)
    result.save("C:/Users/miju/media/day10/result.png")
    result.show()

translate_image("C:/Users/miju/media/day10/8_lena24b_512x512.bmp", x=100, y=100, w=50, h=50, tx=30, ty=20)
