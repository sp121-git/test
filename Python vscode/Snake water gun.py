#SNAKE WATER GUN GAME
import random
import time
options = ("snake", "water", "gun")
player_score = 0
comp_score = 0
running = True
print('snake water gun game')

while running:
    player = None
    computer = random.choice(options)

    while player not in options and player != "q":
        player = input('Please choose between snake, water or gun (Press q to quit): ').lower()

    if player == 'q':
        break

    print(f'Player: {player}')
    time.sleep(1)
    print(f'Computer: {computer}')

    if player == computer:
        time.sleep(1)
        print('It is a Tie!')
        time.sleep(1)
        print(f"Scores are Computer:{comp_score} and Player:{player_score} ")

    elif player == 'snake' and computer == 'water':
        time.sleep(1)
        print("You win!")
        player_score += 1
        time.sleep(1)
        print(f"Scores are Computer:{comp_score} and Player:{player_score} ")

    elif player == 'gun' and computer == 'snake':
        time.sleep(1)
        print("You win!")
        player_score += 1
        time.sleep(1)
        print(f"Scores are Computer:{comp_score} and Player:{player_score} ")

    elif player == 'water' and computer == 'gun':
        time.sleep(1)
        print("You win!")
        player_score += 1
        time.sleep(1)
        print(f"Scores are Computer:{comp_score} and Player:{player_score} ")
    else:
        time.sleep(1)
        print('You lost!')
        comp_score += 1
        time.sleep(1)
        print(f"Scores are Computer:{comp_score} and Player:{player_score} ")

print('Thank you for playing!')