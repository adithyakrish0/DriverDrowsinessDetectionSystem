import csv
import os

class DataLogger:
    def __init__(self, log_path):
        self.log_path = log_path
        # Ensure the directory exists
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        # Write the header if the file is new
        if not os.path.isfile(log_path):
            with open(log_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Timestamp', 'EAR'])

    def log(self, ear):
        """Log the EAR value with a timestamp."""
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, ear])
