# Welcome to Higher Lower Game
# Display the art Logo 
from art import logo, vs
from game_data import data
# Generate the random account from the Game Data
import random
# to get the random data 
def random_account():
    return random.choice(data)
# format the account data into Printable Statement
def format_data(account):
    name=account["name"]
    descr=account["description"]
    country=account["country"]
    return f"{name}, a {descr}, from {country}"

# to check the compare of A and B
def check_point(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"
    
def play_game():
    print(logo)
    score=0    
    game_continue=True
    a_account=random_account()
    b_account=random_account()
    while game_continue:
        a_account = b_account
        b_account = random_account()
        while a_account==b_account:
            b_account=random_account()

        # format the account data into Printable Statement
        print(f"Compare A: {format_data(a_account)}")
        print(vs)
        print(f"Against B: {format_data(b_account)}.")
        # Ask the user to guess
        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers=a_account["follower_count"]
        b_followers=b_account["follower_count"]
        is_correct=check_point(guess,a_followers, b_followers)
        print(logo)
        if is_correct:
            score+=1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue=False
            print(f"Sorry, that's wrong. Final score: {score}")

play_game() 

