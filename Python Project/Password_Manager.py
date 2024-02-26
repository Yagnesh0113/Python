class PasswordManager:
    """
        A simple password manager class that stores account names and passwords in a dictionary.

        Attributes:
            accounts (dict): a dictionary that stores account names as keys and passwords as values
    """

    def __init__(self):
        """
            Initialize the PasswordManager instance by creating an empty accounts dictionary.
        """
        self.accounts = {}

    def add_account(self, account: str, password: str):
        """
            Add a new account to the password manager.

            Args:
                account (str): the name of the account to add
                password (str): the password for the account

            Raises:
                ValueError: if the account already exists in the password manager
        """
        if account in self.accounts:
            raise ValueError(f"Account '{account}' already exists.")
        else:
            self.accounts[account] = password
            print(f"Added account '{account}' successfully.")

    def remove_account(self, account: str):
        """
            Remove an account from the password manager.

            Args:
                account (str): the name of the account to remove

            Raises:
                ValueError: if the account does not exist in the password manager
        """
        if account in self.accounts:
            del self.accounts[account]
            print(f"Removed account '{account}' successfully.")
        else:
            raise ValueError(f"Account '{account}' not found.")

    def get_password(self, account: str) -> str:
        """
            Retrieve the password for an account.

            Args:
                account (str): the name of the account

            Returns:
                str: the password for the specified account, or None if the account does not exist
        """
        if account in self.accounts:
            return self.accounts[account]
        else:
            return None

    def list_accounts(self):
        """
            List all the accounts in the password manager.
        """
        if self.accounts:
            print("Accounts:")
            for account in self.accounts:
                print(account)
        else:
            print("No accounts found.")


def main():
    """
        The main function that runs the password manager.
    """
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
                print(f"Password for '{account}': {password}")
            else:
                print(f"Account '{account}' not found.")
        elif choice == '4':
            manager.list_accounts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()