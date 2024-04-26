import os
import logging
import for_work_with_file 

from enum import Enum
from constants import PATH

"""
Module for working with file operations and data processing.
"""
class VigenerMode(Enum):
    ENCRYPT = 1
    DECRYPT = 2


def vigener_cipher(text, key, mode: VigenerMode, alphabet):
    """
    Encrypt or decrypt text using the Vigenere cipher.

    Parameters:
        text (str): The text to encrypt/decrypt.
        key (str): The encryption key.
        mode (VigenerMode): The mode of the cipher (ENCRYPT or DECRYPT).
        alphabet (str): The alphabet used for encryption.

    Returns:
        str: The encrypted/decrypted text.
    """
    result_text = ""
    key_length = len(key)
    key_index = 0
    try:
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
    except Exception as e:
        logging.error(f"An error occurred during Vigener cipher operation: {str(e)}")
    return result_text


def main():
    """
    Main function of the program.

    Performs encryption and decryption of text using the Vigenere cipher.
    """
    absolute_path = os.path.abspath(os.getcwd())
    json_data = for_work_with_file.read_from_json_file(absolute_path + PATH)
    alphabet_1 = json_data.get("alphabet_1", "")
    key_data = json_data.get("key_data", "")
    text_data = json_data.get("text_data", "")
    encrypted = json_data.get("encrypted", "")
    decrypted = json_data.get("decrypted", "")
    key = for_work_with_file.read_key_from_json_file(absolute_path + key_data)
    alphabet_data = for_work_with_file.read_from_json_file(absolute_path + alphabet_1)
    if 'alphabet' in alphabet_data:
        alphabet = alphabet_data['alphabet']
    else:
        logging.error("Alphabet not found in alphabet.json")
        return
    text = for_work_with_file.read_from_file( absolute_path + text_data)
    encrypted_text = vigener_cipher(text, key, VigenerMode.ENCRYPT, alphabet)
    for_work_with_file.save_to_file(absolute_path + encrypted, encrypted_text)

    encrypted_text = for_work_with_file.read_from_file(absolute_path + encrypted)
    decrypted_text = vigener_cipher(encrypted_text, key, VigenerMode.DECRYPT, alphabet)
    for_work_with_file.save_to_file(absolute_path + decrypted, decrypted_text)


if __name__ == '__main__':
    main()
 