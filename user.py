import os,random,subprocess
#-----------------------color---------------#
B="\033[1;37m" 
#----------------------logo---------------#
logo = (f"""\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0;92m
  __  __ _    _  _____ _    _          _       
 |  \/  | |  | |/ ____| |  | |   /\   | |      
 | \  / | |  | | |  __| |__| |  /  \  | |      
 | |\/| | |  | | | |_ |  __  | / /\ \ | |      
 | |  | | |__| | |__| | |  | |/ ____ \| |____  
 |_|  |_|\____/ \_____|_|  |_/_/    \_\______| 
                                                      
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍    \033[1;39m◈✙◈\033[1;33m MR TAMOOR
\033[1;39m━▷ \033[0;93m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 \033[1;39m◈✙◈ \033[1;33mTAMOOR MUGHAL 
\033[1;39m━▷ \033[0;97m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \033[1;39m◈✙◈ \033[1;33m XX
\033[1;39m━▷ \033[1;36m𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝐓𝐀𝐌𝐎𝐎𝐑 𝙊𝙒𝙉𝙀𝙍 𝙊𝙁 𝐌𝐔𝐆𝐇𝐀𝐋 𝐁𝐑𝐀𝐍𝐃
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●

--------------------------------------------------

\033[1;32m[•] YOUR MIND IS YOUR  BEST  WEAPON

--------------------------------------------------""")

fbcr1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat']
fbcr = random.choice(fbcr1)
fban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
fban = random.choice(fban1)
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
fbpn = random.choice(fbks)
sim_id=''
fbsv = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdv = model
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
fbbv = str(random.randint(10000000, 88888888))
ua = f'[FBAN/{fban};FBAV/{fbav};FBBV/{fbbv};[FBAN/{fban};FBAV/{fbav};FBPN/{fbpn};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBDV/{fbdv};FBSV/7.1.2;FBCA/{fbca};FBDM/{fbdm};FB_FW/1;] FBBK/1;]' 
print(logo)
print(ua)