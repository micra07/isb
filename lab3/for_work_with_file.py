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


def save_to_json_file(filename: str, data):
    """
    Saves data to a JSON file.

    Parameters:
        file_path (str): The path to the JSON file to save the data to.
        data (dict): The data to be saved to the JSON file.

    Raises:
        Exception: If an error occurs while writing data to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
        print(f"Data has been successfully written to the file {filename}\n")
    except Exception as e:
        print(
            f"Error occurred while writing data to the file {filename}: {str(e)}")


def write_bytes_to_txt(data: str, path: str) -> None:
    """
    Writes bytes data to a text file.

    Parameters:
        data (str): The bytes data to write to the file.
        path (str): The path to the text file to write the data to.
    """
    try:
        with open(path, 'wb') as file:
            file.write(data)
    except Exception as e:
        logging.error(f'[write_bytes_to_txt]: {e}')

def read_bytes(path: str) -> bytes:
    """
    Reads bytes data from a text file.

    Parameters:
        path (str): The path to the text file to read the data from.

    Returns:
        bytes: The bytes data read from the file.
    """
    try:
        with open(path, 'rb') as file:
           return file.read()
    except Exception as e:
        logging.error(f'[read_bytes]: {e}')
