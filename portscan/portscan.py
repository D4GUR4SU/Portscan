#!/usr/bin/python3

import socket
import sys
import list
import os
from datetime import datetime

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
BOLD  = "\033[;1m"

if len(sys.argv) != 2:

    print("\n")
    print(GREEN+"\t██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ ███╗   ██╗ ")
    print(GREEN+"\t██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║ ")
    print(GREEN+"\t██████╔╝██║   ██║██████╔╝   ██║   ███████╗██║     ███████║██╔██╗ ██║ ")
    print(GREEN+"\t██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██║     ██╔══██║██║╚██╗██║ ")
    print(GREEN+"\t██║     ╚██████╔╝██║  ██║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║ ")
    print(GREEN+"\t╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ")
    print(GREEN+"\t                            v1.0.0                                   ")
    print(GREEN+"\t                        by Dagurasu56                                ")
    print(GREEN+"\t          Example: portscan.py 192.168.0.1 or example.com            ")
    print("\n")
    
else:
    def portscan(ip):

        print(RED+"\n[+]", "PortScan ->", ip, " [+]")
        conf = bool(os.system("ping -c1 {} 2>/dev/null 1>/dev/null".format(ip)))

        if(conf == False):

            ports = list.getlist()
            print(RED+"[>] Scanned Ports:")
            print(RED, ports, "\n")

            print(GREEN+"\t ┏━┓╺┳╸┏━┓┏━┓╺┳╸╻┏┓╻┏━╸")
            print(GREEN+"\t ┗━┓ ┃ ┣━┫┣┳┛ ┃ ┃┃┗┫┃╺┓")
            print(GREEN+"\t ┗━┛ ╹ ╹ ╹╹┗╸ ╹ ╹╹ ╹┗━┛╹╹╹\n")

            for target in ports:
                psocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                if(psocket.connect_ex((ip, target)) == 0):
                    print("\t[+] Open port -> ", target)
                    psocket.close()
                else:
                    psocket.close()
            print(GREEN+"\n\t ┏━╸╻┏┓╻╻┏━┓╻ ╻┏━╸╺┳┓")
            print(GREEN+"\t ┣╸ ┃┃┗┫┃┗━┓┣━┫┣╸  ┃┃")
            print(GREEN+"\t ╹  ╹╹ ╹╹┗━┛╹ ╹┗━╸╺┻┛")

        else:
            print(RED+"[-] Host Unavailable [-]")
    begin = datetime.now()
    try:
        portscan(sys.argv[1])
    except:
        exit()
    end = datetime.now()
    print(CYAN+"\nTime -> ", (end-begin), "\n")
