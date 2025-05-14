import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 이미지 파일 경로 설정
image_path = "C:/Users/miju/media/day09/8_lena24b_512x512.bmp"  # 파일 경로를 실제 파일 경로로 설정해주세요.
img = Image.open(image_path)


img_array = np.array(img)


adjustment_percentage = float(input("밝기 조정 비율(%)을 입력하세요: "))  


def adjust_brightness(image_array, percentage):
    factor = 1 + percentage / 100.0

    adjusted_image = np.clip(image_array * factor, 0, 255) 
    return adjusted_image.astype(np.uint8)


adjusted_img_array = adjust_brightness(img_array, adjustment_percentage)


adjusted_img = Image.fromarray(adjusted_img_array)


output_image_path = f"C:/Users/miju/media/day09/adjusted_image_{adjustment_percentage}.bmp"
adjusted_img.save(output_image_path)

plt.imshow(adjusted_img)
plt.axis('off')
plt.show()

print(f"조정된 이미지를 '{output_image_path}'로 저장했습니다.")
