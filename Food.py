# Defining the global variables

RESTURANT_NAME = "The Hungry Crabs"

menu = {
    "sku1": {
        "name": "Hamburger",
        "price": 6.51
    },
    "sku2": {
        "name": "Cheeseburger",
        "price": 7.75
    },
    "sku3": {
        "name": "Milkshake",
        "price": 5.99
    },
    "sku4": {
        "name": "Fries",
        "price": 2.39
    },
    "sku5": {
        "name": "Sub",
        "price": 5.87
    },
    "sku6": {
        "name": "Ice Cream",
        "price": 1.55
    },
    "sku7": {
        "name": "Fountain Drink",
        "price": 3.45
    },
    "sku8": {
        "name": "Cookie",
        "price": 3.15
    },
    "sku9": {
        "name": "Brownie",
        "price": 2.46
    },
    "sku10": {
        "name": "Sauce",
        "price": 0.75
        }
}

app_actions = {
    "1": "Add a new menu item to cart",
    "2": "Remove an item from the cart",
    "3": "Modify a cart item's quantity",
    "4": "View cart",
    "5": "Checkout",
    "6": "Exit"
}

SALES_TAX_RATE = 0.07
cart = {}

def greet_customer(name):
    print(f"Welcome to {RESTURANT_NAME}!")
    print(f"My name is {name}, and I'll be your server today.")
    print("Feel free to order anything from the menu .")
    print("-"*20)
  
# Displaying the menu
def display_menu():
    print("Here is the menu:")
    print("-"*20)
    print("\n****Menu****\n")
    for sku in menu:
        parsed_sku = sku[3:]
        item = menu[sku]['name']
        price = menu[sku]['price']
        print("(" + parsed_sku + ")" " " + item +": $" + str(price))
    print("\n")
# Adding menu items to cart

def add_to_cart(sku,quantity = 1):
    if sku in menu:
        if sku in cart:
            cart[menu] += quantity
            
        else:
            cart[sku] = quantity      
        print("Added ", quantity, " of ", menu[sku]['name'], " to cart.")
    else:
        print("Failed to add ", quantity, "of", menu[sku]['name', " to cart"])
          

# removing from cart

def drop_item(sku):
    if sku in cart:
        item_name = menu[sku]['name']
        removed_item = cart.pop(item_name)
        print(f"\nRemoved", removed_item, "from the cart.")
    else:
        print(f"\nfailed ",removed_item,"not in Cart ")


