from dotenv import load_dotenv
import os

load_dotenv()

def shift_char(char: str, shift: int) -> str:
    if not char.isalpha():
        raise ValueError("Can only shift alphabet.")
    char = char.upper()
    code = ord(char) + shift
    if code < ord('A'):
        code += 26
    if code > ord('Z'):
        code -= 26
    return chr(code)

def encrypt(info: str) -> str:
    result: str = ""
    for char in info:
        result += shift_char(char, int(os.getenv("ENCRYPTION_KEY")))
    return result

def decrypt(encrypted_info: str) -> str:
    result: str = ""
    for char in encrypted_info:
        result += shift_char(char, -int(os.getenv("ENCRYPTION_KEY")))
    return result
