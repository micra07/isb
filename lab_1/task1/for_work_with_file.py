import json
import logging

def save_to_file(filename, content):
    """
    Saves content to a file.

    Parameters:
    filename (str): The name of the file to save to.
    content (str): The content to write to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        logging.error(f"Error while saving to file {filename}: {str(e)}")

def read_from_file(filename):
    """
    Reads content from a file.

    Parameters:
    filename (str): The name of the file to read from.
    
    Returns:
    str: The content read from the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error while reading from file {filename}: {str(e)}")
        return ""

def read_from_json_file(filename):
    """
    Reads JSON data from a file.

    Parameters:
    filename (str): The name of the file to read from.
    
    Returns:
    dict: The JSON data read from the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error while reading from file {filename}: {str(e)}")
        return {}

def read_key_from_json_file(filename):
    """
    Reads key data from a JSON file.

    Parameters:
    filename (str): The name of the JSON file to read from.
    
    Returns:
    str: The key data read from the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as key_file:
            key = json.load(key_file)['key']
        return key
    except Exception as e:
        logging.error(f"Error while reading key from JSON file {filename}: {str(e)}")
        return ""
