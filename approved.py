import os,base64,sys,re
try:
    import rich
except:
    os.system("pip install rich")
    import rich
from rich import print as rp
from rich.panel import Panel
from datetime import datetime
logo="""logo"""



K1=str(os.getuid())
K2=str(os.getgid())
num_key="h".join(K1+K2)
cm=num_key.encode("ASCII")
cmr=base64.b64encode(cm)
cm2=str(cmr)
#####KEY NAME ######
kx=cm2.replace("b","SIFAT")
####################
key=kx.upper()
##### APPROVE URL #####

url=base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1RFQU0tRUxJVEUxL2RhdGFiYXNlL21haW4vSm9zcy50eHQ=')

######################
main_url=url.decode("ASCII")
all_datA=[]



def req(team_elite,main_url):
    try:
        lx=team_elite.get(main_url)
        approved=lx.text
        return approved
    except:
        rp("[bold red] Internet Error")
        sys.exit()

def url_sefty():
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py","r").read()
        vx=re.search("print",h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def url_sefty2():
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_api.py","r").read()
        vx=re.search("print",h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def key_sefty():
    global key
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_models.py","r").read()
        vx=re.search(key,h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def key_sefty2():
    global key
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py","r").read()
        vx=re.search(key,h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def lisens():
    global key 
    ky=key.split('\'')[1]
    li=ky[5:15]
    try:
        open("/data/data/com.termux/files/usr/bin/.sifa.txt","r").read()
        expired_ck()
    except:
        while True:
            os.system("clear")
            print(logo)
            xcx=input("License Key =>")
            if xcx == li:
                open("/data/data/com.termux/files/usr/bin/.sifa.txt","a").write("done")
                expired_ck()
                break 
            else:
                continue 
    
def expired_ck():
    global key,all_datA
    tita=str(datetime.now()).split(" ")[0]
    tic=tita.split("-")
    pure_data=int(tic[0]+tic[1]+tic[2])
    for x in all_datA:
        if key in x:
            
            break 
        else:
            continue
    
    HERON=int(x.split("\'|")[1])
    
    if pure_data < HERON:
        ######main()
        print("")
        
        
        
    else:
        print(" YOUR APPROVAL DATE IS EXPIRED")
    
def uninstall_able():
    try:
        open("/data/data/com.termux/files/usr/bin/pip","r").read()
        open("/data/data/com.termux/files/usr/bin/pip3","r").read()
    except:
        print(" you are useing Ant-uninstall system ")
        sys.exit()

def apv():
    global key,main_url
    uninstall_able()
    if "pure_user" == url_sefty():
        pass
    elif "bypass_user" == url_sefty():
        rp(" Trun off your bypass system")
        sys.exit()
    
    if "pure_user" == url_sefty2():
        pass
    elif "bypass_user" == url_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    
    
    if "pure_user" == key_sefty():
        pass
    elif "bypass_user" == key_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    if "pure_user" == key_sefty():
        pass
    elif "bypass_user" == key_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    
    os.system("pip uninstall httpx requests -y")
    os.system("pip install requests httpx")
    import httpx
    team_elite=httpx.Client() 
    data=req(team_elite,main_url)
    for dta in data.splitlines():
        all_datA.append(dta)
    row=[]
    for r in data.splitlines():
        rx=r.split("|")[0]
        row.append(rx)
    if key not in row:
        os.system("clear")
        rp(logo)
        rp(Panel.fit(" [green]</> KEY "+key, title="[bold yellow]NOT APPROVED", subtitle="[bold blue]GET PERMISSION"))
        #####----Message link
        os.system("xdg-open https://m.me/Heron.Afridi.0fficial")
    else:
        lisens()


apv()