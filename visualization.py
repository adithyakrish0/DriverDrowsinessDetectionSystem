import matplotlib.pyplot as plt
import numpy as np

class EARPlot:
    def __init__(self):
        self.ears = []

    def update(self, ear):
        self.ears.append(ear)

    def show(self):
        plt.ion()
        fig, ax = plt.subplots()
        while True:
            ax.clear()
            ax.plot(self.ears, label='EAR')
            ax.set_title('Real-time EAR values')
            ax.legend()
            plt.pause(0.05)
