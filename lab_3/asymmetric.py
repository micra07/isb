from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


class Asymmetric:
    """
    Class for asymmetric encryption operations.
    """
    def __init__(self):
        """
        Initializes the private and public keys to None.
        """
        self.private_key = None
        self.public_key = None

    def generate_and_serialize_key_pair(self, private_key_path: str, public_key_path: str) -> None:
        """
        Generates an asymmetric key pair and serializes them to files.

        Parameters:
        private_key_path (str): The path to save the private key.
        public_key_path (str): The path to save the public key.

        Returns:
        None
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.private_key = keys
        self.public_key = keys.public_key()
        with open(private_key_path, 'wb') as f:
            f.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                   format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                   encryption_algorithm=serialization.NoEncryption()))
        with open(public_key_path, 'wb') as f:
            f.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                 format=serialization.PublicFormat.SubjectPublicKeyInfo))

    def deserialize_key(self, path: str, key_type: str):
        """
        Deserializes a key from a file.

        Parameters:
        path (str): The path to the key file.
        key_type (str): The type of key ('public' or 'private').

        Returns:
        The deserialized key object.
        """
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
        """
        Processes a symmetric key using asymmetric encryption.

        Parameters:
        key (bytes): The symmetric key to process.
        key_path (str): The path to the asymmetric key.
        operation (str): The operation to perform ('encrypt' or 'decrypt').

        Returns:
        The processed key.
        """
        if operation == 'encrypt':
            public_key = self.deserialize_key(key_path, 'public')
            return public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                        algorithm=hashes.SHA256(), label=None))
        elif operation == 'decrypt':
            private_key = self.deserialize_key(key_path, 'private')
            return private_key.decrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                          algorithm=hashes.SHA256(), label=None))
        else:
            raise ValueError("Invalid mode provided. Use 'encrypt' or 'decrypt'.")
 