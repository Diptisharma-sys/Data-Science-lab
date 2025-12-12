#A program that takes the age of an user, and gives their birth year, and if birth
#year was a leap year."""

from datetime import date

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

age = int(input("Enter your age: "))

current_year = date.today().year
birth_year = current_year - age

print("Your birth year is:", birth_year)

if is_leap_year(birth_year):
    print("Your birth year was a Leap year")
else:
    print("Your birth year was NOT a Leap Year ")
