import argparse
import logging
import json
from enum import Enum
from for_work_with_file import save_to_file, read_from_file, read_from_json_file, read_key_from_json_file

class VigenerMode(Enum):
    ENCRYPT = 1
    DECRYPT = 2

def vigener_cipher(text, key, mode: VigenerMode, alphabet):
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

def main(args_file):
    with open(args_file) as file:
        args = [line.strip() for line in file.readlines()]

    key = read_key_from_json_file(args[0])

    alphabet_data = read_from_json_file('lab_1/task1/const.json')
    if 'alphabet' in alphabet_data:
        alphabet = alphabet_data['alphabet']
    else:
        logging.error("Alphabet not found in const.json")
        return

    text = read_from_file(args[1])
    encrypted_text = vigener_cipher(text, key, VigenerMode.ENCRYPT, alphabet)
    save_to_file(args[2], encrypted_text)

    encrypted_text = read_from_file(args[2])
    decrypted_text = vigener_cipher(encrypted_text, key, VigenerMode.DECRYPT, alphabet)
    save_to_file(args[3], decrypted_text)

if __name__ == '__main__':
    main('lab_1/task1/args.txt')