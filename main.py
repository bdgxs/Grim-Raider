from util.plugins.commun import *
def main():
    clear()
    setTitle(f"Grim Raider™")
    astraahometitle()
    print(f"""
\n          {y}[{b}+{y}]{w} Options:
\n          {y}[{w}1{y}]{w} Account Nuker          {y}[{w}6{y}]{w} Token Info              {y}[{w}11{y}]{w} Webhook Remover
\n          {y}[{w}2{y}]{w} Settings Cycler        {y}[{w}7{y}]{w} Discord House Changer   
\n          {y}[{w}3{y}]{w} Mass DM                {y}[{w}8{y}]{w} Discord Server Lookup   
\n          {y}[{w}4{y}]{w} Token Checker          {y}[{w}9{y}]{w} Nitro Generator         
\n          {y}[{w}5{y}]{w} Autologin              {y}[{w}10{y}]{w} Webhook Spammer          
""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    
    if choice == '1':
        transition()
        exec(open('util/accountnuker.py').read())
    elif choice == '2':
        transition()
        exec(open('util/settingscycler.py').read())
    elif choice == '3':
        transition()
        exec(open('util/massdm.py').read())
    elif choice == '4':
        transition()
        exec(open('util/tokenschecker.py').read()) 
    elif choice == '5':
        transition()
        exec(open('util/autologin.py').read())
    elif choice == '6':
        transition()
        exec(open('util/tokeninfo.py').read())
    elif choice == '7':
        transition()
        exec(open('util/housechanger.py').read())
    elif choice == '8':
        transition()
        exec(open('util/serverlookup.py').read())
    elif choice == '9':
        transition()
        exec(open('util/nitrogen.py').read())
    elif choice == '10':
        transition()
        exec(open('util/webhookspam.py').read())
    elif choice == '11':
        transition()
        exec(open('util/webhookremover.py').read())
    else:
        clear()
        main()


if __name__ == "__main__":
    import sys
    import threading
    setTitle("Grim Raider™ Loading...")
    System.Size(150, 45)
    Anime.Fade(Center.Center(banner), Colors.red_to_green, Colorate.Vertical, time=2)
    if not os.path.exists("output"):
        os.makedirs("output", exist_ok=True)
    if os.path.exists("output/QR-Code"):
        shutil.rmtree(f"output/QR-Code")
    os.system("""if not exist "util/chromedriver.exe" echo [#] Downloading chromedriver: """)
    os.system("""if not exist "util/chromedriver.exe" curl -#fkLo "util/chromedriver.exe" "https://github.com/AstraaDev/complement/raw/main/chromedriver.exe" """)
    if os.path.basename(sys.argv[0]).endswith("exe"):
        thread = threading.Thread(target=start_webdriver)
        thread.start()
        clear()
        main()
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} Sorry but, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with @TIO, please download python 3.9 or higher.")
        sys.exit()
    else:
        thread = threading.Thread(target=start_webdriver)
        thread.start()
        clear()
        main()
