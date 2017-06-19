#!usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
__version__ = '1.2'
__copyright__ = 'Copyright (c) 2017 @nZwdeff\n'# All Rights Reserved.

# Github https://github.com/Xdwnff-04x/ZwD-Config
# Copyright (c) 2017 ZwDConfig of copyright Zwdeff

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import sys
import time
import os, re
import fileinput
from os import system
from sys import *
from time import *

if sys.version_info.major < 3:
   print ('\033[31mError: Progama suportado somente em Python3\033[m')
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
   print ('\033[m')
   system('pip3 install simplejson')
   sleep(3)
   print ('\n\033[36mConcluido .. Dependencias instaladas.\033[m')
   import simplejson
   sleep(4)
   system('clear')
   
f0 = '\033[90m'
f1 = '\033[91m'
f2 = '\033[92m'
f3 = '\033[93m'
f4 = '\033[94m'
f5 = '\033[95m'
f6 = '\033[36m'
f7 = '\033[97m'
f8 = '\033[96m'

from urllib.request import *
  
v = sys.version_info.major
H = strftime('%d/%m/%Y %H:%M:%S')
print ('\033[92m\033[92mConnecting .. from python%s /%s\033[m' % (v,H))
sleep(0.9)
try:
   __url_ = str(urlopen('http://check-host.net/ip').read())
   __ip__ = re.compile(r'(\d+\.\d+\.\d+\.\d+)').search(__url_).group()
  
   __main__ = '1) = Configurar VPS\n'\
             +'2) = Desconfigurar /SSH/SQUID3\n'\
             +'3) = Adicionar Domain\n'\
             +'4) = Remover Domain\n'\
             +'5) = Adicionar Banner\n'\
             +'6) = Remover Banner\n'\
             +'7) = Adicionar usuario\n'\
             +'8) = Redefinir usuario\n'\
             +'9) = Remover usuario\n'\
             +'10 = Monitor do Sistema\n'\
             +'11 = Informacoes do IP\n'\
             +'12 = Server Speed Test\n'\
             +'13 = Backup de um usuario\n'\
             +'14 = Backup dos usuarios\n'\
             +'15 = Mais Opcoes\n'\
             +'0) = Sair\n\n\n\033[m'

   __info__ = '\033[32mAuthor:\033[36m %s\n\033[m' %(__author__)\
             +'\033[32mVersion:\033[36m %s\033[m\n' %(__version__)
   __Banner__ = '\033[32m{= \033[92mZwDConfig /SSH/SQUID3\033[32m =}_\n\033[m'
   print (__Banner__)
   print (__info__)
   print ('\033[32mIP:\033[36m %s\033[m' %(__ip__))
   
except IOError:
   print (f1+'Erro: Por favor connecte-se a uma Rede de Dados ..\033[m')
   exit()
   
