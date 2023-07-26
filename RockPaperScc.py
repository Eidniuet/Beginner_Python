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
    elif player == "rock":
        if computer == "scissors":
            return "Win"
        else:
            return "Lose"
    elif player == "paper":
        if computer == "rock":
            return "Win"
        else:
            return "Lose"   
    elif player == "scissors":
        if computer == "paper":
            return "Win"
        else:
            return "Lose"
x=get_choices()
result = checking(x["Player"],x["Computer"])
print (result)
