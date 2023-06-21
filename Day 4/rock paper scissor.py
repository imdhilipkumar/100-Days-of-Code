import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img=[rock,paper,scissors]
#Write your code below this line 👇
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice>=3 or user_choice<0:
    print("You son of Bitch, You Lose")
else:
    print(img[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer Choose:", computer_choice )
    print(img[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("You Win!")
    elif computer_choice==0 and user_choice==2:
        print("You Lose!")
    elif user_choice>computer_choice:
        print("You Win!")
    elif user_choice<computer_choice:
        print("You Lose!")
    elif user_choice==computer_choice:
        print("What...!, IT's s Draw.!")
    
    