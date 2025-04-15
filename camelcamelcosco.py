import platform
import sys
import requests

# USER INFORMATION



HEADERS = {}    # browser header 


def get_os_info():
    system = platform.system()
    release = platform.release()
    arch = platform.machine()
    
    if system == "Windows":
        ua_os = f"Windows NT {release}; {arch}"
    elif system == "Darwin":
        mac_ver = platform.mac_ver()[0]
        mac_version_parts = mac_ver.split(".")
        if len(mac_version_parts) >= 2:
            major, minor = mac_version_parts[:2]
            ua_os = f"Macintosh; Intel Mac OS X {major}_{minor}"
        else:
            ua_os = "Macintosh; Intel Mac OS X 10_15"
    elif system == "Linux":
        ua_os = "X11; Linux x86_64"
    else:
        ua_os = "X11; Unknown OS"

    return ua_os

def get_user_agent():
    os_info = get_os_info()
    return {
        "User-Agent": f"Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }


if __name__ == "__main__":

    # {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    # }
    
    headers = get_user_agent()
    print("Dynamic Headers:\n", headers)

# create session
session = requests.Session()
session.headers.update(HEADERS)

