
from random import randint

def game():
    correctGuess = randint(1,10) #make an random integer between 1 and 10
    guess = input("Please enter a number between 1 and 10 to play the game, or enter 0 to quit\n") #get user guess

    while int(guess) != correctGuess: #while loop that continues until we either get the right guess or if the user presses 0
        if (int(guess) == 0): #if the user presses 0 we break
            break
        elif(int(guess) > correctGuess): #if the guess is too high we tell the user
            guess = input("Your guess is too high. Please guess a lower number\n")
        elif(int(guess) < correctGuess): #if the guess is too low we tell the user
            guess = input("Your guess is to low. Please guess a higher number\n")

    if(int(guess)== correctGuess): #if the user guessed the right number we congratulate the user
        print("Congratulations you guessed the right number, the number was: " + str(correctGuess))
    else: #if the user has not guessed the right input but hit 0 we tell them that they qiot
        print("You quit! Better luck next time")



game()