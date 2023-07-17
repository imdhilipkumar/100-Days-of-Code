
#HINT: You can call clear() to clear the output in the console.
from replit import clear

#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
#ask for name and input bid
bid={}
bid_continues=False
def find_highest_bid(bidding_records):
	high_bid=0
	winner=""
	for bidder in bidding_records:
		bid_amount=bidding_records[bidder]
		if bid_amount>high_bid:
			high_bid=bid_amount
			winner=bidder
	print((f"The winner is {winner} with a bid of ${high_bid}"))
	

while not bid_continues:
	name=input("What is your name : ")
	price=int(input("What is your Bid :"))
	#add name and bid into a dictionary as the the key and value
	bid[name]=price
	# ask if the there are other user wnat to bid
	should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
	if should_continue=="no":
		bid_continues=True
		find_highest_bid(bid)
	elif should_continue=="yes":
		clear()
