# =============================================================
#  cli.py  –  Command-Line Interface for Crypto Toolkit
#  Run with: python cli.py
# =============================================================

import base64
from crypto_core import (
    aes_generate_key, aes_encrypt, aes_decrypt,
    rsa_generate_keypair, rsa_encrypt, rsa_decrypt,
    sha256_hash, sha256_hash_with_salt, sha256_verify
)

# Store session keys so you can encrypt then decrypt in the same run
aes_key = None
rsa_private = None
rsa_public = None


def print_header():
    print("\n" + "=" * 55)
    print("        🔐  CRYPTOGRAPHY TOOLKIT  🔐")
    print("   AES Encryption | RSA Encryption | SHA-256 Hashing")
    print("=" * 55)


def print_menu():
    print("\n--- MAIN MENU ---")
    print("1. AES Encryption / Decryption")
    print("2. RSA Encryption / Decryption")
    print("3. SHA-256 Hashing")
    print("4. Exit")
    print("-" * 20)


def aes_menu():
    global aes_key
    print("\n--- AES (Symmetric Encryption) ---")
    print("How it works: The SAME key is used to encrypt and decrypt.")
    print("1. Generate a new AES key")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    print("4. Back")

    choice = input("\nChoose: ").strip()

    if choice == "1":
        aes_key = aes_generate_key()
        print(f"\n✅ New AES key generated!")
        print(f"   Key (base64): {base64.b64encode(aes_key).decode()}")
        print("   (Key is stored in memory for this session)")

    elif choice == "2":
        if not aes_key:
            print("\n⚠️  No key found. Please generate a key first (option 1).")
            return
        msg = input("Enter message to encrypt: ")
        result = aes_encrypt(msg, aes_key)
        print(f"\n✅ Encrypted!")
        print(f"   IV:         {result['iv']}")
        print(f"   Ciphertext: {result['ciphertext']}")
        print("\n   (Save these two values — you need both to decrypt)")

    elif choice == "3":
        if not aes_key:
            print("\n⚠️  No key found. Please generate a key first (option 1).")
            return
        iv = input("Enter IV (from encryption): ").strip()
        ct = input("Enter Ciphertext (from encryption): ").strip()
        try:
            plaintext = aes_decrypt(iv, ct, aes_key)
            print(f"\n✅ Decrypted message: {plaintext}")
        except Exception as e:
            print(f"\n❌ Decryption failed. Make sure you used the same key + IV. ({e})")

    elif choice == "4":
        return
    else:
        print("Invalid choice.")


def rsa_menu():
    global rsa_private, rsa_public
    print("\n--- RSA (Asymmetric Encryption) ---")
    print("How it works: PUBLIC key encrypts, PRIVATE key decrypts.")
    print("1. Generate RSA key pair")
    print("2. Encrypt a message (with public key)")
    print("3. Decrypt a message (with private key)")
    print("4. Back")

    choice = input("\nChoose: ").strip()

    if choice == "1":
        print("\n⏳ Generating RSA keys (this takes a second)...")
        rsa_private, rsa_public = rsa_generate_keypair()
        print("✅ Key pair generated and stored in memory!")
        print("\n--- PUBLIC KEY (share this freely) ---")
        print(rsa_public)
        print("--- PRIVATE KEY (keep this secret!) ---")
        print(rsa_private)

    elif choice == "2":
        if not rsa_public:
            print("\n⚠️  No key pair found. Generate one first (option 1).")
            return
        msg = input("Enter message to encrypt: ")
        try:
            ciphertext = rsa_encrypt(msg, rsa_public)
            print(f"\n✅ Encrypted (base64):\n{ciphertext}")
        except Exception as e:
            print(f"\n❌ Encryption failed: {e}")

    elif choice == "3":
        if not rsa_private:
            print("\n⚠️  No private key found. Generate a key pair first (option 1).")
            return
        ct = input("Enter encrypted message (base64): ").strip()
        try:
            plaintext = rsa_decrypt(ct, rsa_private)
            print(f"\n✅ Decrypted message: {plaintext}")
        except Exception as e:
            print(f"\n❌ Decryption failed. Wrong key or corrupted data. ({e})")

    elif choice == "4":
        return
    else:
        print("Invalid choice.")


def sha_menu():
    print("\n--- SHA-256 Hashing ---")
    print("How it works: Converts data into a fixed fingerprint. Cannot be reversed.")
    print("1. Hash a message (simple)")
    print("2. Hash with salt (secure — for passwords)")
    print("3. Verify a password against a stored hash")
    print("4. Back")

    choice = input("\nChoose: ").strip()

    if choice == "1":
        msg = input("Enter text to hash: ")
        result = sha256_hash(msg)
        print(f"\n✅ SHA-256 Hash:\n   {result}")

    elif choice == "2":
        msg = input("Enter text to hash (e.g. a password): ")
        result = sha256_hash_with_salt(msg)
        print(f"\n✅ Salted Hash generated!")
        print(f"   Salt: {result['salt']}")
        print(f"   Hash: {result['hash']}")
        print("\n   (Store BOTH the salt and hash — you need both to verify later)")

    elif choice == "3":
        msg = input("Enter the password to verify: ")
        salt = input("Enter the stored salt: ").strip()
        expected = input("Enter the stored hash: ").strip()
        if sha256_verify(msg, salt, expected):
            print("\n✅ Match! The password is correct.")
        else:
            print("\n❌ No match. Incorrect password.")

    elif choice == "4":
        return
    else:
        print("Invalid choice.")


def main():
    print_header()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            aes_menu()
        elif choice == "2":
            rsa_menu()
        elif choice == "3":
            sha_menu()
        elif choice == "4":
            print("\nGoodbye! 🔐\n")
            break
        else:
            print("Invalid option. Please enter 1–4.")


if __name__ == "__main__":
    main()
