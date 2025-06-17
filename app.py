import argparse
from drowsiness_detector import DrowsinessDetector
from plotter import Plotter
from video_handler import VideoHandler
from data_logger import DataLogger

def main():
    parser = argparse.ArgumentParser(description="Drowsiness Detection")
    parser.add_argument('--video', type=str, help='Path to the video file')
    parser.add_argument('--webcam', action='store_true', help='Use webcam for real-time detection')
    args = parser.parse_args()

    # ✅ Initialize the plotter
    plotter = Plotter()

    # ✅ Pass the plotter instance when creating the detector
    detector = DrowsinessDetector(plotter)

    # ✅ Provide input and output paths for VideoHandler
    input_path = args.video if args.video else "webcam"
    output_path = "output/drowsiness_output.avi"  # Adjust the output path

    # ✅ Initialize VideoHandler with the required arguments
    video_handler = VideoHandler(input_path, output_path)

    # ✅ Provide a log path when creating the DataLogger instance
    log_path = "output/ear_log.csv"  # Path for logging the EAR values
    logger = DataLogger(log_path)    # ✅ Pass log_path argument

    if args.video:
        print(f"Processing video: {args.video}")
        video_handler.process_video(detector, plotter, logger, args.video)
    elif args.webcam:
        print("Starting webcam...")
        video_handler.process_webcam(detector, plotter, logger)
    else:
        print("Please specify either --video or --webcam")

if __name__ == "__main__":
    main()
