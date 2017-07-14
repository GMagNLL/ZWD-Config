#!/usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
__version__ = '1.5'

# [Github] https://www.github.com/Xdwnff-04x
# [Telegram - Channel] https://telegram.me/ZWDChannel
# [Telegram - PV] @nZwdeff
# 
# [Unoficial]
#   Progamas utilizados, fora a Dependencia python. que nao foram escrito por mim.
#   speedtest-cli GitHub: https://www.github.com/sivel/speedtest-cli
#   get-pip GitHub: https://www.github.com/pypa/get-pip
#
# [Sobre - v1.5] Melhorias no Codigo.
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
import time
import os, re
import fileinput
from os import system
from sys import *
from time import *

n0='\033[90m'
n1='\033[91m'
n2='\033[92m'
n3='\033[93m'
n4='\033[94m'
n5='\033[95m'
n6='\033[96m'
n7='\033[97m'

u1='\033[31m'
u2='\033[32m'
u3='\033[33m'
u4='\033[34m'
u5='\033[35m'
u6='\033[36m'
u7='\033[37m'
u0='\033[m'

if argv[1:]:
   if argv[1] == '--help':
      help = 'Para utilizar com perfeicao todas as funcoes disponiveis, antes e preciso\n'\
            +'configurar sua VPS com a funcao 1) deste Progama. Para mais\n'\
            +'Informacoes, Duvidas, Relatar Erros, ou sugestoes de '\
            +'melhorias.\nentre em contato comigo.\nTelegram: @nZwdeff'
      print(help)
      exit()
   else:
      print('Comando invalido? Use --help.')
      exit()

if version_info < (3, 0):
   print(u1+'Error: Progama suportado somente em Python3x.'+u0)
   sleep(2)
   exit()
   
try:
   import simplejson
except ImportError:
   print(n1+'Dependencias Desinstaladas.'+u0)
   sleep(1)
   print(n2+'Instalando Dependencias .. Aguarde'+u0)
   if os.path.isfile('/usr/local/bin/pip3') == False:
      system('nohup wget -qc https://raw.githubusercontent.com/pypa/get-pip/master/get-pip.py\
              1> /dev/null 2> /dev/null')
      system('python3 get-pip.py')
      
      if os.path.isfile('/root/nohup.out') == True:
         system('rm -rf /root/nohup.out')
      system('rm -rf get-pip.py')
      
   system('pip3 install simplejson')
   sleep(4)
   print(u3+'\nConcluido .. Dependencias Instaladas.'+u0)
   import simplejson
   sleep(6)
   system('clear')

from urllib.request import *

v = sys.version_info.major
H = strftime('%d/%m/%Y %H:%M:%S')
print(n2+'Connecting .. from python%s ' % (v)+u2+'/%s' %(H)+u0)
sleep(0.6)
try:
   __url_ = str(urlopen('http://check-host.net/ip').read())
   __ip__ = re.compile(r'(\d+\.\d+\.\d+\.\d+)').search(__url_).group()
  
   __information__ ='\n'\
   +u2+'Author: '+u6+'%s\n' % __author__ + u0\
   +u2+'Versao: '+u6+'%s\n' % __version__ + u0
   
   __main__ = '01 = Configurar VPS\n'\
             +'02 = Desconfigurar /SSH/SQUID3\n'\
             +'03 = Adicionar Domain\n'\
             +'04 = Remover Domain\n'\
             +'05 = Adicionar Banner\n'\
             +'06 = Remover Banner\n'\
             +'07 = Adicionar usuario\n'\
             +'08 = Redefinir usuario\n'\
             +'09 = Remover usuario\n'\
             +'10 = Monitor do Sistema\n'\
             +'11 = Informacoes do IP\n'\
             +'12 = Server Speed Test\n'\
             +'13 = Backup de um usuario\n'\
             +'14 = Backup dos usuarios\n'\
             +'15 = Mais Opcoes\n'\
             +'0) = Sair\n\n\033[m'

   __Banner__ = u2+'{= :'+n2+' ZWD Config '+u2+'&'+n2+' MANAGER '+u2+': =}' + u0
   
   print(__Banner__)
   print(__information__)
   print(u2+'IP: '+u6+'%s' %(__ip__)+u0)
   
