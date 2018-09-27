



def int_number_game():
    correct_input = False
    while correct_input != True:
        user_input = input("Please enter the positive number: ")
        if int(user_input) > 0:
            print("The total sum from 1 to " +user_input + " is: "+str(sum_up(int(user_input))))
            print("The total sum of squares from 1 to "+ user_input + " is: " + str(sum_up_squares(int(user_input))))
            correct_input = True
        else:
            print("Could you please enter positive number once again")





def sum_up(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


def sum_up_squares(n):
    total = 0
    for i in range(n+1):
        total += i**2
    return total



int_number_game()