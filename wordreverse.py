"""5. Word Reverser Game
Ask the user for a list of words. Reverse each word only if its length is even. Print the new list of
words after processing."""

words = input("Enter words separated by spaces: ").split()

new_list = []

for word in words:
    if len(word) % 2 == 0:
        new_list.append(word[::-1])
    else:
        new_list.append(word)
print("Processed Words:")
print(new_list)