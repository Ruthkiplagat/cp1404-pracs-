# passwords_stars.py

import getpass

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    password = getpass.getpass("Enter your password: ")
    while len(password) < 5:
        print("Password must be at least 5 characters long.")
        password = getpass.getpass("Enter your password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

if __name__ == "__main__":
    main()
