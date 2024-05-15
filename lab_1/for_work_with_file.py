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
    
def save_to_json_file(file_path: str, data):
    """
    Saves data to a JSON file.

    Parameters:
        file_path (str): The path to the JSON file to save the data to.
        data (dict): The data to be saved to the JSON file.
    
    Raises:
        Exception: If an error occurs while writing data to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data has been successfully written to the file {file_path}\n")
    except Exception as e:
        print(f"Error occurred while writing data to the file {file_path}: {str(e)}")
         
 