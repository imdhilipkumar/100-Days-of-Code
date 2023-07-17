print("Welcome th Treasure Island.")
print("Your mission is to find the treasure")
choice1=input('You\'r at a cross road. where do you want to go ? "left" or "right" !\n').lower()
if choice1=="left":
    choice2=input('you\'r come to a lake . there is an island in the middle of the lake . type "wait" to wait for a boat . type "swi"m to swim accross tha lake\n').lower()
    if choice2=="wait":
        choice3=input('you\'r arrive at the island unharmed. Therre is a house with 3 Door . one Red , one Yellow and one Blue . whcih colur do you want to choose\n').lower()
        if choice3=="yellow":
            print("You reach the Treasure  ... Your Win !!!")
        elif choice3=="red":
            print("you fell in the deep hole , Game Over")
        elif choice3=="blue":
            print("Game over")
        else:
            print("you'r are againtst the rule of the Game, Game Over")
    elif choice2=="swim":
        print("Game Over , you are out of the game ")
    else:
        print("you'r are againtst the rule of the Game, Game Over")
elif choice1=="right":
    print("Game over, you choose the wrong way")
else:
    print("Game over")