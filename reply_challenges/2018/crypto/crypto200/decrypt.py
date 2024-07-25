import os, hashlib
import binascii, base64

with open(os.getcwd()+'/encrypted', 'rb') as fread:
    data = fread.read()
print(data)