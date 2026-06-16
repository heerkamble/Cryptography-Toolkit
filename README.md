#  Cryptography Toolkit

A Python project implementing three fundamental cryptography algorithms from scratch — built as part of a cybersecurity internship.

---

##  Algorithms Implemented

| Algorithm | Type | Use Case |
|---|---|---|
| **AES-256** | Symmetric Encryption | File & message encryption |
| **RSA-2048** | Asymmetric Encryption | Secure key exchange, digital signatures |
| **SHA-256** | Hashing (one-way) | Password storage, file integrity |

---

##  Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/cryptography-toolkit.git
cd cryptography-toolkit
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the CLI
```bash
python cli.py
```

### 4. Run the Web UI
```bash
python app.py
```
Then open **http://127.0.0.1:5000** in your browser.

---

##  Screenshots

AES
<img width="1915" height="742" alt="Screenshot 2026-06-17 002429" src="https://github.com/user-attachments/assets/dc5390a6-716c-45bf-92dc-c61f99c4576b" />
<img width="1918" height="711" alt="Screenshot 2026-06-17 002450" src="https://github.com/user-attachments/assets/6571c499-eb6c-4062-b985-6f94d5a8103e" />
<img width="1913" height="483" alt="Screenshot 2026-06-17 002618" src="https://github.com/user-attachments/assets/b62e161f-0ba5-49fd-8887-f963ed8d9d51" />

RSA
<img width="1918" height="1000" alt="Screenshot 2026-06-17 002936" src="https://github.com/user-attachments/assets/88699beb-51b7-4401-a2b1-a130894b121b" />
<img width="1878" height="693" alt="Screenshot 2026-06-17 002949" src="https://github.com/user-attachments/assets/b045415a-e646-45c6-b24f-e226e1cf427f" />
<img width="1918" height="560" alt="Screenshot 2026-06-17 003007" src="https://github.com/user-attachments/assets/336c2904-c750-4ef8-b2ea-3fc047d68156" />

SHA-256
<img width="1918" height="847" alt="Screenshot 2026-06-17 003241" src="https://github.com/user-attachments/assets/372a857f-7c69-4309-acf3-b3a5ab73801c" />
<img width="1918" height="542" alt="Screenshot 2026-06-17 003320" src="https://github.com/user-attachments/assets/c4b358e4-6ac0-4cfb-b99f-3df287138172" />

---

##  Project Structure

```
cryptography-toolkit/
│
├── crypto_core.py      # Core algorithm implementations (AES, RSA, SHA-256)
├── cli.py              # Command-line interface
├── app.py              # Flask web application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Web UI frontend
└── README.md
```

---

##  How Each Algorithm Works

### AES (Advanced Encryption Standard)
- **Type:** Symmetric — same key encrypts and decrypts
- **Mode:** CBC (Cipher Block Chaining) with PKCS7 padding
- **Key size:** 256 bits (32 bytes)
- **IV:** Random 16-byte Initialization Vector generated per encryption
- **Use case:** Encrypting files, messages, database fields

### RSA (Rivest–Shamir–Adleman)
- **Type:** Asymmetric — public key encrypts, private key decrypts
- **Key size:** 2048 bits
- **Padding:** OAEP with SHA-256 (secure modern padding)
- **Use case:** Secure key exchange, TLS/HTTPS, email encryption (PGP)

### SHA-256 (Secure Hash Algorithm)
- **Type:** One-way hash (cannot be reversed)
- **Output:** Fixed 256-bit (64 hex char) fingerprint
- **Salting:** Random value prepended before hashing to prevent rainbow table attacks
- **Use case:** Password storage, file integrity checks, blockchain

---

##  Skills Demonstrated

- Symmetric and asymmetric encryption
- Cryptographic hashing and salting
- Secure coding with the `cryptography` library
- REST API design with Flask
- CLI design with Python

---

##  Disclaimer

This project is for **educational purposes only**. The implementations use production-grade libraries (`cryptography`) but the application itself is not hardened for production deployment.

---

##  References

- [Python `cryptography` library docs](https://cryptography.io/en/latest/)
- [NIST AES Standard](https://csrc.nist.gov/publications/detail/fips/197/final)
- [RSA Algorithm — Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
