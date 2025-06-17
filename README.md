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

## ▶️ Usage

python app.py

    The system will start your webcam.

    When drowsiness is detected based on EAR threshold and frame count, an alarm will play.

## 📁 File Structure

| File                     | Description                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `app.py`                 | **Main entry point** – Initializes the webcam, runs the real-time detection loop, and handles drowsiness alerts. |
| `data_logger.py`         | **Data logging module** – Records EAR values, alarm triggers, and timestamps for post-run analysis.              |
| `drowsiness_detector.py` | **Detection logic** – Calculates the Eye Aspect Ratio (EAR) and determines drowsiness based on thresholds.       |
| `video_handler.py`       | **Video input handler** – Captures and processes frames from the webcam for analysis.                            |
| `visualization.py`       | **Live visual feedback** – Displays EAR metrics or graphs in real-time while the system is running.              |
| `plotter.py`             | **Offline analysis tool** – Generates plots/graphs from logged data to visualize drowsiness trends.              |


## 🔮 Future Scope

    Integration with GPS-based alert system

    Dashboard to monitor driver behavior over long drives

    Deployable mobile version (via Android + TFLite)

    Real-time cloud sync for fleet management use cases

## 👨‍💻 Developed By

Adithyakrishnan P N
Final Year B.Tech (AI & ML), Marian Engineering College

[LinkedIn](https://www.linkedin.com/in/adithyakrishnanpn/)
