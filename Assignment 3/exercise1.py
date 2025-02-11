import re

with open('/Users/vladchaika/Desktop/NSSA220/Week10/story.txt', 'r') as file: # Open and read the file
    text = file.read()

words = re.findall(r'\b[a-zA-Z]+\b', text) # Remove non-alphabetical characters and split text into words while preserving case

word_count = {} #Initialize an empty dictionary 

for word in words: # Count each word manualy
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count, key=str.lower): # Sorting in case-insentitive way
    print(f"{word} : {word_count[word]}")