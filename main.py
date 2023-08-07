import requests
from colorama import Fore

def get_ip_info(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}?token={token}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    token = 'e7010c58031a67'
    ip_address = input("IP : ")
    ip_info = get_ip_info(ip_address, token)

    print(Fore.LIGHTMAGENTA_EX + f"IP: {ip_info['ip']}")
    print("{")
    print(f"    \"ip\": \"{ip_info['ip']}\",")
    print(f"    \"hostname\": \"{ip_info['hostname']}\",")
    print(f"    \"city\": \"{ip_info['city']}\",")
    print(f"    \"region\": \"{ip_info['region']}\",")
    print(f"    \"country\": \"{ip_info['country']}\",")
    print(f"    \"loc\": \"{ip_info['loc']}\",")
    print(f"    \"org\": \"{ip_info['org']}\",")
    print(f"    \"postal\": \"{ip_info['postal']}\",")
    print(f"    \"timezone\": \"{ip_info['timezone']}\"")
    print("}")

if __name__ == "__main__":
    main()
