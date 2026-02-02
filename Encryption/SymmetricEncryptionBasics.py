# Symmetric Encryption
"""
XOR Operation:
The XOR (Exclusive-OR) operation is a logical operator that outputs true (1) only when its inputs differ—specifically,
when one is true and the other is false, but not both.
Often used in computing and cryptography, it acts as bitwise modulo 2 addition (0^0=0, 0^1=1, 1^0=1, 1^1=0),
meaning it returns 0 if inputs are the same and 1 if they are different.

% Modulo Operation:
modulo operator (%) calculates the remainder when one integer is divided by another.
Why 5%7 = 5 ? - Visualize it with Objects
Imagine you have 5 cookies and you want to give an equal amount to 7 people.
1) Since you don't have enough to give everyone a whole cookie, you give 0 cookies to each person.
2) How many cookies are left in your hand? All 5.
Thus, 6%3 = 0, 10%7 = 3


ord() and chr()
In Python, ord() is the short form of ordinal.
The function returns the integer representing the Unicode code point of a specified character.
It accepts a single-character string as an argument and acts as the inverse of the chr() function,
which converts an integer code point back to its character representation.
"""

# SYMMETRIC ENCRYPTION (same key for encrypt & decrypt)


def encrypt(plain_text, secret_key):
    encrypted = ""

    for i in range(len(plain_text)):
        # Convert characters to numbers, apply XOR
        # print("XOR will be happening between -> ", plain_text[i], secret_key[i % len(secret_key)])
        encrypted_char = ord(plain_text[i]) ^ ord(secret_key[i % len(secret_key)])
        encrypted += chr(encrypted_char)

    return encrypted


def decrypt(encrypted_text, secret_key):
    decrypted = ""

    for i in range(len(encrypted_text)):
        decrypted_char = ord(encrypted_text[i]) ^ ord(secret_key[i % len(secret_key)])
        decrypted += chr(decrypted_char)

    return decrypted


# ---- USAGE ----
message = "SARTHAK M. SHAH"
key = "secret"

cipher_text = encrypt(message, key)
print("Encrypted:", cipher_text)

original_text = decrypt(cipher_text, key)
print("Decrypted:", original_text)

"""
Sample Output:
Encrypted:  $1&-58E.\E';$+
Decrypted: SARTHAK M. SHAH
"""
