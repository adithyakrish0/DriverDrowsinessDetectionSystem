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

app.py
➤ The main entry point of the application.
It initializes the webcam, runs the drowsiness detection loop, and handles real-time alerts.

data_logger.py
➤ Handles logging of drowsiness events and relevant metrics.
Saves data like timestamps, EAR values, and alarm triggers for later analysis.

drowsiness_detector.py
➤ Contains the core detection logic.
Calculates Eye Aspect Ratio (EAR) and determines if the driver is drowsy based on a threshold and frame count.

plotter.py
➤ Utility module to generate plots/graphs from logged data.
Useful for analyzing driver alertness trends over time.

video_handler.py
➤ Manages video input from the webcam.
Provides pre-processed frames for the detection module and handles frame display.

visualization.py
➤ Provides real-time visual feedback.
Displays EAR graphs or other live metrics to the screen while the app runs.
