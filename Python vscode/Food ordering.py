print("Pizza = 9.99")
print('Burger = 5.99')
print('Fries = 3.99')
print('Soda = 1.99')
print('Burrito = 11.99')
print('Taco = 2.99')

# Menu dictionary for easy reference
menu = {
    "Pizza": 9.99,
    "Burger": 5.99,
    "Fries": 3.99,
    "Soda": 1.99,
    "Burrito": 11.99,
    "Taco": 2.99
}

o1 = input("What would you like to order? (only two items can be ordered in single order): ").capitalize()

# Check if the order is valid
if o1 in menu:
    q1 = int(input('How many would you like?: '))
    total_cost1 = menu[o1] * q1
    print(f"Your total cost for {q1} {o1}/s is: ${total_cost1:.2f}")
else:
    print('Please enter a valid item from the menu!')

next1 = input('Would you like to add anything else? (Y/N): ')


if next1 == "Y" or next1 == 'y':
    o2 = input('what item would you like to add?: ').capitalize()
    if o2 in menu:
        q2 = int(input('How many would you like?: '))
        total_cost2 = menu[o2] * q2
        print(f"Your cost for {q2} {o2}/s is: ${total_cost2:.2f}")
        cart_total = total_cost1 + total_cost2
        print(f'So, your cart total is ${cart_total:.2f}')
        print('thank you for shopping!')
    else:
        print('Please enter a valid item from the menu!')
elif next1 == 'N' or next1 == 'n':
    print(f"Your cart total is: ${total_cost1:.2f}")
    print('thank you for shopping!')

