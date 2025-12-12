    """ A program that computes the Body Mass Index (BMI) of a user, taking their
    height and weight as input. The program should allow the user to enter their
    height in either feet/inches or centimeters and their weight in either kilograms or
    pounds.
    Extend the program to convert BMI into a category based on standard criteria:
    ■ Underweight: < 18.5
    ■ Normal weight: 18.5 - 24.9
    ■ Overweight: 25 - 29.9
    ■ Obese: ≥ 30 """

    def BMI (weight,height):
        bmi = weight /(height **2)
    

        print ("enter your weight")
        print("1.enter your weight in kg ")
        print("2.enter your weight in pounds")

        weight_choice = int(input("enter either choice 1 or 2"))
        if weight_choice == 1:
            weight_kg = float(input("Enter weight in kg: "))

        elif weight_choice == 2:
            pounds = float(input("Enter weight in pounds: "))
            weight_kg = pounds * 0.453592  

    
        print("enter your height")
        print("1.enter your height in ft or inches")
        print("2.enter your height in cm")

        height_choice = input("Enter choice (1 or 2): ")

        if height_choice == "1":
            feet = float(input("Enter feet: "))
            inches = float(input("Enter inches: "))

            total_inches = feet * 12 + inches
            height_m = total_inches * 0.0254

        elif height_choice == "2":
            height_cm = float(input("Enter height in cm: "))
            height_m = height_cm / 100
        else:
            print("Invalid Choice. Please enter 1 or 2 only.")
            exit()

        bmi = BMI(weight_kg, height_m)
        print("\nYour BMI is:", round(bmi, 2))
        return bmi








