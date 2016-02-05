#!/usr/bin/python
import os
import datetime
# Hosts that we are going to run the script against
ServerList = ["Servers"]

def deleteUser(userName):
    for Server in ServerList:
        os.system("ssh root@" + (Server) + " userdel -r " + userName)
        print "Deleted User from " + (Server)

class UserInfo:
  userDel = 'Enter username to delete: '

userName = raw_input(UserInfo.userDel)

deleteUser(userName)

