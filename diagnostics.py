from system_monitor import get_system_info
from process_monitor import get_top_processes
from health_analyzer import get_status
import subprocess
import re

def quick_diagnostic():
    print("\n===== QUICK DIAGNOSTIC =====")

    cpu, ram, disk = get_system_info()

    print(f"CPU Usage     : {cpu:.1f}% [{get_status(cpu,70,90)}]")
    print(f"RAM Usage     : {ram:.1f}% [{get_status(ram,75,90)}]")
    print(f"Storage Usage : {disk:.1f}% [{get_status(disk,80,95)}]")

    processes = get_top_processes()

    if processes:
        top = processes[0]
        print(f"\nTop Process: {top['name']} ({top['cpu_percent']:.1f}% CPU)")

    result = subprocess.run(
        ["ping", "-n", "4", "google.com"],
        capture_output=True,
        text=True
    )

    output = result.stdout
    ping = re.search(r"Average = (\d+)ms", output)
    loss = re.search(r"\((\d+)% loss\)", output)

    if result.returncode == 0:
        print("\nNetwork    : CONNECTED")
        print(f"Ping       : {ping.group(1)} ms" if ping else "Ping       : N/A")
        print(f"Packet Loss: {loss.group(1)}%" if loss else "Packet Loss: N/A")
    else:
        print("\nNetwork    : FAILED")

    print("\n===== DIAGNOSTIC RESULT =====")

    issues = 0

    if cpu >= 90:
        print("- Very high CPU usage")
        issues += 1

    if ram >= 75:
        print("- High RAM usage")
        issues += 1

    if disk >= 95:
        print("- Very high storage usage")
        issues += 1

    if result.returncode != 0:
        print("- Network connection problem")
        issues += 1
    elif loss and int(loss.group(1)) > 0:
        print(f"- Packet loss detected: {loss.group(1)}%")
        issues += 1

    if issues == 0:
        print("Status: NORMAL")
        print("No major issues detected.")
    elif issues <= 2:
        print(f"Status: WARNING ({issues} issue(s))")
    else:
        print(f"Status: CRITICAL ({issues} issues)")

    input("\nPress Enter to return...")