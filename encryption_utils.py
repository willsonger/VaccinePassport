# Encryption and Decryption Utilities
# Encrypt Field:
from cryptography.fernet import Fernet
import secrets
import random
import string

def generate_random_salt(length = 32):
    """Generate a random salt"""
    return '' .join(secrets.choice(string.ascii_letters + string.digits) for _ in range (length))

def encrypt_field(field_value, key_file):
    #Reads the symmetric or asymmetric key
    with open(key_file, 'rb') as file:
        key = file.read()
        
      
    salt = generate_random_salt()
    
    #Concatenate the value and salt with |
    concatenaated_value = f"{field_value}|{salt}".encode()
    
    #Create a Fernet cipher object (symmetric key algorithm) using the key
    fernet = Fernet(key)
    encrypted = fernet.encrypt(concatenaated_value)
    
    #returns as a string
    return encrypted.decode()

# Decrypt Field:
def decrypt_field(encrypted_value, key_file):
    """Decrypts the encrypted value with the symmetric key."""
    with open(key_file, 'rb') as file:
        key = file.read()
        
    fernet = Fernet(key)
    #Decrypt
    decrypted = fernet.decrypt(encrypted_value.encode())
    salt = generate_random_salt()
    #split decrypted value into original value and salt
    decrypted_value, salt = decrypted.decode().split('|')
    return decrypted_value