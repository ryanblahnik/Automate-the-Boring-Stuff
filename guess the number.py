# This is a guess the number game
import random
print('Hello. What\'s your name?')
name = input()
secret_number = random.randint(1, 101)
print('Well, ' + name + ', I\'m thinking of a number between 1 and 100.')

# Ask the player to guess 6 times
for guesses_taken in range(1, 2):
    print('Take a guess.')
    guess = int(input())
    if guesses_taken == 6 and guess != secret_number:
        print('No! It was ' + str(secret_number) + '. You lose...')
        
    elif guess < secret_number:
        print('That\'s too low.')
    elif guess > secret_number:
        print('Too high.')
    else:
        break # This condition is a correct guess

for guesses_taken in range(2, 7):
    print('Take another guess.')
    guess = int(input())
    if guesses_taken == 6 and guess != secret_number:
        print('No! It was ' + str(secret_number) + '. You lose...')
        
    elif guess < secret_number:
        print('That\'s too low.')
    elif guess > secret_number:
        print('Too high.')
    else:
        break # This condition is a correct guess

if guess == secret_number:
    print('Nice, ' + name + ', you got it in ' + str(guesses_taken) + ' guesses. I lose...')
    
