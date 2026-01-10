"""
SCRIPT: cve_checker.py
DESCRIPTION: This script checks for known CVEs (Common Vulnerabilities and Exposures) in the software installed on a target system. 
It scans the system for installed packages, compares them against a database of known vulnerabilities, and generates a report of any findings.
"""

import requests


def check_vulnerabilities(service, version):
    base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keyword": f"{service} {version}",
        "resultsPerPage": "10"
    }  
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
    
        if data["totalResults"] > 0:
            print(f"Vulnerabilities found for {service} {version}:")
            for results in data["result"]["CVE_Items"]:
                cve_id = results["cve"]["CVE_data_meta"]["ID"]
                description = results["cve"]["description"]["description_data"][0]["value"]
                print(f"- {cve_id}: {description}")
        else:
            print(f"No known vulnerabilities found for {service} {version}.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error checking vulnerabilities: {e}")
        
        
if __name__ == "__main__":
    service = input("Please enter the service name (e.g., nginx, apache): ")
    version = input("Please enter the service version (e.g., 1.18.0): ")
    check_vulnerabilities(service, version)
    
