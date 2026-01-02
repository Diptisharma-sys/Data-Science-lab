"""Write a Python script that takes a list of student marks and sorts them in 
descending order (highest to lowest) using either the sorted() function or the .sort() method."""


marks = input("Enter marks separated by space: ").split()

marks = [int(m) for m in marks]

sorted_marks = sorted(marks, reverse=True)

print("Marks in descending order:", sorted_marks)

