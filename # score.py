# score.py
import random

def determine_grade(score):
    """
    Determine the grade based on the score.
    """
    if 0 <= score < 50:
        return "Fail"
    elif 50 <= score < 65:
        return "Pass"
    elif 65 <= score < 75:
        return "Credit"
    elif 75 <= score < 85:
        return "Distinction"
    elif 85 <= score <= 100:
        return "High Distinction"
    else:
        return "Invalid score"

def main():
    user_score = float(input("Enter your score: "))
    print(f"Result: {determine_grade(user_score)}")

    # Generate a random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}. Result: {determine_grade(random_score)}")

if __name__ == "__main__":
    main()