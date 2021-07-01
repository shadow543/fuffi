#!/usr/bin/python3
 


import requests,sys,time,threading
#FuFFi Esta Listo!

import socket
import os
import threading
import concurrent.futures #No se si anda 
from urllib.error import *
from urllib.request import *
import requests
from googlesearch import search
import colorama
from colorama import Fore, Style
from time import sleep, time
import time
import requests

try:
        os.system("cp fuffi.py fuffi")
        os.system("mv fuffi /usr/bin")
except:
        pass

if len(sys.argv) < 3:
    print(Fore.RED+"[!] Metodo de uso: python3 fuffi.py <link> <wordlist>")
    sys.exit(0)

 
print(Fore.RESET + Fore.LIGHTRED_EX+ Style.BRIGHT+"""

 ________ ___  ___  ________ ________ ___     
|\  _____|\  \|\  \|\  _____|\  _____|\  \    
\ \  \__/\ \  \\\  \ \  \__/\ \  \__/\ \  \   
 \ \   __\\ \  \\\  \ \   __\\ \   __\\ \  \  
  \ \  \_| \ \  \\\  \ \  \_| \ \  \_| \ \  \ 
   \ \__\   \ \_______\ \__\   \ \__\   \ \__\ 
    \|__|    \|_______|\|__|    \|__|    \|__|
                                              
                                              
                                              

  
          
""")

print(Fore.LIGHTGREEN_EX+ Style.BRIGHT+"[+] Bienvenido a FuFFi :)")
print()
print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT+"[+] Creado por Shadow")

print()
linea = "-----------------------------------------------------------------"

from pwn import *


 
def fuzz(url, wl):

        file = open('{}'.format(wl), 'r')
        print(Fore.LIGHTCYAN_EX+linea)
        count = 0
        p1 = log.progress("Estado")
        
        p1.status("Fuzzeando...")
        print(Fore.LIGHTGREEN_EX+linea)
        print()
        while True:
                
                
                count += 1
                line = file.readline().split("\n")[0]
                if not line:
                        break
                new_url = url + "/" + line
                r = requests.get(new_url)
                if r.status_code == 200:
                    
                        print(Fore.LIGHTMAGENTA_EX+linea)
                        print(Fore.GREEN+ Style.BRIGHT+ "[+] Dominio Valido ! | " +new_url)
                        print(Fore.BLUE+linea)
        file.close()


#/usr/share/wordlists/dirb/big.txt
if __name__ == '__main__':

        url = sys.argv[1]
        wl = sys.argv[2]

         

        t = threading.Thread(target=fuzz ,args=(url, wl)).start()