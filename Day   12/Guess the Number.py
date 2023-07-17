# guesss the number
from random import randint
from art import logo
print(logo)

EASY_LEVEL_DIFFICULTY = 15
MEDIUM_LEVEL_DIFFICULTY =10
HARD_LEVEL_DIFFICULTY = 5
# to check the function
def check_point(guess, result,turns):
    if result>guess:
        print("The Number is Too Low ! ...")
        return turns-1
    elif result<guess:
        print("The Number is Too High ! ...")
        return turns-1
    else:
        print(f"CONGRATS ..! You got it! The Number {guess} is Correct ! ....")
    
def difficulty():
    level=input("Choose a Difficulty. Type 'Easy' or 'Medium'  or 'Hard' :").lower()
    if level=="easy":
        return EASY_LEVEL_DIFFICULTY
    elif level=="medium":
        return MEDIUM_LEVEL_DIFFICULTY
    elif level=="hard":
        return HARD_LEVEL_DIFFICULTY    
# all the turns and guess result are global variable so i created the function clled play game 
def play_game():
    print("Welcome to the Number Guessing Game! ")
    # generate the random number
    result=randint(1,100)

    turns=difficulty() # global variable 
    
    #print(f"the Guess number is {result}")
    guess=0
    while result!=guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Guess the Number :"))
        turns=check_point(guess, result,turns)
        # to stop the loop
        if turns==0:
            print("OHHH...! You've run out of guesses, you Wasted.")
            return
        elif guess!=result:
            print("Guess AGAIN.....!")
play_game()
    
