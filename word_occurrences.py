"""
Word Occurrences
Estimate: 25 minutes
Actual:   30 minutes
"""


def count_word_occurrences(text):
    word_counts = {}
    words = text.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def main():
    print("Word Occurrences")
    user_input = input("Enter a string: ")

    word_counts = count_word_occurrences(user_input)

    # Find the longest word length for formatting
    longest_word_length = max(len(word) for word in word_counts.keys())

    # Sort the word counts by keys
    sorted_word_counts = sorted(word_counts.items())

    # Print the word counts with aligned formatting
    for word, count in sorted_word_counts:
        print(f"{word:>{longest_word_length}} : {count}")


if __name__ == "__main__":
    main()
