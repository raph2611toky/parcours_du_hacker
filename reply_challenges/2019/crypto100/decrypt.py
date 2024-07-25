import os,sys, binascii
import math


def decrypt(key):
    with open('encrypted.txt', 'rb') as file_encrypted:
        data_encrypted = file_encrypted.read()

    ptxt=bytearray(256)
    for i in range(0,256):
        p = 3**(key+i) % 257 - 1
        ptxt[i]=data_encrypted[p]^i^p
    return ''.join(list(map(chr,ptxt)))

for i in range(0,256):
    res = decrypt(i)
    if '{FLG' in res:
        with open(os.getcwd()+'/plain.txt','w', encoding='utf-8') as fd:
            fd.write(res)