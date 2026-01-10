"""
SCRIPT: search_metafiles.py
SRC: WSTG-INFO-03 - Review Webserver Metafiles for Information Leakage

DESCRIPTION:
1. Identify hidden or obfuscated paths and functionality through the analysis of metadata files.
2. Extract and map other information that could lead to a better understanding of the systems at hand.
"""

import requests

target = input('Please enter the target URL (e.g., http://example.com): ')

METAFILES = {
    f"{target}/.git/config": "Git Configuration File",
    f"{target}/.git/config.bak": "Backup of Git Configuration File",
    f"{target}/.git/HEAD": "Git Repository Head File",
    f"{target}/.gitignore": "Git Ignore File",
    f"{target}/.svn/entries": "Subversion Entries File",
    f"{target}/.hg/hgrc": "Mercurial Configuration File",
    f"{target}/.bzr/branch/branch.conf": "Bazaar Branch Configuration File",
    f"{target}/.DS_Store": "macOS Directory Store File",
    f"{target}/.idea/workspace.xml": "JetBrains IDE Workspace File",
    f"{target}/.vscode/settings.json": "Visual Studio Code Settings File",
    f"{target}/.env": "Environment Variables File",
    f"{target}/config.php": "PHP Configuration File",
    f"{target}/wp-config.php": "WordPress Configuration File",  
    f"{target}/.htaccess": "Apache Configuration File",
    f"{target}/.htpasswd": "Apache Password File",
    f"{target}/robots.txt": "Robots Exclusion File",
    f"{target}/sitemap.xml": "Sitemap XML File",
    f"{target}/.well-known/security.txt": "Security Policy File",
    f"{target}/.docker/config.json": "Docker Configuration File",
    f"{target}/.aws/credentials": "AWS Credentials File",
    f"{target}/.azure/credentials": "Azure Credentials File",
    f"{target}/.gcp/credentials.json": "Google Cloud Platform Credentials File",
    f"{target}/.npmignore": "NPM Ignore File",
    f"{target}/humans.txt": "Humans Information File",    
    f"{target}/.npmrc": "NPM Configuration File",
    f"{target}/.pypirc": "Python Package Index Configuration File",
    f"{target}/.dockerignore": "Docker Ignore File",
    f"{target}/.htaccess.bak": "Backup of Apache Configuration File",
    f"{target}/.env.bak": "Backup of Environment Variables File"
}


def test_for_metafiles():
    for url, description in METAFILES.items():
        try:
            response = requests.get(url).status_code == 200
            if response:
                print(f"[FOUND] {description}: {url}")
            else:
                print(f"[NOT FOUND] {description}: {url}")
        except Exception as e:
            print(f"[ERROR] Could not access {url}: {e}")
            
            
if __name__ == "__main__":
    test_for_metafiles()