import json
from enum import Enum

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
class VigenerMode(Enum):
    """Enumeration class for the modes of Vigenere cipher operations."""
    ENCRYPT = 1
    DECRYPT = 2
    
def vigener_cipher(text, key, mode: VigenerMode):
    """
    Encrypts or decrypts the given text using the Vigenère cipher with the specified key and mode.
    
    Parameters:
    text (str): The text to be encrypted/decrypted.
    key (str): The key to be used in the Vigenère cipher.
    mode (VigenerMode): The mode of operation - ENCRYPT for encryption, DECRYPT for decryption.
    
    Returns:
    str: The resulting encrypted or decrypted text.
    """
    result_text = ""        
    key_length = len(key)
    key_index = 0

    for char in text:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            char_index = alphabet.index(char)

            if mode == VigenerMode.ENCRYPT:
                    cipher_char_index = (char_index + shift) % len(alphabet)
                    correct_cipher_char_index = (cipher_char_index + 1) % len(alphabet)
            elif mode == VigenerMode.DECRYPT:
                    cipher_char_index = (char_index - shift) % len(alphabet)
                    correct_cipher_char_index = (cipher_char_index - 1) % len(alphabet)
            result_text += alphabet[correct_cipher_char_index]
            key_index = (key_index + 1) % key_length
        else:
            result_text += char

    return result_text


def save_to_file(filename, content):
    """
    Saves the given content to a file with the specified filename.
    
    Parameters:
    filename (str): The name of the file to save to.
    content (str): The content to be written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def read_from_file(filename):
    """
    Reads the content from a file with the specified filename.
    
    Parameters:
    filename (str): The name of the file to read from.
    
    Returns:
    str: The content read from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    """
    Main function to demonstrate the Vigenere cipher encryption and decryption process.
    """
    key = 'крот'
    with open('lab_1/key.json', 'w', encoding='utf-8') as key_file:
        json.dump({'key': key}, key_file)

    text = read_from_file('lab_1/text.txt')
    encrypted_text = vigener_cipher(text, key, VigenerMode.ENCRYPT)
    save_to_file('lab_1/encrypted_text.txt', encrypted_text)

    encrypted_text = read_from_file('lab_1/encrypted_text.txt')
    decrypted_text = vigener_cipher(encrypted_text, key, VigenerMode.DECRYPT)
    save_to_file('lab_1/decrypted_text.txt', decrypted_text)

if __name__ == '__main__':
    main()
