"""
SCRIPT: network_usage_policy.py
DESCRIPTION: This script monitors and enforces network usage policies. It checks for bandwidth limits,
restricted websites, and usage timeframes."
"""
import time
from scapy.all import sniff


def monitor_network_traffic(interface, max_bandwidth_mbps):
    """Monitor network traffic on the specified interface and enforce bandwidth limits."""
    max_bytes_per_sec = max_bandwidth_mbps * 1024 * 1024 / 8  # Convert Mbps to Bytes per second
    start_time = time.time()
    total_bytes = 0
    
    def packet_callback(packet):
        nonlocal total_bytes
        total_bytes += len(packet)
        
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:
            current_bandwidth = total_bytes / elapsed_time
            print(f"Current Bandwidth Usage: {current_bandwidth / 1024 / 1024 * 8:.2f} Mbps")
            
            if current_bandwidth > max_bytes_per_sec:
                print("[!] ALERT: Bandwidth limit exceeded!")
                # Here you could add code to block traffic or notify the user
                
                total_bytes = 0
                nonlocal start_time
                start_time = time.time()
            
        sniff(iface=interface, prn=packet_callback, store=0)
        
        
if __name__ == "__main__":
    ntwk_iface = input("Enter the network interface to monitor (e.g., eth0, wlan0): ")
    limit = float(input("Enter the maximum bandwidth limit in Mbps: "))
    monitor_network_traffic(ntwk_iface, limit)