# Vigenere cipher encryption (non-alphabetic characters remain unencrypted)

# Define functions
def extend_key(plaintext, key):
    extended_key = ''
    key_length = len(key)
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            extended_key += key[i % key_length]
        else:
            extended_key += plaintext[i]
    return extended_key

def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = extend_key(plaintext, key).upper()
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            p = alphabet.index(plaintext[i].upper())
            k = alphabet.index(key[i])
            c = (p + k) % 26
            ciphertext += alphabet[c]
        else:
            ciphertext += plaintext[i]
    return ciphertext

# Main logic
plaintext = input("Enter the plaintext: ")  # e.g., "HELLO WORLD!"
key = input("Enter the key: ")  # e.g., "ABC"
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)