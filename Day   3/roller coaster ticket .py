print("Welcome to the Roller coaster ...!!!")
height=int(input("Enter your height in cm \n"))
cost=0
if height >=120:
    #print("Yare can Ride the Roller coster")
    age=int(input("Enter your age \n"))
    if age<12:
        cost+=5
        #print(f"you have to pay ${cost}.")
    elif age<=18:
        cost+=7
        print(f"your have to pay ${cost}.")
    elif age>=45 and age<=55:
        cost+=0
        #print(cost)
        print("everything is going to be OK . Have a free Ride on us")
    elif age>=18:
        cost+=12
    #    print(f"your have to pay ${cost}.")
    photo=input('Do you wanna Photo type"Y" or "N"').lower()
    if photo=="y":
        cost+=3
        print(f"the total bill is ${cost}")
    else:
        cost+=0
        print(f"the total bill is ${cost}")
else:
    print("Better luck Next Time. You need to Grow and You can't ride")