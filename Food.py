# Defining the global variables

RESTAURANT_NAME = "The Hungry Crabs"

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
cash_amount = 0
name = input("Hello, What's your name: ")

def greet_customer(cust_name):
    print(f"Welcome {cust_name} to {RESTAURANT_NAME}!")
    print("Feel free to order anything from the menu.")
    print("-" * 20)

def get_cash_amount():
    money = input(f"Hello {name} How much do you have of today: ")
    if int(money) > 0:
        cash_amount += money
        print(f"Money added to wallet your amount is {cash_amount}")
    else:
        print("Invalid amount ! try again")


# Displaying the menu
def display_menu():
    print("Here is the menu:")
    print("-" * 20)
    print("\n****Menu****\n")
    for sku in menu:
        parsed_sku = sku[3:]
        item = menu[sku]['name']
        price = menu[sku]['price']
        print(f"({parsed_sku}) {item}: ${price}")
    print("\n")

# Adding menu items to cart
def add_to_cart(sku, quantity=1):
    if sku in menu:
        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity
        print(f"Added {quantity} of {menu[sku]['name']} to cart.")
    else:
        print(f"Failed to add {quantity} of {menu[sku]['name']} to cart.")

# Removing item from cart
def drop_item(sku):
    if sku in cart:
        removed_name = menu[sku]['name']
        cart.pop(sku)
        print(f"Removed {removed_name} from the cart.")
    else:
        print(f"{menu[sku]['name']} is not currently in the cart.")

# Modifying cart items
def modify_item(sku, quantity):
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
            print(f"Modified {menu[sku]['name']} quantity to {quantity} in the cart.")
        else:
            drop_item(sku)
    else:
        print(f"{menu[sku]['name']} is not currently in the cart.")

# Viewing Cart
def display_cart():
    print('-' * 10)
    print("\n****Cart Contents****\n")
    
    subtotals = 0
    for sku in cart:
        if sku in menu:
            quantity = cart[sku]
            subtotals += menu[sku]['price'] * quantity
            print(f"{quantity} x {menu[sku]['name']}: ${menu[sku]['price'] * quantity}")
    tax = subtotals * SALES_TAX_RATE
    total = subtotals + tax
    print(f"Total: ${round(total, 2)}\n")

# Checking out
def check_out():
    print("****Checkout****")
    display_cart()
    print("Thank you for your order! Goodbye!\n")

# Getting user input for SKU and quantity
def get_sku_and_quantity(sku_prompt, quantity_prompt=None):
    item_sku = input(sku_prompt)
    item_sku = "sku" + item_sku
    if quantity_prompt:
        quantity = input(quantity_prompt)
        if not quantity.isdigit():
            quantity = 1
        quantity = int(quantity)
        return item_sku, quantity
    else:
        return item_sku

# Order loop
def order_loop():
    greet_customer(name)
    ordering = True

    while ordering:
        print("\n****Ordering Actions****\n")
        for number in app_actions:
            description = app_actions[number]
            print(f"({number}) {description}")
        
        response = input("Choose the number of action you want to take: ")
        if response == "1":
            display_menu()
            sku_prompt = "Please enter the SKU number for the item you want to order: "
            quantity_prompt = "Please enter the quantity you want to order [default is 1]: "
            ordered_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            add_to_cart(ordered_sku, quantity)
        elif response == "2":
            display_cart()
            sku_prompt = "Please specify the item SKU you want to remove from cart: "
            item_sku = get_sku_and_quantity(sku_prompt)
            drop_item(item_sku)
        elif response == "3":
            display_menu()
            sku_prompt = "Please enter the SKU number for the item you want to modify: "
            quantity_prompt = "Please enter the quantity you want to change to [default is 1]: "
            item_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            modify_item(item_sku, quantity)
        elif response == "4":
            display_cart()
        elif response == "5":
            check_out()
            ordering = False
        elif response == "6":
            print(f"Goodbye, {name}!")
            ordering = False
        else:
            print("Invalid command. Try again.")

order_loop()