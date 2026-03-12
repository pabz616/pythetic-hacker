"""
SCRIPT: ./vuln_assessment/network_vuln_check.py
DESCRIPTION: This script performs a network vulnerability assessment by scanning specified IP ranges for common vulnerabilities. 
It utilizes Nmap for scanning and generates a report of findings.
"""

import nmap
import paramiko
import socket
from scapy.all import ARP, Ether, srp


class NetworkPenTester:
    def __init__(self, ip_ranges):
        self.ip_ranges = ip_ranges
        
    def discover_live_hosts(self):
        """Discovers live hosts in the specified IP ranges using ARP requests."""
        arp = ARP(pdst=self.ip_ranges)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        result = srp(packet, timeout=3, verbose=0)[0]
        return [received.psrc for sent, received in result]
    
    def port_scan(self, host):
        """Scans the host for open ports and services using Nmap."""
        nm = nmap.PortScanner()
        nm.scan(host, arguments='-T4 -p- -sV -sC --open')
        return nm[host]
        
    def check_ssh_vulnerability(self, host, port=22):
        try:
            sock = socket.create_connection((host, port), timeout=5)
            ssh = paramiko.Transport(sock)
            try:
                ssh.start_client()
                # Check for known vulnerable SSH versions
                if ssh.remote_version.startswith(b'SSH-2.0-OpenSSH_7.2'):
                    print(f"Potential SSH vulnerability on {host}:{port} - OpenSSH 7.2 detected.")
                
                # Attempt to authenticate with common weak credentials
                weak_credentials = [('root', 'toor'), ('admin', 'admin'), ('user', 'password')]
                for username, password in weak_credentials:
                    try:
                        ssh.auth_password(username, password)
                        if ssh.is_authenticated():
                            return True, f"Weak SSH credentials found: {username}/{password}"
                    except paramiko.AuthenticationException:
                        continue
            finally:
                ssh.close()
        except (socket.error, paramiko.SSHException):
            pass
        
    def run_pentest(self):
        print(f"Starting Network Penetration Test on ranges: {self.ip_ranges}")

        # Discover live hosts
        live_hosts = self.discover_live_hosts()
        print(f"Discovered {len(live_hosts)} live hosts.")
        
        for host in live_hosts:
            print(f"Scanning host: {host}")
            scan_results = self.port_scan(host)
            
            # PORT AND SERVICE ANALYSIS
            for proto in scan_results.all_protocols():
                print(f"[-] Protocol: {proto}")
                ports = scan_results[proto].keys()
                
                for port in ports:
                    service = scan_results[proto][port]
                    print(f"[+] Port {port}: {service['name']} - {service['product']} {service['version']}")
             
                # CHECK FOR SSH VULNERABILITIES
                if 22 in scan_results['tcp']:
                    self.check_ssh_vulnerability(host, 22)
                    
            print("\n[✓] Network Penetration Test Completed.\n")               

    def generate_report(self):
        print("Vulnerability Report:")
        for vuln in self.vuln_report:
            print(f"Host: {vuln['host']}, Port: {vuln['port']}, Service: {vuln['service']}")
            print(f"Vulnerability: {vuln['vulnerability']}")
            print(f"Details: {vuln['details']}\n")
            
            
if __name__ == "__main__":
    target_ip_ranges = input("Enter target IP  or full ranges (e.g. 192.168.1.0/24) ")
    pentester = NetworkPenTester(target_ip_ranges)
    pentester.run_pentest()
    pentester.generate_report()