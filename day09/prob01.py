from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


image_path = "C:/Users/miju/media/day09/8_lena24b_512x512.bmp" 
img = Image.open(image_path)


width, height = img.size
print(f"원본 이미지 크기: {width}x{height}")


img_array = np.array(img)


sample_val = 32  


output_img_array = np.zeros((height // sample_val, width // sample_val, 3), dtype=np.uint8)


for i in range(0, height, sample_val):
    for j in range(0, width, sample_val):
       
        r = np.mean(img_array[i:i+sample_val, j:j+sample_val, 0])
        g = np.mean(img_array[i:i+sample_val, j:j+sample_val, 1])
        b = np.mean(img_array[i:i+sample_val, j:j+sample_val, 2])

      
        output_img_array[i // sample_val, j // sample_val] = [r, g, b]

output_img = Image.fromarray(output_img_array)
plt.imshow(output_img)
plt.show()
