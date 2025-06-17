# Driver Drowsiness Detection System

A Python project that detects driver drowsiness in real-time using webcam input and eye aspect ratio (EAR) analysis. If drowsiness is detected, an alarm sound is played to alert the driver.

## Features

- Real-time video analysis
- Eye blink detection using EAR
- Sound alert for drowsiness
- Basic data logging and visualization

## Requirements

- Python 3.7+
- opencv-python
- dlib
- imutils
- numpy
- matplotlib
- pygame

Install using:

pip install -r requirements.txt

Usage

python app.py

Ensure your webcam is enabled. Alarm triggers on drowsiness.

Files

    app.py – Main script
    drowsiness_detector.py – Core logic
    video_handler.py – Webcam input
    alarm.mp3 – Sound alert
