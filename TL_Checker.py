try:import time,requests,random,os;from colorama import Fore
except ModuleNotFoundError:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip uninstall colorama')
	os.system('pip install colorama')
global x2,j
x2='[🖤] @TweakPY'
j='''
[☑️] NEW USER:︎︎
'''
def with_list():
	error,count,done=0,0,0
	file=open('user.txt', 'r')
	try:
		use_checkers=open('id_token.txt', "r").read().splitlines()
		ID=use_checkers[0]
		token=use_checkers[1]
	except:
		pass
		print('[!] No Token/id Detected ')
	while True:
		user=file.readline().split('\n')[0]
		req=requests.get(f"https://t.me/{user}")
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			try:requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
			except:pass
			with open('Available.txt', 'a') as x:
				tl='[] NEW USER -->  '
				x.write(tl + user + '\n')
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
def without_list():
	count,done,error=0,0,0
	user=""
	lena=input('[?] Length: ')
	length=(int(lena))
	try:
		use_checkers = open('id_token.txt', "r").read().splitlines()
		ID=use_checkers[0]
		token=use_checkers[1]
	except:
		pass
		print('[!] No Token/id Detected ')
		chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
		while True:
			for user in range(1):
				user=""
				for item in range(length):
					user+=random.choice(chars)
			send=requests.get(f"https://t.me/{user}")
			if send.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >=0:
				print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
				done+=1
				count+=1
				try:requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
				except:pass
				with open('Available.txt', 'a') as x:
					tl='[] NEW USER -->  '
					x.write(tl+user+'\n')
			else:
				print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
				error+=1
				count+=1
print(f"{Fore.RED}Author:@TweakPY Free Tool Not for sell{Fore.RESET}")
m=int(input("1- Telegram Checker Without List\n2- Telegram Checker with list\n:"))
if m==1:without_list()
elif m==2:with_list()
else:exit('• None !')
