"""
Word Occurrences
Estimate: 30minutes
Actual: 25 minutes
"""
text = input("Text:")

word_counts={}
words = text.split()

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_word_length = max(len(word) for word in word_counts)
sorted_words = sorted(word_counts.keys())

for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_counts[word]}")