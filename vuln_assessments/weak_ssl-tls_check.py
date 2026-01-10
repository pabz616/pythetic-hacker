"""
SCRIPT: vuln_assessments.weak_ssl-tls_check
DESCRIPTION: checks for weak SSL/TLS configurations on a given host
"""

import socket
import ssl
import nmap


def nmap_scan_weak_tls(host, ports):
    nm = nmap.PortScanner()
    print(f"Scanning {host} for weak SSL/TLS protocols using Nmap...")
    
    nm.scan(host, ports, arguments='--script ssl-enum-ciphers')
    
    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                version = nm[host][proto][port]['version']
                print(f"Port: {port}\tState: {state}\tService: {service}\tVersion: {version}")

                              
def scan_ssl_protocols(host, port):
    print(f"\n--- Starting TLS Protocol Scan for {host}:{port} ---\n")

    # Define the protocols we want to check.
    # We use the ssl.TLSVersion enum for modern Python (3.7+)
    protocols_to_test = [
        ("TLSv1.0", ssl.TLSVersion.TLSv1),
        ("TLSv1.1", ssl.TLSVersion.TLSv1_1),
        ("TLSv1.2", ssl.TLSVersion.TLSv1_2),
        ("TLSv1.3", ssl.TLSVersion.TLSv1_3),
    ]

    for proto_name, proto_enum in protocols_to_test:
        check_protocol(host, port, proto_name, proto_enum)
        
    print("\n--- Scan Complete ---")


def check_protocol(host, port, proto_name, proto_version):
    # 1. Create a fresh context for each attempt
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    # 2. Force the specific version
    try:
        context.minimum_version = proto_version
        context.maximum_version = proto_version
    except ValueError:
        # This happens if the local OpenSSL installation has disabled this protocol entirely
        print(f"[*] {proto_name:<10}: SKIPPED (Not supported by your local OpenSSL)")
        return

    # 3. Attempt Connection
    try:
        with socket.create_connection((host, port), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=host) as secure_sock:
                # If we get here, the handshake succeeded
                print(f"[+] {proto_name:<10}: SUPPORTED")
                print(f"    Cipher: {secure_sock.cipher()[0]}")
                
    except ssl.SSLError as e:
        # Handshake failed -> Protocol likely not supported by server
        # We check the error message to be sure it's a handshake failure
        err_str = str(e)
        if "alert" in err_str or "handshake failure" in err_str or "wrong version" in err_str:
            print(f"[-] {proto_name:<10}: NOT SUPPORTED (Server rejected)")
        else:
            print(f"[!] {proto_name:<10}: ERROR ({e})")
            
    except socket.timeout:
        print(f"[!] {proto_name:<10}: TIMEOUT")
    except ConnectionRefusedError:
        print(f"[!] {proto_name:<10}: CONNECTION REFUSED")
    except Exception as e:
        print(f"[!] {proto_name:<10}: ERROR ({type(e).__name__})")


if __name__ == "__main__":
    target_ports = "21-25, 80, 443"
    target_host = input("Enter a domain name to scan (e.g., example.com): ").strip()
    
    scan_ssl_protocols(target_host, target_ports)
    nmap_scan_weak_tls(target_host, target_ports)