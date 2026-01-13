"""
SCRIPT wifi_scan.py
DESCRIPTION Scans for available Wi-Fi networks and displays their SSIDs, signal strengths, and security types.
"""

from scapy.all import sniff, Dot11, Dot11Beacon, Dot11Elt


def wifi_scan():
    print("Scanning for available Wi-Fi networks...\n")
    networks = {}
    
    def packet_handler(pkt):
        if pkt.haslayer(Dot11Beacon):
            ssid = pkt[Dot11Elt].info.decode()
            bssid = pkt[Dot11].addr2
            channel = int(ord(pkt[Dot11Elt:3].info))
            
            if bssid not in networks:
                networks[bssid] = (ssid, channel)
                print(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}")
                sniff(prn=packet_handler, timeout=15)
            
            print("\nScan complete.")
            

if __name__ == "__main__":
    wifi_scan()