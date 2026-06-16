# =============================================================
#  app.py  –  Flask Web Interface for Crypto Toolkit
#  Run with: python app.py
#  Then open: http://127.0.0.1:5000
# =============================================================

import base64
from flask import Flask, render_template, request, jsonify, session
from crypto_core import (
    aes_generate_key, aes_encrypt, aes_decrypt,
    rsa_generate_keypair, rsa_encrypt, rsa_decrypt,
    sha256_hash, sha256_hash_with_salt, sha256_verify
)

app = Flask(__name__)
app.secret_key = "crypto-toolkit-secret-change-in-production"


# ── Home page ──────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


# ── AES routes ─────────────────────────────────────────────
@app.route("/aes/generate-key", methods=["POST"])
def aes_gen_key():
    key = aes_generate_key()
    key_b64 = base64.b64encode(key).decode()
    session["aes_key"] = key_b64          # store in session for this user
    return jsonify({"key": key_b64})


@app.route("/aes/encrypt", methods=["POST"])
def aes_enc():
    data = request.json
    plaintext = data.get("plaintext", "")
    key_b64 = data.get("key") or session.get("aes_key")
    if not key_b64:
        return jsonify({"error": "No AES key. Generate one first."}), 400
    try:
        key = base64.b64decode(key_b64)
        result = aes_encrypt(plaintext, key)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/aes/decrypt", methods=["POST"])
def aes_dec():
    data = request.json
    key_b64 = data.get("key") or session.get("aes_key")
    if not key_b64:
        return jsonify({"error": "No AES key. Generate one first."}), 400
    try:
        key = base64.b64decode(key_b64)
        plaintext = aes_decrypt(data["iv"], data["ciphertext"], key)
        return jsonify({"plaintext": plaintext})
    except Exception as e:
        return jsonify({"error": "Decryption failed. Wrong key or corrupted data."}), 400


# ── RSA routes ─────────────────────────────────────────────
@app.route("/rsa/generate-keys", methods=["POST"])
def rsa_gen_keys():
    private_pem, public_pem = rsa_generate_keypair()
    session["rsa_private"] = private_pem
    session["rsa_public"] = public_pem
    return jsonify({"private_key": private_pem, "public_key": public_pem})


@app.route("/rsa/encrypt", methods=["POST"])
def rsa_enc():
    data = request.json
    plaintext = data.get("plaintext", "")
    public_pem = data.get("public_key") or session.get("rsa_public")
    if not public_pem:
        return jsonify({"error": "No public key. Generate a key pair first."}), 400
    try:
        ciphertext = rsa_encrypt(plaintext, public_pem)
        return jsonify({"ciphertext": ciphertext})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/rsa/decrypt", methods=["POST"])
def rsa_dec():
    data = request.json
    ciphertext = data.get("ciphertext", "")
    private_pem = data.get("private_key") or session.get("rsa_private")
    if not private_pem:
        return jsonify({"error": "No private key. Generate a key pair first."}), 400
    try:
        plaintext = rsa_decrypt(ciphertext, private_pem)
        return jsonify({"plaintext": plaintext})
    except Exception as e:
        return jsonify({"error": "Decryption failed. Wrong key or corrupted data."}), 400


# ── SHA-256 routes ──────────────────────────────────────────
@app.route("/sha/hash", methods=["POST"])
def sha_hash():
    data = request.json
    text = data.get("text", "")
    use_salt = data.get("use_salt", False)
    if use_salt:
        result = sha256_hash_with_salt(text)
        return jsonify(result)
    else:
        return jsonify({"hash": sha256_hash(text)})


@app.route("/sha/verify", methods=["POST"])
def sha_verify():
    data = request.json
    match = sha256_verify(data["text"], data["salt"], data["hash"])
    return jsonify({"match": match})


# ── Run ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("🔐 Crypto Toolkit running at http://127.0.0.1:5000")
    app.run(debug=True)
