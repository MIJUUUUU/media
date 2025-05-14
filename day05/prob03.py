from scipy.signal import resample
import numpy as np
import wave

input_file = 'C:/Users/miju/media/day05/6_input_audio.wav'
output_file = 'C:/Users/miju/media/day05/changed_real.wav'
new_rate = 11025

with wave.open(input_file, 'rb') as wav:
    nch = wav.getnchannels()
    sw = wav.getsampwidth()
    old_rate = wav.getframerate()
    nframes = wav.getnframes()
    audio = np.frombuffer(wav.readframes(nframes), dtype=np.int16)


new_len = int(len(audio) * new_rate / old_rate)
resampled = resample(audio, new_len).astype(np.int16)

with wave.open(output_file, 'wb') as out:
    out.setnchannels(nch)
    out.setsampwidth(sw)
    out.setframerate(new_rate)
    out.writeframes(resampled.tobytes())

print("변경 전")
print("Sample rate:", old_rate)
print("변경 후")
print("Sample rate:", new_rate)
