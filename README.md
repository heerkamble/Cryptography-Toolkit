# 🔐 Cryptography Toolkit

A Python project implementing three fundamental cryptography algorithms from scratch — built as part of a cybersecurity internship.

---

## 📌 Algorithms Implemented

| Algorithm | Type | Use Case |
|---|---|---|
| **AES-256** | Symmetric Encryption | File & message encryption |
| **RSA-2048** | Asymmetric Encryption | Secure key exchange, digital signatures |
| **SHA-256** | Hashing (one-way) | Password storage, file integrity |

---

## 🚀 Getting Started

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

## 🖥️ Screenshots

> *(Add screenshots of the web UI here after running it)*

---

## 📂 Project Structure

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

## 🔍 How Each Algorithm Works

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

## 🛡️ Skills Demonstrated

- Symmetric and asymmetric encryption
- Cryptographic hashing and salting
- Secure coding with the `cryptography` library
- REST API design with Flask
- CLI design with Python

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. The implementations use production-grade libraries (`cryptography`) but the application itself is not hardened for production deployment.

---

## 📚 References

- [Python `cryptography` library docs](https://cryptography.io/en/latest/)
- [NIST AES Standard](https://csrc.nist.gov/publications/detail/fips/197/final)
- [RSA Algorithm — Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
