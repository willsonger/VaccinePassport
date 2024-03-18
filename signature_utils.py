# Signing and Verifying Signatures
# Sign Field
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
 

def sign_field(data, private_key_file):
    
    # Load the private key from a PEM file
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,  # Use a password argument if your key is encrypted
            backend=default_backend()
        )

    # Sign the data
    signature = private_key.sign(
        data.encode(),  # Convert the data to bytes if not already done
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Return the signature in a format that can be easily stored or transmitted
    return signature.hex()


def verify_signature(data, signature, public_key_file):
    # Load the public key from a PEM file
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    try:
        # Verify the signature
        public_key.verify(
            bytes.fromhex(signature),  # Convert the hex signature back to bytes
            data.encode(),  # Convert the data to bytes if not already done
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        # If verification fails, an exception is raised
        return False
