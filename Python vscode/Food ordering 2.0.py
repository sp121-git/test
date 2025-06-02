menu = {
    "Pizza": 9.99,
    "Burger": 5.99,
    "Fries": 3.99,
    "Soda": 1.99,
    "Burrito": 11.99,
    "Taco": 2.99}

cart=[]
total = 0
print("------Menu-------")
for item, value in menu.items():
    print(f"{item:10}: ${value} ")
print("------------------")

while True:
    order = input("Please select an item (press q to quit): ").capitalize()
    if order == "Q":
        break
    elif menu.get(order) is None:
        print("This item is invalid")
    elif menu.get(order) is not None:
        cart.append(order)
for order in cart:
    total += menu.get(order)
    print(order, end=" ")
    print()

print("------------------------")
print(f'Your total is: ${total}')
print("Thank You for Shopping! Enjoy the food!")