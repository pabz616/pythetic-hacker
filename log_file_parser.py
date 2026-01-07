"""
SCRIPT: log_file_parser.py
DESCRIPTION: A script that parses a log file to extract IP addresses and count
their occurrences.
"""

import re
from collections import Counter


def parse_log_file(file_path):
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_addresses = []
    
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(ip_pattern, line)
            ip_addresses.extend(matches)
            
    return Counter(ip_addresses)


def main():
    log_file = 'access.log'
    ip_counts = parse_log_file(log_file)
    
    print("Top 10 IP addresses by occurrence:")
    for ip, count in ip_counts.most_common(10):
        print(f"{ip}: {count}")
        
        
if __name__ == "__main__":
    main()