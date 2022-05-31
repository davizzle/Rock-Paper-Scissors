import random

def play():
    possible_action = ["Rock", "Paper", "Scissor"]
    computer = random.choice(possible_action)
    player = input(''''Select a weapon: 'Rock', 'Paper', or 'Scissor' ''').capitalize()

    while player not in possible_action:
        player = input('''Ínvalid weapon selected! Try again. Select a weapon: 'Rock', 'Paper', or 'Scissor' ''').capitalize()

    if player == computer:
        print(f'player ({player}) : CPU ({computer})')
        print('Tie!')
        return play()
    # Rock > Scissor, Scissor > Paper, Paper > Rock
    elif player == "Rock":
        if computer == "Paper":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "Scissor":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")

    elif player == "Scissor":
        if computer == "Rock":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "Paper":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")

    elif player == "Paper":
        if computer == "Scissor":
            print(f'player ({player}) : CPU ({computer})')
            print("You lose!")
        if computer == "Rock":
            print(f'player ({player}) : CPU ({computer})')
            print("You win!")
play()