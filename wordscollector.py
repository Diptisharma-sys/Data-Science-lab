# Unique Words Collector
#Take a paragraph input from the user. Split it into words, remove duplicates, sort them
#alphabetically, and count the total number of unique words.


paragraph = input("enter a paragraph (minimum 5 words)")
words = paragraph.split()

print("words:",words)

unique_words = set(words)

sorted_words = sorted(unique_words)
total_unique = len(unique_words)
print("\nUnique words (alphabetically):")
for words in sorted_words:
    print(words)

print("\nTotal number of unique words:", total_unique)
                        
                        