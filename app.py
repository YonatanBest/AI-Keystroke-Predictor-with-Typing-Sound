import numpy as np
import librosa
import sounddevice as sd
import joblib
import time
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Load the trained model
clf_loaded = joblib.load('key_prediction_model_large.joblib')
print("Model loaded.")

def extract_features(audio_data, sr):
    # Your existing feature extraction code
    y, _ = librosa.effects.trim(audio_data)

    if len(y) == 0:
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

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/record', methods=['POST'])
def record():
    duration = request.form.get('duration', 2, type=int)
    fs = 22050  
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    print("Recording finished.")
    audio_data = audio_data.flatten()  
    features = extract_features(audio_data, fs)

    if features is not None:
        features = features.reshape(1, -1) 
        probabilities = clf_loaded.predict_proba(features)[0]
        threshold = 0.53
        prediction = 1 if probabilities[1] >= threshold else 0
        label = "Spacebar" if prediction == 1 else "Other Key"
        return jsonify({"label": label, "probabilities": probabilities.tolist()})

    return jsonify({"error": "No features extracted."})

if __name__ == '__main__':
    app.run(debug=True)
