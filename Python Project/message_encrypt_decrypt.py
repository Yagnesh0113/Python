def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if character is alphabetic
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(encrypted_message, key):
    return encrypt_message(encrypted_message, -key)

if __name__ == "__main__":
    message = input("Enter The Message : ")
    key = int(input("Enter The number : "))
    if key != 0:
        encrypted_message = encrypt_message(message, key)
        print("Encrypted message:", encrypted_message)

        decrypted_message = decrypt_message(encrypted_message, key)
        print("Decrypted message:", decrypted_message)
    else:
        quit()
