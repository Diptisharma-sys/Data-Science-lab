from bmi import bmi
def bmi_calculator(bmi):
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return category

category = bmi_calculator(bmi)

print("you are ",category)

