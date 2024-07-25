def xor_encrypt(text, key):
    xored = ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(text, key * (len(text) // len(key)) + key[:len(text) % len(key)]))
    return xored

def xor_decrypt(encrypted_text, key):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(encrypted_text, key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]))

# Encrypt a file using XOR
def xor_encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = bytes([a ^ ord(b) for a, b in zip(data, key * (len(data) // len(key)) + key[:len(data) % len(key)])])
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file using XOR
def xor_decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()
    decrypted_data = bytes([a ^ ord(b) for a, b in zip(data, key * (len(data) // len(key)) + key[:len(data) % len(key)])])
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)



def run():
    input_file = 'test.txt'
    output_encrypted_file = 'encrypted_output.enc'
    key = 'secretkey123'

    xor_encrypt_file(input_file, output_encrypted_file, key)

    # Usage example
    input_file = 'encrypted_output.enc'
    output_decrypted_file = 'decrypted_output.txt'
    key = 'secretkey123'

    # Decrypt the file
    xor_decrypt_file(input_file, output_decrypted_file, key)
run()