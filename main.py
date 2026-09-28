from system_monitor import get_system_info
from process_monitor import get_top_processes
from health_analyzer import generate_health_report
from live_monitor import live_monitor
from diagnostics import quick_diagnostic
from network_monitor import get_network_info, speed_test

def show_menu():
    print("\n")
    print("========================================")
    print("            M-STAT V1.0")
    print("     System & Network Monitor")
    print("========================================")
    print("1. Quick Diagnostic")
    print("2. System Monitor")
    print("3. Process Monitor")
    print("4. Network Monitor")
    print("5. Health Analyzer")
    print("6. Live Monitor")
    print("7. Exit")
    print("========================================")


while True:
    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":
        quick_diagnostic()

    elif choice == "2":
        cpu, ram, disk = get_system_info()

        print("\n===== SYSTEM MONITOR =====")
        print(f"CPU Usage  : {cpu}%")
        print(f"RAM Usage  : {ram}%")
        print(f"Disk Usage : {disk}%")

    elif choice == "3":
        print("\n===== TOP PROCESSES =====")

        processes = get_top_processes()

        for process in processes:
            print(
                f"PID: {process['pid']} | "
                f"{process['name']} | "
                f"CPU: {process['cpu_percent']:.1f}%"
            )

    elif choice == "4":
        hostname, ip, download, upload, wifi, dns = get_network_info()

        print("\n===== NETWORK MONITOR =====")
        print(f"Computer     : {hostname}")
        print(f"WiFi Network : {wifi}")
        print(f"IP Address   : {ip}")
        print(f"DNS Server   : {dns}")
        print(f"Download     : {download:.2f} MB/s")
        print(f"Upload       : {upload:.2f} MB/s")

        speed_test()

    elif choice == "5":
        cpu, ram, disk = get_system_info()
        generate_health_report(cpu, ram, disk)

    elif choice == "6":
        live_monitor()

    elif choice == "7":
        print("Exiting M-STAT...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")