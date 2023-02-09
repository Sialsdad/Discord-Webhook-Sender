import colorama
import requests
import time
from colorama import Fore
from colorama import init

init()
print(Fore.MAGENTA+"""
██████╗  ██████╗  ██████╗ ██████╗  ██████╗  ██████╗ 
██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔═══██╗██╔════╝ 
██████╔╝██║   ██║██║  ███╗██║  ██║██║   ██║██║  ███╗
██╔═══╝ ██║   ██║██║   ██║██║  ██║██║   ██║██║   ██║
██║     ╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝╚██████╔╝
╚═╝      ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                                    """)



time.sleep(0.6)



print(Fore.RED+"Made With Love By pogdog_#1372")
time.sleep(0.6)
print(Fore.BLUE+"Do what you will with the source code but don't make it malicious")
time.sleep(0.6)
print(Fore.CYAN+"discord.gg/giving")
print(" ")
print(" ")
time.sleep(2)
print(Fore.RED+"Loading...")
time.sleep(1)
print(Fore.GREEN+"Welcome To My Tool!!!")
time.sleep(0.5)


with open("config.txt", "r") as f:
    config = f.readlines()
webhook_url = config[0].strip()
webhook_name = config[1].strip()

try:
    response = requests.get(webhook_url, verify=False)
    response.raise_for_status()
    print("Webhook URL is valid.")
except requests.exceptions.HTTPError as err:
    print(f"Error: {err}")
    exit()

avatar_url = config[2].strip()

while True:
    message = input("Enter your message: ")
    data = {
        "username": webhook_name,
        "avatar_url": avatar_url,
        "content": message,
    }
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
input()
