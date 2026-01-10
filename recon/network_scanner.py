"""
RECON STEP: NETWORK SCANNER
"""

from scapy.all import IP, TCP, ICMP, sr1, RandShort


def scan_network(target, ports):
    print(f"Scanning {target} for open TCP ports...")
    for port in ports:
        src_port = RandShort()
        resp = sr1(IP(dst=target)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        
        if resp is None:
            print(f"Port {port}: No response (filtered or closed)")

        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
                sr1(IP(dst=target)/TCP(sport=src_port, dport=port, flags="R"), timeout=1, verbose=0)
                print(f"Port {port}: is Open. Verify if vulnerable.")

            elif resp.getlayer(TCP).flags == 0x14:  # RST-ACK
                print(f"Port {port}: is Closed.")

            elif resp.haslayer(ICMP):
                if int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                    print(f"Port {port}: is Filtered (ICMP response).")

    target = input("Please enter the target IP address to scan: ")
    ports = [21, 22, 80, 443, 3389]
    scan_network(target, ports)
