score_menu.py

import random
from score import determine_grade

def get_valid_score():
    """
    Get a valid score from the user (0-100 inclusive).
    """
    while True:
        try:
            score = float(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100 inclusive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_result(score):
    """
    Print the result of the given score.
    """
    print(f"Result: {determine_grade(score)}")

def show_stars(score):
    """
    Print stars equal to the score.
    """
    print("*" * int(score))

def main():
    score = get_valid_score()

    while True:
        print("\nMENU:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Thank you for using the score menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()