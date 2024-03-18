"""***********************************************************************
*    key_management.py: For generating symmetric and asymmetric keys.    *
*    encryption_utils.py: For encrypting and decrypting fields.          * 
*    signature_utils.py: For signing fields and verifying signatures.    *
*    main.py: The main script where you'll implement the command-line    *
*    interface to tie everything together.                               *
**************************************************************************"""
    
"""***************************************************************"""
# main
import argparse
from key_management import generate_symmetric_key, generate_asymmetric_keys
from encryption_utils import encrypt_field, decrypt_field
from signature_utils import sign_field, verify_signature
from file_management import store_passport, retrieve_passport
def main():
    parser = argparse.ArgumentParser(description="Vaccine Passport Utility")

    # Defining subparsers for different commands
    subparsers = parser.add_subparsers(dest='command')
    
    # Subparser for generating symmetric key
    parser_symkey = subparsers.add_parser('generate-symmetric-key', help='Generate a symmetric key')
    parser_symkey.add_argument('filename', type=str, help='Filename to store the symmetric key')
    
    # Subparser for generating asymmetric key pair
    parser_asymkey = subparsers.add_parser('generate-asymmetric-keys', help='Generate an asymmetric key pair')
    parser_asymkey.add_argument('public_key_filename', type=str, help='Filename to store the public key')
    parser_asymkey.add_argument('private_key_filename', type=str, help='Filename to store the private key')

    # Subparser for encrypting a field
    parser_encrypt = subparsers.add_parser('encrypt', help='Encrypt a field')
    parser_encrypt.add_argument('field_value', type=str, help='Value of the field to encrypt')
    parser_encrypt.add_argument('key_file', type=str, help='Filename of the key file')

    # Subparser for decrypting a field
    parser_decrypt = subparsers.add_parser('decrypt', help='Decrypt a field')
    parser_decrypt.add_argument('encrypted_value', type=str, help='Encrypted value of the field')
    parser_decrypt.add_argument('key_file', type=str, help='Filename of the key file')

    # Subparser for signing a field
    parser_sign = subparsers.add_parser('sign', help='Sign a field')
    parser_sign.add_argument('field_value', type=str, help='Value of the field to sign')
    parser_sign.add_argument('private_key_file', type=str, help='Filename of the private key')

    # Subparser for verifying a signature
    parser_verify = subparsers.add_parser('verify', help='Verify a signature')
    parser_verify.add_argument('field_value', type=str, help='Value of the field')
    parser_verify.add_argument('signature', type=str, help='Signature to verify')
    parser_verify.add_argument('public_key_file', type=str, help='Filename of the public key')

    parser_store = subparsers.add_parser('store-passport', help='Store encrypted passport')
    parser_store.add_argument('passport_file_name', type=str, help='Filename of the plaintext passport')
    parser_store.add_argument('encrypted_passport_file', type=str, help='Filename to store the encrypted passport')
    parser_store.add_argument('symmetric_key_file', type=str, help='Filename of the symmetric key')
    parser_store.add_argument('private_key_file', type=str, help='Filename of the private key')

    parser_retrieve = subparsers.add_parser('retrieve-passport', help='Retrieve and decrypt passport')
    parser_retrieve.add_argument('passport_file_name', type=str, help='Filename to store the decrypted passport')
    parser_retrieve.add_argument('encrypted_passport_file', type=str, help='Filename of the encrypted passport')
    parser_retrieve.add_argument('symmetric_key_file', type=str, help='Filename of the symmetric key')
    parser_retrieve.add_argument('public_key_file', type=str, help='Filename of the public key')

    args = parser.parse_args()

    if args.command == 'generate-symmetric-key':
        generate_symmetric_key(args.filename)
        print(f"Symmetric key generated and saved to {args.filename}")
    elif args.command == 'generate-asymmetric-keys':
        generate_asymmetric_keys(args.public_key_filename, args.private_key_filename)
        print(f"Asymmetric key pair generated. Public key saved to {args.public_key_filename} and private key to {args.private_key_filename}")  
    elif args.command == 'encrypt':
        encrypted_data = encrypt_field(args.field_value, args.key_file)
        print(f"Encrypted data: {encrypted_data}")
    elif args.command == 'decrypt':
        decrypted_data = decrypt_field(args.encrypted_value, args.key_file)
        print(f"Decrypted data: {decrypted_data}")
    elif args.command == 'sign':
        signature = sign_field(args.field_value, args.private_key_file)
        print(f"Field signed. Signature: {signature}")
    elif args.command == 'verify':
        verified = verify_signature(args.field_value, args.signature, args.public_key_file)
        if verified:
            print("Signature is valid.")
        else:
            print("Signature is invalid.")
            
    elif args.command == 'store-passport':
        store_passport(args.passport_file_name, args.encrypted_passport_file, args.symmetric_key_file, args.private_key_file)
    elif args.command == 'retrieve-passport':
        retrieve_passport(args.passport_file_name, args.encrypted_passport_file, args.symmetric_key_file, args.public_key_file)


if __name__ == "__main__":
    main()
