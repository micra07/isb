import json

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def vigener_cipher(text, key):
    
    encrypted_text = ''
    key_length = len(key)
    key_index = 0

    for char in text:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            char_index = alphabet.index(char)
            encrypted_char_index = (char_index + shift) % len(alphabet)
            encrypted_text += alphabet[encrypted_char_index]
            key_index = (key_index + 1) % key_length
        else:
            encrypted_text += char

    return encrypted_text



def vigener_decipher(encrypted_text, key):
    
    decrypted_text = ''
    key_length = len(key)
    key_index = 0

    for char in encrypted_text:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            decrypted_char_index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[decrypted_char_index]
            key_index = (key_index + 1) % key_length
        else:
            decrypted_text += char

    return decrypted_text

def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    key = 'лис'
    with open('lab_1/key.json', 'w', encoding='utf-8') as key_file:
        json.dump({'key': key}, key_file)

    text = read_from_file('lab_1/text.txt')
    encrypted_text = vigener_cipher(text, key)
    save_to_file('lab_1/encrypted_text.txt', encrypted_text)

    decrypted_text = vigener_decipher(encrypted_text, key)
    save_to_file('lab_1/decrypted_text.txt', decrypted_text)

if __name__ == '__main__':
    main()
