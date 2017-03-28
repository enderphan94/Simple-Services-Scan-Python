import socket
from sys import argv
import os
import sys
import re
import argparse
import optparse

parser = argparse.ArgumentParser()

parser.add_argument(
        '-i',
        '--ip',
        help='Your IP range',
        required=True)

args = parser.parse_args()
ip = args.ip

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
    f = open("vulns.txt",'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is Vulnerable: " + banner.strip('\n')
            print "\n"


def scan(ip,port):
    banner = retBanner(ip,port)
    if banner:
        print '[+]' + ip + ': ' + banner
        checkVulns(banner)

def main():
    portList= [21,22,25,80,110,443]
    array = re.split('[. -]',ip)
    if len(array) == 4:
        for port in portList:
            scan(ip,port)
    else:
        for x in range(int(array[3]),int(array[4])):
            ips = ".".join(str(va) for va in array[0:3])
            ip_now = ips+"."+str(x)
            for port in portList:
                scan(ip_now,port)

if __name__ == '__main__':
    main()
