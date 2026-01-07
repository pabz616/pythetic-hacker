"""
SIMPLE SCRIPT USING REQUESTS TO MAKE A GET REQUEST
"""

import requests


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully connected to {url}")
            print(f"Server: {response.headers.get('Server')}")
        else:
            print(f"Failed to connect to {url}. Status code:{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


url = input("Please enter a URL: ")
check_website(url)