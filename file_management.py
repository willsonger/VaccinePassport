
from encryption_utils import encrypt_field, decrypt_field
from signature_utils import sign_field, verify_signature


def store_passport(passport_file_name, encrypted_passport_file, symmetric_key_file, private_key_file):
    """Encrypts each field of the passport and creates MAC codes."""
    with open(passport_file_name, 'r') as passport_file:
        with open(encrypted_passport_file, 'w') as encrypted_file:
            for line in passport_file:
                field_name, field_value = line.strip().split('=')
                encrypted_value = encrypt_field(field_value, symmetric_key_file)
                mac = sign_field(encrypted_value, private_key_file)
                encrypted_file.write(f"{field_name}={encrypted_value}|{mac}\n")

def retrieve_passport(passport_file_name, encrypted_passport_file, symmetric_key_file, public_key_file):
    """Verifies each field and decrypts the passport."""
    with open(encrypted_passport_file, 'r') as encrypted_file:
        with open(passport_file_name, 'w') as passport_file:
            for line in encrypted_file:
                field_name, encrypted_value_with_mac = line.strip().split('=')
                encrypted_value, mac = encrypted_value_with_mac.split('|')

                if verify_signature(encrypted_value, mac, public_key_file):
                    decrypted_value = decrypt_field(encrypted_value, symmetric_key_file)
                    passport_file.write(f"{field_name}={decrypted_value}\n")
                else:
                    print(f"Failed to verify field: {field_name}")