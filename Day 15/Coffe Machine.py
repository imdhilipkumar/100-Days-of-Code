# Coffe Machine 
from main import MENU, resources  
is_on=True
profit=0

#check resources
def check_sufficent_resources(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"Sorry there not enough {item}")
            return False
        return True
    
# process the coin 
def process_coin():
    print("Please Enter the Coin")
    total = int(input("How many Quaters : "))*0.25
    total += int(input("How many Dimes : "))*0.1
    total += int(input("How many Nikles : "))*0.05
    total+= int(input("How many Pennis : "))* 0.01
    return total
#Transcation 
def is_transcation_sucessful(money_receive, drink_cost):
    if money_receive>=drink_cost:
        change=round(money_receive-drink_cost , 2)
        print(f"Here Your Change {change} ")
        global profit
        profit+=drink_cost
        return True
    else:
        print("SOrry, Thats not Enough money , Money Refunded")
        return False  
def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here Your {drink_name} ☕  Enjoy !!! ")


while is_on:
    choice = input("What would you like ? (espresso / latte / cappuccino): ").lower()
    # turn of the machine user choosse the off keyword
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']} ml ")
        print(f"milk : {resources['milk']} ml")
        print(f"coffee : {resources['coffee']} g")
        print(f"profit : $ {profit}")
    else:
        drink=MENU[choice]
        if check_sufficent_resources(drink["ingredients"]):
            payment=process_coin()
            if is_transcation_sucessful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
        