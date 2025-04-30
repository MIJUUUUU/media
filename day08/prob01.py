from PIL import Image

image_paths = [
    r"C:\Users\miju\media\day08\5_Dcu.png",
    r"C:\Users\miju\media\day08\5_sample.bmp",
    r"C:\Users\miju\media\day08\5_nuts.jpg"
]

for path in image_paths:
    try:
        img = Image.open(path)
        print(f"{path} 파일은 {img.format} 포맷 이미지입니다.")
    except FileNotFoundError:
        print(f"{path} 파일을 찾을 수 없습니다.")
   
