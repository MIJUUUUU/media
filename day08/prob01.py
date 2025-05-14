#실습1 정보출력
import struct

def bmp_header(filename):
    with open(filename, 'rb') as bmp_file:
        magic_num = bmp_file.read(2)
        print("Type :", magic_num.hex())

        file_size = struct.unpack('<I', bmp_file.read(4))[0]
        print("Size :", hex(file_size)[2:])
        bmp_file.read(2)
        bmp_file.read(2)

        off_bits = struct.unpack('<I', bmp_file.read(4))[0]
        print("OffBits :", off_bits)

        bmp_file.read(4)

        width = struct.unpack('<I', bmp_file.read(4))[0]
        height = struct.unpack('<I', bmp_file.read(4))[0]
        print("Height :", height)
        print("Width :", width)

        bmp_file.read(2)

        bit_count = struct.unpack('<H', bmp_file.read(2))[0]
        print("BitCount :", bit_count)

        bmp_file.read(4)

        size_image = struct.unpack('<I', bmp_file.read(4))[0]
        print("SizeImage :", size_image)

        xppm = struct.unpack('<I', bmp_file.read(4))[0]
        yppm = struct.unpack('<I', bmp_file.read(4))[0]
        print("XPelsPerMeter :", xppm)
        print("YPelsPerMeter :", yppm)

        clr_used = struct.unpack('<I', bmp_file.read(4))[0]
        print("ClrUsed :", clr_used)

        clr_important = struct.unpack('<I', bmp_file.read(4))[0]
        print("ClrImportant :", clr_important)

bmp_header("C:/Users/miju/media/day09/8_lena24b_512x512.bmp")
