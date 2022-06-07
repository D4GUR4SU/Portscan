#!/usr/bin/python3

import socket
import sys
import list
import os
from datetime import datetime

if len(sys.argv) != 2:
    print("|#########################################################|")
    print("|\t____            _                                 |")
    print("|\t|  _ \ ___  _ __| |_ ___  ___ __ _ _ __           |")
    print("|\t| |_) / _ \| '__| __/ __|/ __/ _  | '_ \          |")
    print("|\t|  __/ (_) | |  | |_\__ \ (_| (_| | | | |         |")
    print("|\t|_|   \___/|_|   \__|___/\___\__,_|_| |_|         |")
    print("|\t                                                  |")
    print("|\t               v1.0.0                             |")
    print("| ->               by Dagurasu56                        <-|")
    print("| ->   Example: portscan.py 192.168.0.1 or example.com  <-|")
    print("|#########################################################|")
else:
    def portscan(ip):

        print("\t\t[+]", "PortScan ->", ip, " [+]")
        conf = bool(os.system("ping -c1 {} 2>/dev/null 1>/dev/null".format(ip)))

        if(conf == False):

            ports = list.getlist()
            print("[>] Scanned Ports:")
            print(ports, "\n")

            print("\t==========Starting Scanning=========\n")
            for target in ports:
                psocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                if(psocket.connect_ex((ip, target)) == 0):
                    print("\t[+] Open port -> ", target)
                    psocket.close()
                else:
                    psocket.close()
            print("\n\t==========Scan Finished=============")
        else:
            print("[-] Host Unavailable [-]")
    begin = datetime.now()
    try:
        portscan(sys.argv[1])
    except:
        exit()
    end = datetime.now()
    print("\nTime -> ", (end-begin))
