#BMI 
print("Welcome to the BMI 2.0 !")
weight =float(input("enter your weight : "))
height =float(input("enter the height in meter :"))
bmi=(weight/height**2)
BMI=round(bmi,2)
#print((f"your BMI score is {BMI}"))
# range calculator
if BMI<18.5:
    print(f"you BMI score is {BMI},you are under Weight")
elif BMI<25:
    print(f"you BMI score is {BMI} ,you are Normal Weight")
elif BMI<30:
    print(f"you BMI score is {BMI} ,you are Over weight")
elif BMI<35:
    print("you BMI score is {BMI} ,you are Obese")
else:
    print(f"you BMI score is {BMI} ,you are extreme obese")
    
    
    
print("thank you for using our website th check your BMI hope you statisfied with your score  ")