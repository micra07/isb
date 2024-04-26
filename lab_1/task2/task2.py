import os
import logging
import task2_key
import for_work_with_file

from constants import PATH

def frequency_analysis(text: str) -> list:
    """
    Perform frequency analysis on the given text.

    Parameters:
        text (str): The text to analyze.
    
    Returns:
        list: A list of tuples where each tuple contains a letter and its frequency in the text.
    """
    dictonary_of_frequency = {}
    len_text = len(text)
    try:
        for letter in text:
            if (letter not in dictonary_of_frequency.keys()):
                frequency = text.count(letter) / len_text
                dictonary_of_frequency[letter] = frequency
            else:
                continue
        result = sorted(dictonary_of_frequency.items(), key=lambda x: x[1], reverse=True)
        return result
    except Exception:
        logging.error(f"Error in function frequency_analysis(text): could not return the list")


def main():
    """
    Perform frequency analysis on encrypted text and decrypt it using a predefined key.
    """
    absolute_path = os.path.abspath(os.getcwd())
    json_data = for_work_with_file.read_from_json_file(absolute_path + PATH)
    analis_data = json_data.get("analis_data", "")
    encrypted = json_data.get("encrypted", "")
    decrypted = json_data.get("decrypted", "")
    text = for_work_with_file.read_from_file(absolute_path + encrypted)
    analis = frequency_analysis(text)
    for_work_with_file.save_to_json_file(absolute_path + analis_data, analis)
    for letter in task2_key.dictonary_letter_value:
        text = text.replace(task2_key.dictonary_letter_value[letter], letter)
    for_work_with_file.save_to_file(absolute_path + decrypted, text)


if __name__ == '__main__':
    main()
 