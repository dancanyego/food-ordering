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


# Defining the functions
def greet_customer(name):
    print(f"Welcome to {RESTURANT_NAME}!")
    print(f"My name is {name}, and I'll be your server today.")
    print("Please have a seat, and I'll be right back with your menu.")
    print("Here is our menu:")
    print(menu)


