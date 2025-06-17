import cv2
import time

class VideoHandler:
    def __init__(self, input_path=None, output_path=None):
        self.input_path = input_path
        self.output_path = output_path

    def process_webcam(self, detector, plotter, logger):
        """Process webcam feed in real-time."""
        cap = cv2.VideoCapture(0)  

        if not cap.isOpened():
            print("Error: Could not access webcam.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # Detect drowsiness
            ear = detector.detect(frame, logger)

            # Display EAR and alert status
            cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.7, (0, 255, 0), 2)

            # Alert overlay
            if ear < 0.20:
                cv2.putText(frame, "DROWSY ALERT!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.8, (0, 0, 255), 2)

            cv2.imshow("Webcam Feed", frame)
            plotter.update(ear)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
