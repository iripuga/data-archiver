''' 
vir: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

RUN ONLY ONCE - just to generate encryption key
'''
import sys
from cryptography.fernet import Fernet

## Definiranje funkcij ##
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Začetek zabave
key = write_key()
print(f'Encryption key generated and saved as key.key in current directory')