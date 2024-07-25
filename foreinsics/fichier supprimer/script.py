import os


with open('rockyou.txt', 'rb') as rockyou:
    passwords = rockyou.readlines()
    passwords = [line.decode('utf-8', errors='ignore').strip() for line in passwords]

for passphrase in passwords:
	exit_code = os.system(f'steghide extract -sf recovered_files/anonyme.jpg -p {passphrase}')
	if exit_code==0:
		print(passphrase)
		print('---------------------------------------------------------------')
		exit(0)