except IOError:
   print(n1+'Erro: Por favor connecte-se a uma Rede de Dados ..'+u0)
   exit()
   
print(u6+'\n'+__main__)
def case():
  try:
     def casa():
         print(u6+'\n'+__main__)
         case()
         
     w = input(u6+' :: '+u0)
     
     while w != '1' or w != '2' or w != '3' or w != '4' or w != '5' or w != '6' or w != '13'\
      or w != '7' or w != '8' or w != '9' or w != '0' or w != '10' or w != '11' or w != '12'\
       or w != '14' or w != '15' or w != '01' or w != '02' or w != '03' or w != '04'\
        or w != '05' or w != '06' or w != '07' or w != '08' or w != '09':
        
        if w == '1' or w == '2' or w == '3' or w == '4' or w == '5' or w == '6' or w == '7'\
         or w == '8' or w == '9' or w == '0' or w == '10' or w == '11' or w == '00'\
          or w == '12' or w == '13' or w == '14' or w == '15' or w == '01' or w == '02'\
           or w == '03' or w == '04' or w == '05' or w == '06' or w == '07' or w == '08'\
            or w == '09':
           if w == '13':
              def bsck():
                  bus = input(u6+'De Qual usuario voce quer fazer Backup :: '+u0)
                  if bus == '0':
                     casa()
                  if os.path.isfile('/etc/setup/senhas/%s' %(bus)) == False:
                     print(n1+'Error: o usuario %s nao existe.' %(bus)+u0)
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
                     print(n1+'Error: o usuario %s ja se encontra no Backup.' %(bus)+u0)
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
                  print(u3+'Concluido. usuario %s adicionado ao Backup.\n' %(bus)+u0)
                  sleep(1)
                  case()
              bsck()
                     
           if w == '12':
              if os.path.isfile('/etc/setup/senhas/except') == False:
                 print(n1+'Error: Para utilizar esta funcao.. antes e\n'\
                       +'preciso configurar a sua vps com este script.'+u0)
                 sleep(2)
                 casa()
                 
              if os.path.isfile('/etc/setup/speedtest.py') == False:
                 system('nohup wget -qc \
                 https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py\
                  1> /dev/null 2> /dev/null')
                 system('cp speedtest.py /etc/setup')
                 if os.path.isfile('/root/index.html') == True:
                    system('rm -rf /root/index.htm')
                 system('rm -rf speedtest.py')
                 if os.path.isfile('/root/nohup.out') == True:
                    system('rm -rf /root/nohup.out')
              system('python3 /etc/setup/speedtest.py')
              case()

           if w == '14':
              if os.path.isfile('/etc/setup/backup/0dir') == True:
                 print(n1+'Isto excluirar todo Backup antigo ..'+u0)
              bk = input(u3+'Deseja fazer Backup de todos os usuarios (y/n)?'+u6+' :: '+u0)
              if bk == '0':
                 casa()
              if bk == 'y' or bk == 'Y':
                 print(n2+'Fazendo Backup dos usuarios .. aguarde.'+u0)
                 if os.path.isfile('/etc/setup/backup/users') == True:
                    system('rm -rf /etc/setup/backup')

                 system('mkdir /etc/setup/backup')
                 sleep(1)
                 system('touch /etc/setup/backup/0dir')
                 sleep(1)
                 system('cp /etc/setup/users /etc/setup/backup')
                 sleep(1)
                 system('cp -r /etc/setup/bkp /etc/setup/backup')
                 sleep(1)
                 system('touch /etc/setup/backup/bkp/0dir')
                 sleep(1)
                 system('cp /etc/setup/ario /etc/setup/backup')
                 print(u3+'\nConcluido. Backup feito em /etc/setup/backup.\n'+u0)
                 sleep(1)
                 case()
                 
              if bk == 'n' or bk == 'N':
                 case()
           if w == '15':
              __sbm__ = u6+'\n1) = Restaurar usuario do Backup\n'\
                          +'2) = Deletar um usuario do Backup\n'\
                          +'3) = Deletar Todos os usuarios\n'\
                          +'4) = Deletar Backup\n'\
                          +'0) = Home\n' + u0
                          
              print(__sbm__)
 
              def mopt():
                  sbm = input(u6+' :: '+u0)
                  if sbm == '0':
                     casa()

                  if sbm == '1':
                     def userrs():
                         if os.path.isfile('/etc/setup/backup/users') == False:
                           print(n1+'Error: Voce ainda nao tem um Backup.'+u0)
                           sleep(2)
                           casa()
                           
                         print(u3+'Usuarios no Backup:'+u6)
                         system('cat /etc/setup/backup/ario')
                         print('\n'+u0)
                         
                         us = input(u6+'Qual usuario voce Deseja Restaurar :: '+u0)
                         if us == '0':
                            casa()
                            
                         if os.path.isfile('/etc/setup/backup/bkp/%s' %(us)) == False:
                            print(n1+'Error: o usuario %s nao se encontra no Backup.' %(us)+u0)
                            userrs()
                         system('grep -v ^'+us+' /etc/setup/backup/ario\
                          > /tmp/bkp; cat /tmp/bkp > /etc/setup/backup/ario')
                         system('''echo
                         usr="$(cat /etc/setup/backup/bkp/'''+us+''' | cut -d' ' -f1)"
                         lm="$(cat /etc/setup/backup/bkp/'''+us+''' | cut -d' ' -f2)"
                         pas="$(cat /etc/setup/backup/bkp/'''+us+''' | cut -d' ' -f3)"
                         dx="$(cat /etc/setup/backup/bkp/'''+us+''' | cut -d' ' -f5)"
                         d=$(date '+%C%y-%m-%d' -d '+'$dx' days')
                         da=$(date '+%d/%m/%Y' -d '+'$dx' days')
                         useradd -M -s /bin/false $usr -e $d
                         (echo "$pas" ; echo "$pas" ) |passwd $usr > /dev/null 2>/dev/null
                         echo '\033[33mConcluido ..\033[32m'
                         echo 'Usuario:' $usr
                         echo 'Senha:' $pas
                         echo 'Maxlogin:' $lm
                         echo '\033[33mRestaurado.\033[m'
                         echo '\033[32mExpira:' $da
                         echo $usr $lm >> /root/usuarios.db
                         echo $usr' - maxlogins '$lm > /etc/setup/limite/$usr
                         echo $usr' - maxlogins '$lm >> /etc/security/limits.conf
                         grep -v ^$usr[[:space:]] /etc/setup/users\
                          > /tmp/bkp; cat /tmp/bkp > /etc/setup/users
                         grep -v ^$usr[[:space:]] /etc/setup/backup/users\
                          > /tmp/bkp; cat /tmp/bkp > /etc/setup/backup/users
                          
                         rm -rf /etc/setup/bkp/$usr
                         echo $pas > /etc/setup/senhas/$usr
                         echo $usr $lm $pas $d $dx >> /etc/setup/users
                         echo $usr $lm $pas $d $dx > /etc/setup/bkp/$usr''')
                                
                         system('rm -rf /etc/setup/backup/bkp/%s' %(us))
                         sleep(1)
                         casa()
                         
                     userrs()
                  if sbm == '2':
                     def bacf():
                         if os.path.isfile('/etc/setup/backup/users') == False:
                           print(n1+'Error: Voce ainda nao tem um Backup.'+u0)
                           sleep(3)
                           casa()
                           
                         print(u3+'Usuarios no Backup:'+u6)
                         system('cat /etc/setup/backup/ario')
                         print('\n'+u0)
                         
                         rtb = input(u6+'Que usuario voce quer tirar do Backup :: '+u0)
                         if rtb == '0':
                            casa()
                         if os.path.isfile('/etc/setup/backup/bkp/%s' %(rtb)) == False:
                            print(n1+'Error: o usuario %s nao se encontra no Backup.'%(rtb)+u0)
                            bacf()
                         system('rm -rf /etc/setup/backup/bkp/'+rtb)
                         system('grep -v ^'+rtb+'[[:space:]] /etc/setup/backup/users\
                          > /tmp/bkp; cat /tmp/bkp > /etc/setup/backup/users')
                         system('grep -v ^'+rtb+'[[:space:]] /etc/setup/backup/ario\
                          > /tmp/bkp; cat /tmp/bkp > /etc/setup/backup/ario')
                          
                         print(u3+'Concluido. o usuario '+rtb+' foi deletado'\
                               +' do Backup.'+u0)
                         sleep(2)
                         casa()
                         
                     bacf()
                  if sbm == '3':
                     print(u1+'\nEsta funcao Deletarar todos os usuarios ..\n'\
                           +'ativos e criados por este progama.'+u0)
                     dlt = input(u3+'Deseja deletar mesmo assim (y/n)?'+u6+' :: '+u0)
                     if dlt == '0':
                        casa()
                        
                     if dlt == 'y' or dlt == 'Y':
                        if os.path.isfile('/etc/setup/limite/lm') == False:
                           print(n1+'Error: Voce ainda nao fez usuarios com este script.'+u0)
                           sleep(2)
                           casa()
                           
                        up = input(u3+'Voce fez, ou Deseja fazer o Backup futuramente\n'\
                                  +'de algum desses usuarios. (y/n)?'+u6+' :: '+u0)
         
                        system('rm -rf /etc/setup/limite && mkdir /etc/setup/limite')
                        system('touch /etc/setup/limite/lm')
                        if up == 'y' or up == 'Y':
                           print(n2+'Certo .. Algumas Informacoes ficaram Preservadas.'+u0)
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
                        
                        print(u3+'\nConcluido. Todos os usuarios foram excluidos.'+u0)
                        sleep(2)
                        casa()
                        
                     if dlt == 'n' or dlt == 'N':
                        casa()
                        
                  if sbm == '4':
                     print(n1+'Esta funcao excluirar todos os usuarios\n'\
                           +'que estao no Backup. Deseja continuar.'+u0)
                     def rtu():
                         bex = input(u3+'      ... (y/n)?'+u6+' :: '+u0)
                         if bex == '0':
                            casa()
                         if bex == 'y' or bex == 'Y':
                            system('rm -rf /etc/setup/backup')
                         if bex == 'n' or bex == 'N':
                            casa()
                         print(u3+'Concluido. Backup foi Deletado.'+u0)
                         sleep(2)
                         casa()
                         
                         if bex != 'n' or bex != 'N' or bex != 'y' or bex != 'Y':
                            rtu()
                     rtu()
                  if sbm != '1' or sbm != '2' or sbm != '0' or sbm != '4' or sbm != '3':
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
              print(__ADD__+'\n')
              case()

           if w == '10':
              print(n2+'Monitor do Sistema ..'+u0)
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
                      DIST=`awk -F "PRETTY_NAME=" '{print$2}' /etc/os-release | tr -d '\n"'`
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
               |grep "model name" |uniq |awk -F : {'print$2'})''')
              system('''echo '\033[32mNucleos:' $(cat /proc/cpuinfo |grep "cpu cores"\
               |uniq |awk -F : {'print$2'})''')
              system('''arq=$(uname -m)\necho '\033[92mArquitetura\033[32m:' $arq''')
              system('''kernel=$(uname -r)\necho '\033[32mKernel\033[92m:' $kernel''')
              system('''serv=$(cat /etc/resolv.conf | sed '1 d' | awk '{print$2}')\n
                     echo '\033[92mServidor DNS\033[32m:' $serv''')
              system('''host=$(hostname)\necho '\033[32mHostName\033[92m:' $host''')
              system('''internal=$(hostname -i)\necho '\033[92mIP Interno\033[32m:'\
                $internal''')
              print(u2+'IP Externo: '+n2+'%s' %(__ip__)+u0)
              print(n2+'Memoria Ram'+u2)
              system('''echo 'Total:' $(free -h |grep -i mem |awk {'print$2'})''')
              system('''echo 'Usada:' $(free -h |grep -i mem |awk {'print$3'})''')
              system('''echo 'Livre:' $(free -h |grep -i mem |awk {'print$4'})''')
              print(n2+'Swap ..'+u2)
              system('''echo 'Total:' $(free -h |grep -i swap |awk {'print$2'})''')
              system('''echo 'Usada:' $(free -h |grep -i swap |awk {'print$3'})''')
              system('''echo 'Livre:' $(free -h |grep -i swap |awk {'print$4'})''')
              print(n2+'Usuarios Conectados:'+u0)
              if os.path.isfile('/root/usuarios.db') == False:
                 system('touch /root/usuarios.db')
                 
              system('''database='/root/usuarios.db'
              while read us
              do
                usr="$(echo $us | cut -d' ' -f1)"
                ss1="$(echo $us | cut -d' ' -f2)"
                ps x | grep [[:space:]]$usr[[:space:]] | grep -v grep | \
                grep -v pts > /tmp/tmp4
                printf '\033[32m%-35s%s\n' $usr\033[92m $(cat /tmp/tmp4\
                 | wc -l)\033[32m/\033[31m$ss1; tput sgr0
              done < $database
              rm -rf /tmp/tmp4''')
              system('''load=$(top -n 1 -b | grep 'load average:'\
               | awk '{print$11 $12 $13 $14}')\n
                     echo '\033[92mCarga Media\033[92m:' $load''')
              system('''time=$(uptime | awk '{print$3,$4}' | cut -f1 -d,)\n
                     echo '\033[32mTempo de Atividade\033[92m:' $time''')
              case()

           if w == '1' or w == '01':
              print(u3+'Configurando servidor. Aguarde ..'+u0)
              sleep(2)
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
                 system('''echo 'Ola, Neste arquivo e armazenado todas as senhas '''\
                       +'''criadas por este progama.' > /etc/setup/senhas/except''')
                       
              if os.path.isfile('/etc/setup/users') == False:
                 system('touch /etc/setup/users')
                 system('touch /etc/setup/ario')
                 system('mkdir /etc/setup/bkp')
              if os.path.isfile('/etc/setup/limite/lm') == False:
                 system('mkdir /etc/setup/limite')
                 system('touch /etc/setup/limite/lm')
              if os.path.isfile('/usr/bin/dpkg') == True:
                 system('dpkg --configure -a')
              if t == True:
                 system('apt-get autoremove ssh -y 1> /dev/null')
                 system('apt-get update && apt-get install ssh -y 1> /dev/null')
              if d == True:
                 system('apt-get autoremove squid -y 1> /dev/null')
              if s == True:
                 system('apt-get autoremove squid3 -y 1> /dev/null')

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
                 print(u3+'Configurando Portas SQUID IP: '+n2+'%s' %(__ip__)+u0)
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
                               
                    print(u2+'Portas SQUID: 80, 8080, 8799, 3128 Ativadas.\n'+u0)
                    sleep(2)
                    
              else:
                 system('rm -rf /etc/squid3/squid.conf')
                 system('touch /etc/squid3/squid.conf')
                 print(u3+'Configurando Portas SQUID3 IP: '+n2+'%s' %(__ip__)+u0)
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
                    
                    print(u2+'Portas SQUID3: 80, 8080, 8799, 3128 Ativadas.\n'+u0)
                    sleep(2)
                    
              print(u3+'Configurando Portas SSH 22/443.'+u0)
              sleep(2)
              for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config', inplace=1)):
                  sys.stdout.write(line.replace('Port 22', 'Port 22\nPort 443'))
              print(u2+'Reiniciando Servidor SSH.\033[m')
              system('cd /etc && service ssh restart')
              sleep(2)
              if os.path.isfile('/etc/squid/squid.conf') == True:
                 sleep(2)
                 print(u2+'Reiniciando Servidor SQUID.'+u0)
                 system('cd /etc && service squid restart')
                 sleep(2)
                 print(u3+'Portas SSH[22/443]SQUID Rodando 100%'+u0)
              else:
                 print(u2+'Reiniciando Servidor SQUID3.'+u0)
                 system('cd /etc && service squid3 restart')
                 sleep(2)
                 print(u3+'Portas SSH[22/443]SQUID3 Rodando 100%'+u0)
              sleep(3)
              print(n2+'Concluido. Portas 22/443/80/8080/8799/3128 100% ativas ..'+u0)
              print(u2+'Crie um usuario e teste.'+u0)
              sleep(2)
              casa()
              
           if w == '2' or w == '02':
              print (u1+'Esta funcao exluirar todas as modificacoes\n'\
                    +'feitas por ZWDConfig. Incluindo usuarios, Squid, Banner\n'\
                    +'e porta ssh 443.'+u0)
              rc = input(u3+'Deseja Remover. (y/n)?'+u6+' :: '+u0)
              if rc == 'y' or rc == 'Y':
                 print(u3+'Removendo alteracoes. Aguarde ..'+u0)
                 sleep(2)
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
                 print(u3+'\nConcluido.. Pode reconfigurar a sua vps com um script da\n'\
                       +'sua Preferencia. Desculpe desapontalo(a).'+u0)
                 sleep(2)
                 casa()
                 
              if rc == 'n' or rc == 'N':
                 casa()
              if rc == '0':
                 print(u1+'\nGoing out ..'+u0)
                 sleep(2)
                 exit()
                 
           if w == '3' or w == '03':
              if os.path.isfile('/etc/squid3/domains/domain') == False\
               or os.path.isfile('/etc/squid/domains/domain') == False:
                 if os.path.isfile('/etc/squid/squid.conf') == True:
                    system('touch /etc/squid/domains/domain')
                 else:
                    system('touch /etc/squid3/domains/domain')
              print(u3+'Domains do arquivo:'+u6)
              if os.path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
              print('\n'+u0)
              def dom():
                  do = input(u6+'Adicionar Domain :: '+u0)
                  if do == '0':
                     if os.path.isfile('/etc/squid/squid.conf') == True:
                        system('cd /etc && service squid restart')
                     else:
                        system('cd /etc && service squid3 restart')
                     casa()
                  if os.path.isfile('/etc/squid3/domains/domain') == True:
                     if os.path.isfile('/etc/squid3/domains/%s' %(do)) == True:
                        print(u1+'Error: o domain %s ja existe.' %(do)+u0)
                        dom()
                     system('''echo '%s' >> /etc/squid3/domains/domain''' % (do))
                     system('''touch /etc/squid3/domains/%s''' % (do))
                     print(u3+'Domain: %s Adicionado. [0] Para Home.' % (do)+u0)
                     dom()
                  else:
                     if os.path.isfile('/etc/squid/domains/%s' %(do)) == True:
                        print(n1+'Error: o domain %s ja existe.' %(do)+u0)
                        dom()
                     system('''echo '%s' >> /etc/squid/domains/domain''' % (do))
                     system('''touch /etc/squid/domains/%s''' % (do))
                     print(u3+'Domain: %s Adicionado. [0] Para Home.' % (do)+u0)
                     dom()
              dom()
 
           if w == '4' or w == '04':
              if os.path.isfile('/etc/squid/domains/domain') == False\
               or os.path.isfile('/etc/squid3/domains/domain') == False:
                 if os.path.isfile('/etc/squid3/squid.conf') == True:
                    system('touch /etc/squid3/domains/domain')
                 else:
                    system('touch /etc/squid/domains/domain')
              print(u3+'Domains do arquivo:'+u6)
              if os.path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
                 
              print('\n'+u0)
              def delet():
                  de = input(u6+'Deletar Domain :: '+u0)
                  if de == '0':
                     if os.path.isfile('/etc/squid/squid.conf') == True:
                        system('cd /etc && service squid restart')
                     else:
                        system('cd /etc && service squid3 restart')
                     casa()
                     
                  if os.path.isfile('/etc/squid/domains/domain') == True:
                     if os.path.isfile('/etc/squid/domains/%s' %(de)) == False:
                        print(u1+'Erro: o domain %s nao existe.' %(de)+u0)
                        delet()
                     system('rm -rf /etc/squid/domains/%s' %(de))
                     for i, line in enumerate(fileinput.input('/etc/squid/domains/domain',\
                      inplace=1)):
                         sys.stdout.write(line.replace(de+'\n', ''))
                     sleep(1)
                     print(u3+'Domain: %s Excluido. [0] Para Home.' % (de)+u0)
                     delet()
                  else:
                     if os.path.isfile('/etc/squid3/domains/%s' %(de)) == False:
                        print(n1+'Error: o domain %s nao existe.' %(de)+u0)
                        delet()
                     system('rm -rf /etc/squid3/domains/%s' %(de))
                     for i, line in enumerate(fileinput.input('/etc/squid3/domains/domain',\
                      inplace=1)):
                         sys.stdout.write(line.replace(de+'\n', ''))
                     sleep(1)
                     print(u3+'Domain: %s Excluido.. [0] Para Home.' % (de)+u0)
                     delet()
              delet()
                     
           if w == '5' or w == '05':
              if os.path.isfile('/etc/Banner') == False:
                 system('touch /etc/Banner')
              if os.path.isfile('/etc/issue.net') == True:
                 system('rm -rf /etc/issue.net')
                 for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config', inplace=1)):
                     sys.stdout.write(line.replace('#Banner /etc/issue.net',\
                      'Banner /etc/Banner'))
                      
              nb = input(u6+'Adicionar ao Banner :: '+u0)
              system('''echo '%s' > /etc/Banner''' % (nb))
              system('cd /etc && service ssh restart')
              print(u2+'Banner: '+n2+'%s' % (nb)+u2+'\nAdicionado com Sucesso.'+u0)
              sleep(2)
              case()
              
           if w == '6' or w == '06':
              rb = input(u3+'Deseja deletar o Banner por completo. (y/n)?'+u6+' :: '+u0)
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
                    print(u3+'Concluido .. Banner Retirado.'+u0)
                    sleep(2)
                    casa()
                    
              if rb == 'n' or rb == 'N':
                 casa()
                 
           if w == '7' or w == '07':
              if os.path.isfile('/etc/setup/senhas/except') == False:
                 system('touch /etc/setup/senhas/except')
              def user():
                  n = input(u6+'Nome do usuario :: '+u0)
                  if os.path.isfile('/root/usuarios.db') == False:
                     system('touch /root/usuarios.db')
                  if os.path.isfile('/etc/setup/senhas/%s' %(n)) == True:
                     print(u1+'Error: o usuario %s ja existe.' %(n)+u0)
                     user()
                  sn = input(u6+'Senha Para '+n+' :: '+u0)
                  dx = input(u6+'Quantos dias '+n+' deve durar :: '+u0)
                  lm = input(u6+'Maximo de conexoes simultaneas :: '+u0)
                  system("d=$(date '+%C%y-%m-%d' -d '+"+dx+" days')\
                         \nda=$(date '+%d/%m/%Y' -d '+"+dx+" days')\
                         \nuseradd -M -s /bin/false "+n+" -e $d\
                         \necho '\033[33m\nConcluido .. usuario criado.'\n\
                         \necho '\033[32mUsuario:\033[92m "+n+"'\
                         \necho '\033[32mSenha:\033[92m "+sn+"'\
                         \necho '\033[32mExpira:\033[92m '$da'\n\033[m'\
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
              
           if w == '9' or w == '09':
              def dex():
                  df = input(u6+'Que usuario voce deseja deletar :: '+u0)
                  if df == '0':
                     casa()
                     
                  if os.path.isfile('/etc/setup/senhas/'+df) == False:
                     print(u1+'Error: o usuario %s nao existe.. ou nao '%(df)\
                          +'foi criado por este progama.'+u0)
                     dex()
                  cup = input(u3+'Deseja fazer Backup de '+df\
                             +' futuramente. (y/n)?'+u6+' :: '+u0)
                  if cup == 'N' or cup == 'n':
                     system('rm -rf /etc/setup/bkp/%s' %(df))
                     system('grep -v ^'+df+'[[:space:]] /etc/setup/users\
                      > /tmp/bkp; cat /tmp/bkp > /etc/setup/users')
                  if cup == 'Y' or cup == 'y':
                     print(n2+'Certo? informacoes do usuario Guardadas.'+u0)
                  for i, line in enumerate(fileinput.input('/etc/setup/ario', inplace=1)):
                        sys.stdout.write(line.replace(df, ''))
                  system('userdel --force %s > /dev/null 2>/dev/null' %(df))
                  system('rm -rf /etc/setup/senhas/%s' %(df))
                  system('grep -v ^'+df+'[[:space:]] /etc/security/limits.conf\
                   > /tmp/mite; cat /tmp/mite > /etc/security/limits.conf')
                  system('grep -v ^'+df+'[[:space:]] /root/usuarios.db\
                   > /tmp/usdb; cat /tmp/usdb > /root/usuarios.db')
                  system('rm -rf /etc/setup/limite/'+df)
                  print(u3+'Usuario %s excluido com exito. [0] Para Home.' %(df)+u0)
                  sleep(2)
                  dex()
              dex()
              
           if w == '8' or w == '08':
              main = u6+'\n1) = Mudar senha\n'\
                    +'2) = Mudar Data de expiracao\n'\
                    +'3) = Mudar limite de logins\n'\
                    +'4) = Mudar Nome de usuario\n'\
                    +'0) = Home\n\n\033[m'
              print(main)
              
              def rdf():
                   rd = input(u6+'Que usuario voce deseja redefinir :: '+u0)
                   if rd == '0':
                      casa()
                      
                   if os.path.isfile('/etc/setup/senhas/%s' %(rd)) == False:
                      print(u1+'\nError: o usuario %s nao existe ..' %(rd)+u0)
                      rdf()
                   md = input(u6+' ::'+n6+' ')
                   if md == '0':
                      casa()
                      
                   if md == '1':
                      sna = input(u6+'\nNova senha para '+rd+' :: '+u0)
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
                      print(u3+'Concluido. Nova senha aplicada para %s' %(rd)+u0)
                      sleep(2)
                      casa()
                      
                   if md == '2':
                      dt = input(u6+'Quantos dias '+rd+' deve durar :: '+u0)
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
                      casa()
                      
                   if md == '3':
                      mt = input(u6+'Qual o novo limite para '+rd+' :: '+u0)
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
                      print(u3+'Concluido. Novo limite de '+mt+' conexoes aplicado'\
                            +' para '+rd+'.'+u0)
                      sleep(2)
                      casa()
                      
                   if md == '4':
                      no = input(u6+'Qual o novo nome para '+rd+' :: '+u0)
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
                             
                      print(u3+'Concluido. '+rd+' Agora se chama '+no+'.'+u0)
                      sleep(2)
                      casa()
                      
              rdf()
           if w == '0':
              print(u1+'Going out ..'+u0)
              sleep(2)
              exit()
        else:
            w = input(u6+' :: '+u0)

  except EOFError:
     ex = input(u3+'Deseja sair do progama (y/n)?'+u6+' :: '+u0)
     if ex == 'y' or ex == 'Y':
        print(u1+'\nGoing out ..'+u0)
        sleep(2)
        exit()
     if ex == 'n' or ex == 'N':
        print(u6+'{ Home }'+u0)
        case()
  except KeyboardInterrupt:
     print(u1+'\nGoing out ..'+u0)
     sleep(2)
     exit()
if __name__ == '__main__':
   case()