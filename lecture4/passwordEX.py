password = "ban401"
guessedPassword = " "
while guessedPassword != password:
    guessedPassword = input("Please enter the correct password: \n")
    if guessedPassword == password:
        print("nice job, that is correct")
    else:
        print("sorry try again")