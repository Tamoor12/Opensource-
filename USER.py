#MAKED-BY-MAMA SAAD
#GITHUB-MAMA-143
#WORKING USER AGENT
#OPEN BY SAAD MAMA
#SCRIPT SELLER
#------------------[ Install-1 ]-------------------#
import random

#__________________LINE____________#
def linex():
    print(f'\033[1;97m×××××××××××××××××××××××××××××××××××××××')
def clear():
        os.system(f'clear')
        print(logo)
#______________COLOUR_____________#
G1 = '\x1b[38;5;46m'
A = '\x1b[1;97m' 
#__________________LOGO____________
logo=(f"""\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\033[1;33m███    ███\033[1;31m  █████\033[1;33m  ███    ███\033[1;31m  █████  
\033[1;33m████  ████\033[1;31m ██   ██\033[1;33m ████  ████\033[1;31m ██   ██ 
\033[1;33m██ ████ ██\033[1;31m ███████\033[1;33m ██ ████ ██\033[1;31m ███████ 
\033[1;33m██  ██  ██\033[1;31m ██   ██\033[1;33m ██  ██  ██\033[1;31m ██   ██ 
\033[1;33m██      ██\033[1;31m ██   ██\033[1;33m ██      ██\033[1;31m ██   ██ 
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝   \033[0;92m  
 \033[0;92m═════════════════════════════════════════════
\033[0;92m • 𝙵𝙰𝙷𝙰𝙳 𝙰𝙷𝙼𝙴𝙳 𝚂𝙰𝙰𝙳(😌)
\033[0;92m • 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝚄𝚂𝙴𝚁 𝙰𝙶𝙴𝙽𝚃(🔥)
\033[0;92m • 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 𝙲𝙾𝙳𝙴 [ 𝚃𝚁𝚈 ] 𝙵𝙸𝚁𝙴(😻)
\033[0;92m═════════════════════════════════════════════ \033[1;31m""")
#__________________MAIN____________#
print(logo)
print(f'{A}[{G1}1{A}]\x1b[38;5;208m GENERATE WORKING USER ')
sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢\x1b[1;96m ')
linex()
if sex in ['1']:

#__________USER DEF_____________#
    user_agent = ""
    os = input("What user agent do you download? Windows or Android: ")
    linex()
    
    if os.lower() == "android":
        brand = random.choice(["Apple","Samsung", "Google", "OnePlus", "Xiaomi", "Huawei"])
        model = random.choice(["iPhone","Galaxy S20", "Pixel 5", "OnePlus 9", "Mi 11", "P40 Pro"])
        version = random.choice(["Android 11", "Android 10", "Android 9", "Android 8", "Android 7"])
        mozilla =random.choice(["Mozilla/5.0", "Mozilla/4.0", "Mozilla/3.0", "Mozilla/2.0", "Mozilla/1.0"])
        user_agent = f"{mozilla} (Linux; Android {version}; {brand} {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
    elif os.lower() == "windows":
        brand = random.choice(["Apple", "Samsung", "Microsoft", "Lenovo", "HP", "Dell", "Asus"])
        model = random.choice(["iPhone", "Galaxy", "Surface", "ThinkPad", "Pavilion", "XPS", "ZenBook"])
        version = random.choice(["Windows NT 10.0", "Windows NT 6.3", "Windows NT 6.2", "Windows NT 6.1", "Windows NT 6.0", "Windows NT 5.1", "Windows NT 5.0"])
        user_agent = f"{mozilla} ({version}; {brand} {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
    file_name = input("User Agent Save storage input your file name: ")
    linex()
    num_agents = int(input("How many user agents do you want to generate? "))
    linex()
    
    with open(file_name, "w") as file:
        for _ in range(num_agents):
            file.write(user_agent + "\n")
    linex()
    print("User agents generated and saved successfully.")
    linex()

generate_user_agent()
