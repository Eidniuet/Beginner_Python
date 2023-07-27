import random

def get_choices():
    player =""
    option = ["rock", "paper", "scissors"]
    
    while player not in option:
        player = input("Enter a choice(rock, paper, scissors)").lower()
        print()
    computer = random.choice(option)
    choice = {"Player": player, "Computer": computer}
    return choice

def checking(player, computer):
    print (f"You choose {player}, Computer choose {computer}" )
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock")\
          or (player == "scissors" and computer == "paper"):
        return "Win"
    return "Lose"
x=get_choices()
result = checking(x["Player"],x["Computer"])
print (result)

"""
import random

def play():
    user = input('r', 'p', 's')
    computer = random.choice([('r', 'p', 's')])

    if is_win(user,computer):
        return 'Won!'
    if user == computer:
        return 'Tie!'
    return "Lost!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r')
"""