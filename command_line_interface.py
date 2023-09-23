from encription_by_shift import encrypt, decrypt
from encription_by_xor import xor_conversion

print("--- Encryption By Shift ---")

info: str = input("Enter the information you wish to encrypt.: ")
print("Encrypted information.: ", encrypt(info))

encrypted_info: str = input(f"\nEnter the Encrypted information.: ")
print("Decrypted information.: ", decrypt(encrypted_info))

print("\n--- Encryption By XOR ---")

text: str = input("Enter the information you wish to encrypt.: ")
print("Encrypted information.: ", xor_conversion(text))

encrypted_text: str = input(f"\nEnter the Encrypted information.: ")
print("Decrypted information.: ", xor_conversion(encrypted_text))