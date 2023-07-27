import random

def guess_number(high):
    low = 1
    random_number = random.randint(low,high)
    guess = None
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between {low} and {high}: '))
            if guess < low or guess > high:
                print(f'Please enter a number between {low} and {high}.')
            elif guess < random_number:
                low = guess
                print('Too low. Try again.')
            elif guess > random_number:
                high = guess
                print('Too high. Try again.')
        except ValueError:
            print("Invalid Value")

    print(f'Correct {guess}')

def computer_guess(high):
    low = 1
    feedback = ""
    
    while feedback !="c":
        guess = random.randint(low, high)  
        feedback = input(f'Is {guess} too low (L), too high (H) or correct (C)').lower()
        if feedback == "l":
            low = guess + 1
        elif feedback == "h":
            high = guess -1
        break
      
    print(f'{guess} is correct.')
