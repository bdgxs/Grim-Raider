import requests
import threading
from colorama import Fore
from util.plugins.commun import setTitle, getheaders, clear, main, massdmtitle

def MassDM(token, channels, message):
    for channel in channels:
        for user in [f"{x['username']}#{x['discriminator']}" for x in channel["recipients"]]:
            try:
                setTitle(f"Messaging {user}")
                response = requests.post(
                    f"https://discord.com/api/v9/channels/{channel['id']}/messages",
                    headers={'Authorization': token},
                    data={"content": message}
                )
                if response.status_code == 200:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Messaged: {user}")
                else:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Failed to message: {user}")
            except Exception as e:
                print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error encountered: {e}")

def main_mass_dm():
    setTitle("Mass DM")
    clear()
    massdmtitle()

    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter the token of the account you want to spam")
    token = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Token: ")

    validity_test = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if validity_test.status_code != 200:
        print(f"\n{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Invalid token")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to exit")
        main()

    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Message that will be sent to every friend")
    message = input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Message: ")

    clear()

    channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    
    if not channel_ids:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} No direct messages found.")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
        main()

    processes = []
    for channel_batch in [channel_ids[i:i + 3] for i in range(0, len(channel_ids), 3)]:
        t = threading.Thread(target=MassDM, args=(token, channel_batch, message))
        t.start()
        processes.append(t)

    for process in processes:
        process.join()

    input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to continue")
    main()

main_mass_dm()