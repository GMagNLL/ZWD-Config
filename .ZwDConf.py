#!usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
__version__ = '1.1'
__copyright__ = 'Copyright (c) 2017 @nZwdeff\n'# All Rights Reserved.

"""
 Github https://github.com/Xdwnff-04x/ZwD-Config
 Copyright 2017 ZwDConfig of copyright .Zwdeff

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

import sys
import time
import os, re
from os import system
from sys import *
from time import *

if sys.version_info.major < 3:
   print (f1+'Erro: Progama suportado somente em Python3\033[m')
   sleep(2)
   exit()
try:
   import simplejson
except ImportError:
   print ('\033[31mDependencias nao instaladas.\033[m')
   sleep(1)
   print ('\033[92mInstalando Dependencias .. aguarde\033[30m')
   if os.path.isfile('/usr/local/bin/pip') == False:
      system('nohup wget -qc https://raw.githubusercontent.com/pypa/get-pip/master/get-pip.py')
      system('python3 get-pip.py')
      if os.path.isfile('/root/nohup.out') == True:
         system('rm -rf /root/nohup.out')
      system('rm -rf get-pip.py')
      system('clear')
   system('pip3 install simplejson')
   sleep(2)
   print ('\033[36mConcluido .. Dependencias instaladas.\033[m')
   import simplejson
   sleep(3)
   system('clear')
import fileinput
from urllib.request import *

f0 = '\033[90m'
f1 = '\033[91m'
f2 = '\033[92m'
f3 = '\033[93m'
f4 = '\033[94m'
f5 = '\033[95m'
f6 = '\033[36m'
f7 = '\033[97m'
f8 = '\033[96m'
  
v = sys.version_info.major
H = strftime('%d/%m/%Y %H:%M:%S')
print ('\033[92m\033[92mConectando .. via python%s /%s\033[m' % (v,H))
sleep(0.9)
url = str(urlopen('http://check-host.net/ip').read())
__ip__ = re.compile(r'(\d+\.\d+\.\d+\.\d+)').search(url).group()
  
__main__ = '\n\033[32mI) =\033[92m Informacoes do IP\n\033[m'\
          +'\033[92mM) =\033[32m Monitor do Sistema\n\033[m'\
          +'\033[32m1) =\033[92m Configurar VPS\n\033[m'\
          +'\033[92m2) =\033[32m Desconfigurar\033[92m /SSH/SQUID3\n\033[m'\
          +'\033[32m3) =\033[92m Adicionar Domain\n\033[m'\
          +'\033[92m4) =\033[32m Remover Domain\n\033[m'\
          +'\033[32m5) =\033[32m Adicionar Banner\n\033[m'\
          +'\033[92m6) =\033[92m Remover Banner\n\033[m'\
          +'\033[32m7) =\033[32m Adicionar usuario\n\033[m'\
          +'\033[92m8) =\033[92m Redefinir usuario\n\033[m'\
          +'\033[32m9) =\033[32m Remover usuario\n\033[m'\
          +'\033[92m0) =\033[92m Sair\n\n\n\033[m'
# I = True.
# M = True.
# 1 = True.
# 2 = True.
# 3 = True.
# 4 = True.
# 5 = True.
# 6 = True.
# 7 = True.
# 8 = True.
# 9 = True.
# 0 = True.
__info__ = '\033[32mAuthor:\033[92m %s\n\033[m' %(__author__)\
          +'\033[32mVersion:\033[92m %s\033[m\n\n' %(__version__)
__Banner__ = '\033[32m{= ZwDConfig /SSH/SQUID3 =}_\n\033[m'
print (__Banner__)
print (__info__)
print ('\033[32mIP:\033[92m %s\033[m' %(__ip__))

def case():
  try:
     print (__main__)
     w = input(f6+' :: _\033[92m'+' ')
     
     while w != '1' or w != '2' or w != '3' or w != '4' or w != '5' or w != '6'\
      or w != '7' or w != '8' or w != '9' or w != '0' or w != 'm' or w != 'M'\
       or w != 'monitor' or w != 'Monitor' or w != 'MONITOR' or w != 'i' or w != 'I':
        if w == '1' or w == '2' or w == '3' or w == '4' or w == '5' or w == '6' or w == '7'\
         or w == '8' or w == '9' or w == '0' or w == 'm' or w == 'M' or w == 'monitor'\
          or w == 'Monitor' or w == 'MONITOR' or w == 'i' or w == 'I':
           if w == 'i' or w == 'I':
              url = 'http://ip-api.com/json/%s' % (__ip__)
              req = urlopen(url).read()
              json_data = simplejson.loads(req)
              if ':' not in json_data:
                  if json_data['zip'] == '':
                     json_data['zip'] = 'Null'
              __ADD__ = '\033[92m\nIPAddress\033[92m: ' + str(json_data['query'])\
                       +'\033[32m\nPais\033[92m: ' + str(json_data['country'])\
                       +'\033[92m\nPais Code\033[32m: ' + str(json_data['countryCode'])\
                       +'\033[32m\nHospedado por\033[92m: ' + str(json_data['as'])\
                       +'\033[92m\nProvedor\033[32m: ' + str(json_data['isp'])\
                       +'\033[32m\nCidade\033[92m: ' + str(json_data['city'])\
                       +'\033[92m\nRegiao:\033[32m ' + str(json_data['regionName'])\
                       +'\033[32m\nRegiao Code\033[92m: ' + str(json_data['region'])\
                       +'\033[92m\nFuso horario\033[32m: ' + str(json_data['timezone'])\
                       +'\033[32m\nZip\033[92m: ' + str(json_data['zip'])\
                       +'\033[92m\nStatus\033[32m: ' + str(json_data['status'])\
                       +'\033[32m\nLat/Long\033[32m: ' + str(json_data['lat'])\
                       +', '+str(json_data['lon'])
                       
              print (__ADD__+'\n')
              w = input(f6+' :: _\033[92m'+' ')
           if w == 'm' or w == 'M' or w == 'monitor' or w == 'Monitor' or w == 'MONITOR':
              print ('\033[92mMonitor do Sistema\033[32m ..\033[m')
              system('''v=$(uname -o)\necho '\033[92mSistema Operacional\033[32m:' $v''')
              if os.path.isfile('/etc/debian_version') == True:
                 system('''deb=$(cat /etc/debian_version)\necho\
                        '\033[32mVersao Debian\033[92m:' $deb''')
              system('''arq=$(uname -m)\necho '\033[92mArquitetura\033[32m:' $arq''')
              system('''kernel=$(uname -r)\necho '\033[32mKernel\033[92m:' $kernel''')
              system('''serv=$(cat /etc/resolv.conf | sed '1 d' | awk '{print $2}')\n
                     echo '\033[92mServidor DNS\033[32m:' $serv''')
              system('''host=$(hostname)\necho '\033[32mHostName\033[92m:' $host''')
              system('''internal=$(hostname -i)\necho '\033[92mIP Interno\033[32m:'\
                $internal''')
              system('''free -h | grep -v + > /tmp/ramcache''')
              system('''echo '\033[92mRam Usages\033[32m:'  && cat /tmp/ramcache\
               | grep -v 'Swap' ''')
              system('''echo '\033[92mSwap Usages\033[32m:' && cat /tmp/ramcache\
               | grep -v 'Mem' ''')
              print ('\033[92mUsuarios Conectados:\033[m')
              if os.path.isfile('/root/usuarios.db') == False:
                 system('touch /root/usuarios.db')
              system('''database='/root/usuarios.db'
              while read us
              do
                usr="$(echo $us | cut -d' ' -f1)"
                ss1="$(echo $us | cut -d' ' -f2)"
                ps x | grep [[:space:]]$usr[[:space:]] | grep -v grep | \
                grep -v pts > /tmp/tmp4
                ss2="$(cat /tmp/tmp4 | wc -l)"
                printf ' %-35s%s\n' $usr $ss2/$ss1; tput sgr0
              done < $database
              rm -rf /tmp/tmp4''')
              system('''load=$(top -n 1 -b | grep 'load average:'\
               | awk '{print $11 $12 $13 $14}')\n
                     echo '\033[92mCarga Media\033[92m:' $load''')
              system('''time=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)\n
                     echo '\033[32mTempo de Atividade\033[92m:' $time''')
              w = input(f6+' :: _\033[92m'+' ')
           if w == '1':
              t = os.path.isfile('/usr/bin/ssh')
              s = os.path.isfile('/usr/sbin/squid3')
              d = os.path.isfile('/usr/sbin/squid')
              if os.path.isfile('/root/usuarios.db') == False:
                 system('touch /root/usuarios.db')
              if os.path.isfile('/etc/setup/senhas/except') == False:
                 system('mkdir /etc/setup')
                 system('mkdir /etc/setup/limits')
                 system('cp /etc/security/limits.conf /etc/setup/limits')
                 system('mkdir /etc/setup/senhas')
                 system('touch /etc/setup/senhas/except')
                 system('''echo 'Ola anqui fica armazenado todas as senhas'''\
                       +'''criadas por este progama.' > /etc/setup/senhas/except''')
              if os.path.isfile('/etc/setup/limite/lm') == False:
                 system('mkdir /etc/setup/limite')
                 system('touch /etc/setup/limite/lm')
              if t == True:
                 system('apt-get autoremove ssh -y')
                 system('apt-get update && apt-get install ssh -y')
              if d == True:
                 system('apt-get autoremove squid -y')
              if s == True:
                 system('apt-get autoremove squid3 -y')

              system('apt-get install squid3 -y')
              sleep(2)
  
              if os.path.isfile('/etc/squid/squid.conf') == False\
               and os.path.isfile('/etc/squid3/squid.conf') == True:
                 system('touch /etc/squid3/squid.conf')
              if os.path.isfile('/etc/squid3/squid.conf') == False\
               and os.path.isfile('/etc/squid/squid.conf') == True:
                 system('touch /etc/squid/squid.conf')
              if os.path.isfile('/etc/squid/squid.conf') == True:
                 system('rm -rf /etc/squid/squid.conf')
                 system('touch /etc/squid/squid.conf')
                 print (f2+'Configurando Portas SQUID IP:\033[36m %s\033[m' %(__ip__))
                 sleep(2)
                 system('mkdir /etc/squid/domains')
                 if os.path.isfile('/etc/squid/domains/domain') == False:
                    system('touch /etc/squid/domains/domain')
                    system('''echo '.vivo.com.br\n.claro.com.br\n.oi.com.br\
                           \n.tim.com.br' >> /etc/squid/domains/domain''')
                    system('touch /etc/squid/domains/.claro.com.br')
                    system('touch /etc/squid/domains/.vivo.com.br')
                    system('touch /etc/squid/domains/.tim.com.br')
                    system('touch /etc/squid/domains/.oi.com.br')
                    system('rm -rf /etc/squid/squid.conf')
                    system('touch /etc/squid/squid.conf')
                    
                    system('''echo '# ACL DE CONEXAO\n' >> /etc/squid/squid.conf''')
                    system('''echo 'acl accept src %s' >> /etc/squid/squid.conf''' %(__ip__))
                    system('''echo 'acl ip url_regex -i %s' >> /etc/squid/squid.conf'''\
                    %(__ip__))
                    system('''echo 'acl payload dstdomain -i "/etc/squid/domains/domain"\n'\
                            >> /etc/squid/squid.conf''')
                    system('''echo '\n# PORTAS DE ACESSO\n' >> /etc/squid/squid.conf''')
                    system('''echo 'http_port 80' >> /etc/squid/squid.conf''')
                    system('''echo 'http_port 8080' >> /etc/squid/squid.conf''')
                    system('''echo 'http_port 8799' >> /etc/squid/squid.conf''')
                    system('''echo 'http_port 3128' >> /etc/squid/squid.conf''')
                    system('''echo '\n# Nome do servidor\n' >> /etc/squid/squid.conf''')
                    system('''echo 'visible_hostname ZWDConfig' >> /etc/squid/squid.conf''')
                    system('''echo '\n# ACCEPT ACL\n' >> /etc/squid/squid.conf''')
                    system('''echo 'http_access allow accept' >> /etc/squid/squid.conf''')
                    system('''echo 'http_access allow ip' >> /etc/squid/squid.conf''')
                    system('''echo 'http_access allow payload' >> /etc/squid/squid.conf''')
                    system('''echo 'http_access deny all' >> /etc/squid/squid.conf''')
                               
                    print ('\033[32mPortas SQUID: 80, 8080, 8799, 3128 Ativadas.\n\033[m')
                    sleep(2)
              else:
                 system('rm -rf /etc/squid3/squid.conf')
                 system('touch /etc/squid3/squid.conf')
                 print ('\033[32mConfigurando Portas SQUID3 IP:\033[36m %s\033[m' %(__ip__))
                 sleep(2)
                 system('mkdir /etc/squid3/domains')
                 if os.path.isfile('/etc/squid3/domains/domain') == False:
                    system('touch /etc/squid3/domains/domain')
                    system('''echo '.vivo.com.br\n.claro.com.br\n.oi.com.br\
                           \n.tim.com.br' >> /etc/squid3/domains/domain''')
                    system('touch /etc/squid3/domains/.claro.com.br')
                    system('touch /etc/squid3/domains/.vivo.com.br')
                    system('touch /etc/squid3/domains/.tim.com.br')
                    system('touch /etc/squid3/domains/.oi.com.br')
                    system('rm -rf /etc/squid3/squid.conf')
                    system('touch /etc/squid3/squid.conf')
                    system('''echo '# ACL DE CONEXAO\n' >> /etc/squid3/squid.conf''')
                    system('''echo 'acl accept src %s' >> /etc/squid3/squid.conf''' %(__ip__))
                    system('''echo 'acl ip url_regex -i %s' >> /etc/squid3/squid.conf'''\
                    %(__ip__))
                    system('''echo 'acl payload dstdomain -i "/etc/squid3/domains/domain"\n'\
                            >> /etc/squid3/squid.conf''')
                    system('''echo '\n# PORTAS DE ACESSO\n' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_port 80' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_port 8080' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_port 8799' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_port 3128' >> /etc/squid3/squid.conf''')
                    system('''echo '\n# Nome do servidor\n' >> /etc/squid3/squid.conf''')
                    system('''echo 'visible_hostname ZWDConfig' >> /etc/squid3/squid.conf''')
                    system('''echo '\n# ACCEPT ACL\n' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_access allow accept' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_access allow ip' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_access allow payload' >> /etc/squid3/squid.conf''')
                    system('''echo 'http_access deny all' >> /etc/squid3/squid.conf''')
                    
                    print ('\033[32mPortas SQUID3: 80, 8080, 8799, 3128 Ativadas.\n\033[m')
                    sleep(2)
              print ('\033[32mConfigurando Portas SSH.\033[m')
              sleep(2)
              for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config', inplace=1)):
                  sys.stdout.write(line.replace('Port 22', 'Port 22\nPort 443'))
              print ('\033[32mReiniciando Servidor SSH.\033[m')
              system('cd /etc && service ssh restart')
              sleep(2)
              if os.path.isfile('/etc/squid/squid.conf') == True:
                 sleep(2)
                 print ('\033[32mReiniciando Servidor SQUID.\033[m')
                 system('cd /etc && service squid restart')
                 sleep(2)
                 print ('\033[32mPortas SSH[22/443]SQUID Rodando 100%n\n\033[m')
              else:
                 print ('\033[32mReiniciando Servidor SQUID3.\033[m')
                 system('cd /etc && service squid3 restart')
                 sleep(2)
                 print ('\033[32mPortas SSH[22/443]SQUID3 Rodando 100%\n\033[m')
              sleep(3)
              print (f2+'Concluido. Portas 22/443/80/8080/8799/3128 100% ativas ..\033[m')
              print (f2+'Crie um usuario e teste.\033[m')
              sleep(2)
              case()
              
           if w == '2':
              rc = input(f6+'\nDeseja Remover todas as Alteracoes. [y/n] :: _\033[92m'+' ')
              if rc == 'y' or rc == 'Y':
                 t = os.path.isfile('/usr/bin/ssh')
                 s = os.path.isfile('/usr/sbin/squid3')
                 d = os.path.isfile('/usr/sbin/squid')
                 if os.path.isfile('/etc/squid/domains/domain') == True:
                    system('rm -rf /etc/squid/domains')
                 else:
                    system('rm -rf /etc/squid3/domains')
                 if os.path.isfile('/root/usuarios.db') == True:
                     system('rm -rf /root/usuarios.db')
                 if os.path.isfile('/etc/Banner') == True:
                    system('rm -rf /etc/Banner')
                    if os.path.isfile('/etc/issue.net') == False:
                       system('touch /etc/issue.net')
                       for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config',\
                       inplace=1)):
                           sys.stdout.write(line.replace('Banner /etc/Banner',\
                           '#Banner /etc/issue.net'))
                 if os.path.isfile('/etc/setup/senhas/except') == True:
                    for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config',\
                     inplace=1)):
                        sys.stdout.write(line.replace('Port 443\n', ''))
                    system('rm -rf  /etc/security/limits.conf')
                    system('cp /etc/setup/limits/limits.conf /etc/security')
                    system('rm -rf /etc/setup')
                 if d == True:
                    system('apt-get autoremove squid -y')
                 if s == True:
                    system('apt-get autoremove squid3 -y')
                 if os.path.isfile('/etc/squid/squid.conf') == True:
                    system('rm -rf /etc/squid/squid.conf')
                    system('touch /etc/squid/squid.conf')
                 if os.path.isfile('/etc/squid3/squid.conf') == True:
                    system('rm -rf /etc/squid3/squid.conf')
                    system('touch /etc/squid3/squid.conf')
                 system('cd /etc && service ssh restart')
                 print (f2+'\nConcluido.. Pode reconfigurar sua vps com um script da\n'\
                       +'sua Preferencia. Desculpe desapontalo(a).\033[m')
                 sleep(2)
                 case()
              if rc == 'n' or rc == 'N':
                case()
              if rc == '0':
                 print (f1+'\n Going out ..\033[m')
                 sleep(2)
                 exit()
                 
           if w == '3':
              if os.path.isfile('/etc/squid3/domains/domain') == False\
               or os.path.isfile('/etc/squid/domains/domain') == False:
                 if os.path.isfile('/etc/squid/squid.conf') == True:
                    system('touch /etc/squid/domains/domain')
                 else:
                    system('touch /etc/squid3/domains/domain')
              print (f2+'Domains do arquivo:\033[36m')
              if os.path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
              def dom():
                  do = input(f6+'\nAdicionar Domain :: _\033[92m'+' ')
                  if do == '0':
                     case()
                  if os.path.isfile('/etc/squid3/domains/domain') == True:
                     if os.path.isfile('/etc/squid3/domains/%s' %(do)) == True:
                        print (f1+'Erro: o domain %s ja existe.\033[m' %(do))
                        dom()
                     system('''echo '%s' >> /etc/squid3/domains/domain''' % (do))
                     system('''touch /etc/squid3/domains/%s''' % (do))
                     print ('\033[m')
                     system('cd /etc && service squid3 restart')
                     print ('\033[92mDomain: %s Adicionado [0] Para Home.' % (do))
                     dom()
                  else:
                     if os.path.isfile('/etc/squid/domains/%s' %(do)) == True:
                        print (f1+'Erro: o domain %s ja existe.\033[m' %(do))
                        dom()
                     system('''echo '%s' >> /etc/squid/domains/domain''' % (do))
                     system('''touch /etc/squid/domains/%s''' % (do))
                     print ('\033[m')
                     system('cd /etc && service squid restart')
                     print ('\033[92mDomain: %s Adicionado.. [0] Para Home.' % (do))
                     dom()
              dom()
              
           if w == '4':
              if os.path.isfile('/etc/squid/domains/domain') == False\
               or os.path.isfile('/etc/squid3/domains/domain') == False:
                 if os.path.isfile('/etc/squid3/squid.conf') == True:
                    system('touch /etc/squid3/domains/domain')
                 else:
                    system('touch /etc/squid/domains/domain')
              print (f2+'Domains do arquivo:\033[36m')
              if os.path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
              def delet():
                  de = input(f6+'\nDeletar Domain :: _\033[92m'+' ')
                  if de == '0':
                     case()
                  if os.path.isfile('/etc/squid/domains/domain') == True:
                     if os.path.isfile('/etc/squid/domains/%s' %(de)) == False:
                        print (f1+'Erro: o domain %s nao existe.\033[m' %(de))
                        delet()
                     system('rm -rf /etc/squid/domains/%s' %(de))
                     for i, line in enumerate(fileinput.input('/etc/squid/domains/domain',\
                      inplace=1)):
                         sys.stdout.write(line.replace(de+'\n', ''))
                     sleep(2)
                     print ('\033[m')
                     system('cd /etc && service squid restart')
                     print ('\033[92m\nDomain: %s Excluido. [0] Para Home.\033[m' % (de))
                     delet()
                  else:
                     if os.path.isfile('/etc/squid3/domains/%s' %(de)) == False:
                        print (f1+'Erro: o domain %s nao existe.\033[m' %(de))
                        delet()
                     system('rm -rf /etc/squid3/domains/%s' %(de))
                     for i, line in enumerate(fileinput.input('/etc/squid3/domains/domain',\
                      inplace=1)):
                         sys.stdout.write(line.replace(de+'\n', ''))
                     sleep(2)
                     print ('\033[m')
                     system('cd /etc && service squid3 restart')
                     print ('\033[92m\nDomain: %s Excluido.. [0] Para Home.\033[m' % (de))
                     delet()
              delet()
                     
           if w == '5':
              if os.path.isfile('/etc/Banner') == False:
                 system('touch /etc/Banner')
              if os.path.isfile('/etc/issue.net') == True:
                 system('rm -rf /etc/issue.net')
                 for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config', inplace=1)):
                     sys.stdout.write(line.replace('#Banner /etc/issue.net',\
                      'Banner /etc/Banner'))
              nb = input(f6+'\nAdicionar ao Banner :: _ \033[92m'+' ')
              system('''echo '%s' > /etc/Banner''' % (nb))
              system('cd /etc && service ssh restart')
              print ('\033[32mBanner:\033[96m %s \033[92m\nAdicionado com Sucesso.\033[m'\
               % (nb))
              sleep(2)
              case()
              
           if w == '6':
              rb = input(f6+'\nDeseja deletar o Banner por completo ficarar\ncomo de'\
                        +' fabrica. [y/n] :: _\033[92m'+' ')
              if rb == 'Y' or rb == 'y':
                 if os.path.isfile('/etc/Banner') == True:
                    system('rm -rf /etc/Banner')
                 if os.path.isfile('/etc/issue.net') == False:
                    system('touch /etc/issue.net')
                    for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config',\
                     inplace=1)):
                        sys.stdout.write(line.replace('Banner /etc/Banner',\
                         '#Banner /etc/issue.net'))
                    system('cd /etc && service ssh restart')
                    print (f2+'Concluido .. Banner Retirado.\033[m')
                    sleep(2)
                    case()
              if rb == 'n' or rb == 'N':
                 case()
                 
           if w == '7':
              if os.path.isfile('/etc/setup/senhas/except') == False:
                 system('touch /etc/setup/senhas/except')
              if os.path.isfile('/etc/setup/limite/mite/lm') == False:
                 system('mkdir /etc/setup/limite/mite')
                 system('touch /etc/setup/limite/mite/lm')
              def user():
                  n = input(f6+'\nNome do usuario :: _\033[92m'+' ')
                  if os.path.isfile('/root/usuarios.db') == False:
                     system('touch /root/usuarios.db')
                  if os.path.isfile('/etc/setup/senhas/%s' %(n)) == True:
                     print (f1+'Erro: o usuario %s ja existe.\033[m' %(n))
                     user()
                  sn = input(f6+'Senha Para '+n+' :: _\033[92m'+' ')
                  dx = input(f6+'Quantos dias '+n\
                             +' deve durar :: _\033[92m'+' ')
                  lm = input(f6+'Maximo de conexoes simultaneas :: _\033[92m'+' ')
                  system("d=$(date '+%C%y-%m-%d' -d '+"+dx+" days')\
                         \nda=$(date '+%d/%m/%Y' -d '+"+dx+" days')\
                         \nuseradd -M -s /bin/false "+n+" -e $d\
                         \necho '\033[92m\nConcluido .. usuario criado.'\n\
                         \necho '\033[32mUsuario:\033[92m "+n+"'\
                         \necho '\033[32mSenha:\033[92m "+sn+"'\
                         \necho '\033[32mExpira:\033[92m '$da'\033[m'\
                         \necho '"+sn+"' > /etc/setup/senhas/"+n)
                  system('(echo "'+sn+'" ; echo "'+sn\
                        +'" ) |passwd '+n+' > /dev/null 2>/dev/null')
                  system('''echo '%s %s' >> /root/usuarios.db''' %(n,lm))
                  system('''echo '%s - maxlogins %s' >> /etc/setup/limite/%s''' %(n,lm,n))
                  system('''echo '%s - maxlogins %s' >> /etc/security/limits.conf'''\
                   %(n,lm))
                   
                  case()
              user()
              
           if w == '9':
              def dex():
                  df = input(f6+'\nQue usuario voce deseja deletar :: _\033[92m'+' ')
                  if df == '0':
                     case()
                  if os.path.isfile('/etc/setup/senhas/'+df) == False\
                   or os.path.isfile('/etc/setup/limite/mite/'+df) == False:
                     print (f1+'Erro: o usuario %s nao existe.. ou nao '%(df)\
                          +'foi criado por este progama.\033[m')
                     dex()
                  system('userdel --force %s > /dev/null 2>/dev/null' %(df))
                  system('rm -rf /etc/setup/senhas/%s' %(df))
                  system('grep -v ^'+df+'[[:space:]] /etc/security/limits.conf\
                   > /tmp/mite; cat /tmp/mite > /etc/security/limits.conf')
                  system('grep -v ^'+df+'[[:space:]] /root/usuarios.db\
                   > /tmp/usdb; cat /tmp/usdb > root/usuarios.db')
                  system('rm -rf /etc/setup/limite/'+df)
                  print (f2+'Usuario %s excluido com exito.. [0] Para Home.\033[m' %(df))
                  sleep(2)
                  dex()
              dex()
              
           if w == '8':
              def rdf():
                   main = '\n\033[36m1\033[92m) = Alterar senha\033[m'\
                         +'\n\033[36m2\033[92m) = Mudar data de expiracao\033[m'\
                         +'\n\033[36m3\033[92m) = Mudar limite de logins\033[m'\
                         +'\n\033[36m0\033[92m) = Home\n\n\033[m'
                   # 1 = True.
                   # 2 = True.
                   # 3 = True.
                   rd = input(f6+'\nQue usuario voce deseja redefinir :: _\033[92m'+' ')
                   if rd == '0':
                      case()
                   if os.path.isfile('/etc/setup/senhas/%s' %(rd)) == False:
                      print (f1+'\nErro: o usuario %s nao existe ..\033[m' %(rd))
                      rdf()
                   print (main)
                   md = input(f6+' :: _\033[92m'+' ')
                   if md == '0':
                      case()
                   if md == '1':
                      sna = input(f6+'\nNova senha para '+rd+' :: _\033[92m'+' ')
                      system('(echo "'+sna+'" ; echo "'+sna\
                            +'" ) |passwd '+rd+' > /dev/null 2>/dev/null')
                      system('rm -rf /etc/setup/senhas/'+rd)
                      system('echo "'+sna+'" > /etc/setup/senhas/'+rd)
                      print (f2+'Concluido. nova senha aplicada para %s' %(rd))
                      case()
                   if md == '2':
                      print (f1+'\nUtileze-a no formato dia/mes/ano\033[m\n')
                      dt = input(f6+'\nQual a nova data para '+rd+' :: _\033[92m'+' ')
                      system('chage -E '+dt+' '+rd+' 2> /dev/null')
                      print (f2+'Concluido. nova data %s aplicada para %s.\033[m' %(dt,rd))
                      case()
                   if md == '3':
                      mt = input(f6+'\nQual o novo limite para '+rd+' :: _\033[92m'+' ')
                      system('grep -v ^'+rd+'[[:space:]] /etc/security/limits.conf\
                       > /tmp/mite; cat /tmp/mite > /etc/security/limits.conf')
                      system('grep -v ^'+rd+'[[:space:]] /root/usuarios.db\
                       > /tmp/usdb; cat /tmp/usdb > root/usuarios.db')
                      system('''echo '%s %s' >> /root/usuarios.db''' %(rd,mt))
                      system('''echo '%s - maxlogins %s' > /etc/setup/limite/%s''' %(rd,mt,rd))
                      system('''echo '%s - maxlogins %s' >> /etc/security/limits.conf'''\
                       %(rd,mt))
                      print (f2+'Concluido. novo limete de %s conexoes aplicado para %s.\033[m'\
                      %(mt,rd))
                      case()
                      
              rdf()
           if w == '0':
              print (f1+' Going out ..\033[m')
              sleep(2)
              exit()
        else:
            w = input(f6+' :: _\033[92m'+' ')
  except KeyboardInterrupt:
     print (f1+'\n Going out ..\033[m')
     sleep(2)
     exit()
if __name__ == '__main__':
   case()