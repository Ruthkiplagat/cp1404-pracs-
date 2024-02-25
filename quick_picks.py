import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_NUMBERS_PER_LINE = 6

def generate_quick_pick():
    """Generate a single quick pick (line of numbers)"""
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_NUMBERS_PER_LINE))

def main():
    num_quick_picks = int(input("How many quick picks? "))

    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(map(str, quick_pick)))

if __name__ == "__main__":
    main()