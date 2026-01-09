"""
SCRIPT: login_form_check.py
DESCRIPTION: a script that automates form submission and checks for basic vulnerabilities
"""

import requests
from bs4 import BeautifulSoup


def submit_form(url, username, password):
    """HANDLES THE FORM SUBMISSION SESSION CREATION"""
    session = requests.Session()
    
    # GET THE LOGIN PAGE AND RETRIEVE CSRF TOKEN
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name', 'csrf_token'})['value']

    # PREP THE LOGIN FORM DATA
    data = {
        'username': username,
        'password': password,
        'csrf_token': csrf_token
    }
    
    # SUBMIT FORM
    response = session.post(url, data=data)
    return response


def check_vulnerabilities(response):
    """PERFORMS THE VULNERABILITY CHECK FOR THE GIVEN URL"""
    vulnerabilities = []

    # CHECK FOR SQL INJECTION VULN
    if "SQL syntax" in response.text:
        vulnerabilities.append("Potential SQL injection vulnerability found on this form.")

    # CHECK FOR XSS
    if "<script>" in response.text:
        vulnerabilities.append("Potential XSS vulnerability found on the form.")

    # CHECK FOR SENSITIVE DATA EXPOSURE
    if "password" in response.text.lower():
        vulnerabilities.append("Potential sensitive data exposure vulnerability found.")

    return vulnerabilities


def main():
    """THE FUNCTION THAT RUNS THE SCRIPT INTERACTION WITH THE USER"""
    
    url = input("Enter the login form URL: ")
    username = input("Enter the username or email: ")
    password = input("Enter the password: ")

    response = submit_form(url, username, password)

    print(f"Status code: {response.status_code}")
    print(f"Response.length: {len(response.text)}")

    vulnerabilities = check_vulnerabilities(response)

    if vulnerabilities:
        print("Potential vulnerabilities found:")
        for vuln in vulnerabilities:
            print(f"-{vuln}")
    else:
        print(f"No obvious vulnerabilities detected for {url}")


if __name__ == "__main__":
    main()
