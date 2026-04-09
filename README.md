# Network Reconnaissance Tool 🔍

A network reconnaissance tool built in Python that gathers information about a target.

## Features
- IP address lookup from hostname
- Ping to check if host is alive
- Reverse hostname resolution
- Port scanning with service detection
- Save scan results to a report file

## Usage
```bash
python recon_tool.py
```

## Example Output
[+] IP Address : 45.33.32.156
[+] Host is ALIVE and responding!
[+] Hostname : scanme.nmap.org
[OPEN] Port 22 --> ssh
[OPEN] Port 80 --> http

## Note
> Port scanning works best on Linux/Kali Linux.
> Windows Firewall may affect port scan results.

## Legal Target for Testing
scanme.nmap.org

## Tech
- Python 3
- Socket module
- Subprocess module

## Disclaimer
This tool is for educational purposes only.
Always scan targets you have permission to test.
