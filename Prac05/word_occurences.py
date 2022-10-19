"""
Word Occurrences
Estimate: 45 minutes
Actual:   52 minutes
"""

words = {}
user_string = input("Enter string: ")
word_frequency = user_string.split()
for frequency in word_frequency:
    amount = words.get(frequency, 0)
    words[frequency] = amount + 1

word_frequency = list(words.keys())
word_frequency.sort()

max_length = max((len(frequency) for frequency in word_frequency))
for frequency in word_frequency:
    print(f"{frequency:{max_length}} : {words[frequency]}")
