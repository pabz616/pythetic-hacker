"""
SCRIPT_NAME = "password_policy_enforcement.py"
DESCRIPTION = "This script enforces a strong password policy for user accounts.
It checks for minimum length, complexity requirements, and expiration settings.
The script generates a report of non-compliant accounts and can optionally"
"""

import re


def check_password_strength(password):
    """Check if the password meets the minimum length requirement."""
    if len(password) < 12:
        return False, "[!] RESULT: Password must be at least 12 characters long."
    
    """Check for complexity: at least one uppercase."""
    if not re.search(r'[A-Z]', password):
        return False, "[!] RESULT: Password must contain at least one uppercase letter."

    """Check for complexity: at least one lowercase."""
    if not re.search(r'[a-z]', password):
        return False, "[!] RESULT: Password must contain at least one lowercase letter."
    
    """Check for complexity: at least one digit."""
    if not re.search(r'\d', password):
        return False, "[!] RESULT: Password must contain at least one digit."
    
    """Check for complexity: at least one special character."""
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "[!] RESULT: Password must contain at least one special character."
    
    return True, "[✓] RESULT: Password meets all strength requirements."


def enforce_password_policy():
    """Main function to enforce password policy."""
    while True:
        password = input("Enter a new password to check: ")
        is_strong, message = check_password_strength(password)
       
        if is_strong:
            print(message)
            return password
        else:
            print(f"Invalid password. {message} Please try again.\n")
  
            
if __name__ == "__main__":
    new_password = enforce_password_policy()