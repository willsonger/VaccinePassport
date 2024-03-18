# Key Management
# Symmetric Key Generation
from cryptography.fernet import Fernet

# Asymmetric Key Pair Generation
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_symmetric_key(filename):
    key = Fernet.generate_key()
    with open(filename, 'wb') as file:
        file.write(key)



def generate_asymmetric_keys(public_key_filename, private_key_filename):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    with open(private_key_filename, 'wb') as p_key_file:
        p_key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open(public_key_filename, 'wb') as pub_key_file:
        pub_key_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
