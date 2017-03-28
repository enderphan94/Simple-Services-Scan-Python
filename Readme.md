# SePy - Simple services scan in Python

Coded by Ender Phan

Written in Python 

Operating System: Linux (All Linux Distribution)

# Introduction:

Scan vulnerabilities of Linux common services such as: TCP/UDP, SSH, HTTP, HTTPs, SMTP based on the banners responses from server.

# Usage:

usage: sepy.py [-h] -i IP

optional arguments:

  -h, --help      show this help message and exit
  
  -i IP, --ip IP  Your IP or IP-range (e.g: 192.168.1.1-255)

# Example:

+ For single IP:

    `$python sepy.py -i 192.168.1.1`

+ For IP-range:

    `$python sepy.py -i 192.168.1.1-255`
