
from bmi import bmi  

def army_eligibility():
    age = int(input("Enter your age: "))
    user_bmi = bmi  

    print(f"Your BMI is: {user_bmi:.2f}")

    if 18 <= age <= 40 and 18.5 <= user_bmi <= 29.9:
        print("You are eligible for army entrance!")
    else:
        print("You are NOT eligible for army entrance.")
        if not (18 <= age <= 40):
            print("Reason: Age not within 18-40 years.")
        if not (18.5 <= user_bmi <= 29.9):
            print("Reason: BMI not within 18.5-29.9.")


army_eligibility()

