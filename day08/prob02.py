#실습2 무작위 점
import struct

def flip_bytearray(bytearr, width):
    row_len = width * 3
    flipped_bytearr = bytearr[::-1]
    for i in range(len(bytearr) // row_len):
        start_index = i * row_len
        end_index = start_index + row_len
        flipped_bytearr[start_index:end_index] = flipped_bytearr[start_index:end_index][::-1]
    return flipped_bytearr

with open("C:/Users/miju/media/day09/8_lena24b_512x512.bmp", "rb") as f:
    header_data = f.read(54)
    width = struct.unpack('<I', header_data[18:22])[0]
    height = struct.unpack('<I', header_data[22:26])[0]
    pixel_data = bytearray(f.read())

pixel_data = flip_bytearray(pixel_data, width)


x, y = 300, 400
index = (y * width + x) * 3
pixel_data[index] = 255      
pixel_data[index + 1] = 255  
pixel_data[index + 2] = 255  

pixel_data = flip_bytearray(pixel_data, width)

with open("C:/Users/miju/media/day09/output2.bmp", "wb") as f:
    f.write(header_data)
    f.write(pixel_data)

