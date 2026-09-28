import psutil
import time
import os


def live_monitor():
    try:
        while True:
            cpu = psutil.cpu_percent(interval=0.5)
            ram = psutil.virtual_memory().percent

            old = psutil.disk_io_counters()
            time.sleep(0.5)
            new = psutil.disk_io_counters()

            disk_activity = (
                (new.read_bytes - old.read_bytes) +
                (new.write_bytes - old.write_bytes)
            ) / 1024 / 1024

            storage = psutil.disk_usage('/').percent

            os.system("cls")

            print("===== M-STAT LIVE =====")
            print(f"CPU      : {cpu:.1f}%")
            print(f"RAM      : {ram:.1f}%")
            print(f"Disk     : {disk_activity:.1f} MB/s")
            print(f"Storage  : {storage:.1f}% used")
            print("\nRefreshing...")
            print("Press Ctrl+C to stop")

    except KeyboardInterrupt:
        print("\nStopped.")