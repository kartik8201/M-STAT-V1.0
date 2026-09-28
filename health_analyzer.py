def get_status(value, warning, critical):
    if value >= critical:
        return "HIGH"
    elif value >= warning:
        return "WARNING"
    else:
        return "NORMAL"

def generate_health_report(cpu, ram, disk):
    print("\n========== SYSTEM HEALTH ==========")

    cpu_status = get_status(cpu, 70, 90)
    ram_status = get_status(ram, 75, 90)
    disk_status = get_status(disk, 80, 95)

    print(f"CPU Usage   : {cpu:.1f}%   [{cpu_status}]")
    print(f"RAM Usage   : {ram:.1f}%   [{ram_status}]")
    print(f"Disk Usage  : {disk:.1f}%   [{disk_status}]")

    print("\nIssues detected:")
    issues = 0

    if cpu >= 90:
        print("- Very high CPU usage")
        issues += 1

    if ram >= 90:
        print("- Very high RAM usage")
        issues += 1

    if disk >= 95:
        print("- Very low disk space")
        issues += 1

    if issues == 0:
        print("- No major system issues detected")

    print("===================================")