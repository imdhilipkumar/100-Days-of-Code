print("Welcome to the Tip Calculator. ")
bill=float(input("What was the total bill ? $"))
people_split=float(input("How many people to split the bill? "))
tip=float(input("WHat percentage tip would you like to give ? 10, 12 or 15 ? "))
tip_percent=tip/100 # to find percent
total_bill=tip_percent*bill+bill
final_bill=round(total_bill/people_split,2)
print(f"Each person should pay : {final_bill}")