try:import random;from colorama import Fore;from requests import get,post
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
def saver(user):
    ID=''#telegram id
    token=''#telegram bot token
    try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• New username’s Claimed @{user} 🦦\n\nBy\t@TweakPY\t-\t@vv1ck')
    except:pass
    with open('Available.txt', 'a') as x:
        x.write(user+'\n')
def with_list():
    error,count,done=0,0,0
    try:file=open('user.txt', 'r')
    except FileNotFoundError:exit('[!] No users File Detected - Note users file must be in user.txt File ..')
    while True:
        user=file.readline().split('\n')[0]
        ru=get(f"https://t.me/{user}")
        if ru.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
            done+=1
            count+=1
            saver(user)
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
def without_list():
    count,done,error=0,0,0
    user=""
    lena=input('[?] Length: ');length=(int(lena))
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
    while True:
        for user in range(1):
            user=""
            for item in range(length):
                user+=random.choice(chars)
        ru=get(f"https://t.me/{user}")
        if ru.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >=0:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
            done+=1
            count+=1
            saver(user)
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
print("""
████████╗██╗       ██████╗██╗  ██╗
╚══██╔══╝██║      ██╔════╝██║  ██║
   ██║   ██║█████╗██║     ███████║
   ██║   ██║╚════╝██║     ██╔══██║
   ██║   ███████╗ ╚██████╗██║  ██║
   ╚═╝   ╚══════╝  ╚═════╝╚═╝  ╚═╝
        By @TweakPY - @vv1ck                          
""")
LW=int(input("[1] without List\n[2] with List\n---------------\nEnter > : "))
if LW==1:without_list()
elif LW==2:with_list()
else:exit('\n[!] Exit... \n\nBy @TweakPY - @vv1ck')
