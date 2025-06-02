import random
import time

dice_art = {
    1:("┌───────────┐",
       "│           │",
       "│     ●     │",
       "│           │",
       "└───────────┘"),

    2:("┌───────────┐",
       "│  ●        │",
       "│           │",
       "│        ●  │",
       "└───────────┘"),

    3:("┌───────────┐",
       "│  ●        │",
       "│     ●     │",
       "│        ●  │",
       "└───────────┘"),

    4:("┌───────────┐",
       "│  ●     ●  │",
       "│           │",
       "│  ●     ●  │",
       "└───────────┘"),

    5:("┌───────────┐",
       "│  ●     ●  │",
       "│     ●     │",
       "│  ●     ●  │",
       "└───────────┘"),

    6:("┌───────────┐",
       "│  ●     ●  │",
       "│  ●     ●  │",
       "│  ●     ●  │",
       "└───────────┘")
}

dice = []
total = 0
while True:
    number_of_die = (input("How many dice?: "))
    while not number_of_die.isdigit():
        number_of_die = input("How many dice?: ")
        if not number_of_die.isdigit():
            print('Please enter a valid number!')
    print('Rolling the dice...')
    number_of_die = int(number_of_die)
    time.sleep(1)

    for die in range(number_of_die):
        dice.append(random.randint(1,6))

    for die in range(number_of_die):
        for line in dice_art.get(dice[die]):
            print(line)
        time.sleep(1)
        print('Rolling the dice...')
        time.sleep(1)

    # Print dice faces side by side
    #for i in range(5):  # Each die face has 5 lines
    #   print("   ".join(dice_art[dice[j]][i] for j in range(number_of_die)))

    for die in dice:
        total += die
    print(f'Counting total...')
    time.sleep(2)
    print(f'Your total roll: {total}')

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break





