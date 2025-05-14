import struct

# BMP 파일 경로
bmp_path = r"C:\Users\miju\media\day08\5_sample.bmp"

with open(bmp_path, 'rb') as f:
    header = f.read(54)  

    magic_number = header[0:2]
    file_size = struct.unpack('<I', header[2:6])[0]
    width = struct.unpack('<I', header[18:22])[0]
    height = struct.unpack('<I', header[22:26])[0]
    bits = struct.unpack('<H', header[28:30])[0]
    raw_size = struct.unpack('<I', header[34:38])[0]

    print("Magic number :", magic_number)
    print("File size :", file_size)
    print("Width :", width)
    print("Height :", height)
    print("bits :", bits)
    print("Raw size :", raw_size)
