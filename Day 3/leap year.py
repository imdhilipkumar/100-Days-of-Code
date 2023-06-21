print("welcome to find Leap Year or Normal Year !...")
year=int(input("enter the year : "))
if year%4==0 or year%100!=0 and year%400==0:
    print("Leap Year")
else:
    print("NOt Leap Year")

