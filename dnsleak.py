#!/usr/bin/env python3
from __future__ import print_function

print(r"""
__   _______ ____  _____ _______ 
\ \ / /  __ \___ \|  __ \__   __|
 \ V /| |__) |__) | |__) | | |   
  > < |  ___/|__ <|  _  /  | |   
 / . \| |    ___) | | \ \  | |   
/_/ \_\_|   |____/|_|  \_\ |_|   """)


from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.YELLOW + 'Discord : https://discord.gg/DBhNkfppEk')
print(Style.RESET_ALL)


#Time
print(Back.GREEN + 'Waktu Dimulakan :')
print(Style.RESET_ALL)
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time) 
#TIME


import sys, socket, getopt, os.path
from uuid import uuid4
from json import loads, dumps
try:
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib2 import urlopen, Request, HTTPError, URLError

import os

import subprocess

import json

from random import randint

from platform import system as system_name

from subprocess import call as system_call



try:

    from urllib.request import urlopen

except ImportError:

    from urllib2 import urlopen





def ping(host):

    fn = open(os.devnull, 'w')

    param = '-n' if system_name().lower() == 'windows' else '-c'

    command = ['ping', param, '1', host]

    retcode = system_call(command, stdout=fn, stderr=subprocess.STDOUT)

    fn.close()

    return retcode == 0





leak_id = randint(1000000, 9999999)

for x in range(0, 10):

    ping('.'.join([str(x), str(leak_id), "bash.ws"]))



response = urlopen("https://bash.ws/dnsleak/test/"+str(leak_id)+"?json")

data = response.read().decode("utf-8")

parsed_data = json.loads(data)


print(Style.RESET_ALL)
print(Back.RED + 'Info :')
print(Style.RESET_ALL)
for dns_server in parsed_data:

    if dns_server['type'] == "ip":

        if dns_server['country_name']:

            if dns_server['asn']:

                print(dns_server['ip']+" ["+dns_server['country_name']+", " +

                      dns_server['asn']+"]")

            else:

                print(dns_server['ip']+" ["+dns_server['country_name']+"]")

        else:

            print(dns_server['ip'])



servers = 0

for dns_server in parsed_data:

    if dns_server['type'] == "dns":

        servers = servers + 1



if servers == 0:

    print("DNS Server Tidak Ditemui")

else:
    print(Style.RESET_ALL)
    print("Anda Menggunakan "+str(servers)+" DNS Servers:")
    print(Style.RESET_ALL)
    for dns_server in parsed_data:

        if dns_server['type'] == "dns":

            if dns_server['country_name']:

                if dns_server['asn']:

                    print(dns_server['ip']+" ["+dns_server['country_name'] +

                          ", " + dns_server['asn']+"]")

                else:

                    print(dns_server['ip']+" ["+dns_server['country_name']+"]")

            else:

                print(dns_server['ip'])
    print(Style.RESET_ALL)


print(Back.BLUE + 'Note :')
print(Style.RESET_ALL)
for dns_server in parsed_data:

    if dns_server['type'] == "conclusion":

        if dns_server['ip']:

            print(dns_server['ip'])