#import os
words = ("Mom", "Dad", "Brother", "Sister", "Cousin", "Cousin", "Cousin", "Sister", "Brother")
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"{word}: {count}")
#C:\Users\kutay\Desktop\Intro\Story for Word Counting.md
