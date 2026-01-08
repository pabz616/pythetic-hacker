"""
SCRIPT: python_basics.py
DESCRIPTION: A simple refresher on all things python .. because it's been a bit!
"""

import webbrowser

# VARIABLES
# my_var = "cool variable"
# my_number = 12345

# PRINT THE VARIABLE
# a = 1
# b = 2
# sum = a + b
# print("this is a cool refresher", sum)

# BOOLEANS- True/False for conditional logic
is_open = True
has_permission = False

# LISTS - Ordered collections of items used for storing multiple values.
open_ports = [80, 443, 22]
usernames = ["admin", "root", "user"]

# DICTIONARY - Key-value pairs used for storing structured data (found in JSON)
server_info = {
    "ip": "10.0.0.1",
    "os": "Kali Linux"
}

# TUPLES - Immutable ordered collection used for storing FIXED data (strings or ints that you don't want to be modified!)
ip_ports = ("192.168.1.1", 80)
version_info = (2, 7, 20)

# SET - Editable unordered collection of unique items; no dupes
unique_ips = {"192.168.1.1", "10.0.0.1", "172.16.0.1"}

# LOOPING / ITERATING
for i in range(1, 5, 1):
    print("I love ethical hacking!")
print("*"*10)

# fruit_basket = ["grapes", "apple", "banana", "cherry"]
for fruit in fruit_basket:
    if fruit == "banana":
        continue
    print("I love ", fruit)

breaking_news = True
while not breaking_news:
    print("Nothing happened!")
    breaking_news += 1
else:
    print("Miami Dolphins have 86d HC Mike MacDaniel after 5 seasons.")

print("*"*10)
# ACCEPTING INPUTS (w. FString)
website = input("Please enter a url: ")


# DEFINED FUNCTION (def)
def visit_site():
    print(f"You've entered the website {website}.")

    visit = input("Shall we visit the site? Enter Y for yes, or N for no. ")    
    if (visit == "Y"):
        webbrowser.open(website)
    elif (visit == "N"):
        print("Okie dokie! Have a great day.")
    else:
        print("The value you entered is unacceptable. Please try again.")


visit_site()

# PRO TIP: always be using small, digestible functions with appropriate variable names
# CODE COMMENT: Add comments to explain complex logic or provide context for your code.
# HANDLE EXCEPTIONS - Use try-except blocks to handle potential errors gracefully.
