import wave


filename = 'C:/Users/miju/media/day05/6_input_audio.wav'


wav = wave.open(filename, 'rb')


channels = wav.getnchannels()
width = wav.getsampwidth()
framerate = wav.getframerate()
num_frames = wav.getnframes()
duration = num_frames / framerate


print(f"Channels : {channels}")
print(f"Width : {width}")
print(f"original_frame_rate : {framerate}")
print(f"num_frames : {num_frames}")
print(f"Duration : {duration:.1f}")


wav.close()
