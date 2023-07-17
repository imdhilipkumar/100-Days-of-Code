#BMI calculator
print("Welcome to BMI calculator")
# bmi=weight in kg/ height in m
weight=float(input("Enter your weight in kg :"))
height=float(input("Enter your Height in meter :"))
BMI=float(weight/height**2)
print(round(BMI))