Oh une capture d’écran.
Énoncé

Un employé a perdu son mot de passe KeePass. Il ne s’en souvient plus et il ne trouve plus son fichier de mot de passe. Après des heures de recherche, il se trouve qu’il a envoyé à un de ses collègues un screen de ses mots de passe, cependant il reste introuvable.

Il demande votre aide pour essayer de retrouver ce dernier.
A vous de jouer.

sha256sum : 028c8561f087da873b08968d55141dcfc8f10a47e787f79c35b2da611a5e07ce
------------------------------------------------------------------------

en extractant ch42, on y trouve deux fichier:1 images (capture.png) et 1 fichier kepassdatabase(Database.kdbx)

pour interagir avec le fichier keepassdatabase, on utilise kpcli(keepass command line interface)
                                                                                                                                                                       
┌──(root㉿kali)-[/media/…/foreinsics/root-me/capture_moi_ca/ch42]
└─# kpcli --kdb=./Database.kdbx ls
Provide the master password:

mais c'est ce mot de passe qu'on recherche.Alors je me suis debrouillé pour trouver une indice sur l'image Capture.png.
J'ai utilisé toutes les commandes possibles pour cusiner l'image:
┌──(root㉿kali)-[/media/…/foreinsics/root-me/capture_moi_ca/ch42]
└─# identify -verbose ./Capture.png 

┌──(root㉿kali)-[/media/…/foreinsics/root-me/capture_moi_ca/ch42]
└─# binwalk Capture.png

j'ai meme essayer d'extracter ce que binwalk a trouver:
┌──(root㉿kali)-[/media/…/foreinsics/root-me/capture_moi_ca/ch42]
└─# binwalk -e --run-as=root Capture.png

mais ca ne mène à rien.Puis j'ai tenter une autre approche en installant (GNU Image Manipulation Program)
┌──(root㉿kali)-[/media/…/foreinsics/root-me/capture_moi_ca/ch42]
└─# sudo apt-get install gimp

puis j'ai installé zsteg
┌──(root㉿kali)-[/media/…/foreinsics/root-me/capture_moi_ca/ch42]
└─# gem install zsteg

puis j'ai essayer ceci pour extraire des informations mais que dall.
┌──(root㉿kali)-[/media/…/foreinsics/root-me/capture_moi_ca/ch42]
└─# zsteg -a Capture.png

LIEN UTILE
-----------
https://github.com/alphaSeclab/awesome-forensics/blob/master/Readme_en.md
