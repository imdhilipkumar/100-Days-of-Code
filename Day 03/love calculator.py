# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine=name1+name2
lower_combine=combine.lower()
#print(lower_combine)

t=lower_combine.count("t")
r=lower_combine.count("r")
u=lower_combine.count("u")
e=lower_combine.count("e")
first_digit=t+r+u+e

l=lower_combine.count("l")
o=lower_combine.count("o")
v=lower_combine.count("v")
e=lower_combine.count("e")
second_digit=l+o+v+e

love_score=int(str(first_digit)+str(second_digit))
#print(love)
if love_score<10 or love_score>90:
    print(f"You are score is {love_score}, you go together like coke and mentos")
elif love_score >=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}")