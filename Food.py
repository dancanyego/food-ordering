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
    name = input("Hellow Whats your name")
    print(f"Welcome {name} to {RESTURANT_NAME}!")
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
    """
    Remove an item from the cart.
    
    :param string sku: The input SKU number to remove from the cart.
    """
    if sku in cart:
        removed_val = cart.pop(sku)
        print(f"Removed", removed_val['name'], "from the cart.")
    else:
        print("I'm sorry.", removed_val['name'], "is not currently in the cart.")

# modify the cart items 

def modify_item(sku,quantity):
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
            print("Modified", menu[sku]['name'], "quantity to ", quantity, " in the cart.")
        else:
            drop_item(sku)
    else:
        print(f"I'm sorry.", menu[sku]['name'], "is not currently in the cart.")

# view Cart

def display_cart():
    print('-'*10)
    print("\n****Cart Contents****\n")
    
    subtotals = 0
    for sku in cart:
        if sku in menu:
            quantity = cart[sku]
            subtotals += menu[sku]['price'] * quantity
            print(quantity, " X ",menu[sku]['name'])

    tax = subtotals * SALES_TAX_RATE
    total = subtotals + tax
    print("Total : $ ", round(total,2))
    print("\n")

# cheking out

def check_out():
    print("****Checkout****")
    display_cart()
    print("Thank you for your order! Goodbye!")
    print("\n")

# get user input

def get_sku_and_quantity(sku_prompt,quantity_prompt = None):
    """
    Get input from the user.
    
    :param string sku_prompt: A string representing the prompt to display to the user before they enter the SKU number.
    :param string quantity_prompt: A string representing the prompt to display to the user before they enter the quantity.
        This defaults to None for cases where quanitity input is not needed.
        
    :returns: The full sku# value and the quantity (in certain cases)
    """
    
    item_sku = input(sku_prompt)

    # concatinate sku to the string number
    item_sku = "sku" +item_sku
    if quantity_prompt:
        quantity = input(quantity_prompt)
        # check if the user has typed a digit
        if not quantity.isdigit():
            quantity = 1 # default value if not digit
        quantity = int(quantity)

        return item_sku,quantity

    # when quantity is none no need to get the input of quantity
    else:
        return item_sku



