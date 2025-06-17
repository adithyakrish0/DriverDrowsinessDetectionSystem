import cv2
import numpy as np
import dlib
from scipy.spatial import distance
import time
import threading
import pygame  # ✅ Use pygame for sound playback

class DrowsinessDetector:
    def __init__(self, plotter=None, threshold=0.20, alarm_duration=2):
        """Initialize the Drowsiness Detector."""
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.plotter = plotter
        self.last_drowsy_time = None
        self.threshold = threshold
        self.alarm_duration = alarm_duration
        self.alarm_on = False

        # ✅ Initialize pygame mixer
        pygame.mixer.init()

    def eye_aspect_ratio(self, eye):
        """Calculate the Eye Aspect Ratio (EAR)."""
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def play_alarm(self):
        """Play the alarm sound in a separate thread."""
        def alarm_thread():
            pygame.mixer.music.load("alarm.mp3")  # Load the alarm sound
            pygame.mixer.music.play(-1)  # Play on loop

        # Start the alarm in a non-blocking thread
        threading.Thread(target=alarm_thread, daemon=True).start()

    def stop_alarm(self):
        """Stop the alarm sound."""
        pygame.mixer.music.stop()

    def detect(self, frame, logger):
        """Detect faces and calculate EAR."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)

        if len(faces) == 0:
            return 0  

        for face in faces:
            landmarks = self.predictor(gray, face)

            # Extract eye coordinates
            left_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)]
            right_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)]

            # Calculate EAR
            ear = (self.eye_aspect_ratio(left_eye) + self.eye_aspect_ratio(right_eye)) / 2.0
            logger.log(ear)

            # Drowsiness detection logic
            if ear < self.threshold:
                if self.last_drowsy_time is None:
                    self.last_drowsy_time = time.time()

                elif time.time() - self.last_drowsy_time > self.alarm_duration:
                    # Trigger alarm only if it's not already playing
                    if not self.alarm_on:
                        self.alarm_on = True
                        print("🚨 Alarm ON 🚨")
                        self.play_alarm()

                    # Display drowsiness alert
                    cv2.putText(frame, "DROWSY ALERT!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (0, 0, 255), 2)

            else:
                # Reset drowsiness timer and stop alarm if EAR is above threshold
                self.last_drowsy_time = None
                if self.alarm_on:
                    print("✅ Alarm OFF ✅")
                    self.alarm_on = False
                    self.stop_alarm()

            return ear

        return 0
