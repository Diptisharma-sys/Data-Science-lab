"""2. Use a list comprehension to create a new list containing only the even numbers between 1 and 20, 
demonstrating a more concise and readable alternative to traditional loops."""


even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Even numbers between 1 and 20:", even_numbers)

