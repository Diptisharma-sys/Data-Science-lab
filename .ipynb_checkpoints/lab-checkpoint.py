a = (input("enter first  number"))
b = (input("enter another  number"))
if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
    a = float(a)
    b = float(b)
    sum = a+b
    if sum.is_integer():
        sum = int(sum)
    print("Sum:",sum)
else:
    print("invalid input, enter a integer")