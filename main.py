import random

def play():
    possible_action = ["R", "P", "S"]
    computer = random.choice(possible_action)
    player = input('''Select a weapon: 'R' for Rock, 'P' for Paper, and 'S' for Scissor  ''').capitalize()

    while player not in possible_action:
        player = input('''Invalid weapon selected! Try again. Select a weapon: 'R' for Rock, 'P' for Paper, and 'S' for Scissor ''').capitalize()

    if player == computer:
        print(f'player ({player}) : CPU ({computer})')
        print('Tie!')
        return play()
    # R > S, S > P, P > R
    elif player == "R":
        if computer == "P":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")

    elif player == "S":
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "P":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")

    elif player == "P":
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")
play()