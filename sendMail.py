#!/usr/bin/python3.6

###########################################################################
#               Script created by Cedric Brisebois                        #
###########################################################################

# Usage: 
# Please have a file named sendMail.conf in the same directory as sendMail.py in the following format:

# [DEFAULT]
# server : smtp.gmail.com
# port : 465
# sendtodef : exampleTo@gmail.com
# sendFrom : exampleFrom@gmail.com

##################################   Shell   ###########################################
#This script can be used as an executable.
#In linux, make sure your python executable path is correct after the #! on the first line
#Make sure you set the script as an executable (chmod +x senMail.py)
#Type ./sendMail.py -h for usage
############################################################################################

##################################   API   ###########################################
#This script can be used as an API in an other python script
#You still need the config file in order for the script to know which server & port to use
#Import using: from sendMail import Sender
#Call the constructor by adding sender = Sender()
#Send emails by adding: sender.send(emailFrom,emailTo,Subject,Body)
############################################################################################

import smtplib
import configparser
from email.mime.text import MIMEText
import argparse
import pathlib

class Sender:

    def __init__(self):

        #Most config file parsing stuff happens here
        self.conf=configparser.ConfigParser()
        self.conf.read(__file__.rstrip('sendMail.py')+'sendMail.conf')
        self.default=self.conf.defaults() #Store all attributes under DEFAULT
        self.parser = argparse.ArgumentParser(description='Send emails')
        self.parser.add_argument('--sendTo', '-t', help='Specifies to which addresses the email will be sent excluding the recipients specified in sendMail.conf. Leave blank if you want to send to the default list in the config file', metavar='EMAILADDRESS1;EMAILADDRESS2;EMAILADDRESS3;...')
        self.parser.add_argument('--subject', '-u', help='Specifies the subject of the email', metavar='SUBJECT')
        self.parser.add_argument('--message', '-m', help='Specifies the message body', metavar='MESSAGE')
        self.parser.add_argument('--file', '-o', help='Specifies the file to send as message body', metavar='FILE')

        self.args=self.parser.parse_args()

    #Function called for use in commandLine
    def build(self):
        mailto = self.default['sendtodef']
        subject='Sent by sendMail Script'
        body=''
        if self.args.sendTo != None:
            mailto = self.args.sendTo
        if self.args.subject!=None:
            subject=self.args.subject
        if self.args.message!=None:
            body=self.args.message
        elif self.args.file!=None:
            body=""
            with open(self.args.file, 'r') as file:
                lines=file.readlines()
                for line in lines:
                    body+=line
        mailto=mailto.split(';')
        for address in mailto:
            self.send(self.default['sendfrom'], address, subject, body)

    #Function to send strings
    def send(self, mailfrom, mailto, subject, string):
        try:
            msg=MIMEText(string)

            msg['Subject'] = subject
            msg['From'] = mailfrom
            msg['To'] = mailto

            toSend=msg.as_string()
            #Needed for email services that use SSL such as Gmail
            server=smtplib.SMTP_SSL(self.default['server'], self.default['port'])
            server.login('UserName', 'Password')

            server.sendmail(mailfrom, mailto, toSend)
            return 1
        except Exception as err:
            print(err)
            return 0
if __name__=='__main__':
    sender=Sender()
    sender.build()
