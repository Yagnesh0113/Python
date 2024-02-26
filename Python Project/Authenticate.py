import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def load_credentials():
    try:
        with open('credentials.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_credentials(credentials):
    with open('credentials.json', 'w') as f:
        json.dump(credentials, f, indent=4)

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    credentials = load_credentials()
    credentials[username] = hashed_password
    save_credentials(credentials)
    print("Register Successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    credentials = load_credentials()
    if username in credentials and credentials[username] == hashed_password:
        print("Login Successful!")
    else:
        print("Invalid username or password")
    
def main():
    while True:
        print("\nWelcome to the Password Manager")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the Password Manager")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()