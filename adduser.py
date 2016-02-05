#!/usr/bin/python
import os
# Hosts that we are going to run the script against
ServerList = ["Array of servers"]

class Strings:
  Intro1 = 'This tool is for adding user accounts for GPFS'
  Intro2 = 'Please be sure that you are not violating security policy in any way by adding this user.'
  Exists = ' already exists!'
  Added = ' has been added to '
  Error1 = 'Failed to add a user!'
  Error2 = 'Only root may add a user to the system.'
  Finish = 'Done.'
  Creation = 'The user account has been created on '
  Expire = 'User account password has been expired on '

def userCreation():
    for Server in ServerList:
        os.system("ssh root@" + (Server) + " useradd -m -p " + Username + " " + Password + " -s " + "/bin/bash")
        print Color.Green + Strings.Creation + (Server)

def userExpire():
    for Server in ServerList:
        os.system("ssh root@" + (Server) + " chage -d 0 " + Username)
        print Color.LightWhite + Strings.Expire + (Server)

class Color:
  DarkRed  = '\033[31m'
  LightRed = '\033[91m'
  LightWhite = '\033[97m'
  Green = '\033[92m'

class UserInfo:
  UserName = 'Enter username: '
  UserPass = 'Enter password: '
  UserShell = '/bin/bash'

print Color.DarkRed + Strings.Intro1
print Color.LightRed + Strings.Intro2
print Color.LightWhite

Username = raw_input(UserInfo.UserName)
Password = raw_input(UserInfo.UserPass)

if Username in open('/etc/passwd').read():
  print Username + Strings.Exists

else:
    userCreation()
    userExpire()
print Color.Green + Strings.Finish
print Color.LightWhite #