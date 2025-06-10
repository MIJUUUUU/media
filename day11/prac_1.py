import pickle
import struct

def compress_rle(data):
    compressed_data = bytearray()
    count = 1

    for i in range(3, len(data), 3):
        if data[i:i+3] == data[i-3:i]:  # 현재 RGB 픽셀이 이전 RGB 픽셀과 같으면
            count += 1
        else:
            compressed_data.extend(struct.pack('IBBB',
                                               count,
                                               data[i - 3],
                                               data[i - 2],
                                               data[i - 1]))
            count = 1

    # 마지막 픽셀 처리
    compressed_data.extend(struct.pack('IBBB',
                                       count,
                                       data[-3],
                                       data[-2],
                                       data[-1]))
    return compressed_data

def decompress_rle(compressed_data):
    decompressed_data = bytearray()

    for i in range(0, len(compressed_data), 7):
        count, r, g, b = struct.unpack('IBBB', compressed_data[i:i + 7])
        decompressed_data.extend([r, g, b] * count)

    return decompressed_data

# -----------------------
# 이미지 3개 반복 처리
# -----------------------
for i in range(1, 4):
    input_file = f'sample_{i}.bmp'
    output_bin = f'compressed_sample_{i}'
    output_bmp = f'sample_{i}_output.bmp'

    print(f'\n▶ sample_{i}.bmp 처리 시작')

    with open(input_file, 'rb') as file:
        header = file.read(54)
        pixel_data = bytearray(file.read())

    compressed = compress_rle(pixel_data)

    with open(output_bin, 'wb') as file:
        pickle.dump(compressed, file)

    decompressed = decompress_rle(compressed)

    with open(output_bmp, 'wb') as file:
        file.write(header)
        file.write(decompressed)

    print(f'  - 압축 전 크기: {len(pixel_data)} bytes')
    print(f'  - 압축 후 크기: {len(compressed)} bytes')
