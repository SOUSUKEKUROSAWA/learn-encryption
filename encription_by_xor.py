from dotenv import load_dotenv
import os

load_dotenv()

def xor_conversion(text: str) -> str:
    """
    Encryption and decryption using the XOR operation
    :param text: str
    :return: str
    """
    result = ""
    for char in text:
        result += chr(ord(char) ^ ord(os.getenv("ENCRYPTION_KEY")))
    return result
