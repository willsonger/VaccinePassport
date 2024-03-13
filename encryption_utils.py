# Encryption and Decryption Utilities
# Encrypt Field:
from cryptography.fernet import Fernet

def encrypt_field(field_value, key_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(field_value.encode())
    return encrypted.decode()

# Decrypt Field:
def decrypt_field(encrypted_value, key_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_value.encode())
    return decrypted.decode()