string = input("Enter a string: ")

if string.isalpha():
    text = string.lower()
    
    if text == text[::-1]:  
        print("Palindrome")
    else:
        print("Not Palindrome")
else:
    print("Invalid")
