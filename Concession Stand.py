menu = {"popcorn" : 6.00,
        "pizza" : 3.00,
        "nachos" : 4.50,
        "fries" : 2.50,
        "chips" : 1.00,
        "pretzel" : 3.50,
        "soda" : 3.00,
        "lemonade" : 4.25}

cart = []
total = 0

print("---------MENU---------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("This item isn't on the menu")

for food in cart:
    total += menu.get(food)
print()
print(cart)
print(f"Your total is ${total:.2f}")
