# broken_score.py
def main():
    score = float(input("Enter score: "))
    result = determine_score_category(score)
    print(result)


def determine_score_category(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid score"


main()

