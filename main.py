from typing import List, Union, Dict, Any, Tuple, Optional
import platform
import os
import re
import time
import threading
import random
import requests
from pystyle import Colors, Colorate, System, Anime, Center
import ctypes

# Function to check if the current system is Linux
def check_linux() -> bool:
    if platform.system() == "Linux":
        return True
    return False

# ANSI color codes for console output
B = '\033[35m'
R = '\033[31m'
N = '\033[0m'
A = '\033[34m'
BB = '\033[36m'

# Class to represent log timestamps
class LogTime:
    def __str__(self) -> str:
        timestamp = time.strftime("%H:%M:%S", time.localtime()) + f".{int(time.time() * 1000) % 1000:03d}"
        return f" {Colors.reset}[{Colors.yellow}{timestamp}{Colors.reset}]{Colors.reset}"
log_time = LogTime()

# Function to check if the proxies file exists and contains valid entries
def check_proxies_file() -> bool:
    print(f"{log_time} {Colors.green}Checking proxies.txt file...")

    if not os.path.isfile('proxies.txt'):
        # Create a default proxies.txt file if it doesn't exist
        with open('proxies.txt', 'w') as file:
            file.write('proxy1.example.com:8080\n')
            file.write('proxy2.example.com:8080\n')
        print(f"{log_time} {Colors.red}proxies.txt file does not exist.")
        print(f"{log_time} {Colors.green}Created proxies.txt file.")
        print(f"{log_time} {Colors.green}Edit proxies.txt file & run the script again to be able to use proxies.")
        print(f"{log_time} {Colors.yellow}Note: if you dont know what is this just dont use or edit it.")
        print()
        return False
    elif check_linux():
        # Currently not supporting proxies on Linux
        print(f"{log_time} {Colors.red}We don't support Linux proxy system yet. Coming soon...")
        print(f"{log_time} {Colors.red}Can't use proxies.")
        print()
        return False
    else:
        print(f"{log_time} {Colors.green}proxies.txt file exists.")
        with open('proxies.txt', 'r') as file:
            content = file.readlines()
            valid_proxies = []
            for proxy in content:
                proxy = proxy.strip()
                if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+$', proxy):
                    valid_proxies.append(proxy)
            if len(valid_proxies) > 0:
                print(f"{log_time} {Colors.green}Valid proxies found in proxies.txt file.")
                print()
                return True
            else:
                print(f"{log_time} {Colors.red}No valid proxies found in proxies.txt file.")
                print(f"{log_time} {Colors.green}Edit proxies.txt file & run the script again to add valid proxies.")
                print(f"{log_time} {Colors.yellow}Note: if you don't know what this is, just don't use or edit it.")
                print()
                return False

# Function to change the system proxy settings
def change_proxy():
    with open('proxies.txt', 'r') as file:
        proxies = file.read().splitlines()
    selected_proxy = random.choice(proxies)
    proxy_setting_command = f"netsh winhttp set proxy proxy-server={selected_proxy} > NUL"
    os.system(proxy_setting_command)

# Introduction animation
intro = """
██████╗ ██╗    ██╗███████╗██████╗       
██╔══██╗██║    ██║██╔════╝██╔══██╗       ██╗
██████╔╝██║ █╗ ██║█████╗  ██████╔╝     ██████╗
██╔═══╝ ██║███╗██║██╔══╝  ██╔══██╗       ██╔═╝
██║     ╚███╔███╔╝███████╗██████╔╝       ╚═╝
╚═╝      ╚══╝╚══╝ ╚══════╝╚═════╝

              > Press Enter
"""

Anime.Fade(Center.Center(intro), Colors.red_to_yellow, Colorate.Vertical, interval=0.035, enter=True)

