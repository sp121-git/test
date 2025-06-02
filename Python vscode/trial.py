import random
import time

# Dice art representation
dice_art = {
    1: ("┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘"),
    2: ("┌───────────┐",
        "│  ●        │",
        "│           │",
        "│        ●  │",
        "└───────────┘"),
    3: ("┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘"),
    4: ("┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘"),
    5: ("┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘"),
    6: ("┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘")
}

def roll_dice():
    """Function to roll dice and display results."""
    while True:
        # Get user input for number of dice
        while True:
            number_of_die = input("How many dice? ")
            if number_of_die.isdigit() and int(number_of_die) > 0:
                number_of_die = int(number_of_die)
                break
            print("Please enter a valid number greater than 0!")

        # Simulate rolling dice
        dice = [random.randint(1, 6) for _ in range(number_of_die)]

        # Print dice faces side by side
        print("\nRolling the dice...\n")
        time.sleep(1)
        for i in range(5):  # Each die face has 5 lines
            print("   ".join(dice_art[dice[j]][i] for j in range(number_of_die)))

        # Display total
        total = sum(dice)
        print(f"\nYour total roll: {total}")

        # Ask if the user wants to roll again
        roll_again = input("\nRoll again? Enter (Y/N): ").strip().lower()
        if roll_again == "y":  # ✅ Your line is now included!
            continue  # Repeats the loop to roll again
        else:
            print("Thanks for playing! Goodbye.")
            break  # Exit the loop if the user doesn't enter 'y'

# Run the dice rolling function
roll_dice()
