import struct
from comp import compare_lowdata  # comp.py에서 함수 불러오기

def parse_wave_samples(filename):
    with open(filename, 'rb') as wav_file:
        wav_file.read(4)  # ChunkID
        wav_file.read(4)  # ChunkSize
        wav_file.read(4)  # Format

        wav_file.read(4)  # Subchunk1ID
        wav_file.read(4)  # Subchunk1Size
        wav_file.read(2)  # AudioFormat
        num_channels = struct.unpack('<H', wav_file.read(2))[0]
        wav_file.read(4)  # SampleRate
        wav_file.read(4)  # ByteRate
        wav_file.read(2)  # BlockAlign
        bits_per_sample = struct.unpack('<H', wav_file.read(2))[0]

        wav_file.read(4)  # Subchunk2ID
        subchunk2_size = struct.unpack('<I', wav_file.read(4))[0]

        bytes_per_sample = bits_per_sample // 8
        sample_count = subchunk2_size // bytes_per_sample

        samples = []
        for _ in range(sample_count):
            data = wav_file.read(bytes_per_sample)
            sample = int.from_bytes(data, byteorder='little', signed=True)
            samples.append(sample)

        return samples

# 경로는 본인에 맞게 조정
samples = parse_wave_samples(r"C:\Users\miju\media\day06\7_3seconds.wav")

# 결과 확인
print(compare_lowdata(samples))
