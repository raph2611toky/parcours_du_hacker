Tu peux regarder ce que tu veux, mais cette clé est vide...
Énoncé

Votre cousin a trouvé une clé USB à la bibliothèque ce matin. Il n’est pas très doué avec les ordinateurs, alors il compte sur vous pour retrouver le propriétaire de cette clé !

Le flag est l’identité du propriétaire sous la forme prénom_nom

sha256sum : cd9f4ada5e2a97ec6def6555476524712760e3d8ee99c26ec2f11682a1194778

---------------------------------------------------------------------------

CH9.gz contient un fichier nommé fichie_supprime après extraction.

en analysant fichier_supprime, on a:

┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# file fichier_supprime
fichier_supprime: POSIX tar archive (GNU)

donc c'est un archive tar puis on l'extract pour avoir son contenu.
en utilisant la commande:
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# tar -xf fichier_supprime -c .

et on trouve le fichier usb.image dedans, et voici le resultat de son analyse

┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# file usb.image       
usb.image: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, reserved sectors 4, root entries 512, sectors 63488 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 64, sectors/track 62, heads 124, hidden sectors 2048,

en essayant de voir ce qui s'y trouve , on a:
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# fls -r ./usb.image

r/r 3:  USB         (Volume Label Entry)
r/r * 5:        anonyme.png
v/v 1013699:    $MBR
v/v 1013700:    $FAT1
v/v 1013701:    $FAT2
V/V 1013702:    $OrphanFiles

puis , on extract aussi le contenu de usb.image en utilisant tsk_recover.
                                                                                                                                                                       
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# tsk_recover ./usb.image ./recovered_files

Files Recovered: 1
                                                                                                                                                                       
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# ls
fichier_supprime  fichier_supprime.gz  recovered_files  usb.image
                                                                      
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# ls recovered_files 
anonyme.png
 
je croyais qu'il s'agit de steganographie alors j'ai utiliser steghide extract pour extraire son contenu mais je connais pas le passephrase(j'ai meme essayer Orphan mais en vain)
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# convert recovered_files/anonyme.png recovered_files/anonyme.jpg

                                                                                  
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# ls
fichier_supprime  fichier_supprime.gz  read-me.md  recovered_files  usb.image
                                                                                  
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# ls recovered_files
anonyme.jpg  anonyme.png
                                                                                  
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# steghide extract -sf recovered_files/anonyme.jpg

Enter passphrase: 
steghide: could not extract any data with that passphrase!

alors j'ai tenter une autre approche en extractant les contenus de usb.image avec foremost
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# foremost -i usb.image -o usb_output      

Processing: usb.image
|*|
                                                                                              
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# ls
fichier_supprime     read-me.md       rockyou.txt  usb_output
fichier_supprime.gz  recovered_files  usb.image
                                                                                              
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# ls usb_output     
audit.txt  png

mais toujours le meme resultat, j'ai meme essayer de brutforce steghide avec rockyou dans python mais sans resultat, enfin j'ai decidé de regarder dans l'hexadecimale de anonyme.png et j'ai trouvé ceci:

                                                                                                                                                                       
┌──(root㉿kali)-[/media/…/CYBERSECURITY/foreinsics/root-me/fichier supprimer]
└─# xxd recovered_files/anonyme.png|more
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0190 0000 012c 0802 0000 0062 d572  .......,.....b.r
00000020: 9500 0000 0467 414d 4100 00b1 8f0b fc61  .....gAMA......a
00000030: 0500 0000 2063 4852 4d00 007a 2600 0080  .... cHRM..z&...
00000040: 8400 00fa 0000 0080 e800 0075 3000 00ea  ...........u0...
00000050: 6000 003a 9800 0017 709c ba51 3c00 0000  `..:....p..Q<...
00000060: 0662 4b47 4400 ff00 ff00 ffa0 bda7 9300  .bKGD...........
00000070: 0001 be69 5458 7458 4d4c 3a63 6f6d 2e61  ...iTXtXML:com.a
00000080: 646f 6265 2e78 6d70 0000 0000 003c 3f78  dobe.xmp.....<?x
00000090: 7061 636b 6574 2062 6567 696e 3d27 efbb  packet begin='..
000000a0: bf27 2069 643d 2757 354d 304d 7043 6568  .' id='W5M0MpCeh
000000b0: 6948 7a72 6553 7a4e 5463 7a6b 6339 6427  iHzreSzNTczkc9d'
000000c0: 3f3e 0a3c 783a 786d 706d 6574 6120 786d  ?>.<x:xmpmeta xm
000000d0: 6c6e 733a 783d 2761 646f 6265 3a6e 733a  lns:x='adobe:ns:
000000e0: 6d65 7461 2f27 2078 3a78 6d70 746b 3d27  meta/' x:xmptk='
000000f0: 496d 6167 653a 3a45 7869 6654 6f6f 6c20  Image::ExifTool 
00000100: 3131 2e38 3827 3e0a 3c72 6466 3a52 4446  11.88'>.<rdf:RDF
00000110: 2078 6d6c 6e73 3a72 6466 3d27 6874 7470   xmlns:rdf='http
00000120: 3a2f 2f77 7777 2e77 332e 6f72 672f 3139  ://www.w3.org/19
00000130: 3939 2f30 322f 3232 2d72 6466 2d73 796e  99/02/22-rdf-syn
00000140: 7461 782d 6e73 2327 3e0a 0a20 3c72 6466  tax-ns#'>.. <rdf
00000150: 3a44 6573 6372 6970 7469 6f6e 2072 6466  :Description rdf
00000160: 3a61 626f 7574 3d27 270a 2020 786d 6c6e  :about=''.  xmln
00000170: 733a 6463 3d27 6874 7470 3a2f 2f70 7572  s:dc='http://pur
00000180: 6c2e 6f72 672f 6463 2f65 6c65 6d65 6e74  l.org/dc/element
00000190: 732f 312e 312f 273e 0a20 203c 6463 3a63  s/1.1/'>.  <dc:c
000001a0: 7265 6174 6f72 3e0a 2020 203c 7264 663a  reator>.   <rdf:
000001b0: 5365 713e 0a20 2020 203c 7264 663a 6c69  Seq>.    <rdf:li
##################000001c0: 3e4a 6176 6965 7220 5475 7263 6f74 3c2f  >Javier Turcot</
000001d0: 7264 663a 6c69 3e0a 2020 203c 2f72 6466  rdf:li>.   </rdf
000001e0: 3a53 6571 3e0a 2020 3c2f 6463 3a63 7265  :Seq>.  </dc:cre
000001f0: 6174 6f72 3e0a 203c 2f72 6466 3a44 6573  ator>. </rdf:Des
00000200: 6372 6970 7469 6f6e 3e0a 3c2f 7264 663a  cription>.</rdf:
00000210: 5244 463e 0a3c 2f78 3a78 6d70 6d65 7461  RDF>.</x:xmpmeta
00000220: 3e0a 3c3f 7870 6163 6b65 7420 656e 643d  >.<?xpacket end=
00000230: 2772 273f 3e27 9a87 0a00 0080 0049 4441  'r'?>'.......IDA
00000240: 5478 da74 fdd7 b3ad 5972 1f88 65ae efdb  Tx.t....Yr..e...
00000250: feec bd8f b7d7 9bf2 55dd a86e 7403 8d06  ........U..nt..

le flag est sous la forme prénom_nom: javier_turcot