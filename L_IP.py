import requests
import json
import pprint
import os



def label():
    print(BOLD)
    os.system('pyfiglet IP Trace | lolcat')
    print('\n\n')


def IP_Trace(IP):
    print('\n\n'+CYAN)
    req=requests.get(f'https://ipapi.co/{IP}/json')
    pprint.pprint(req.json())
    
#variable
RED='\033[31m'
GRN='\033[32m'
YLW='\033[33m'
CYAN='\033[36m'
BOLD='\033[1m'

#start
#_____________________________________________________________

label()
ip=input(f'{BOLD}{RED}[{YLW}+{RED}] {GRN}Enter Track IP:{RED} ')

IP_Trace(ip)


