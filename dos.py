#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import os
import sys
import time
import webbrowser

class colors:
    WHITE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[93m'
    YELLOW = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = "http://www.insa.gov.et/"

os.system("clear");
print"  ___  _                   _       _       "
print" / _ \| |                 (_)     (_)      "
print"/ /_\ \ |__  _   _ ___ ___ _ _ __  _  __ _ "
print"|  _  | '_ \| | | / __/ __| | '_ \| |/ _` |"
print"| | | | |_) | |_| \__ \__ \ | | | | | (_| |"
print"\_| |_/_.__/ \__, |___/___/_|_| |_|_|\__,_|"
print"              __/ |                        "
print"             |___/                         \n"

print colors.GREEN + " Abyssinia Multi Exploitation Framework" + colors.ENDC 
print colors.YELLOW + "        Ethiopian Cyber sword" + colors.ENDC
print colors.RED + "         Mati Ethiopia 2010" + colors.ENDC
print colors.GREEN + "       Kali Linux Edition"+ colors.ENDC

domain = raw_input('Enter the URL ')
Port = raw_input('Enter the Port Number ')
print ""
print ""
os.system("chmod +x dos")
os.system("./dos\t"+domain+"\t"+Port)
#webbrowser.open_new(url)
