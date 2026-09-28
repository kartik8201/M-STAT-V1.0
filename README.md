# M-STAT V1.0

### System & Network Monitoring and Diagnostic Tool

M-STAT is a Python based terminal application designed to monitor system resources and network conditions from a single interface. It combines system monitoring, process analysis, network information, speed testing, and diagnostic analysis.

## Problem Statement

When a computer becomes slow or the internet connection becomes unstable, users often need to check multiple tools to identify the cause. M-STAT provides these checks through one lightweight terminal based application.

## Objectives

- Monitor CPU, RAM, and storage usage.
- Identify processes using high CPU resources.
- Display important network information.
- Test internet download and upload speeds.
- Check ping latency and packet loss.
- Provide an overall system and network diagnostic.

## Features

### Quick Diagnostic
Performs a combined check of system resources, top processes, internet connectivity, ping, and packet loss, then provides an overall status.

### System Monitor
Displays current CPU, RAM, and storage usage.

### Process Monitor
Displays the top CPU-consuming processes with their PID and CPU usage.

### Network Monitor
Displays the connected WiFi network, IP address, DNS server, current network traffic, internet speed, and ping.

### Health Analyzer
Classifies system resource usage as NORMAL, WARNING, or HIGH.

### Live Monitor
Continuously displays changing system resource information.

## Technologies Used

- Python
- psutil
- speedtest-cli
- Windows networking utilities

## Project Structure
M-STAT/
├── main.py
├── system_monitor.py
├── process_monitor.py
├── network_monitor.py
├── diagnostics.py
├── health_analyzer.py
├── live_monitor.py
└── README.md

## Installation

Install the required packages:
pip install psutil speedtest-cli

## Running the Project

Run the application using:
python main.py

The main menu provides access to all monitoring and diagnostic modules.

## Testing

Each major module has been tested through the main application, including system monitoring, process monitoring, network monitoring, speed testing, health analysis, quick diagnostics, and live monitoring.

## Demo

M-STAT can be demonstrated through the following workflow:

1. Launch the application using `python main.py`.
2. Run Quick Diagnostic to check overall system and network conditions.
3. View CPU, RAM, and storage information.
4. Analyze the top CPU-consuming processes.
5. Check network information and run an internet speed test.
6. View the system health analysis.
7. Run Live Monitor to observe changing system resources.

A demonstration video and screenshots can be included with the project submission.

## Future Enhancements

Diagnostic history and logging
Exportable diagnostic reports
Additional network diagnostics
More detailed process analysis
Cross-platform support