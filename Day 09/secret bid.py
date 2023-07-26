# secret bidding game 
from art import logo
print(logo)
# this line of code use to find who is the higher bitter
def find_highest_bid(bidding_record):
    winner=""
    high_bid=0
    for bidder in bidding_record:
        bid_price=bidding_record[bidder]
        if bid_price>high_bid:
            high_bid=bid_price
        winner=bidder
    print(f"The winner is {winner} with the bid of ₹{high_bid}")
        
# this line are template to repate the bid or not
bid_repeat=False
while not bid_repeat:
    name=input("enter your name :")
    price=int(input("enter the bid price: ₹"))

    #add name and bid into dictionary 
    bid={}
    bid[name]=price
    bid_continue=input("there is any other bidder is there press 'yes' or 'no' " ).lower()
    if bid_continue=="no":
        bid_repeat=True
        find_highest_bid(bid)
    elif bid_continue=="yes":
        bid_repeat=False