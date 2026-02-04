# Asymmetric Encryption
"""
Two keys created - Public and Private
1) Encryption uses public key
2) Decryption uses private key only

-You share public key with everyone
-Anyone can encrypt using public key
-Only you can decrypt using private key
-Used in HTTPS, SSH, email security
We’ll use RSA with one small library

📌 Key takeaway:
👉 Lock with 🔐 public key, unlock with 🔓 private key
"""

"""
SHA-256 (Secure Hash Algorithm 256-bit) is a widely used cryptographic hash function that converts input data of any 
size into a fixed-size 256-bit (32-byte) unique, irreversible "fingerprint" or digest. It is essential for ensuring data 
integrity, securing blockchain transactions (like Bitcoin), creating digital signatures, and storing passwords safely.

-> Key Aspects and Benefits of SHA-256
1) One-Way Function: It is computationally infeasible to reverse the algorithm to find the original data from its hash.
2) Collision Resistance: It is highly unlikely that two different inputs will produce the same 256-bit hash.

SHA-256 is used for: Creating randomness, Verifying message integrity, Mixing data securely
Why SHA-256? = Secure, Fast, Collision-resistant, Industry standard
"""

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 1. Generate key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

"""
The b prefix in Python creates a bytes object, which represents raw binary data. Cryptographic functions 
require bytes because encryption operates on exact byte values, not Unicode strings.
(Except that scenario, UTF-8 is the standard — always use it unless you have a reason not to.)
"""

# 2. Encrypt using PUBLIC KEY
"""
we use bytes of data (raw binary data) instead of string, as python ecodes it with unicodes and 
Crypto libraries don’t trust this ambiguity.
-Raw binary data
- Gives Exact values (0–255)
- No encoding confusion
- Required by encryption algorithms 
- Ex, b'Hello' = [72, 101, 108, 108, 111]
- Each number = ASCII value of a character.
"""
message = b"Hello Sarthak"

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Encrypted:", encrypted)

# 3. Decrypt using PRIVATE KEY
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted:", decrypted.decode())

