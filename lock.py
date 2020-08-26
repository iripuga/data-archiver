''' 
vir: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
'''
## cela pot do datoteke, ki jo kriptiram ##
path2file = "/Users/iripuga/Documents/0.UNI/2.Magisterij/4.magistrska/data-archiver/"	### CHANGE PATH
filename = 'KodirnaTabela.xlsx'
file = path2file + filename 

import sys
from cryptography.fernet import Fernet

## Lokacija ključa ##
path2key = "/Users/iripuga/Documents/0.UNI/2.Magisterij/4.magistrska/data-archiver/"	### CHANGE PATH

## Zapisujem stanje - ali je tabela kriptirana ali ne? ##
fh = open('.lockstate.txt', 'r+') 
text = fh.read()
fh.seek(0)
print(text) # zato, da veš al je kriptirano al ne

if text.split('=')[1] == 'False':
	state = False
else:
	state = True
#print(type(state))

## Definiranje funkcij ##
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open(path2key + "key.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key) 

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)
    
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Začetek zabave
key = load_key()
choice = input('encrypt(PRESS e) or decrypt(PRESS d) your file: ')

if choice == 'e' and state == False:
    # encrypt it
    encrypt(file, key)
    fh.write('encryption=True')
    fh.truncate()
    print(f'File {file} is encrypted')
elif choice == 'e' and state == True:
	print("File is already encrypted, so DON\'T HAPPY BE WORRY")
elif choice == 'd' and state == True:
    # decrypt the file
    decrypt(file, key)
    fh.write('encryption=False')
    fh.truncate()
    print(f'File {file} is decrypted')
elif choice == 'd' and state == False:
	print('File is already decrypted, go check it out')
else:
    print('Oops, try again!')

fh.close()