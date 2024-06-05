import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from for_work_with_file import *

class Symmetric:
    def __init__(self):
        self.key = None

def generate_key(self) -> bytes:
    self.key = os.urandom(16)
    return self.key

def serialize_key(self, path: str) -> None:
    write_bytes_to_txt(self.key, path)

def deserialize_key(self, path: str) -> None:
    self.key = read_bytes(path)

def __pad_data(self, text: str) -> bytes:
    padder = padding.PKCS7(128).padder()
    btext = bytes(text, 'UTF-8')
    padded_text = padder.update(btext) + padder.finalize()
    return padded_text

def __unpad_data(self, decrypted_text: bytes) -> str:
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_text = unpadder.update(decrypted_text) + unpadder.finalize()
    return unpadded_text.decode('UTF-8')

def process_text(self, text: str, key: bytes, mode: str):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
    if mode == 'encrypt':
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(self.__pad_data(text)) + encryptor.finalize()
        return iv + encrypted_text
    elif mode == 'decrypt':
        iv = text[:16]
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(text[16:]) + decryptor.finalize()
        return self.__unpad_data(decrypted_text)
    else:
        raise ValueError("Invalid mode provided. Use 'encrypt' or 'decrypt'.")

        