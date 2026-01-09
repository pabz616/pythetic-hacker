"""
SCRIPT: recon.who_is
DESCRIPTION: performs a WHOIS lookup for a given domain or IP address
"""


import whois


def perform_whois_lookup(target):
    try:
        w = whois.whois(target)
        print(f"WHOIS information for {target}:")
        print(f"Domain Name: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
        return w
    except Exception as e:
        return f"Error performing WHOIS lookup: {e}"


if __name__ == "__main__":
    domain = input("Enter a domain or IP address for WHOIS lookup: ")
    perform_whois_lookup(domain)
