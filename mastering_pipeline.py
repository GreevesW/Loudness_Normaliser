import pyttsx3
import librosa
import pydub 
import pyloudnorm as pyln
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

# TTS engine


# engine = pyttsx3.init()

# text = "Try this audio"
# engine.save_to_file(text, "raw_tts.wav")
# engine.runAndWait()

# data, rate = librosa.data, rate = librosa.load("raw_tts.wav", sr=None)


# Recording

INPUT_FILE = "recordings/my_recording.wav"
data, rate = librosa.load(INPUT_FILE, sr=None)

audio_segment = pydub.AudioSegment.from_file(INPUT_FILE)  # MP3 or WAV
audio_segment.export("recordings/input.wav", format="wav")

meter = pyln.Meter(rate)
loudness_before = meter.integrated_loudness(data)

print(f"Original Loudness: {loudness_before:.2f} LUFS")

t_lufs = -24.0
n_audio = pyln.normalize.loudness(data, loudness_before, t_lufs)

sf.write("recordings/normalised.wav", n_audio, rate)

audio_segment = pydub.AudioSegment.from_wav("recordings/normalised.wav")

compressed_audio = pydub.effects.compress_dynamic_range(
    audio_segment,
    threshold=-20.0,
    ratio=3.0,
    attack=5,
    release=50
)

compressed_audio.export("recordings/mastered_output.wav", format="wav")

print("Mastered file saved as mastered_output.wav")


# Compressed audio
compressed = pydub.AudioSegment.from_wav("recordings/mastered_output.wav")

compressed_samples = np.array(compressed.get_array_of_samples(), dtype=np.float32)

compressed_samples /= 2**15

plt.figure(figsize=(12,4))
plt.plot(n_audio, alpha=0.5, label="Normalised")
plt.plot(compressed_samples, alpha=0.5, label="Compressed")
plt.plot(data, alpha=0.5, label="Original")
plt.legend()
plt.title("Waveform Comparison")
plt.show()
