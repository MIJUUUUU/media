import struct

def parse_wave_header(filename):
    with open(filename, 'rb') as wav_file:
        
        chunk_id = wav_file.read(4)
        chunk_size = struct.unpack('<I', wav_file.read(4))[0]
        wav_format = wav_file.read(4)

       
        sub_chunk_1_id = wav_file.read(4)
        sub_chunk_1_size = struct.unpack('<I', wav_file.read(4))[0]
        audio_format = struct.unpack('<H', wav_file.read(2))[0]
        num_channels = struct.unpack('<H', wav_file.read(2))[0]
        sample_rate = struct.unpack('<I', wav_file.read(4))[0]
        byte_rate = struct.unpack('<I', wav_file.read(4))[0]
        block_align = struct.unpack('<H', wav_file.read(2))[0]
        bits_per_sample = struct.unpack('<H', wav_file.read(2))[0]

        
        print("chunk_id:", chunk_id)
        print("chunk_size:", chunk_size)
        print("wav_format:", wav_format)
        print("sample_rate:", sample_rate)
        print("byte_rate:", byte_rate)


parse_wave_header(r"C:\Users\miju\media\day06\7_3seconds.wav")
