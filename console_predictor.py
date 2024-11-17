import numpy as np
import librosa
import sounddevice as sd
import joblib
import time

def extract_features(audio_data, sr):
    y, _ = librosa.effects.trim(audio_data)
    if len(y) == 0:
        print("Audio is empty after trimming.")
        return None
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    features = np.hstack([
        np.mean(mfccs, axis=1),
        np.mean(chroma, axis=1),
        np.mean(zcr),
        np.mean(spectral_contrast, axis=1)
    ])
    return features

def record_audio(duration=2):
    print("Recording...")
    fs = 22050
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    print("Recording finished.")
    return audio_data.flatten(), fs

clf_loaded = joblib.load('key_prediction_model.joblib')
print("Model loaded.")

try:
    while True:
        recorded_audio, sample_rate = record_audio(duration=2)
        features = extract_features(recorded_audio, sample_rate)
        if features is not None:
            features = features.reshape(1, -1)
            probabilities = clf_loaded.predict_proba(features)[0]
            print(f"Probabilities: Spacebar: {probabilities[1]:.2f}, Other Key: {probabilities[0]:.2f}")
            threshold = 0.8
            prediction = 1 if probabilities[1] >= threshold else 0
            label = "Spacebar" if prediction == 1 else "Other Key"
            print(f"Prediction: {label}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting the testing loop.")