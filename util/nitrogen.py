import time
import os
import random
import string
import ctypes
import requests
from colorama import Fore
from util.plugins.commun import setTitle, clear, nitrogentitle

def generate_code(length=16):
    """Generate a random Nitro code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=length))

def check_nitro_code(code, webhook=None):
    """Check if a Nitro code is valid and optionally send it to a webhook."""
    url = f"https://discord.gift/{code}"
    response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    
    if response.status_code == 200:
        print(f"{Fore.GREEN}[!]{Fore.WHITE} VALID NITRO: {url}")
        if webhook:
            try:
                requests.post(webhook, json={'content': url})
            except Exception as e:
                print(f"{Fore.YELLOW}[!]{Fore.WHITE} Failed to send to webhook: {e}")
        return True, url
    
    elif response.status_code == 429:
        retry_after = response.json().get('retry_after', 1000) / 1000
        print(f"{Fore.LIGHTRED_EX}[!]{Fore.WHITE} Rate limited, retrying in {retry_after:.2f} seconds")
        time.sleep(retry_after)
        return check_nitro_code(code, webhook)  # Retry the same code after sleeping

    else:
        print(f"{Fore.RED}[!]{Fore.WHITE} INVALID NITRO: {url}")
        return False, None

def main():
    setTitle("Nitro Generator and Checker")
    clear()
    nitrogentitle()

    num = int(input(f"{Fore.YELLOW}[#{Fore.WHITE}]{Fore.WHITE} Input the number of codes to generate and check: "))
    webhook = input(f"{Fore.YELLOW}[#{Fore.WHITE}]{Fore.WHITE} Enter Discord Webhook URL (or press enter to skip): ") or None

    valid_codes = []
    invalid_count = 0

    clear()
    for _ in range(num):
        code = generate_code()
        is_valid, url = check_nitro_code(code, webhook)
        
        if is_valid:
            valid_codes.append(url)
            with open("output/NitroCodes.txt", "a") as file:
                file.write(f"{url}\n")
        else:
            invalid_count += 1

        # Update console title with progress
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Nitro Generator and Checker - {len(valid_codes)} Valid | {invalid_count} Invalid - Made by Astraa"
            )

    # Results summary
    print(f"\n{Fore.YELLOW}[+]{Fore.WHITE} Results:")
    print(f"    {Fore.LIGHTGREEN_EX}[!]{Fore.WHITE} Valid: {len(valid_codes)}")
    print(f"    {Fore.LIGHTRED_EX}[!]{Fore.WHITE} Invalid: {invalid_count}")
    print(f"    {Fore.WHITE}[!]{Fore.WHITE} Valid Codes: {', '.join(valid_codes) if valid_codes else 'None'}")

    input(f"\n{Fore.YELLOW}[#{Fore.WHITE}]{Fore.WHITE} Press ENTER to exit")

if __name__ == "__main__":
    main()