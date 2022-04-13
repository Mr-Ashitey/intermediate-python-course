import random


def main():
    no_of_players = int(input("How many players are there? "))
    players = []
    for i in range(no_of_players):
        player_name = input("What is your name? ")
        players.append(player_name)

    team_name = input("What is your team name? ")
    dice_rolls = int(input('How many dice would you like to roll?'))
    dice_size = int(input('How many sides are the dice?'))
    dice_sum = 0

    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success')
        else:
            print(f'You rolled a {roll}')

    # for player in players:
    #     print(f'{player}')

    print(f'{team_name} have rolled a total of {dice_sum} dice')


if __name__ == "__main__":
    main()
