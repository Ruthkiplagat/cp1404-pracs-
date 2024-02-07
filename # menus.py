# menus.py
# Menu-Driven Program

# Function to display the menu
def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

# Function to get user's choice
def get_choice():
    return input(">>> ").upper()

# Function to greet the user
def greet_user(name):
    print("Hello", name)

# Function to bid farewell to the user
def say_goodbye(name):
    print("Goodbye", name)

# Main function
def main():
    name = input("Enter name: ")
    
    choice = ''
    while choice != 'Q':
        display_menu()
        choice = get_choice()

        if choice == 'H':
            greet_user(name)
        elif choice == 'G':
            say_goodbye(name)
        elif choice != 'Q':
            print("Invalid choice")

    print("Finished.")

if __name__ == "__main__":
    main()