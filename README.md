# 🛑 Driver Drowsiness Detection System

A real-time Python-based driver drowsiness detection system using Eye Aspect Ratio (EAR) analysis and webcam video feed. Alerts drivers through a sound alarm and logs drowsiness events for further analysis.

---

## 🚀 Features

- 🎥 Real-time video processing via webcam
- 👁️ Eye blink and drowsiness detection using Eye Aspect Ratio (EAR)
- 🔊 Alarm sound triggers on drowsiness detection
- 📊 Logs EAR values and timestamps for visualization
- 📈 Graphical analysis of drowsiness trends over time

---

## 📦 Tech Stack

- Python 3.7+
- OpenCV
- dlib
- imutils
- numpy
- matplotlib
- pygame

---

## 🛠️ Installation

git clone https://github.com/adithyakrish0/DriverDrowsinessDetectionSystem.git
cd DriverDrowsinessDetectionSystem
pip install -r requirements.txt

Ensure your webcam is connected and accessible.
▶️ Usage

python app.py

    The system will start your webcam.

    When drowsiness is detected based on EAR threshold and frame count, an alarm will play.

📁 File Structure
File	Description
app.py	Main entry point. Runs webcam loop and triggers alert logic.
data_logger.py	Logs EAR values and drowsiness events with timestamps.
drowsiness_detector.py	Computes EAR and detects drowsiness from facial landmarks.
video_handler.py	Handles webcam video input and frame processing.
visualization.py	Provides real-time feedback and EAR graphs.
plotter.py	Generates analysis plots from logged data.
🔮 Future Scope

    Integration with GPS-based alert system

    Dashboard to monitor driver behavior over long drives

    Deployable mobile version (via Android + TFLite)

    Real-time cloud sync for fleet management use cases

👨‍💻 Developed By

Adithyakrishnan P N
Final Year B.Tech (AI & ML), Marian Engineering College
GitHub | LinkedIn
