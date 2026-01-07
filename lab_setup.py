import socket
import subprocess
import json
import sys
import platform  # New import for OS info


def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def get_installed_packages():
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'list', '--format=json'], 
            capture_output=True, 
            text=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        return {"error": f"Could not retrieve packages: {str(e)}"}


def document_lab_setup():
    lab_info = {
        # OS and System Details
        "os_name": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        
        # Network and Environment
        "hostname": socket.gethostname(),
        "ip_address": get_ip_address(),
        "python_version": sys.version,
        "installed_packages": get_installed_packages()
    } 
    try:
        with open('lab_setup.json', 'w') as f:
            json.dump(lab_info, f, indent=2)
        print("✅ Comprehensive lab setup documented in lab_setup.json")
    except IOError as e:
        print(f"❌ Failed to write file: {e}")
        
        
if __name__ == "__main__":
    document_lab_setup()