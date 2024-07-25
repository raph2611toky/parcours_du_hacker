import hashlib
import zipfile
import io
import base64
import sys, os

PTXT_END = "6c81d06ac6d2709a81f76a9bf6c3f5933002f00053302447b122260a0ac0c18e\n"


with open('TOP_secret.zip.enc', 'rb') as f:
    ctxt = base64.b64decode(f.read())
ptxt = PTXT_END
for i in reversed(range(len(ctxt)-len(ptxt))):
    ptxt = chr(ctxt[i+32] ^ ord(ptxt[31])) + ptxt
print(ptxt)

ptxt_bin = bytes([ord(i) for i in ptxt])
zf = zipfile.ZipFile(io.BytesIO(ptxt_bin), "r")
for fileinfo in zf.infolist():
    print(zf.read(fileinfo).decode('ascii'))
zip_dest = os.getcwd() + '/top_secret'
zf.extractall(zip_dest)


