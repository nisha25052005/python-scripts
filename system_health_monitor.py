import psutil
import time

# Define threshold values
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 90.0

def check_cpu_usage():
    """Check CPU usage and alert if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT! CPU usage is high: {cpu_usage}%")
    else:
        print(f"CPU usage: {cpu_usage}%")

def check_memory_usage():
    """Check memory usage and alert if it exceeds the threshold."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"ALERT! Memory usage is high: {memory_usage}%")
    else:
        print(f"Memory usage: {memory_usage}%")

def check_disk_usage():
    """Check disk usage and alert if it exceeds the threshold."""
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        print(f"ALERT! Disk usage is high: {disk_usage}%")
    else:
        print(f"Disk usage: {disk_usage}%")

def main():
    """Main function to monitor system health."""
    while True:
        print("\n--- System Health Check ---")
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
