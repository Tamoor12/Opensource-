import os,random,sys,time
os.system("pkg install espeak")
from os import system as _HERON_
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def logo():
	os.system("clear")
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
	print(f"""\n\033[1;90m██   ██ ███████ ██████   ██████ {color_logo} ███    ██ \n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ████   ██ \n\033[1;90m███████ █████   ██████  ██    ██{color_logo} ██ ██  ██    \033[1;97m┏━┓\n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ██  ██ ██  \033[1;92m ┫\033[1;90m│\033[1;91m\033[47m𝘽\033[00m\033[1;90m│\033[1;92m┣\n\033[1;90m██   ██ ███████ ██   ██  ██████  {color_logo}██   ████   \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙍\033[00m\033[1;90m│\033[1;92m┣\n\t\t\t\t\t      \033[1;90m│\033[1;91m\033[47m𝘼\033[00m\033[1;90m│\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙉\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘈𝘜𝘛𝘏𝘖𝘙        \033[1;35m:  \033[1;37m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝘿\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;35m:  \033[1;37mheroncyber99      \x1b[38;5;208m│   \033[1;97m┗━┛\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \033[1;35m:  \033[1;37m01722183463       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘗𝘖𝘞𝘌𝘙         \033[1;35m:  \033[1;31m𝙃𝙀𝙍𝙊𝙉 𝘼𝙁𝙍𝙄𝘿𝙄      \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n\t\t \033[1;30m [\033[1;31m\033[1;47m𝙈𝘼𝙍𝙎𝙃𝘼𝙇\033[00m\033[1;30m] """)
try:
    import marshal
    os.system('clear')
    lo("     𝙋𝙇𝙕 𝙒𝘼𝙄𝙏...")
    _HERON_("clear")
    logo()
    _HERON_("espeak \"import your script\"")
    __F = input('\n \033[1;92m╔══[🐼] \033[1;90mInput script path\033[1;91m:\033[1;97m ')
    _HERON_(f"espeak \"you choose input {__F}\"")
    O__ = input(' \033[1;92m╚══[🐼] \033[1;90mOut put path\033[1;91m:\033[1;97m ')
    _HERON_(f"espeak \"you choose out put {O__}\"")
    logo()
    ltt=int(input("\n\033[1;92m____[\033[1;90m𝙘𝙝𝙤𝙤𝙨𝙚\033[1;91m: \033[1;93m4, \033[1;94m5, \033[1;95m6, \033[1;96m7, \033[1;97m9, \033[1;90m10, \033[1;91m11\033[1;93m ,12\033[1;92m]____\n\n\t 𝘾𝙃𝙊𝙊𝙎𝙀:/>\033[1;97m"))
    _HERON_(f"espeak \"you choose {ltt}\"")
    try:
        __R = open(__F,'r').read()
    except:
        exit('\n script not found ')
        
    os.system(f'cp {__F} {O__}')
    for _ in range(ltt):
        cc = open(O__,'r').read()
        data = marshal.dumps(cc)
        _nop_ = open(O__,'w')
        _nop_.write('#_____________________________________\n#|>| THIS TOOL IS ENC BY HERON-AFRIDI\n#|>|FB_LINK:-https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN\n#|>|WHATS_APP:-+8801722183463\n#_____________________________________\n')
        _nop_.write('import marshal\n')
        _nop_.write(f'exec(marshal.loads({repr(data)}))')
        _nop_.close()
    os.system("xdg-open https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN")
    print(f'\n [•] file saved in: {O__}')
    exit()
except Exception as e:
    exit(e)