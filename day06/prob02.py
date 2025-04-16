# 📄 prob02.py

import struct
from comp import compare_lowdata  # 같은 폴더에 comp.py 있어야 함!

def parse_wave_samples(filename):
    with open(filename, 'rb') as wav_file:
        # Header 부분 skip
        wav_file.read(4)  # chunk_id
        wav_file.read(4)  # chunk_size
        wav_file.read(4)  # format
        wav_file.read(4)  # sub_chunk_1_id
        wav_file.read(4)  # sub_chunk_1_size
        wav_file.read(2)  # audio_format
        num_channels = struct.unpack('<H', wav_file.read(2))[0]
        wav_file.read(4)  # sample_rate
        wav_file.read(4)  # byte_rate
        wav_file.read(2)  # block_align
        bits_per_sample = struct.unpack('<H', wav_file.read(2))[0]

        wav_file.read(4)  # sub_chunk_2_id
        sub_chunk_2_size = struct.unpack('<I', wav_file.read(4))[0]

        # 샘플 수 계산
        bytes_per_sample = bits_per_sample // 8
        sample_count = sub_chunk_2_size // bytes_per_sample

        # 샘플 읽기
        samples = []
        for _ in range(sample_count):
            data = wav_file.read(bytes_per_sample)
            sample = int.from_bytes(data, byteorder='little', signed=True)
            samples.append(sample)

        return samples

# 📌 실행
samples = parse_wave_samples(r"C:\Users\miju\media\day06\7_3seconds.wav")

# 📌 정답 비교
print(compare_lowdata(samples))  # 👉 True가 뜨면 성공!
# prob02.py 마지막
print(samples)  # 리스트 복사해서 comp.py에 붙여넣기
