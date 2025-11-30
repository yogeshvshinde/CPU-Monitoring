
# This script monitors the CPU usage of the system. If the CPU usage exceeds the specified threshold (default is 80%), it prints a warning message. The monitoring continues until interrupted by the user (Ctrl+C).


import psutil
import time


def monitor_cpu_usage(threshold=80):

    print ("Monitoring CPU usage...")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold:{cpu_usage}%")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("CPU usage monitor stopped.")

    except Exception as e:
        print(f"An error occurred: {e}")    

if __name__ == "__main__":
    monitor_cpu_usage(threshold=80)

    

