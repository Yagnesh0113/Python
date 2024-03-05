from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_message(message, password):
    salt = b'salt_'
    key = generate_key(password, salt)
    iv = b'initializationVe'  # 16 bytes for AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode()

def decrypt_message(encrypted_message, password):
    salt = b'salt_'
    key = generate_key(password, salt)
    iv = b'initializationVe'  # 16 bytes for AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    ciphertext = base64.b64decode(encrypted_message.encode())
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()
    return data.decode()

# Example usage:
password = input("Enter your password : ")
message = input("Enter Your Message : ")

# Encrypt message
encrypted_message = encrypt_message(message, password)
print("Encrypted message:", encrypted_message)

# Decrypt message
decrypted_message = decrypt_message(encrypted_message, password)
print("Decrypted message:", decrypted_message)
