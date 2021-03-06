#!/usr/bin/python3

from scapy.all import *

# usage: $0 <target ip> <message>

from scapy.all import *
import sys
import time

class sendMe():

    def udpSend(self, s, t, m, uP):
        for prio in range(0, 7):
            for faci in range(0, 23):
                priority = (prio << 3) | faci
                syslog = IP(src=s,dst=t)/UDP(dport=uP)/Raw(load='<' + str(priority) + '>' + time.strftime("%b %d %H:%M:%S ") + m)
                send(syslog, verbose=0)
                sys.stdout.write(".")
                sys.stdout.flush()
    
        print("")



    def tcpSend(self, s, t, m, tP):
        for prio in range(0, 7):
            for faci in range(0, 23):
                priority = (prio << 3) | faci
                syslog = IP(src=s,dst=t)/TCP(dport=tP)/Raw(load='<' + str(priority) + '>' + time.strftime("%b %d %H:%M:%S ") + m)
                send(syslog, verbose=0)
                sys.stdout.write(".")
                sys.stdout.flush()
    
        print("")


def helpMe():
    print('''

  Usage: syslogFuzz.py <SourceIP> <Target IP> <Message> <TCP or UDP> <port> <-f or --fuzz OPTIONAL>

Example: python syslogFuzz.py 192.168.1.1 192.168.52.131 "Feb 23 07:55:01 ubuntu CRON[49988]: pam_unix(cron:session): session opened for user root by (uid=0)" -u 514 -f

    ''')
    quit()

def main(sip, mt, mm, po, p):
    fuzz = sendMe()
    if p == '-t':
        fuzz.tcpSend(str(sip), str(mt), str(mm), int(po))
    elif p == '-u':
        fuzz.udpSend(str(sip), str(mt), str(mm), int(po))
    else:
        print('You need to specify tcp or udp. Using UDP')
        fuzz.udpSend(str(sip), str(mt), str(mm), int(po))
        


if __name__ == "__main__":
    print('''
    This Tool was developed to fuzz syslog traffic into Splunk instances on the network.

    Example: syslogFuzz.py <Source IP> <target ip> <message> <TCP or UDP> <port> <-f or --fuzz OPTIONAL>
        
        -t              == TCP
        -u              == UDP
        -f  or --fuzz   == Optionally Fuzz by Generating Large Messages to the Server

    Author: Austin James Scott
    Email: austin.j.scott@lmco.com

    ''')
    try:
        sourceIP = str(sys.argv[1])
    except:
        print('Error argv[1]')
        helpMe()
    try:
        target = str(sys.argv[2])
    except:
        print('Error argv[2]')
        helpMe()
    try:
        msg = str(sys.argv[3])
    except:
        print('Error argv[3]')
        helpMe()
    try:
        p = str(sys.argv[4])
    except:
        print('Error argv[4]')
        helpMe()
    try:
        portN = str(sys.argv[5])
    except:
        print('Error argv[5]')
        helpMe()
    if len(sys.argv) == 7:
        if sys.argv[6] == '--fuzz' or sys.argv[6] == '-f':
            try:
                while True:
                    msg = str(msg) + str(msg)
                    print(str(len(msg)) + " Characters being sent")
                    print(sourceIP + target + msg + portN + p)
                    main(sourceIP, target, '%s' % msg, portN, p)
            except:
                print('Fuzz fail')
                quit()
    try:
        print(target + ' ' + '"' + msg + '"' + ' ' + p + ' ' + portN)
        main(sourceIP, target, "%s" % msg, portN, p)
    except:
        "error... try again"


