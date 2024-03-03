def extract_name(email):
    """
    Extracts the name from an email address.

    Args:
    email (str): The email address.

    Returns:
    str: The extracted name.
    """
    username = email.split("@")[0]
    name_parts = username.split(".")
    name = " ".join(name_parts).title()
    return name


def main():
    print("Emails Program")
    email_dict = {}

    while True:
        email = input("Email: ")
        if email == "":
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation == "n":
            name = input("Name: ").strip().title()

        email_dict[email] = name

    print("\nStored Emails and Names:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()