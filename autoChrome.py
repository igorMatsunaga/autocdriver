#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Code by: IgorMatsunaga - NSW
#Site: https://nsworld.com.br
#Github: https://github.com.br/igorMatsunaga
#Versão 64 bits
import os

logo = '''

 █████╗ ██╗   ██╗████████╗ ██████╗  ██████╗██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗
███████║██║   ██║   ██║   ██║   ██║██║     ██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝
██╔══██║██║   ██║   ██║   ██║   ██║██║     ██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╗██████╔╝██║  ██║██║ ╚████╔╝ ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                                       
                                                                                      
                                                                                                                                                                          
-----------------------------------coded by igorMatsunaga----------------------------------------
-----------------------------------------nsworld-------------------------------------------------
'''
print('\033[34m' + logo + '\033[0m')
os.system("sudo apt-get install chromium-browser")
os.system("sudo apt-get install libxss1 libappindicator1 libindicator7")

instalar_chrome = input("Você ja possui o Google Chrome instalado no seu sistema? sim(s) não(n): ")

if(instalar_chrome == "s"):
    menu = '''
        Escolha o número da opção que deseja utilizar:
        (1)  Versão 79 do Chrome
        (2)  Versão 78 do Chrome
        (3)  Versão 77 do Chrome
        '''
    print('\033[33m' + menu)
    versao = input("Digite o número correspondente a versão correta usada no Google Chrome: ")
    if(versao == "1"):
        os.system("wget https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip")
        os.system("unzip chromedriver_linux64.zip")
        os.system("chmod +x chromedriver")
        os.system("sudo mv -f chromedriver /usr/local/share/chromedriver")
        os.system("sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver")
        os.system("sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver")
    elif(versao == "2"):
        os.system("wget https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip")
        os.system("unzip chromedriver_linux64.zip")
        os.system("chmod +x chromedriver")
        os.system("sudo mv -f chromedriver /usr/local/share/chromedriver")
        os.system("sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver")
        os.system("sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver")
    elif(versao == "3"):
        os.system("wget https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip")
        os.system("unzip chromedriver_linux64.zip")
        os.system("chmod +x chromedriver")
        os.system("sudo mv -f chromedriver /usr/local/share/chromedriver")
        os.system("sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver")
        os.system("sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver")
    else:
        exit()
if(instalar_chrome == "n"):
   print("Você deve instalar o Google Chrome antes de continuar")
   exit()
