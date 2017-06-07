#!usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
__version__ = '0.9'
__copyright__ = 'Copyright (c) 2017 @nZwdeff\n'# All Rights Reserved.

# Github https://github.com/Xdwnff-04x/VPS-Config
# Este progama foi feito pra configurar sua VPS perfeitamente.
# Sobre: este script edita no meio do arquivo /etc/ssh/sshd_config
# Substituindo Port 22 por 22 e 443. sem precisar deletar ou escrever
# no final do arquivo, evitando erros futuros.
# Para configurar o squid ele indentifica se á pasta squid e squid ou squid3
# configurando assim qualquer VPS.

# Aviso: este script não é um Gerenciador de VPS..
# foi feito somente para configurala.

"""
 Copyright 2017 Config of copyright .Zwdeff

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

from os import *
from sys import *
from time import *
from urllib.request import *
import fileinput
import sys, re

f0 = '\033[90m'
f1 = '\033[91m'
f2 = '\033[92m'
f3 = '\033[93m'
f4 = '\033[94m'
f5 = '\033[95m'
f6 = '\033[36m'
f7 = '\033[97m'

if sys.version_info.major < 3:
   print (f1+'Erro: Progama suportado somente em Python3\033[m')
   sleep(2)
   exit()

v = sys.version_info.major
H = strftime('%d/%m/%Y %H:%M:%S')
print ('Conectando .. via python%s /%s' % (v,H))
sleep(1)
url = str(urlopen('http://ipv4.icanhazip.com/').read())
__ip__ = re.compile(r'(\d+\.\d+\.\d+\.\d+)').search(url).group()

__main__ = '\n\033[36m1\033[92m) = Configurar VPS\n\033[m'\
          +'\033[36m2\033[92m) = Desconfigurar /SSH/SQUID3\n\033[m'\
          +'\033[36m3\033[92m) = Adicionar Domain\n\033[m'\
          +'\033[36m4\033[92m) = Remover Domain\n\033[m'\
          +'\033[36m5\033[92m) = Adicionar Banner\n\033[m'\
          +'\033[36m6\033[92m) = Remover Banner\n\033[m'\
          +'\033[36m7\033[92m) = Adicionar usuario\n\033[m'\
          +'\033[36m8\033[92m) = Remover usuario\n\033[m'\
          +'\033[36m0\033[92m) = Sair\n\n\n\033[m'
# 1 = Beta.
# 2 = Beta.
# 3 = Beta.
# 4 = Beta.
# 5 = Beta.
# 6 = Beta.
# 7 = Beta.
# 8 = Beta.
# 0 = True.
__info__ = f2+'Author:\033[36m %s\n\033[m' %(__author__)\
          +f2+'Version:\033[36m %s\033[m\n' %(__version__)
__Banner__ = f2+'^-------------------------------------_\n'\
               +' {= Config VPS /SSH/SQUID3 =}\n\033[m'
print (__Banner__)
print (__info__)
print ('\033[92mIP:\033[96m %s\033[m' %(__ip__))

def case():
  try:
     print (__main__)
     
     w = input(f6+' :: _\033[92m'+' ')
     while w != '1' or w != '2' or w != '3' or w != '4' or w != '5'\
      or w != '6' or w != '7' or w != '8' or w != '0':
        if w == '1' or w == '2' or w == '3' or w == '4' or w == '5' or w == '6'\
         or w == '7' or w == '8' or w == '0':          
           if w == '1':
              t = path.isfile('/usr/bin/ssh')
              s = path.isfile('/usr/sbin/squid3')
              if path.isfile('/etc/setup/senhas/except') == False:
                 system('touch /etc/setup/senhas/except')
                 system('''echo 'Olá anqui fica armazenado todas as senhas\
                  criadas por este progama.' > /etc/setup/senhas/except''')
              if t == True:
                 system('apt-get autoremove ssh -y')
                 system('apt-get update && apt-get install ssh -y')
              if s == True:
                 system('apt-get autoremove squid3 -y')
                 
              system('apt-get install squid3 -y')
              sleep(2)
  
              if path.isfile('/etc/squid/squid.conf') == False\
               and path.isfile('/etc/squid3/squid.conf') == False:
                 print (f1+'Erro: Ocorreu um erro na instalacao do squid3.\033[m')
                 exit()
              if path.isfile('/etc/squid/squid.conf') == True:
                 print (f2+'Configurando Portas SQUID IP:\033[96m %s\033[m' %(__ip__))
                 sleep(2)
                 if path.isfile('/etc/squid/domains') == False:
                    system('touch /etc/squid/domains')
                    system('''echo '.vivo.com.br\n.claro.com.br\n.oi.com.br\
                           \n.tim.com.br' >> /etc/squid/domains/domain''')
                    system('touch /etc/squid/domains/.claro.com.br')
                    system('touch /etc/squid/domains/.vivo.com.br')
                    system('touch /etc/squid/domains/.tim.com.br')
                    system('touch /etc/squid/domains/.oi.com.br')
                    system('rm -rf /etc/squid/squid.conf')
                    system('touch /etc/squid/squid.conf')
                    system('''echo '# ACL DE CONEXÃO\n\nacl accept src '''+__ip__\
                          +'''\nacl ip url_regex -i '''+__ip__\
                          +'''\nacl payload dstdomain -i "/etc/squid3/domains/domain"\n'\
                            > /etc/squid3/squid.conf''')
                    system('''echo '# PORTAS DE ACESSO\n\nhttp_port 80\nhttp_port 8080\
                           \nhttp_port 8799\nhttp_port 3128\n\n# Nome do servidor\
                           \n\nvisible_hname ZWDConfig\n\n# ACCEPT ACL\
                           \n\nhttp_access allow accept\nhttp_access allow ip\
                           \nhttp_access allow payload\nhttp_access deny all'\
                            >> /etc/squid/squid.conf''')
                               
                    print (f2+'Portas SQUID: 80, 8080, 8799, 3128 Ativadas.\n\033[m')
                    sleep(2)
              else:
                 print (f2+'Configurando Portas SQUID3 IP:\033[96m %s\033[m' %(__ip__))
                 sleep(2)
                 if path.isfile('/etc/squid3/domains') == False:
                    system('touch /etc/squid3/domains')
                    system('''echo '.vivo.com.br\n.claro.com.br\n.oi.com.br\
                           \n.tim.com.br' >> /etc/squid3/domains/domain''')
                    system('touch /etc/squid3/domains/.claro.com.br')
                    system('touch /etc/squid3/domains/.vivo.com.br')
                    system('touch /etc/squid3/domains/.tim.com.br')
                    system('touch /etc/squid3/domains/.oi.com.br')
                    system('rm -rf /etc/squid3/squid.conf')
                    system('touch /etc/squid3/squid.conf')
                    system('''echo '# ACL DE CONEXÃO\n\nacl accept src '''+__ip__\
                          +'''\nacl ip url_regex -i '''+__ip__\
                          +'''\nacl payload dstdomain -i "/etc/squid3/domains/domain"\n'\
                            > /etc/squid3/squid.conf''')
                    system('''echo '# PORTAS DE ACESSO\n\nhttp_port 80\nhttp_port 8080\
                           \nhttp_port 8799\nhttp_port 3128\n\n# Nome do servidor\
                           \n\nvisible_hname ZWDConfig\n\n# ACCEPT ACL\
                           \n\nhttp_access allow accept\nhttp_access allow ip\
                           \nhttp_access allow payload\nhttp_access deny all'\
                            >> /etc/squid3/squid.conf''')
                               
                    print (f2+'Portas SQUID3: 80, 8080, 8799, 3128 Ativadas.\n\033[m')
                    sleep(2)
              print (f2+'Configurando Portas SSH.\033[m')
              sleep(2)
              for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config', inplace=1)):
                  sys.stdout.write(line.replace('Port 22', 'Port 22\nPort 443'))
                  system('''echo '\nPort 22' >> /etc/ssh/sshd_config''')
              print (f2+'Reiniciando Servidor SSH.\033[m')
              system('cd /etc && service ssh restart')
 
              if path.isfile('/etc/squid/squid.conf') == True:
                 sleep(2)
                 print (f2+'Reiniciando Servidor SQUID.\033[m')
                 system('cd /etc && service squid restart')
                 print (f2+'Portas SSH[22/443]SQUID Rodando 100%n\n\033[m')
              else:
                 print (f2+'Reiniciando Servidor SQUID3.\033[m')
                 system('cd /etc && service squid3 restart')
                 print (f2+'Portas SSH[22/443]SQUID3 Rodando 100%\n\033[m')
              sleep(1)
              print (f2+'Concluido. Portas 22/443/80/8080/8799/3128 100% ativas ..\033[m')
              print (f2+'Crie um usuario e teste.\033[m')
              sleep(2)
              case()
           if w == '2':
              rc = input(f2+' Deseja Remover todas as alteracoes '\
                        +'feitas ..\n por este script. [y/n]\n\033[96m :: _\033[92m'+' ')
              if rc == 'y' or rc == 'Y':
                 t = path.isfile('/usr/bin/ssh')
                 s = path.isfile('/usr/sbin/squid3')
                 if path.isfile('/etc/setup/senhas/except') == True:
                    system('rm -rf /etc/setup')
                 if t == True:
                    system('apt-get autoremove ssh -y')
                    system('apt-get update && apt-get install ssh -y')
                 if s == True:
                    system('apt-get autoremove squid3 -y')
                 print ('\nConcluido.. Pode reconfigurar sua vps com um script da \n'\
                       +'sua Preferencia. Desculpe desapontalo(a).\033[m')
                 sleep(2)
                 case()
              if rc == 'n' or rc == 'N':
                case()
              if rc == '0':
                 print (f1+'\nSaindo..\033[m')
                 sleep(2)
                 exit()
           if w == '3':
              if path.isfile('/etc/squid3/domains/domain') == False\
               or path.isfile('/etc/squid/domains/domain') == False:
                 if path.isfile('/etc/squid/squid.conf') == True:
                    system('touch /etc/squid/domains/domain')
                 else:
                    system('touch /etc/squid3/domains/domain')
              print (f2+'Domains do arquivo:\033[36m')
              if path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
              def dom():
                  do = input(f2+'\nAdicionar Domain\033[96m :: _\033[92m'+' ')
                  if do == '0':
                     case()
                  if path.isfile('/etc/squid3/domains/domain') == True:
                     if path.isfile('/etc/squid3/domains/%s' %(do)) == True:
                        print (f1+'Erro: o domain %s ja existe.\033[m' %(do))
                        dom()
                     system('''echo '%s' >> /etc/squid3/domains/domain''' % (do))
                     system('''echo '%s' >> /etc/squid3/domains''' % (do))
                     system('cd /etc && service squid3 restart')
                     print (f2+'Domain: %s Adicionado [0] Para Home.' % (do))
                     dom()
                  else:
                     if path.isfile('/etc/squid/domains/%s' %(do)) == True:
                        print (f1+'Erro: o domain %s ja existe.\033[m' %(do))
                        dom()
                     system('''echo '%s' >> /etc/squid/domains/domain''' % (do))
                     system('''echo '%s' >> /etc/squid/domains''' % (do))
                     system('cd /etc && service squid restart')
                     print (f2+'Domain: %s Adicionado.. [0] Para Home.' % (do))
                     dom()
              dom()
           if w == '4':
              if path.isfile('/etc/squid/domains/domain') == False:
                 system('touch /etc/squid/domains/domain')
              if path.isfile('/etc/squid3/domains/domain') == False:
                 system('touch /etc/squid3/domains/domain')
              print (f2+'Domains do arquivo:\033[36m')
              if path.isfile('/etc/squid/domains/domain') == True:
                 system('cat /etc/squid/domains/domain')
              else:
                 system('cat /etc/squid3/domains/domain')
              def delet():
                  de = input(f2+'\nDeletar Domain\033[96m :: _\033[92m'+' ')
                  if de == '0':
                     case()
                  if path.isfile('/etc/squid/domains/domain') == True:
                     if path.isfile('/etc/squid/domains/%s' %(de)) == False:
                        print (f1+'Erro: o domain %s nao existe.\033[m' %(de))
                        delet()
                     system('rm -rf /etc/squid/domains/%s' %(de))
                     for i, line in enumerate(fileinput.input('/etc/squid/domains/domain',\
                      inplace=1)):
                         sys.stdout.write(line.replace(de+'\n', ''))
                     sleep(2)
                     system('cd /etc && service squid restart')
                     print (f2+'\nDomain: %s Excluido. [0] Para Home.\033[m' % (de))
                     delet()
                  else:
                     if path.isfile('/etc/squid3/domains/%s' %(de)) == False:
                        print (f1+'Erro: o domain %s nao existe.\033[m' %(de))
                        delet()
                     system('rm -rf /etc/squid3/domains/%s' %(de))
                     for i, line in enumerate(fileinput.input('/etc/squid3/domains',\
                      inplace=1)):
                         sys.stdout.write(line.replace(de+'\n', ''))
                     sleep(2)
                     system('cd /etc && service squid3 restart')
                     print (f2+'\nDomain: %s Excluido.. [0] Para Home.\033[m' % (de))
                     delet()
                     
           if w == '5':
              if path.isfile('/etc/Banner') == False:
                 system('touch /etc/Banner')
              if path.isfile('/etc/issue.net') == True:
                 system('rm -rf /etc/issue.net')
                 for i, line in enumerate(fileinput.input('/etc/ssh/sshd_config', inplace=1)):
                     sys.stdout.write(line.replace('#Banner /etc/issue.net',\
                      'Banner /etc/Banner'))
              nb = input(f3+'Adicionar mensagem\033[96m :: _ '+' ')
              system('''echo '%s' > /etc/Banner''' % (nb))
              system('cd /etc && service ssh restart')
              print (f2+'Banner:\033[97m %s \033[92m\nAdicionado com Sucesso.\033[m' % (nb))
              sleep(2)
              case()
              
           if w == '6':
              rb = input(f2+' Deseja deletar o Banner por completo .. '\
                        +'\n ficarar como de fabrica. [y/n]\n\033[96m :: _\033[92m'+' ')
              if rb == 'Y' or rb == 'y':
                 if path.isfile('/etc/Banner') == True:
                    system('rm -rf /etc/Banner')
                 if path.isfile('/etc/issue.net') == False:
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
              if path.isfile('/etc/setup/senhas/except') == False:
                 system('touch /etc/setup/senhas/except')
              def user():
                  n = input(f2+'Nome do usuario\033[96m :: _\033[92m'+' ')
                  if path.isfile('/etc/setup/senhas/%s') == True:
                     print (f1+'Erro: o usuario %s ja existe.\033[m' %(n))
                     user()
                  sn = input(f2+'Senha Para '+n+'\033[96m :: _\033[92m'+' ')
                  dx = input(f2+'Quantos dias '+n\
                             +' deve durar\033[96m :: _\033[92m'+' ')
                  system("d=$(date '+%C%y-%m-%d' -d '+"+dx+" days')\
                         \nda=$(date '+%d/%m/%Y' -d '+"+dx+" days')\
                         \nuseradd -M -s /bin/false "+n+" -e $d -p "+sn+"\
                         \necho 'Concluido .. usuario criado.'\n\
                         \necho 'Usuario: "+n+"\n\
                         \necho 'Senha: "+sn+"\n\
                         \necho 'Expira: $da\n\
                         \necho '"+sn+"' > /etc/setup/senhas/"+u)
                  case()
              user()
              
           if w == '8':
              def dex():
                  df = input(f2+'Qual usuario voce deseja deletar.\033[96m :: _\033[92m'+' ')
                  if df == '0':
                     case()
                  if path.isfile('/etc/setup/senhas/%s' %(df)) == False:
                     print (f1+'Erro: o usuario %s nao existe.\033[m' %(df))
                     dex()
                  system('userdel --force %s > /dev/null 2>/dev/null' %(df))
                  system('rm -rf /etc/setup/senhas/%s' %(df))
                  print (f2+'Usuario %s excluido com exito.. [0] Para Home.\033[m')
                  sleep(2)
                  dex()
              dex()
           if w == '0':
              print (f1+' Saindo..\033[m')
              sleep(2)
              exit()
        else:
            w = input(f6+' :: _\033[92m'+' ')
  except KeyboardInterrupt:
     print (f1+'\nSaindo..\033[m')
     sleep(2)
     exit()
if __name__ == '__main__':
   case()