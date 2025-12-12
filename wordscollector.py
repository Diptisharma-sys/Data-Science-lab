paragraph = input("enter a paragraph (minimum 5 words)")
words = paragraph.split()

unique_words = set(words)

sorted_words = sorted(unique_words)
total_unique = len(unique_words)
print("\nUnique words (alphabetically):")
for word in sorted_words:
    print(word)

print("\nTotal number of unique words:", total_unique)
                        
                        