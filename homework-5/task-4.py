from functools import reduce

sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."

words = sentence.replace(".", "").split()

lower_words = list(map(lambda w: w.lower(), words))

word_count = reduce(
    lambda acc, w: acc | {w: acc.get(w, 0) + 1},
    lower_words,
    {}
)

most_used = max(word_count, key = lambda w: word_count[w])

long_words = list(filter(lambda w: len(w) > 3, lower_words))

print("Words:", words)
print("Lowercase:", lower_words)
print("Word count:", word_count)
print("Most frequent word:", most_used)
print("Words > 3 letters:", long_words)