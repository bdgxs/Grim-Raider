def main():
    setTitle("Nitro Generator and Checker")  
    clear()
    
    num = int(input(f"{Fore.YELLOW}[#{Fore.WHITE}]{Fore.WHITE} Input the number of codes to generate and check: "))
    webhook = input(f"{Fore.YELLOW}[#{Fore.WHITE}]{Fore.WHITE} Enter Discord Webhook URL (or press enter to skip): ") or None
    
    valid_codes = []
    invalid_count = 0
    
    for _ in range(num):
        code = generate_code()
        is_valid, url = check_nitro_code(code, webhook)
        
        if is_valid:
            valid_codes.append(url)
            with open("output/NitroCodes.txt", "a") as file:
                file.write(f"{url}\n")
        else:
            invalid_count += 1
    
    # Results summary  
    print(f"\n{Fore.YELLOW}[+]{Fore.WHITE} Results:")  
    print(f"    {Fore.LIGHTGREEN_EX}[!]{Fore.WHITE} Valid: {len(valid_codes)}")
    print(f"    {Fore.LIGHTRED_EX}[!]{Fore.WHITE} Invalid: {invalid_count}") 
    print(f"    {Fore.WHITE}[!]{Fore.WHITE} Valid Codes: {', '.join(valid_codes) if valid_codes else 'None'}")

    input(f"\n{Fore.YELLOW}[#{Fore.WHITE}]{Fore.WHITE} Press ENTER to exit")
