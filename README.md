# PythonMail

Python script for sending emails with string or file using an smtp server of your choice
## Usage 

A Config file named config.conf must be present with the following format:
```
[DEFAULT]
server : smtp.gmail.com
port : 465
sendtodef : exampleTo@gmail.com
sendFrom : exampleFrom@gmail.com
```

### Shell
This script can be used as an executable.
 In linux, make sure your python executable path is correct after the #! on the first line.
 Make sure you set the script as an executable (chmod +x senMail.py).
#### Shell Usage
```
./SendMail.py -t Recipient -f Sender -u Subject -m "Message" OR -o File
```
### API

This script can be used as an API in an other python script.
You still need the config file in order for the script to know which server & port to use

Import: 
```
from sendMail import Sender
```
Call the constructor:
```
sender = Sender()
```
Send emails: 
```
sender.send(emailFrom,emailTo,Subject,Body)
```