# Main function
def main():
    avatar_url = ""
    banner = """
██████╗ ██╗    ██╗███████╗██████╗       
██╔══██╗██║    ██║██╔════╝██╔══██╗       ██╗
██████╔╝██║ █╗ ██║█████╗  ██████╔╝     ██████╗
██╔═══╝ ██║███╗██║██╔══╝  ██╔══██╗       ██╔═╝
██║     ╚███╔███╔╝███████╗██████╔╝       ╚═╝
╚═╝      ╚══╝╚══╝ ╚══════╝╚═════╝

"""

    # Set window title and clear screen based on the platform
    if platform.system() == "Windows":
        os.system("title PWeb - Made by P1shi")
        os.system("cls")
    else:
        System.Title("PWeb - Made by P1shi")

    try:
        print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(banner), 2))
        webhook_url = input(Colorate.Horizontal(Colors.red_to_yellow, f" Webhook URL : ", 1))
        time.sleep(1)

        # Function to check if the webhook exists
        def check_webhook_existence(webhook_url):
            try:
                response = requests.head(webhook_url)
                if response.status_code in [200, 201, 202, 203, 204]:
                    return True
                elif response.status_code == 404:
                    return False
            except requests.exceptions.RequestException as e:
                return False

        if check_webhook_existence(webhook_url):
            print(f"{log_time} {Colors.green}Webhook Exists.")
        else:
            print(f"{log_time} {Colors.red}Webhook does not exist please check the Webhook URL.")
            time.sleep(2)
            main()

        # Function to get the username for the webhook
        def get_username():
            time.sleep(1.5)
            System.Clear()
            print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(banner), 2))
            custom_username = input(Colorate.Horizontal(Colors.red_to_yellow, f" Webhook username : ", 1))
            if custom_username == "":
                time.sleep(1)
                print(f"{log_time} {Colors.red}Please Enter a Valid Username.")
                time.sleep(3)
                get_username()
            time.sleep(1)

            # Function to get the number of messages to send
            def get_msgs_count():
                time.sleep(0.5)
                System.Clear()
                print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(banner), 2))
                count = input(Colorate.Horizontal(Colors.red_to_yellow, f" Messages Count : ", 1)) 
                if not count.isdigit():
                    print(f"{log_time} {Colors.red}Please Enter a Valid Number.")
                    time.sleep(2)
                    get_msgs_count()
                count = int(count)
                time.sleep(1)

                # Function to get the content of the message
                def get_content():
                    time.sleep(0.5)
                    System.Clear()
                    print(Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(banner), 2))
                    message_content = input(Colorate.Horizontal(Colors.red_to_yellow,f" Content : ", 1))
                    if message_content == "":
                        print(f"{log_time} {Colors.red}Please fill the content.")
                        time.sleep(2)
                        get_content()
                    time.sleep(1)
                    message = {"content": message_content, "username": custom_username, "avatar_url": avatar_url}

                    # Function to send messages
                    def send_msg():
                        use_proxy = input(Colorate.Horizontal(Colors.red_to_yellow, " do you want to use proxy ? [y/n] : ", 1))

                        if use_proxy.lower() == "y":
                            if check_proxies_file():
                                use_proxy = True
                            else:
                                use_proxy = False
                        else:
                            use_proxy = False

                        import requests
                        from requests.adapters import HTTPAdapter
                        from requests.packages.urllib3.util.retry import Retry

                        def send_message():
                            session = requests.Session()
                            retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[429, 500, 502, 503, 504])
                            session.mount('http://', HTTPAdapter(max_retries=retries))

                            for i in range(count):
                                try:
                                    response = session.post(webhook_url, json=message)
                                    if response.status_code == 204:
                                        print(f"{log_time} {Colors.green}Message Successfully Sent.")
                                    elif response.status_code == 429:
                                        if use_proxy:
                                            print(f"{log_time} {Colors.red}You are being rate limited. Changing Proxy and Waiting 1 second.")
                                            change_proxy()
                                            time.sleep(1)
                                            response = session.post(webhook_url, json=message)
                                            continue  # continue to the next iteration of the loop
                                        else:
                                            print(f"{log_time} {Colors.red}You are being rate limited. Trying again in 1 second.")
                                            time.sleep(1)
                                            response = session.post(webhook_url, json=message)
                                            continue  # continue to the next iteration of the loop
                                    elif response.status_code == 404:
                                        print(f"{log_time} {Colors.red}Can't Find The Webhook.")
                                        continue
                                    else:
                                        print(f"{log_time} {Colors.red}An Unknown Error Occurred : {response.text}")
                                        if use_proxy:
                                            change_proxy()
                                        continue
                                except requests.exceptions.RequestException as e:
                                    print(f"{log_time} {Colors.red}Request Exception occurred: {e}")
                                    if use_proxy:
                                        change_proxy()
                                    continue

                            print(f"{log_time} {Colors.green}All Messages Sent.")
                            print()
                            back = input(f"{log_time} {Colors.reset}Do you want to go back? [y/n] : ")
                            if back == "y" or back == "yes" or back == "Y" or back == "Yes":
                                print(f"{log_time} {Colors.green}Returning back...")
                                time.sleep(2)
                                main()
                            else:
                                print(f"{log_time} {Colors.green}Closing...")
                                time.sleep(2)
                                exit()

                        send_message()

                    send_msg()

                get_content()

            get_msgs_count()

        get_username()

    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f'Error Reason : {e}', 'An Error Occurred with PWeB.', 16)
        exit()

main()
