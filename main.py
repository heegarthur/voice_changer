import librosa
import sounddevice as sd
import os
import numpy as np

def speel_extreem_raar(audio_file):
    if not os.path.exists(audio_file):
        print(f"file not found {audio_file}")
        return
    y, sr = librosa.load(audio_file)
    pitch_steps = 9
    tempo = 0.9  
    y = librosa.effects.pitch_shift(y, sr=sr, n_steps=pitch_steps)
    y = librosa.effects.time_stretch(y, rate=tempo)
    y = y * 1.3  
    y = np.clip(y, -1.0, 1.0)

    sd.play(y, sr)
    sd.wait()

if __name__ == "__main__":
    sound_file = "yourfile.wav"
    speel_extreem_raar(sound_file)
