"""
SCRIPT: web_scraper.py
DESCRIPTION: A script that scrapes the headers of a given website
"""

import requests
from bs4 import BeautifulSoup


def scrape_headers(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        print(f"Headers found on {url}:")
        for header in headers:
            print(f"{header.name}: {header.text.strip()}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
        
def main():
    url = input("Enter the URL to scrape: ")
    scrape_headers(url)
        
        
if __name__ == "__main__":
    main()