# Configurar VPS SSH/SQUID3
<body>
  <tr>
    <td width="100px" class="main2"><b></b></td><td width="780px"></td>
  </tr>
   <tr>
    <td width="100px" class="main2"><b></b></td><td width="780px"></td>
  </tr>
<table border="0" cellpadding="0" cellspacing="2" width="100%">
  <tr>
    <td width="100px" class="main2"><b>Ferramenta:</b></td>
    <td width="780px" class="main2"><b>ZwDConfig V1.3</b></td>
  <tr>
    <td width="100px" class="main2"><b>Author:</b></td><td width="780px">Zwdeff</td>
  </tr>
  <tr>
    <td width="100px" class="main2"><b>Versão:</b></td><td width="780px">1.2</td>
  </tr>
  <tr>
    <td width="100px" class="main2"><b>Termo:</b></td><td width="780px">Bom? Eu fiz este script sem nenhuma intenção maliciosa ... Podem usar sem medo, mais não asumirei nenhuma responsabilidade por usarem meu scripts alterado por terceiros .. Quaisquer erro duvida, ou sujestão contacte meu telegram.</td>
  </tr>
  <tr>
    <td width="100px" class="main2"><b>Novidades v1.3</b></td><td width="780px">Correcoes de erros, melhorias, funçoes novas: 1) Mudar nome de usuario, 2) Backup de usuarios, 3) restauração de usuarios, 4) Remover todos os usuarios, 5) Excluir Backup 6) speedtest.</td>
  </tr>
  <tr>
    <td width="100px" class="main2"><b>Telegram:</b></td><td width="780px">@nZwdeff</td>
  </tr>
<table border="0" cellpadding="2" cellspacing="5" width="100%">
  <tr>
    <td class="main3">&#9733; <b>Descrição:</b></td>
  </tr>
  <tr>
    <td class="main" width="890px"><p>ZwDConfig é um script em python3 que ao configurar uma vps, ele detecta se a pasta do squid é squid ou squid3, configurando(a) assim qualquer vps. para editrar o arquivo /ssh/sshd_config ele substitue no meio do arquivo Port 22 por Port 22,443 deixando o arquivo sshd intacto, ao contrario de outros scripts em shell, que alterão todo o arquivo para alterar um simples texto, é outros que escrevem Port 443 no final do arquivo ocasionando erros em sua VPS.
<br />
    </table>
<table border="0" cellpadding="2" cellspacing="5" width="100%">
  <tr>
    <td class="main3" width="890px">&#9733; <b>Download:</b></td>
  </tr>
  <tr>
    <td class="main">
      wget https://raw.githubusercontent.com/Xdwnff-04x/ZwD-Config/master/.ZwDConf.py <br/>
    </td>
</table>
<table border="0" cellpadding="2" cellspacing="5" width="100%">
  <tr>
    <td class="main3" width="890px">&#9733; <b>Como usar:</b></td>
  </tr>
  <tr>
    <td class="main"> <br>wget https://raw.githubusercontent.com/Xdwnff-04x/ZwD-Config/master/.ZwDConf.py<br/> <br>chmod +x .ZwDConf.py<br/> <br>python3 .ZwDConf.py<br/> <b> Caso o python3 não estiver instalado : apt-get install python3</td>
  </tr>
</body>
</html>
