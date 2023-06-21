
###########DEBUGGING#####################

#Describe Problem
def my_function():
    # the line of Debug is the for loop in this case we need to print the 20but the range(1,20) mean 20 is not includeed 
  #for i in range(1, 20):
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

#Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# in this line of code the loop index are start with (0, n-1) so that i changes the range(0,5)
#dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

#Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
# in these code the 1994 is not included in both if and else condition
#elif year > 1994:
elif year >= 1994:
  print("You are a Gen Z.")

#Fix the Errors
#this line of code simply metion input so it take as the str so convert in to intit gives perfect answer
age = input("How old are you?")
age = int(input("How old are you?"))
if age > 18:
#print(f"You can drive at age {age}.") # this line has the indentation error
    print(f"You can drive at age {age}.")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
#== represent the equal value = respresent the assign value
#word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    #this line nto included in the loop 
  #b_list.append(new_item)
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# odd or even Debug
number = int(input("Which number do you want to check?"))
# the bug is = is assign and == is equality means
#if number % 2 = 0:
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
#Debugging Leap Year 
#year = (input("Which year do you want to check?")) int is missed in this line 
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
## Debugging FizzBuzz 
for number in range(1, 101):
    # the statment should be in and 
    #if number % 3 == 0 or number % 5 == 0:
    if number % 3 == 0 and  number % 5 == 0:
        print("FizzBuzz")
# elif statment should be applied
    #if number % 3 == 0:
    elif number % 3 == 0:
        print("Fizz")
    #if number % 5 == 0:
    elif number % 5 == 0:
        print("Buzz")
    else:
        # list should be remove
        print(number)
  

