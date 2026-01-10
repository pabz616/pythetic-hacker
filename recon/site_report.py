"""
RECON STEP: USING SITE REPORT
scope: Obtain invaluable site information via Netcraft
"""

import webbrowser


netcraft = "https://sitereport.netcraft.com"


def run_search(site):
    webbrowser.open(netcraft+f"?url={site}")

# ###*******************************************#######


def view_report(url):
    run_search(url)


if __name__ == "__main__":
    target = input("Please enter the domain name (e.g., example.com) to obtain the site's report: ")
    view_report(target)

