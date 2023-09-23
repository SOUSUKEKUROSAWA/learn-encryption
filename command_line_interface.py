from encription_by_shift import encrypt, decrypt

print("--- Encryption By Shift ---")

info: str = input("Enter the information you wish to encrypt.: ")
print("Encrypted information.: ", encrypt(info))

encrypted_info: str = input(f"\nEnter the Encrypted information.: ")
print("Decrypted information.: ", decrypt(encrypted_info))