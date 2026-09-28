import psutil
import time

def get_top_processes():
    processes = []

    for process in psutil.process_iter(["pid", "name"]):
        try:
            name = process.info["name"]
            if name == "System Idle Process":
                continue
            process.cpu_percent()
            processes.append(process)

        except:
            pass

    time.sleep(1)
    results = []

    for process in processes:
        try:
            cpu = process.cpu_percent()

            results.append({
                "pid": process.pid,
                "name": process.name(),
                "cpu_percent": cpu
            })

        except:
            pass

    results.sort(
        key=lambda x: x["cpu_percent"],
        reverse=True
    )
    return results[:5]