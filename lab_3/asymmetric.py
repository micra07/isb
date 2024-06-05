from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class Asymmetric:
    def __init__(self):
        self.private_key = None
        self.public_key = None

def generate_and_serialize_key_pair(self, private_key_path: str, public_key_path: str) -> None:
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.private_key = keys
        self.public_key = keys.public_key()

        with open(private_key_path, 'wb') as f:
            f.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))

        with open(public_key_path, 'wb') as f:
            f.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
        
def deserialize_key(self, path: str, key_type: str):
    with open(path, 'rb') as f:
        key_bytes = f.read()
        if key_type == 'public':
            self.public_key = load_pem_public_key(key_bytes)
            return self.public_key
        elif key_type == 'private':
            self.private_key = load_pem_private_key(key_bytes, password=None)
            return self.private_key
        else:
            raise ValueError("Invalid key type specified")

def process_symmetric_key(self, key: bytes, key_path: str, operation: str) -> bytes:
    if operation == 'encrypt':
        public_key = self.deserialize_key(key_path, 'public')
        return public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    elif operation == 'decrypt':
        private_key = self.deserialize_key(key_path, 'private')
        return private_key.decrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    else:
        raise ValueError("Invalid operation specified")
