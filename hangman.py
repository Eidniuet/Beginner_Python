import random
from word import words
import string

# find one word
def get_valid_word(words): 
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 5
    while len(word_letters) >0 and lives >0:
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -=1
                print ('Letter is not in word')
        
        elif user_letter in used_letters:
            print("Used character.")
        else:
            print("Invalid character")
    if lives ==0:
        print ("Your died, the word was ", word)
    else:
        print ("You guessed the word ",  word, "!!" )

hangman()