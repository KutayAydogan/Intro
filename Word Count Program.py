import os
filename = r"C:\Users\kutay\Desktop\Intro\Story for Word Counting.md"
word_counts = {}
with open(filename, 'r') as file:
    text = file.read()
    text = text.lower()
    words = text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
for word, count in word_counts.items():
    print(f"{word}: {count}")