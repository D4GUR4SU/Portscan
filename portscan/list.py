#!/usr/bin/python3

RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"

def getlist():

    top10 = [21, 22, 23, 25, 80, 110, 139, 443, 445, 3389]
    top20 = [135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    top30 = [3389, 5060, 5666, 5900, 6001, 8000, 8008,
             8080, 8443, 8888, 10000, 32768, 49152, 49154]

    all = (top10+top20+top30)
    all_ports = range(1, 65535)

    print(CYAN+"\n ┏━┓┏━┓╺┳╸╻┏━┓┏┓╻┏━┓")
    print(CYAN+" ┃ ┃┣━┛ ┃ ┃┃ ┃┃┗┫┗━┓")
    print(CYAN+" ┗━┛╹   ╹ ╹┗━┛╹ ╹┗━┛\n")

    print(CYAN+" [1] - TOP 10")
    print(CYAN+" [2] - TOP 20")
    print(CYAN+" [3] - TOP 30")
    print(CYAN+" [4] - ALL LISTS")
    print(CYAN+" [5] - ALL PORTS (1-65535)")
    print("\n")


    try:
        resp = int(input(RED+"Choose your list: "))
        list = []

        if(resp == 1):
            list = top10
            return list
        elif(resp == 2):
            list = top20
            return list
        elif(resp == 3):
            list = top30
            return list
        elif(resp == 4):
            list = all
            return list
        elif(resp == 5):
            list = all_ports
            return list
        else:
            print(RED+"Pick a list - Ending portscan...")
    except:
        print(RED+"[-] ERROR: Value not supported")
