#!/usr/bin/env python3
# =======================================
# Network Reconnaissance Tool
# By PxCSA | For educational use only
# =======================================

import socket
import subprocess
import platform
import os
from datetime import datetime

def banner():
    print("=" * 55)
    print("      Network Reconnaissance Tool by PxCSA")
    print("=" * 55)

def get_ip(target):
    print(f"\n[*] Resolving IP for: {target}")
    try:
        ip = socket.gethostbyname(target)
        print(f"  [+] IP Address : {ip}")
        return ip
    except socket.gaierror:
        print("  [-] Could not resolve hostname!")
        return None

def ping_target(target):
    print(f"\n[*] Pinging {target}...")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "3", target]
    try:
        output = subprocess.run(command, capture_output=True, text=True, timeout=10)
        if output.returncode == 0:
            print("  [+] Host is ALIVE and responding!")
        else:
            print("  [-] Host is not responding or offline.")
    except Exception as e:
        print(f"  [-] Ping failed: {e}")

def get_hostname(ip):
    print(f"\n[*] Getting hostname for {ip}...")
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"  [+] Hostname : {hostname}")
    except:
        print("  [-] Could not get hostname.")

def scan_ports(ip, start_port, end_port):
    print(f"\n[*] Scanning ports {start_port} to {end_port} on {ip}...")
    print("  Please wait...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            sock.close()
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"  [OPEN] Port {port:5d}  -->  {service}")
                open_ports.append((port, service))
        except:
            pass

    return open_ports

def save_report(target, ip, open_ports):
    filename = f"recon_{target.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as f:
        f.write("=" * 55 + "\n")
        f.write("   Network Reconnaissance Report by PxCSA\n")
        f.write("=" * 55 + "\n")
        f.write(f"Target   : {target}\n")
        f.write(f"IP       : {ip}\n")
        f.write(f"Date     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 55 + "\n\n")
        f.write("Open Ports:\n")
        if open_ports:
            for port, service in open_ports:
                f.write(f"  Port {port} --> {service}\n")
        else:
            f.write("  No open ports found.\n")
    print(f"\n  [+] Report saved as: {filename}")

def main():
    banner()
    print("\nDISCLAIMER: Use this tool only on targets you have permission to scan!")
    print("-" * 55)

    target = input("\nEnter target (IP or hostname): ").strip()
    if not target:
        print("No target entered. Exiting.")
        return

    start = int(input("Start port (e.g. 1)  : "))
    end   = int(input("End port   (e.g. 100): "))

    print("\n" + "=" * 55)
    print(f"  Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    # Step 1 - Get IP
    ip = get_ip(target)
    if not ip:
        return

    # Step 2 - Ping
    ping_target(target)

    # Step 3 - Hostname
    get_hostname(ip)

    # Step 4 - Port Scan
    open_ports = scan_ports(ip, start, end)

    # Step 5 - Summary
    print("\n" + "=" * 55)
    print(f"  Scan complete!")
    print(f"  Open ports found: {len(open_ports)}")
    print("=" * 55)

    # Step 6 - Save report
    save = input("\nSave report to file? (yes/no): ").strip().lower()
    if save == 'yes':
        save_report(target, ip, open_ports)

    print("\n  Thank you for using Recon Tool by PxCSA!")
    print("=" * 55)

if __name__ == "__main__":
    main()