# PythonMail
Python script for sending emails


Usage: 
Please have a file named sendMail.conf in the same directory as sendMail.py in the following format:

[DEFAULT]
server : smtp.gmail.com
port : 465
sendtodef : exampleTo@gmail.com
sendFrom : exampleFrom@gmail.com

##################################   Shell   ###########################################
This script can be used as an executable.
In linux, make sure your python executable path is correct after the #! on the first line
Make sure you set the script as an executable (chmod +x senMail.py)
Type ./sendMail.py -h for usage
############################################################################################

##################################   API   ###########################################
This script can be used as an API in an other python script
You still need the config file in order for the script to know which server & port to use
Import using: from sendMail import Sender
Call the constructor by adding sender = Sender()
Send emails by adding: sender.send(emailFrom,emailTo,Subject,Body)
############################################################################################

