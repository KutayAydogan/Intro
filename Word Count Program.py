import os
filename = r"C:\Users\kutay\Desktop\Intro\Story for Word Counting.md"
if not os.path.isfile(filename):
    print(f"Error: File '{filename}' not found.")
else:
    word_counts = {}
    with open(filename, 'r') as file:
        text = file.read()
        text = text.replace(",","")
        text = text.replace(".","")
        text = text.lower()
        words = text.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    for word, count in word_counts.items():
        print(f"{word}: {count}")