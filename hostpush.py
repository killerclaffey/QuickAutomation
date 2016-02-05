#!/usr/bin/python
import os
import datetime
# Hosts that we are going to run the script against
ServerList = ["eccgems1","eccgio1","eccgio2","fmcgio1","fmcgio2","eccgproto1","fmcgproto1","fmcgems1"]
def Backup(Filename):
    for Server in ServerList:
        FilePath = Filename # replace the temp with your file path/name
        modifiedTime = os.path.getmtime(FilePath)
        timeStamp =  datetime.datetime.fromtimestamp(modifiedTime).strftime("%b-%d-%y-%H:%M:%S")
        os.system("ssh root@" + (Server) + " cp " + Filename + " " + FilePath + "_" + timeStamp)
        print "Backed up " + Filename + " on " + (Server) + " to " + FilePath + "_" + timeStamp
def Transfer(Filename):
    for Server in ServerList:
        os.system("scp " + Filename + " root@" + (Server) + ":" + Filename)
        print "transferred " + Filename + " over to" + " " + (Server)

Backup("/etc/hosts")
Transfer("/etc/hosts")
