#!/usr/bin/python2.7
import os
import hashlib, base64, sys


def decriptMe():
    with open("TOP_secret.zip.enc") as f:
        return f.read()

def encryptionKey(k): 
    m = hashlib.md5()
    m.update(k.encode('utf-8'))
    key = m.hexdigest()
    return key

def decryption(key, cyphertext):
    plaintext = ""
    k = 0
    for i in cyphertext:
        p = ord(key[k]) ^ ord(i)
        plaintext = plaintext + chr(p)
        key += chr(p)
        k += 1
    return plaintext

def encryption(plaintext, key_):
    key = encryptionKey(key_)
    cyphertext = ""
    for i in range(len(plaintext)):
        c = (ord(key[i]) ^ ord(plaintext[i]))
        cyphertext = cyphertext + chr(c)
        key += plaintext[i]
    return base64.b64encode(cyphertext)

def xor_encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = base64.b64decode(file.read())
    print(data)
    encrypted_data = encryption(data, key)
    with open(output_file, 'wb') as file:
        encrypted_data = "".join([i for i in encrypted_data if i.isalnum()])
        file.write(encrypted_data)

def xor_decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = base64.b64decode(file.read())
    decrypted_data = decryption(key, data)
    with open(output_file, 'w') as file:
        file.write(decrypted_data)

def check(plaintext):
    if plaintext[-65:] == "6c81d06ac6d2709a81f76a9bf6c3f5933002f00053302447b122260a0ac0c18e\n":
        return True
    return False

def main(key):
    input_file = os.getcwd() + '/test.txt'

    output_file = os.getcwd() + '/test.zip.enc'
    xor_encrypt_file(input_file, output_file, key)

    encrypted_file = os.getcwd() + '/test.zip.enc'
    decrypted_file = os.getcwd() + '/final_plain.txt'
    xor_decrypt_file(encrypted_file, decrypted_file, key)
#     enkey = encryptionKey(key)
#     print "[*] Key Encrypted: %s" % (enkey)
#     plaintext = decryption(enkey, decriptMe())
#     if check(plaintext):
#         print "[*] Key Correct! Plaintext:\n %s" % (plaintext)
    
if __name__=="__main__":
    key = 'cle'
    main(key)
#     if len(sys.argv) != 2:
#         print 'Give me the key\n Example: %s key' % (sys.argv[0])
#         exit(1)
#     main(sys.argv[1])

