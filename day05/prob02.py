import wave
import numpy as np
import scipy.signal as signal


input_file = 'C:/Users/miju/media/day05/6_input_audio.wav'  # 너가 가진 파일 경로로 수정했어
output_file = 'C:/Users/miju/media/day05/resampled.wav'     # 리샘플링한 파일 저장 위치


new_sample_rate = 5000


with wave.open(input_file, 'rb') as wav_file:
    n_channels = wav_file.getnchannels()
    sample_width = wav_file.getsampwidth()
    sample_rate = wav_file.getframerate()
    n_frames = wav_file.getnframes()


    audio_data = wav_file.readframes(n_frames)
    audio_data = np.frombuffer(audio_data, dtype=np.int16)


new_length = int(len(audio_data) * float(new_sample_rate) / sample_rate)
resampled_data = signal.resample(audio_data, new_length)


resampled_data = resampled_data.astype(np.int16)


with wave.open(output_file, 'wb') as wav_file:
    wav_file.setnchannels(n_channels)
    wav_file.setsampwidth(sample_width)
    wav_file.setframerate(new_sample_rate)
    wav_file.writeframes(resampled_data.tobytes())

print("저장된 파일:", output_file)
