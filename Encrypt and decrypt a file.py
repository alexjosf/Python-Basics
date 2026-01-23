# Write a Python program to encrypt and decrypt a file
from cryptography.fernet import Fernet  # import required module

key = Fernet.generate_key()  # key generation
with open('filekey.key', 'wb') as fp:  # storing the key in a file
    fp.write(key)
with open('filekey.key', 'rb') as fp:  # opening the key file and storing the key to a variable
    key = fp.read()
fernet = Fernet(key)  # using the generated key
with open('bcae.csv', 'rb') as f:  # opening the original file to encrypt
    original = f.read()
encrypted = fernet.encrypt(original)  # encrypting the file
# opening the file in write mode and writing the encrypted data
with open('ebcae.csv', 'wb') as ef:
    ef.write(encrypted)
fernet = Fernet(key)  # using the key
with open('ebcae.csv', 'rb') as ef:  # opening the encrypted file
    encrypted = ef.read()
decrypted = fernet.decrypt(encrypted)  # decrypting the file
# opening the file in write mode and writing the decrypted data
with open('dbcae.csv', 'wb') as df:
    df.write(decrypted)
