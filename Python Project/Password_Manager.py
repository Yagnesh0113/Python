class PasswordManager:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account, password):
        if account in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account] = password
            print("Account added successfully.")

    def remove_account(self, account):
        if account in self.accounts:
            del self.accounts[account]
            print("Account removed successfully.")
        else:
            print("Account not found.")

    def get_password(self, account):
        if account in self.accounts:
            return self.accounts[account]
        else:
            return None

    def list_accounts(self):
        if self.accounts:
            print("Accounts:")
            for account in self.accounts:
                print(account)
        else:
            print("No accounts found.")

def main():
    manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Account")
        print("2. Remove Account")
        print("3. Get Password")
        print("4. List Accounts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account = input("Enter account name: ")
            password = input("Enter password: ")
            manager.add_account(account, password)
        elif choice == '2':
            account = input("Enter account name: ")
            manager.remove_account(account)
        elif choice == '3':
            account = input("Enter account name: ")
            password = manager.get_password(account)
            if password:
                print("Password:", password)
            else:
                print("Account not found.")
        elif choice == '4':
            manager.list_accounts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
