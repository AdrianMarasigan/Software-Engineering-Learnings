import hashlib
from base64 import b64encode, b64decode
import os
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import argparse

# Clear the screen based on the OS
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

# Encryption function
def encrypt(plain_text, password):
    salt = get_random_bytes(AES.block_size)
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(private_key, AES.MODE_GCM)
    cipher_text, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))
    return {
        "cipher_text": b64encode(cipher_text).decode('utf-8'),
        "salt": b64encode(salt).decode('utf-8'),
        "nonce": b64encode(cipher.nonce).decode('utf-8'),
        "tag": b64encode(tag).decode('utf-8')
    }

# Decryption function
def decrypt(enc_dict, password):
    salt = b64decode(enc_dict["salt"])
    cipher_text = b64decode(enc_dict["cipher_text"])
    nonce = b64decode(enc_dict["nonce"])
    tag = b64decode(enc_dict["tag"])
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)
    return decrypted.decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description="AES 256 Encryption and Decryption Algorithm")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Specify 'encrypt' or 'decrypt' action")
    parser.add_argument("password", help="Password for encryption/decryption")

    args = parser.parse_args()

    if args.action == "encrypt":
        secret_message = input("Enter the Secret Message: ")
        encrypted = encrypt(secret_message, args.password)
        print("\nEncrypted:")
        print("---------------\n")
        print("\n".join("{}: {}".format(k, v) for k, v in encrypted.items()))

    elif args.action == "decrypt":
        encrypted_message = input("Enter the encrypted message (as a dictionary): ")
        try:
            encrypted_message_dict = eval(encrypted_message)
            decrypted = decrypt(encrypted_message_dict, args.password)
            print("\nDecrypted:")
            print("-----------------\n")
            print(decrypted)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
