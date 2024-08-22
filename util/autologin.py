import requests
import time
from colorama import Fore
from util.plugins.commun import *

from selenium import webdriver

def autologin():
    setTitle("Auto Login")
    clear()

    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the token of the account you want to connect to")
    entertoken = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Token: ")

    headers = {'Authorization': entertoken, 'Content-Type': 'application/json'}
    validity_test = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

    if validity_test.status_code != 200:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid token")
        input(f"""\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to exit""")
        main()

    try:
        driver = webdriver.Chrome(executable_path=r'util/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://discord.com/login')

        # JavaScript code to inject the token into localStorage
        js = (
            'function login(token) {'
            'setInterval(() => {'
            'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`;'
            '}, 50);'
            'setTimeout(() => {location.reload();}, 500);'
            '}'
        )

        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)

        if driver.current_url == 'https://discord.com/login':
            clear()
            print(f"""{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Connection Failed""")
        else:
            clear()
            print(f"""{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Connection Established""")

        driver.close()
        input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to exit""")
        main()

    except Exception as e:
        print(f"      {Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} A problem occurred: {e}")
        time.sleep(2)
        clear()
        main()

autologin()
