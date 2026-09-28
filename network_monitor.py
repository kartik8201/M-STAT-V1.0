import psutil
import socket
import subprocess
import time
import speedtest

def speed_test():
    print("\n===== INTERNET SPEED TEST =====")
    print("Testing... please wait.")

    st = speedtest.Speedtest()

    st.get_best_server()

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    ping = st.results.ping

    print(f"Download Speed : {download:.2f} Mbps")
    print(f"Upload Speed   : {upload:.2f} Mbps")
    print(f"Ping           : {ping:.0f} ms")


def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    old_stats = psutil.net_io_counters()
    time.sleep(1)
    new_stats = psutil.net_io_counters()

    download_speed = (
        new_stats.bytes_recv - old_stats.bytes_recv
    ) / 1024 / 1024

    upload_speed = (
        new_stats.bytes_sent - old_stats.bytes_sent
    ) / 1024 / 1024

    # WiFi name
    wifi = subprocess.run(
        ["netsh", "wlan", "show", "interfaces"],
        capture_output=True,
        text=True
    )

    wifi_name = "Not connected"

    for line in wifi.stdout.splitlines():
        if "SSID" in line and "BSSID" not in line:
            wifi_name = line.split(":", 1)[1].strip()
            break

    # DNS server
    dns = subprocess.run(
        ["nslookup", "localhost"],
        capture_output=True,
        text=True
    )

    dns_server = "Unknown"

    for line in dns.stdout.splitlines():
        if "Address:" in line:
            dns_server = line.split(":", 1)[1].strip()
            break

    return (
        hostname,
        ip_address,
        download_speed,
        upload_speed,
        wifi_name,
        dns_server
    )
def run_diagnostics():
    import subprocess

    print("\n===== NETWORK DIAGNOSTICS =====")

    host = input("Enter website/host to test: ")

    result = subprocess.run(
        ["ping", "-n", "4", host],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode == 0:
        print("Status: Connection successful")
    else:
        print("Status: Connection failed")

    input("\nPress Enter to return...")