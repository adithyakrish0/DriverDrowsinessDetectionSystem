import matplotlib.pyplot as plt
from collections import deque
import numpy as np

class Plotter:
    def __init__(self, max_points=100, smooth_window=5):
        """Initialize the plotter with smoothing."""
        self.max_points = max_points
        self.smooth_window = smooth_window
        self.ear_values = deque(maxlen=max_points)

    def update(self, ear):
        """Update the plot with smoothed EAR values."""
        self.ear_values.append(ear)
        plt.clf()

        # Smooth the graph using a moving average
        if len(self.ear_values) >= self.smooth_window:
            smoothed_ear = np.convolve(
                np.array(self.ear_values), 
                np.ones(self.smooth_window)/self.smooth_window, 
                mode='valid'
            )
        else:
            smoothed_ear = np.array(self.ear_values)

        plt.plot(smoothed_ear, label="Smoothed EAR", color='green')
        plt.ylim(0, 0.4)
        plt.axhline(y=0.20, color='red', linestyle='--', label='Drowsiness Threshold')
        plt.xlabel('Frames')
        plt.ylabel('EAR')
        plt.legend()
        plt.pause(0.01)
