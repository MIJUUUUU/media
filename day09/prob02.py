import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


image_path = "C:/Users/miju/media/day09/8_lena24b_512x512.bmp"  
img = Image.open(image_path)


img_array = np.array(img)


L = int(input("양자화할 밝기 단계 수를 입력하세요: ")) 


def quantize_channel(channel, L):
   
    step = 256 // L
   
    return (channel // step) * step


quantized_img_array = np.zeros_like(img_array)


for i in range(3): 
    quantized_img_array[:, :, i] = quantize_channel(img_array[:, :, i], L)


quantized_img = Image.fromarray(quantized_img_array)


plt.imshow(quantized_img)
plt.axis('off')  
plt.show()


quantized_img.save("quantized_image.bmp")

