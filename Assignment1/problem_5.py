
from random import randint

def game():
    correctGuess = randint(1,10)
    guess = input("Please enter a number between 1 and 10 to play the game, or enter 0 to quit\n")

    while int(guess) != correctGuess:
        if (int(guess) == 0):
            break
        elif(int(guess) > correctGuess):
            guess = input("Your guess is too high. Please guess a lower number\n")
        elif(int(guess) < correctGuess):
            guess = input("Your guess is to low. Please guess a higher number\n")

    if(int(guess)== correctGuess):
        print("Congratulations you guessed the right number, the number was: " + str(correctGuess))
    else:
        print("You quit! Better luck next time")



game()