def case():
  try:
     print (f6+'\n'+__main__)
         
     w = input(f6+' :: _\033[92m'+' ')
     
     while w != '1' or w != '2' or w != '3' or w != '4' or w != '5' or w != '6' or w != '13'\
      or w != '7' or w != '8' or w != '9' or w != '0' or w != '10' or w != '11' or w != '12'\
       or w != '14' or w != '15':
        if w == '1' or w == '2' or w == '3' or w == '4' or w == '5' or w == '6' or w == '7'\
         or w == '8' or w == '9' or w == '0' or w == '10' or w == '11' or w == '00'\
          or w == '12' or w == '13' or w == '14' or w == '15':
           if w == '13':
              def bsck():
                  bus = input(f6+'De qual usuario voce quer fazer Backup :: _\033[92m'+' ')
                  if bus == '0':
                     case()
                  if os.path.isfile('/etc/setup/senhas/%s' %(bus)) == False:
                     print (f1+'Error: o usuario %s nao existe.\033[m' %(n))
                     bsck()
                  if os.path.isfile('/etc/setup/backup/0dir') == False:
                     system('mkdir /etc/setup/backup')
                     system('touch /etc/setup/backup/0dir')                      
                  if os.path.isfile('/etc/setup/backup/bkp/0dir') == False:
                     system('mkdir /etc/setup/backup/bkp')
                     system('touch /etc/setup/backup/bkp/0dir')                           
                  if os.path.isfile('/etc/setup/backup/users') == False:
                     system('touch /etc/setup/backup/users')
                  if os.path.isfile('/etc/setup/backup/ario') == False:
                     system('touch /etc/setup/backup/ario')
                  if os.path.isfile('/etc/setup/backup/bkp/%s' %(bus)) == True:
                     print (f1+'Error: o usuario %s ja se encontra no Backup.\033[m' %(bus))
                     bsck()
                  system('''xdif='/etc/setup/bkp/'''+bus+''''
                  while read n
                  do
                    usr="$(echo $n | cut -d' ' -f1)"
                    lm="$(echo $n | cut -d' ' -f2)"
                    pas="$(echo $n | cut -d' ' -f3)"
                    d="$(echo $n | cut -d' ' -f4)"
                    dx="$(echo $n | cut -d' ' -f5)"
                    echo $usr $lm $pas $d $dx > /etc/setup/backup/bkp/$usr
                    echo $usr $lm $pas $d $dx >> /etc/setup/backup/users
                    echo $usr >> /etc/setup/backup/ario                         
                  done < $xdif''')
                  print ('\033[33mConcluido. usuario %s adicionado ao Backup.\033[m' %(bus))
                  sleep(1)
                  case()
              bsck()
                     
           if w == '12':
              if os.path.isfile('/etc/setup/senhas/except') == False:
                 print ('\033[31mError: Para utilizar esta funcao.. antes e\n'\
                       +'preciso configurar sua VPS com este script.')
                 sleep(2)
                 case()
                 
              if os.path.isfile('/etc/setup/speedtest.py') == False:
                 print ('\033[30m')
                 system('nohup wget -qc \
                 https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py')
                 print ('\033[m')
                 system('cp speedtest.py /etc/setup')
                 if os.path.isfile('/root/index.html') == True:
                    system('rm -rf /root/index.htm')
                 system('rm -rf speedtest.py')
                 if os.path.isfile('/root/nohup.out') == True:
                    system('rm -rf /root/nohup.out')
              system('python3 /etc/setup/speedtest.py')
              
              w = input(f6+'\n :: _\033[92m'+' ')
           if w == '14':
              if os.path.isfile('/etc/setup/backup/0dir') == True:
                 print (f1+'Isto excluirar todo o Backup antigo ..\033[m')
              bk = input(f6+'Deseja fazer o Backup de todos os usuarios'\
                        +' [y/n] :: _\033[32m'+' ')
              if bk == '0':
                 case()
              if bk == 'y' or bk == 'Y':
                 print ('\033[32mfazendo o Backup dos usuarios .. aguarde.\033[m')
                 if os.path.isfile('/etc/setup/backup/users') == True:
                    system('rm -rf /etc/setup/backup')
                    
                 system('mkdir /etc/setup/backup')
                 system('touch /etc/setup/backup/0dir')
                 sleep(3)
                 system('cp /etc/setup/users /etc/setup/backup')
                 system('cp -r /etc/setup/bkp /etc/setup/backup')
                 system('touch /etc/setup/backup/bkp/0dir')
                 system('cp /etc/setup/ario /etc/setup/backup')
                 print ('\n\033[33mConcluido. Backup feito em /etc/setup/backup.\033[m')
                 sleep(2)
                 case()
                 
              if bk == 'n' or bk == 'N':
                 w = input(f6+'\n :: _\033[92m'+' ')
           if w == '15':
              __sbm__ = f6+'\n1) = Restaurar usuarios\n'\
                          +'2) = Restaurar um usuario\n'\
                          +'3) = Deletar um usuario do Backup\n'\
                          +'4) = Deletar Todos os usuarios\n'\
                          +'5) = Deletar Backup\n'\
                          +'0) = Home\033[m\n'
                          
              print (__sbm__)
              # 4 = True
              # 5 = True
              # 0 = True
              def mopt():
                  sbm = input(f6+' :: _\033[92m'+' ')
                  if sbm == '0':
                     case()

                  if sbm == '1':
                     rst = input(f6+'Voce quer restaurar todos os usuarios do'\
                                +' Backup [y/n] :: _\033[92m'+' ')
                     if rst == '0':
                        system('clear')
                        case()
                     if rst == 'y' or rst == 'Y':
                        if os.path.isfile('/etc/setup/backup/users') == False:
                           print (f1+'Error: voce ainda nao tem um Backup.\033[m')
                           sleep(3)
                           case()
                           
                        system('''backup='/etc/setup/backup/users'\
                               \nwhile read us\
                               \ndo\
                               \nusr="$(echo $us | cut -d' ' -f1)"\
                               \nlm="$(echo $us | cut -d' ' -f2)"\
                               \npas="$(echo $us | cut -d' ' -f3)"\
                               \ndx="$(echo $us | cut -d' ' -f5)"\
                               \nd=$(date '+%C%y-%m-%d' -d '+'$dx' days')\
                               \nda=$(date '+%d/%m/%Y' -d '+'$dx' days')\
                               \nuseradd -M -s /bin/false $usr -e $d\
                               \n(echo "$pas" ; echo "$pas" ) |passwd $usr\
                                > /dev/null 2>/dev/null\
                               \necho '\033[33mUsuario: '$usr'\nsenha: '$pas\
                               '\nmaxlogin '$lm '\nRestaurado ..\nExpira:' $da'\n\033[m'\
                               \nsleep 1\
                               \necho $usr $lm >> /root/usuarios.db\
                               \necho $usr' - maxlogins '$lm >> /etc/setup/limite/$usr\
                               \necho $usr' - maxlogins '$lm >> /etc/security/limits.conf\
                               
                               \ngrep -v ^$usr[[:space:]] /etc/setup/users\
                                > /tmp/bkp; cat /tmp/bkp > /etc/setup/users\
                               \ngrep -v ^$usr[[:space:]] /etc/setup/backup/users\
                                > /tmp/bkp; cat /tmp/bkp > /etc/setup/backup/users\
                                
                               \necho $usr $lm $pas $d $dx >> /etc/setup/users\
                               \necho $usr $lm $pas $d $dx >> /etc/setup/bkp/$usr\
                               \nrm -rf /etc/setup/backup/bkp/$usr\
                               \ndone < $backup''')
                               
                        system('rm -rf /etc/setup/backup/users')
                        system('rm -rf /etc/setup/backup')
                        print ('\033[33mConcluido. Restauracao do Backup completa.\033[m')
                        sleep(2)
                        case()
                        
                     if rst == 'n' or rst == 'N':
                        mopt()
                  if sbm == '2':
                     def userrs():
                         if os.path.isfile('/etc/setup/backup/users') == False:
                           print (f1+'Error: Voce ainda nao tem um Backup.\033[m')
                           sleep(2)
                           case()
                           
                         print ('\033[33mUsuarios no Backup:')
                         system('cat /etc/setup/backup/ario')
                         print ('\n\033[m')
                         
                         us = input(f6+'Qual usuario voce Deseja Restaurar :: _'+' ')
                         if us == '0':
                            case()
                            
                         if os.path.isfile('/etc/setup/backup/bkp/%s' %(us)) == False:
                            print (f1+'Error: o usuario %s nao se encontra no Backup.\033[m'\
                            %(us))
                            userrs()
                         system('''ss="/etc/setup/backup/bkp/'''+us+'''"\
                                \nusr="$(cat $ss | cut -d' ' -f1)"\
                                \nlm="$(cat $ss | cut -d' ' -f2)"\
                                \npas="$(cat $ss | cut -d' ' -f3)"\
                                \ndx="$(cat $ss | cut -d' ' -f5)"\ 
                                \nd=$(date '+%C%y-%m-%d' -d '+'$dx' days')\
                                \nda=$(date '+%d/%m/%Y' -d '+'$dx' days')\
                               
                                \nuseradd -M -s /bin/false $usr -e $d\
                                \n(echo "$pas" ; echo "$pas" ) |passwd $usr\
                                 > /dev/null 2>/dev/null\
                                \necho '\033[33mConcluido. usuario: '$usr' senha: '$pas\
                                 'maxlogin '$lm' Restaurado.\nExpira:' $da'\033[m'\
                                \necho $usr $lm >> /root/usuarios.db\
                                \necho $usr' - maxlogins '$lm > /etc/setup/limite/$usr\
                                \necho $usr' - maxlogins '$lm >> /etc/security/limits.conf\
                                
                                \ngrep -v ^$usr[[:space:]] /etc/setup/users\
                                 > /tmp/bkp; cat /tmp/bkp > /etc/setup/users\
                                \ngrep -v ^$usr[[:space:]] /etc/setup/backup/users\
                                 > /tmp/bkp; cat /tmp/bkp > /etc/setup/backup/users\
                                \nrm -rf /etc/setup/bkp/$usr\
                                
                                \necho $usr $lm $pas $d $dx >> /etc/setup/users\
                                \necho $usr $lm $pas $d $dx > /etc/setup/bkp/$usr''')
                                
                         system('rm -rf /etc/setup/backup/bkp/%s' %(us))
                         sleep(1)
                         case()
                         
                     userrs()
                  if sbm == '3':
                     def bacf():
                         if os.path.isfile('/etc/setup/backup/users') == False:
                           print (f1+'Error: Voce ainda nao tem um Backup.\033[m')
                           sleep(3)
                           case()
                           
                         rtb = input(f6+'Qual usuario voce quer tirar do Backup :: _\033[92m'\
                                    +' ')
                         if rtb == '0':
                            case()
                         if os.path.isfile('/etc/setup/backup/bkp/%s' %(us)) == False:
                            print (f1+'Error: o usuario %s nao se encontra no Backup.\033[m'\
                            %(us))
                            bacf()
                         system('rm -rf /etc/setup/backup/bkp/'+rtb)
                         system('grep -v ^'+rtb+'[[:space:]] /etc/setup/backup/users\
                          > /tmp/bkp; cat /tmp/bkp > /etc/setup/backup/users')
                          
                         print ('\033[33mConcluido. o usuario %s foi deletado'\
                               +' do Backup.\033[m'\
                         %(rtb))
                         sleep(2)
                         case()
                         
                     bacf()
                  if sbm == '4':
                     print (f1+'\nEsta funcao Deletarar todos os usuarios ..\n'\
                           +'ativos e criados por este progama.\033[m')
                     dlt = input(f6+'Deseja deletar mesmo assim [y/n] :: _\033[92m'+' ')
                     if dlt == '0':
                        case()
                        
                     if dlt == 'y' or dlt == 'Y':
                        if os.path.isfile('/etc/setup/limite/lm') == False:
                           print (f1+'Error: Voce ainda nao fez usuarios com este script.'\
                                 +'\033[m')
                           sleep(2)
                           case()
                           
                        up = input('\033[33mVoce fez ou Deseja fazer o Backup de algum\n'\
                                  +'desses usuarios futuramente. [y/n]\033[36m :: _\033[92m'\
                                  +' ')
         
                        system('rm -rf /etc/setup/limite && mkdir /etc/setup/limite')
                        system('touch /etc/setup/limite/lm')
                        if up == 'y' or up == 'Y':
                           print ('\033[32mCerto.. as informacoes ficaram Preservadas.\033[m')
                           sleep(1)
                        system('''exc='/etc/setup/ario'
                        while read ex
                        do
                          userdel --force $ex > /dev/null 2>/dev/null
                          grep -v ^$ex[[:space:]] /etc/security/limits.conf\
                           > /tmp/dx; cat /tmp/dx > /etc/security/limits.conf
                          rm -rf /tmp/dx
                                 
                          echo 'Usuario' $ex '.. Deletado.'
                          sleep 1
                          
                        done < $exc''')
                               
                        if up == 'n' or up == 'N':
                           system('rm -rf /etc/setup/bkp && mkdir /etc/setup/bkp')
                           system('rm -rf /etc/setup/users && touch /etc/setup/users')
                           system('rm -rf /etc/setup/ario && touch /etc/setup/ario')
                           
                        system('rm -rf /root/usuarios.db && touch /root/usuarios.db')
                        system('rm -rf /etc/setup/senhas && mkdir /etc/setup/senhas')
                        
                        print ('\033[33m\nConcluido.. Todos os usuarios foram excluidos.'\
                              +'\033[m')
                        sleep(2)
                        case()
                        
                     if dlt == 'n' or dlt == 'N':
                        case()
                        
                  if sbm == '5':
                     print (f1+'Esta funcao excluirar todos os usuarios\n'\
                           +'que estao no Backup deseja continuar.')
                     def rtu():
                         bex = input(f6+' ... [y/n] :: _\033[92m'+' ')
                         if bex == '0':
                            system('clear')
                            case()
                         if bex == 'y' or bex == 'Y':
                            system('rm -rf /etc/setup/backup')
                         if bex == 'n' or bex == 'N':
                            system('clear')
                            case()
                         print ('\033[33mConcluido. todo o Backup foi Deletado.\033[m')
                         sleep(2)
                         case()
                         
                         if bex != 'n' or bex != 'N' or bex != 'y' or bex != 'Y':
                            rtu()
                     rtu()
                  if sbm != '1' or sbm != '2' or sbm != '0' or sbm != '4' or sbm != '3'\
                   or sbm != '5' or sbm != '6':
                     mopt()
              mopt()
           if w == '11':
              url = 'http://ip-api.com/json/%s' % (__ip__)
              req = urlopen(url).read()
              json_data = simplejson.loads(req)
              if ':' not in json_data:
                  if json_data['zip'] == '':
                     json_data['zip'] = 'Null'
              __ADD__ = '\033[92m\nIPAddress\033[92m: '+ str(json_data['query'])\
                       +'\033[32m\nPais\033[92m: '+ str(json_data['country'])\
                       +'\033[92m\nPais Code\033[32m: '+ str(json_data['countryCode'])\
                       +'\033[32m\nHospedado por\033[92m: '+ str(json_data['as'])\
                       +'\033[92m\nProvedor\033[32m: '+ str(json_data['isp'])\
                       +'\033[32m\nCidade\033[92m: '+ str(json_data['city'])\
                       +'\033[92m\nRegiao:\033[32m '+ str(json_data['regionName'])\
                       +'\033[32m\nRegiao Code\033[92m: '+ str(json_data['region'])\
                       +'\033[92m\nFuso horario\033[32m: '+ str(json_data['timezone'])\
                       +'\033[32m\nZip\033[92m: '+ str(json_data['zip'])\
                       +'\033[92m\nStatus\033[32m: '+ str(json_data['status'])\
                       +'\033[32m\nLat/Long\033[32m: '+ str(json_data['lat'])\
                                                    +', '+ str(json_data['lon'])
                                                    
              print (__ADD__+'\n')
              w = input(f6+' :: _\033[92m'+' ')

           if w == '10':
              print ('\033[92mMonitor do Sistema\033[32m ..\033[m')
              system('''OS=`uname -s` && REV=`uname -r` && MACH=`uname -m` &&
              if [ "${OS}" = "SunOS" ]; then
                 OS=Solaris
                 ARCH=`uname -p`
                 OSSTR="${OS} ${REV}(${ARCH} `uname -v`)"
              elif [ "{OS}" = "AIX" ]; then
                 OSSTR="${OS} `oslevel` (`oslevel -r`)"
              elif [ "${OS}" = "Linux" ]; then
                   KERNEL=`uname -r`
                   if [ -f /etc/redhat-releas ]; then
                      DIST='RedHat'
                      PSUEDONAME=`cat /etc/redhat-release | sed s/.*\(// | sed s/\)//`
                      REV=`cat /etc/redhat-release | sed s/.*release\ // | sed s/\ .*//`
                   elif [ -f /etc/SuSE-release ]; then
                      DIST=`cat /etc/SuSE-release | tr "\n" ' '| sed s/VERSION.*//`
                      REV=`cat /etc/SuSE-release | tr "\n" ' ' | sed s/.*=\ //`
                   elif [ -f /etc/mandrake-release ]; then
                      DIST=`Mandrake`\
                      PSUEDONAME=`cat /etc/mandrake-release | sed s/.*\(// | sed s/\)//`
                      REV=`cat /etc/mandrake-release | sed s/.*release\ // | sed s/\ .*//`
                   elif [ -f /etc/os-release ]; then
                      DIST=`awk -F "PRETTY_NAME=" '{print $2}' /etc/os-release | tr -d '\n"'`
                   elif [ -f /etc/debian_version ]; then
                      DIST="Debian `cat /etc/debian_version`"
                      REV=''
                   fi
                   if ${OSSTR} [ -f /etc/UnitedLinux-release ]; then
                      DIST="${DIST}[`cat /etc/UnitedLinux-release | tr "\n" ' '\
                       | sed s/VERSION.*//`]"
                   fi
                   OSSTR="${OS} ${DIST} ${REV}(${PSUEDONAME}${MACH})"
                   echo '\033[32mVersao do OS\033[92m:' $OSSTR
              fi''')
              system('''echo '\033[92mSistema Operacional\033[32m:' $(uname -o)''')
              if os.path.isfile('/etc/debian_version') == True:
                 system('''echo '\033[32mVersao Debian\033[92m:' $(cat /etc/debian_version)''')
              system('''echo '\033[32mProcessador ..\n\033[92mModelo:' $(cat /proc/cpuinfo\
               |grep "model name" |uniq |awk -F : {'print $2'})''')
              system('''echo '\033[32mNucleos:' $(cat /proc/cpuinfo |grep "cpu cores"\
               |uniq |awk -F : {'print $2'})''')
              system('''arq=$(uname -m)\necho '\033[92mArquitetura\033[32m:' $arq''')
              system('''kernel=$(uname -r)\necho '\033[32mKernel\033[92m:' $kernel''')
              system('''serv=$(cat /etc/resolv.conf | sed '1 d' | awk '{print $2}')\n
                     echo '\033[92mServidor DNS\033[32m:' $serv''')
              system('''host=$(hostname)\necho '\033[32mHostName\033[92m:' $host''')
              system('''internal=$(hostname -i)\necho '\033[92mIP Interno\033[32m:'\
                $internal''')
              print ('\033[92mMemoria Ram\033[32m')
              system('''echo 'Total:' $(free -h |grep -i mem |awk {'print $2'})''')
              system('''echo 'Usada:' $(free -h |grep -i mem |awk {'print $3'})''')
              system('''echo 'Livre:' $(free -h |grep -i mem |awk {'print $4'})''')
              print ('\033[92mSwap ..\033[32m')
              system('''echo 'Total:' $(free -h |grep -i swap |awk {'print $2'})''')
              system('''echo 'Usada:' $(free -h |grep -i swap |awk {'print $3'})''')
              system('''echo 'Livre:' $(free -h |grep -i swap |awk {'print $4'})''')
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
                printf ' %-35s%s\n' $usr $(cat /tmp/tmp4 | wc -l)/$ss1; tput sgr0
              done < $database
              rm -rf /tmp/tmp4''')
              system('''load=$(top -n 1 -b | grep 'load average:'\
               | awk '{print $11 $12 $13 $14}')\n
                     echo '\033[92mCarga Media\033[92m:' $load''')
              system('''time=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)\n
                     echo '\033[32mTempo de Atividade\033[92m:' $time''')
              w = input(f6+'\n :: _\033[92m'+' ')

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
                 system('''echo 'Ola, anqui fica armazenado todas as senhas '''\
                       +'''criadas por este progama.' > /etc/setup/senhas/except''')
                       
              if os.path.isfile('/etc/setup/users') == False:
                 system('touch /etc/setup/users')
                 system('touch /etc/setup/ario')
                 system('mkdir /etc/setup/bkp')
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
                 print ('\033[33mConfigurando Portas SQUID IP:\033[92m %s\033[m' %(__ip__))
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
                 print ('\033[33mConfigurando Portas SQUID3 IP:\033[92m %s\033[m' %(__ip__))
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
                    
                    print ('\033[32mPortas SQUID3: 80, 8080, 8799, 3128 Ativadas.\033[m')
                    sleep(2)
                    
              print ('\033[33mConfigurando Portas SSH.\033[m')
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
                 print ('\033[32mPortas SSH[22/443]SQUID Rodando 100%\033[m')
              else:
                 print ('\033[32mReiniciando Servidor SQUID3.\033[m')
                 system('cd /etc && service squid3 restart')
                 sleep(2)
                 print ('\033[32mPortas SSH[22/443]SQUID3 Rodando 100%\033[m')
              sleep(3)
              print ('\033[32mConcluido. Portas 22/443/80/8080/8799/3128 100% ativas ..\033[m')
              print ('\033[32mCrie um usuario e teste.\033[m')
              sleep(2)
              case()
              
           if w == '2':
              rc = input(f6+'Deseja Remover todas as Modificacoes. [y/n] :: _\033[92m'+' ')
              if rc == 'y' or rc == 'Y':
                 if os.path.isfile('/etc/setup/ario') == True:
                    system('''exc='/etc/setup/ario'
                    while read ex
                    do
                      userdel --force $ex > /dev/null 2>/dev/null
                      grep -v ^$ex[[:space:]] /etc/security/limits.conf\
                       > /tmp/dx; cat /tmp/dx > /etc/security/limits.conf
                      rm -rf /tmp/dx
                      echo 'Usuario' $ex '.. Deletado.'
                      sleep 1            
                    done < $exc''')
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
                 print ('\n\033[33mConcluido.. Pode reconfigurar sua vps com um script da\n'\
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
              print ('\033[33mDomains do arquivo:\033[36m')
              if os.path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
              print ('\n')
              def dom():
                  do = input(f6+'Adicionar Domain :: _\033[92m'+' ')
                  if do == '0':
                     if os.path.isfile('/etc/squid/squid.conf') == True:
                        system('cd /etc && service squid restart')
                     else:
                        system('cd /etc && service squid3 restart')
                     case()
                  if os.path.isfile('/etc/squid3/domains/domain') == True:
                     if os.path.isfile('/etc/squid3/domains/%s' %(do)) == True:
                        print (f1+'Error: o domain %s ja existe.\033[m' %(do))
                        dom()
                     system('''echo '%s' >> /etc/squid3/domains/domain''' % (do))
                     system('''touch /etc/squid3/domains/%s''' % (do))
                     print ('\033[33mDomain: %s Adicionado. [0] Para Home.' % (do))
                     dom()
                  else:
                     if os.path.isfile('/etc/squid/domains/%s' %(do)) == True:
                        print (f1+'Error: o domain %s ja existe.\033[m' %(do))
                        dom()
                     system('''echo '%s' >> /etc/squid/domains/domain''' % (do))
                     system('''touch /etc/squid/domains/%s''' % (do))
                     print ('\033[33mDomain: %s Adicionado. [0] Para Home.' % (do))
                     dom()
              dom()
              
           if w == '4':
              if os.path.isfile('/etc/squid/domains/domain') == False\
               or os.path.isfile('/etc/squid3/domains/domain') == False:
                 if os.path.isfile('/etc/squid3/squid.conf') == True:
                    system('touch /etc/squid3/domains/domain')
                 else:
                    system('touch /etc/squid/domains/domain')
              print ('\033[33mDomains do arquivo:\033[36m')
              if os.path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
                 
              print ('\n')
              def delet():
                  de = input(f6+'Deletar Domain :: _\033[92m'+' ')
                  if de == '0':
                     if os.path.isfile('/etc/squid/squid.conf') == True:
                        system('cd /etc && service squid restart')
                     else:
                        system('cd /etc && service squid3 restart')
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
                     print ('\033[33mDomain: %s Excluido. [0] Para Home.\033[m' % (de))
                     delet()
                  else:
                     if os.path.isfile('/etc/squid3/domains/%s' %(de)) == False:
                        print (f1+'Error: o domain %s nao existe.\033[m' %(de))
                        delet()
                     system('rm -rf /etc/squid3/domains/%s' %(de))
                     for i, line in enumerate(fileinput.input('/etc/squid3/domains/domain',\
                      inplace=1)):
                         sys.stdout.write(line.replace(de+'\n', ''))
                     sleep(2)
                     print ('\033[33mDomain: %s Excluido.. [0] Para Home.\033[m' % (de))
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
                      
              nb = input(f6+'Adicionar ao Banner :: _ \033[92m'+' ')
              system('''echo '%s' > /etc/Banner''' % (nb))
              system('cd /etc && service ssh restart')
              print ('\033[32mBanner:\033[92m %s \033[32m\nAdicionado com Sucesso.\033[m'\
               % (nb))
              sleep(2)
              case()
              
           if w == '6':
              rb = input(f6+'Deseja deletar o Banner por completo. [y/n] :: _\033[92m'+' ')
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
                    print ('\033[33mConcluido .. Banner Retirado.\033[m')
                    sleep(2)
                    case()
                    
              if rb == 'n' or rb == 'N':
                 case()
                 
           if w == '7':
              if os.path.isfile('/etc/setup/senhas/except') == False:
                 system('touch /etc/setup/senhas/except')
              def user():
                  n = input(f6+'Nome do usuario :: _\033[92m'+' ')
                  if os.path.isfile('/root/usuarios.db') == False:
                     system('touch /root/usuarios.db')
                  if os.path.isfile('/etc/setup/senhas/%s' %(n)) == True:
                     print (f1+'Error: o usuario %s ja existe.\033[m' %(n))
                     user()
                  sn = input(f6+'Senha Para '+n+' :: _\033[92m'+' ')
                  dx = input(f6+'Quantos dias '+n+' deve durar :: _\033[92m'+' ')
                  lm = input(f6+'Maximo de conexoes simultaneas :: _\033[92m'+' ')
                  system("d=$(date '+%C%y-%m-%d' -d '+"+dx+" days')\
                         \nda=$(date '+%d/%m/%Y' -d '+"+dx+" days')\
                         \nuseradd -M -s /bin/false "+n+" -e $d\
                         \necho '\033[33m\nConcluido .. usuario criado.'\n\
                         \necho '\033[32mUsuario:\033[92m "+n+"'\
                         \necho '\033[32mSenha:\033[92m "+sn+"'\
                         \necho '\033[32mExpira:\033[92m '$da'\033[m'\
                         \necho '"+sn+"' > /etc/setup/senhas/"+n+"\
                         \necho '"+n+"' '"+lm+"' '"+sn+"' $d '"+dx+"' >> /etc/setup/users\
                         \necho '"+n+"' '"+lm+"' '"+sn+"' $d '"+dx+"' > /etc/setup/bkp/"+n)
                         
                  system('(echo "'+sn+'" ; echo "'+sn\
                        +'" ) |passwd '+n+' > /dev/null 2>/dev/null')
                  system('''echo '%s' >> /etc/setup/ario''' %(n))
                  system('''echo '%s %s' >> /root/usuarios.db''' %(n,lm))
                  system('''echo '%s - maxlogins %s' > /etc/setup/limite/%s''' %(n,lm,n))
                  system('''echo '%s - maxlogins %s' >> /etc/security/limits.conf''' %(n,lm))
                  case()
              user()
              
           if w == '9':
              def dex():
                  df = input(f6+'Que usuario voce deseja deletar :: _\033[92m'+' ')
                  if df == '0':
                     case()
                     
                  if os.path.isfile('/etc/setup/senhas/'+df) == False:
                     print (f1+'Error: o usuario %s nao existe.. ou nao '%(df)\
                          +'foi criado por este progama.\033[m')
                     dex()
                  cup = input('\033[33mDeseja fazer o Backup de '+df\
                             +' futuramente. [y/n]\033[36m :: _\033[92m'+' ')
                  if cup == 'N' or cup == 'n':
                     system('rm -rf /etc/setup/bkp/%s' %(df))
                     system('grep -v ^'+df+'[[:space:]] /etc/setup/users\
                      > /tmp/bkp; cat /tmp/bkp > /etc/setup/users')
                  if cup == 'Y' or cup == 'y':
                     print ('\033[32mCerto? informacoes do usuario Guardadas.\033[m')
                  for i, line in enumerate(fileinput.input('/etc/setup/ario', inplace=1)):
                        sys.stdout.write(line.replace(df, ''))
                  system('userdel --force %s > /dev/null 2>/dev/null' %(df))
                  system('rm -rf /etc/setup/senhas/%s' %(df))
                  system('grep -v ^'+df+'[[:space:]] /etc/security/limits.conf\
                   > /tmp/mite; cat /tmp/mite > /etc/security/limits.conf')
                  system('grep -v ^'+df+'[[:space:]] /root/usuarios.db\
                   > /tmp/usdb; cat /tmp/usdb > /root/usuarios.db')
                  system('rm -rf /etc/setup/limite/'+df)
                  print ('\033[33mUsuario %s excluido com exito. [0] Para Home.\033[m' %(df))
                  sleep(2)
                  dex()
              dex()
              
           if w == '8':
              main = '\n\033[36m1) = Mudar senha\n'\
                    +'2) = Mudar Data de expiracao\n'\
                    +'3) = Mudar limite de logins\n'\
                    +'4) = Mudar Nome de usuario\n'\
                    +'0) = Home\n\n\033[m'
              print (main)
              
              def rdf():
                   rd = input(f6+'Que usuario voce deseja redefinir :: _\033[92m'+' ')
                   if rd == '0':
                      case()
                      
                   if os.path.isfile('/etc/setup/senhas/%s' %(rd)) == False:
                      print (f1+'\nErro: o usuario %s nao existe ..\033[m' %(rd))
                      rdf()
                   md = input(f6+' :: _\033[92m'+' ')
                   if md == '0':
                      case()
                      
                   if md == '1':
                      sna = input(f6+'\nNova senha para '+rd+' :: _\033[92m'+' ')
                      system('grep -v ^'+rd+'[[:space:]] /etc/setup/users\
                       > /tmp/bkp; cat /tmp/bkp > /etc/setup/users')
                      system('''usr="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f1)"\
                             \nlm="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f2)"\
                             
                             \nd="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f4)"\
                             \ndx="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f5)"\
                             \n(echo "'''+sna+'''" ; echo "'''+sna\
                             +'''" ) |passwd '+rd+' > /dev/null 2>/dev/null\
                             \necho $usr $lm '''+sna+''' $d $dx >> /etc/setup/users\
                             \necho $usr $lm '''+sna+''' $d $dx > /etc/setup/bkp/$usr''')
                             
                      system('rm -rf /etc/setup/senhas/'+rd)
                      system('echo "'+sna+'" > /etc/setup/senhas/'+rd)
                      print ('\033[33mConcluido. nova senha aplicada para %s' %(rd))
                      sleep(2)
                      case()
                      
                   if md == '2':
                      dt = input(f6+'Quantos dias '+rd+' deve durar :: _\033[92m'+' ')
                      system('''d=$(date '+%C%y-%m-%d' -d "+"'''+dt+'''" days")\
                             \nda=$(date '+%d/%m/%Y' -d "+"'''+dt+'''" days")\
                             
                             \nusr="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f1)"\
                             \nlm="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f2)"\
                             \npas="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f3)"\
                             \nchage -E $d '''+rd+''' 2> /dev/null\
                             \necho '\033[33mConcluido. nova data aplicada para '''+rd\
                             +'''\033[m'\
                             \necho '\033[32mExpira:\033[m' $da\
                             \ngrep -v ^'''+rd+'''[[:space:]] /etc/setup/users\
                              > /tmp/bkp; cat /tmp/bkp > /etc/setup/users\
                             \necho $usr $lm $pas $d '''+dt+''' >> /etc/setup/users\
                             \necho $usr $lm $pas $d '''+dt+''' > /etc/setup/bkp/$usr''')
                      sleep(2)
                      case()
                      
                   if md == '3':
                      mt = input(f6+'Qual o novo limite para '+rd+' :: _\033[92m'+' ')
                      system('''usr="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f1)"\
                             \npas="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f3)"\
                             \nd="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f4)"\
                             \ndx="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f5)"\
                             
                             \ngrep -v ^'''+rd+'''[[:space:]] /etc/security/limits.conf\
                              > /tmp/mite; cat /tmp/mite > /etc/security/limits.conf\
                             \ngrep -v ^'''+rd+'''[[:space:]] /root/usuarios.db\
                              > /tmp/usdb; cat /tmp/usdb > /root/usuarios.db\
                             \ngrep -v ^'''+rd+'''[[:space:]] /etc/setup/users\
                              > /tmp/bkp; cat /tmp/bkp > /etc/setup/users\
                             \necho $usr '''+mt+''' $pas $d $dx >> /etc/setup/users\
                             \necho $usr '''+mt+''' $pas $d $dx > /etc/setup/bkp/$usr''')
                             
                      system('''echo '%s %s' >> /root/usuarios.db''' %(rd,mt))
                      system('''echo '%s - maxlogins %s' > /etc/setup/limite/%s''' %(rd,mt,rd))
                      system('''echo '%s - maxlogins %s' >> /etc/security/limits.conf'''\
                      %(rd,mt))
                      print ('\033[33mConcluido. novo limete de '+mt+' conexoes aplicado'\
                            +' para '+rd+'.\033[m')
                      sleep(2)
                      case()
                      
                   if md == '4':
                      no = input(f6+'Qual o novo nome para '+rd+' :: _\033[92m'+' ')
                      system('''lm="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f2)"\
                             \npas="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f3)"\
                             \nd="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f4)"\
                             \ndx="$(cat /etc/setup/bkp/'''+rd+''' | cut -d' ' -f5)"\
                             \nuserdel --force '''+rd+''' > /dev/null 2>/dev/null\
                             \nuseradd -M -s /bin/false '''+no+''' -e $d\
                             \n(echo "$pas" ; echo "$pas" ) |passwd '''+no+'''\
                              > /dev/null 2>/dev/null\
                             \ngrep -v ^'''+rd+'''[[:space:]] /etc/setup/ario\
                              > /tmp/tmp4; cat /tmp/tmp4 > /etc/setup/ario\
                             \ngrep -v ^'''+rd+'''[[:space:]] /etc/setup/users\
                              > /tmp/tmp4; cat /tmp/tmp4 > /etc/setup/users\
                             \ngrep -v ^'''+rd+'''[[:space:]] /etc/security/limits.conf\
                              > /tmp/tmp4; cat /tmp/tmp4 > /etc/security/limits.conf\
                             \ngrep -v ^'''+rd+'''[[:space:]] /root/usuarios.db\
                              > /tmp/tmp4; cat /tmp/tmp4 > /root/usuarios.db\
                              
                             \necho '''+no+''' >> /etc/setup/ario\
                             \necho $pas >> /etc/setup/senhas/'''+no+'''\
                             \necho  '''+no+''' $lm $pas $d $dx > /etc/setup/bkp/'''+no+'''\
                             \necho '''+no+''' $lm >> /root/usuarios.db\
                             \necho '''+no+''' '- maxlogins '$lm >> /etc/setup/limite/'''\
                             +no+'''\
                             \necho '''+no+''' '- maxlogins '$lm >> /etc/security/limits.conf\
                             \necho '''+no+''' $lm $pas $d $dx >> /etc/setup/users\
                             \necho '''+no+''' $lm $pas $d $dx >> /etc/setup/bkp/'''+no+'''\
                             \nrm -rf /etc/setup/senhas/'''+rd+'''\
                             \nrm -rf /etc/setup/bkp/'''+rd)
                             
                      print ('\033[33mConcluido. '+rd+' agora se chama '+no+'.\033[m')
                      sleep(2)
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