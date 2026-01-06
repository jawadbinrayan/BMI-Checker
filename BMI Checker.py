height = int(input("Enter your height in meter:"))
weight = int(input("Enter your weight in kilogram:"))
BMI = weight(height**2)
print("Your BMI is", BMI)
if BMI <= 18.9:
    print("You are underweight")
elif BMI <= 24.4:
    print("You are healthy")
elif BMI <= 29.4:
    print("You are overweight")
elif BMI < 34.4:
    print("You are obese")
elif BMI <= 39.4:
    print("You are severely obese")
