# AI Keystroke Predictor with Typing Sound

## Overview

This project utilizes AI to predict keystrokes from typing sounds. By capturing audio via compromised microphones, the system demonstrates how typing sounds can be leveraged to infer sensitive information, showcasing the potential risks and security challenges in modern digital environments.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Ethical Considerations](#ethical-considerations)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Sound-based Keystroke Prediction**
- **Real-time Console and Web Interface**
- **Machine Learning Model Integration**
- **Behavioral Analysis for Security**

## Installation

### Prerequisites

- Python 3.8 or later
- Required Libraries:
  ```bash
  pip install -r requirements.txt
  ```

### Clone the Repository

```bash
git clone https://github.com/YonatanBest/AI-Keystroke-Predictor-with-Typing-Sound.git
cd AI-Keystroke-Predictor-with-Typing-Sound
```

## Usage

### Running the Console Predictor

Use the `console_predictor.py` script to run predictions directly from the terminal:

```bash
python console_predictor.py
```

### Running the Web App

The project includes a Flask web app for a more interactive interface.

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.

### Sample Audio Files

The `others/` and `space/` folders contain sample `.wav` files for testing the model.

## Project Structure

```
AI Keystroke Predictor/
│
├── others/                   # Sample typing sound files for non-space keys
├── space/                    # Sample typing sound files for space key
├── templates/                # HTML files for Flask web app
│   └── index.html            # Main interface for the web app
├── app.py                    # Flask web app
├── console_predictor.py      # Command-line keystroke predictor
├── key_prediction_model.joblib  # Trained ML model for prediction
├── key_prediction_model_large.joblib  # Larger trained model for broader datasets
├── Model.ipynb               # Jupyter notebook for model development
├── Others.wav                # Sample wav file (Other key sound)
├── Other_Large.wav           # Larger dataset key sound sample
├── Space.wav                 # Sample wav file (Space key sound)
├── Space_Large.wav           # Larger dataset space key sound sample
└── requirements.txt          # Dependencies for the project
```

## How It Works

1. **Audio Capture**: Typing sounds are collected via a microphone.
2. **Feature Extraction**: Audio data is processed to extract features such as frequency and amplitude patterns.
3. **Machine Learning**: A pre-trained model predicts the keystrokes based on the extracted audio features.
4. **Web and Console Interfaces**: The results are displayed either via a console or a web interface.

## Ethical Considerations

This project demonstrates potential vulnerabilities in open environments. It is strictly intended for research and awareness purposes. Users are advised to use it responsibly and ensure compliance with privacy laws.

## Future Work

- Enhance model accuracy with larger datasets.
- Integrate countermeasure techniques such as sound obfuscation.
- Extend real-time prediction capabilities.

## Contributing

Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and open a pull request.
