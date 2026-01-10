"""
SCRIPT: dns_resolver.py
DESCRIPTION: A simple DNS resolver that takes a domain name as input and returns its corresponding IP address
(Requires 'dnspython' library: pip install dnspython)
"""

import dns.resolver


def dns_enumerate(domain):
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT']
        
    for record_type in record_types:
        try:
            # Perform DNS resolution for A records
            answers = dns.resolver.resolve(domain, record_type)
            print(f"\n{record_type} Records for {domain}:")

            for rdata in answers:
                print(f" - {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"No {record_type} record found")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist.")
        except Exception as e:
            return f"An error occurred: {e}"
        print() 
 
    
if __name__ == "__main__":
    domain = input("Please enter a domain name to resolve (e.g., example.com): ")
    dns_enumerate(domain)