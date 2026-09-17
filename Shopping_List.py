import os 
import time as t 
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent 
STOCK_FILE = BASE_DIR/"stock.txt"


#utilities
def proceed():
    proceed = input("press enter to continue...")

#catalogue
def view_dict(stock):
    for item in stock:
        print(item,"Price:",stock[item]["price"],"Quantity:",stock[item]["quantity"])

#memory setup
def get_storage():
    stock = {}
    with open(STOCK_FILE,"r") as f:
        for line in f:
            if not line.strip():
                continue
            item, price, quantity = line.strip().split(",")
            stock[item] = {
                "price": float(price),
                "quantity": int(quantity)
            }
    return stock
   
def update_stock_status(quantity,item,stock):
    stock[item]["quantity"]=-quantity
    if stock[item]["quantity"] == 0:
        del stock[item]
    
#adding items 
def get_item_details():
    os.system("clear")
    alert("Please input an item you want to add to stock:")
    name = input('').strip()

    alert("Please input the price of an item:")
    price = float(input("").strip())

    alert("Please input the avalible quantity of that item:")
    quantity = int(input("").strip())

    return name, price, quantity

def add_to_stock(stock,name,price,quantity):
    stock[name] = {
        "price": price, 
        "quantity": quantity
    }

def write_memory(stock):
    with open(STOCK_FILE, "w") as f:
        for item in stock:
            f.write(f"{item},{stock[item]["price"]},{stock[item]["quantity"]}\n")

def add_item(stock):
    name, price, quantity = get_item_details()
    add_to_stock(stock,name,price,quantity)
    write_memory(stock)
 
    alert("operation complete")


# buy items
def add_to_cart(cart,item,stock,quantity):
    cart[item] = {
        "price": stock[item]["price"],
        "quantity": quantity
    } 
     
def avalability(quantity,item,stock):

    if quantity > stock[item]["quantity"]:
        alert(f"Demand Exceeds Supply {stock[item]["quantity"]} purchased")
        quantity = stock[item]["quantity"]
        return quantity
    
    return quantity

def get_quantity():
    alert("quantity?")
    quantity = input('').strip()

    if not quantity:
        return 1

    return int(quantity)
    
def add_cart(cart,stock):
    for item in stock:
        alert(f"checkout {item} (Y/N)?")
        answer = input('').strip().upper()

        if answer == "Y":
            quantity = get_quantity()
            quantity = avalability(quantity,item,stock)
            add_to_cart(cart,item,stock,quantity)
            update_stock_status(quantity,item,stock)
            

def buy_items(cart,stock):
    add_cart(cart,stock)
    write_memory(stock)
    checkout(cart)


# calculations
def get_subtotal(cart):
    subtotal = 0
    for item in cart:
        subtotal += cart[item]["price"]*cart[item]["quantity"]
    return subtotal

def apply_discount(subtotal=100):
    print("\n")
    discounts  = [0,0.1, 0.2, 0.3, 0.4, 0.5]
    number = 1
    for discount in discounts:
        print(f"{discount} ({number})")
        number += 1
    alert("Please select discount")

    return int(input('')), discounts
     
def get_total(subtotal):
    value, discounts = apply_discount()
    total = subtotal - (subtotal * discounts[value-1])
    return total

def print_recipt(subtotal, total, cart):
    os.system("clear")
    alert("Thank for Visiting the Shrimp Market")
    for item in cart:
        print(f"{item} Price: ${cart[item]["price"]}  Quantity: {cart[item]["quantity"]}")
    print("\n")
    print(f"${subtotal}")
    print("\n")
    alert(str(f"${total}"))

def checkout(cart):
    subtotal = get_subtotal(cart)
    total = get_total(subtotal)
    print_recipt(subtotal,total,cart)


#UI
def menuinterface():
    alert("🦐Welcome to the Shrimp Market(We do not sell Shrimps)🦐")

    options = [
        "1. View Catalogue(1)",
        "2. Buy Item(2)",
        "3. Edit Stock(3)",
        "4. Exit(4)",
        "//Please select and option//"
        ]

    for option in options:
        print("\n")
        print(option)

def menu_choice(cart,stock):
    choice = int(input(''))
    if choice == 1:
        alert("Catalogue")
        os.system("clear")
        view_dict(stock)
    elif choice == 2:
        alert("Buy Item")
        os.system("clear")
        buy_items(cart,stock)
    elif choice == 3:
        alert("Inventory")
        os.system("clear")
        add_item(stock)
    elif choice == 4:
        alert("Goodbye")
        exit()
    else:
        alert("Invalid Input Please Enter Another")
        t.sleep(2)
        menu_choice()

def menu(cart,stock):
    while True:
        os.system("clear")
        menuinterface()
        menu_choice(cart,stock)
        proceed()

def alert(text):
    print("-"*len(text))
    print(text)
    print("-"*len(text))

#main
def main():
    stock = get_storage()
    cart = {}
    menu(cart,stock)

main()