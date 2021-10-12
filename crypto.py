from Crypto.Hash import MD5
from Crypto.Cipher import AES
from base64 import b64encode
from tkinter import messagebox
import sys


from Crypto.Util.Padding import pad, unpad


right_hash = b'#\xff\xae\x9b\xde#\r\x9d\xbb\xe2U\xc9\xeaz\xb96'
salt = 4


def encrypt():
    with open('data.json', 'rb') as json_file:
        encrypter = AES.new(right_hash, AES.MODE_CBC, right_hash)
        bytes = json_file.read()
        data = encrypter.encrypt(pad(bytes, AES.block_size))
        with open('CryptedFile.txt', 'wb') as file:
            file.write(data)

def decrypt(password):
    pass_str = password.get() + str(salt)
    hash_value = MD5.new(pass_str.encode()).digest()
    if right_hash == hash_value:
        with open('CryptedFile.txt', 'rb') as file:
            decrypter = AES.new(right_hash, AES.MODE_CBC, right_hash)
            bytes = file.read()
            data = unpad(decrypter.decrypt(bytes), AES.block_size)
            with open('data.json', 'wb') as json_file:
                json_file.write(data)
            with open('check.json', 'wb') as json_file:
                json_file.write(data)
        return True
    elif right_hash != hash_value:
        messagebox.showerror("Попытка расшифровки", "Фраза не верна")
        return False


if __name__ == '__main__':
    decrypt("its admin")