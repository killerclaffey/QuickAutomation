#!/usr/bin/python
import os
import datetime
# Hosts that we are going to run the script against
ServerList = ["fmcgems1","eccgems1","eccgio1","eccgio2","fmcgio1","fmcgio2","eccgproto1","fmcgproto1"]

def Transfer(Filename):
for Server in ServerList:
os.system("scp " + Filename + " root@" + (Server) + ":" + Filename)
print " transfered" + Filename + " over to " + (Server)

def Backup(Filename):
    for Server in ServerList:
        FilePath = Filename # replace the temp with your file path/name
        modifiedTime = os.path.getmtime(FilePath)
        timeStamp =  datetime.datetime.fromtimestamp(modifiedTime).strftime("%b-%d-%y-%H:%M:%S")
        os.system("ssh root@" + (Server) + " cp " + Filename + " " + FilePath + "_" + timeStamp)
        print "Backed up " + Filename + " on " + (Server) + " to " + FilePath + "_" + timeStamp

Backup("/etc/logrotate.d/aide")
Transfer("/etc/logrotate.d/aide")

Backup("/etc/systemd/system/aideauto.service")
Transfer("/etc/systemd/system/aideauto.service")

Backup("/etc/systemd/system/aideauto.timer")
Transfer("/etc/systemd/system/aideauto.timer")

Backup("/etc/aide.conf")
Transfer("/etc/aide.conf")
