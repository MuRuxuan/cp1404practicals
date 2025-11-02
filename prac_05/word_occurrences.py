"""
Count the occurrences of each word in a user-input text.
Words are split by whitespace, and results are sorted alphabetically with aligned formatting.
"""

def main():
    """Coordinate input collection, word counting, and result display."""
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    if not word_counts:
        print("No words entered.")
        return
    max_word_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{max_word_length}} : {word_counts[word]}")

def count_word_occurrences(text):
    """Count how many times each word appears in the input text using count()."""
    unique_words = sorted(set(text.split()))
    word_occurrences = {}
    for word in unique_words:
        word_occurrences[word] = text.split().count(word)
    return word_occurrences

main()