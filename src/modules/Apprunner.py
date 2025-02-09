from cryptography.fernet import Fernet
import qrcode
import os
import json

# Connect With Json File
try:
    data = open(file="src/json/api.json")
    js = json.load(data)
except(Exception):
    try:
        data = open(file="json/api.json")
        js = json.load(data)
    except(Exception):
        print("File Not Found")


class Apprun():
    # File Encrypter Function
    def enc(self, Path, ReadFile, WriteFile):
        global key
        global fd
        key = Fernet.generate_key()
        try:
            with open("src/key/Mykey.key", "wb") as f:
                f.write(key)
                f.close()
        except(Exception):
            print("Key Not Found")

        fd = Fernet(key)

        try:
            with open(f"{Path}{ReadFile}", "rb") as f:
                global enc
                enc = f.read()
                f.close()
        except(Exception):
            print("File Not Read")

        encrypt = fd.encrypt(enc)

        try:
            with open(f"{Path}{WriteFile}", "wb") as f:
                f.write(encrypt)
                f.close()
        except(Exception):
            print("Write File Not Found")

    # File Decrypter Function
    def dec(self, Path, ReadFile, WriteFile):
        global dec
        try:
            with open("src/key/Mykey.key", "rb") as f:
                key = f.read()
                f.close()
        except(Exception):
            print("Key Not Found")

        fd = Fernet(key)

        try:
            with open(f"{Path}{ReadFile}", "rb") as f:
                dec = f.read()
                f.close()
        except(Exception):
            print("File Not Read")

        decrypt = fd.decrypt(dec)

        try:
            with open(f"{Path}{WriteFile}", "wb") as f:
                f.write(decrypt)
                f.close()
        except(Exception):
            print("Write File Not Found")

    # Make Qrcode Using Text data
    def makeqr(self, TextData, SaveQrData):
        img = qrcode.make(TextData)
        img.save(f"{SaveQrData}.png")


path = js["Path"]
global FileName
try:
    with open("src/doc/Filename.txt", "r") as f:
        FileName = f.read()
        f.close()
except(Exception):
    pass

# Code Run Functions Class
class CodeRunner():
    # Code Run Function For Python
    def Python(self):
        os.system("clear")
        os.system(f"cd {path} && python3 {FileName}")

    # Code Run Function For C++
    def cpp(self):
        os.system('clear')
        os.system(f'cd {path} && g++ {FileName} -o a && ./a')

    # Code Run Function For C
    def c(self):
        os.system('clear')
        os.system(f'cd {path} && gcc {FileName} -o a && ./a')

    # Code Run Function For Java
    def java(self):
        os.system('clear')
        os.system(f'cd {path} && java {FileName}')

    # Code Run Function For JavaScript
    def javaScript(self):
        os.system('clear')
        os.system(f'cd {path} && node {FileName}')

    # Code Run Function For Html
    def html(self):
        os.system('clear')
        os.system(f'cd {path} && chromium {FileName}')
