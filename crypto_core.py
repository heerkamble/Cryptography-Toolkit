# =============================================================
#  crypto_core.py  –  Core cryptography functions
#  Algorithms: AES (symmetric), RSA (asymmetric), SHA-256 (hashing)
#  Library used: 'cryptography' (pip install cryptography)
# =============================================================

import os
import base64
import hashlib

# --- AES imports ---
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# --- RSA imports ---
from cryptography.hazmat.primitives.asymmetric import rsa, padding as rsa_padding
from cryptography.hazmat.primitives import hashes, serialization


# ==============================================================
#  SECTION 1: AES ENCRYPTION (Symmetric)
#  Same key is used to both encrypt AND decrypt.
#  AES works in blocks of 16 bytes, so we pad our data first.
# ==============================================================

def aes_generate_key():
    """Generate a random 32-byte (256-bit) AES key."""
    return os.urandom(32)  # 32 bytes = AES-256


def aes_encrypt(plaintext: str, key: bytes) -> dict:
    """
    Encrypt a string using AES-256 in CBC mode.
    Returns a dict with 'iv' and 'ciphertext', both base64-encoded strings.
    """
    # IV (Initialization Vector) = random 16 bytes, makes each encryption unique
    iv = os.urandom(16)

    # Pad the plaintext so its length is a multiple of 16 bytes
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Return as base64 strings (safe to store/display)
    return {
        "iv": base64.b64encode(iv).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode()
    }


def aes_decrypt(iv_b64: str, ciphertext_b64: str, key: bytes) -> str:
    """
    Decrypt AES-encrypted data.
    Takes base64-encoded iv and ciphertext, returns original plaintext.
    """
    iv = base64.b64decode(iv_b64)
    ciphertext = base64.b64decode(ciphertext_b64)

    # Recreate the same cipher with the same key + IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt and remove padding
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()


# ==============================================================
#  SECTION 2: RSA ENCRYPTION (Asymmetric)
#  Uses a PUBLIC key to encrypt, PRIVATE key to decrypt.
#  Anyone can encrypt; only the key owner can decrypt.
# ==============================================================

def rsa_generate_keypair():
    """
    Generate an RSA key pair (private + public).
    Returns both keys as PEM-format strings.
    """
    # Generate a 2048-bit private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,   # Standard value used in RSA
        key_size=2048,           # 2048 bits = strong & common
        backend=default_backend()
    )

    # Serialize private key to PEM string
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()

    # Derive and serialize the public key
    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    return private_pem, public_pem


def rsa_encrypt(plaintext: str, public_pem: str) -> str:
    """Encrypt a short message using an RSA public key. Returns base64 string."""
    public_key = serialization.load_pem_public_key(
        public_pem.encode(), backend=default_backend()
    )

    ciphertext = public_key.encrypt(
        plaintext.encode(),
        rsa_padding.OAEP(               # OAEP = secure RSA padding scheme
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode()


def rsa_decrypt(ciphertext_b64: str, private_pem: str) -> str:
    """Decrypt an RSA-encrypted message using the private key."""
    private_key = serialization.load_pem_private_key(
        private_pem.encode(), password=None, backend=default_backend()
    )

    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = private_key.decrypt(
        ciphertext,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()


# ==============================================================
#  SECTION 3: SHA-256 HASHING
#  One-way function: converts data into a fixed-length fingerprint.
#  Used for storing passwords, verifying file integrity, etc.
#  CANNOT be reversed (that's the point!).
# ==============================================================

def sha256_hash(text: str) -> str:
    """Return the SHA-256 hash of a string as a hex string."""
    return hashlib.sha256(text.encode()).hexdigest()


def sha256_hash_with_salt(text: str, salt: str = None) -> dict:
    """
    Hash a string with a random salt.
    Salt makes identical passwords produce different hashes (defeats rainbow tables).
    Returns dict with 'salt' and 'hash'.
    """
    if salt is None:
        # Generate a random 16-byte salt, encode as hex string
        salt = os.urandom(16).hex()

    salted = salt + text  # Prepend salt to the text before hashing
    hashed = hashlib.sha256(salted.encode()).hexdigest()

    return {"salt": salt, "hash": hashed}


def sha256_verify(text: str, salt: str, expected_hash: str) -> bool:
    """Verify if a text matches a stored salted hash."""
    result = sha256_hash_with_salt(text, salt)
    return result["hash"] == expected_hash
