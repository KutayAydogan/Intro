#import os
text = '''Once upon a time in a small village nestled between rolling hills and whispering forests, there lived a young girl named Elara. Elara was known for her boundless curiosity and adventurous spirit. She spent her days exploring the woods, climbing trees, and befriending creatures big and small.
One crisp autumn morning, Elara stumbled upon a hidden path she had never noticed before. Intrigued, she followed it deeper into the woods until she reached a clearing bathed in golden sunlight. In the center of the clearing stood a magnificent oak tree, its branches stretching towards the sky like reaching fingers.
As Elara approached the tree, she noticed something shimmering amidst the roots. It was a tiny key, glinting with an otherworldly light. Without hesitation, Elara picked up the key and slipped it into her pocket.
That night, as the moon rose high above the village, Elara's dreams were filled with whispers of adventure and mystery. When she awoke, she knew she had to return to the oak tree and unlock its secrets.
With the key clutched tightly in her hand, Elara made her way back to the clearing. As she reached the oak tree, she noticed a small door nestled within its trunk, almost hidden from sight. Excitement coursing through her veins, Elara inserted the key into the lock and turned it with a click.
The door swung open, revealing a staircase spiraling down into darkness. Heart pounding with anticipation, Elara descended into the depths below.
At the bottom of the staircase, Elara found herself in a vast underground chamber, illuminated by the soft glow of luminescent mushrooms. Strange plants adorned the walls, their leaves shimmering with iridescent colors.
But the most wondrous sight of all was a shimmering pool at the center of the chamber, its waters reflecting the stars above. Elara approached the pool, drawn by its mesmerizing beauty.
As she gazed into the depths, she saw visions of distant lands and forgotten realms. She saw forests older than time itself, and mountains that reached the heavens. She saw creatures of myth and legend, dancing beneath the moonlight.
And in that moment, Elara knew that her thirst for adventure would never be quenched. For she had unlocked a world beyond imagination, a world waiting to be explored.
With a smile on her lips and a sparkle in her eye, Elara stepped into the pool, ready to embark on her greatest adventure yet.
And as she disappeared beneath the surface, the whispers of the oak tree echoed in her ears, promising wonders untold and mysteries yet to be unraveled.
For Elara had found the key to the realm of dreams, and nothing would ever be the same again.'''
text = text.lower()
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"{word}: {count}")
#C:\Users\kutay\Desktop\Intro\Story for Word Counting.md
