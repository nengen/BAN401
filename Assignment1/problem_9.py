



def int_number_game():
    correct_input = False #boolean for checking if correct input is given
    while correct_input != True:
        user_input = input("Please enter the positive number: ") #get user input
        if int(user_input) > 0: #if the number is positive
            print("The total sum from 1 to " +user_input + " is: "+str(sum_up(int(user_input)))) #call helper function sum_up to get the sum from 1 to user_input, cast it to a string and print it
            print("The total sum of squares from 1 to "+ user_input + " is: " + str(sum_up_squares(int(user_input)))) #same as above except we call the sum_up_squares function
            correct_input = True #end game
        else: #if the user input is negative or 0 we prompt the user for a new number
            print("Could you please enter positive number once again")





def sum_up(n):
    total = 0 #initialize int
    for i in range(n+1): #increment total with i until we get to the parameter n
        total += i
    return total #return total


def sum_up_squares(n):
    total = 0 #initialize int
    for i in range(n+1): #increment total with square of i until we get to the paramter n
        total += i**2
    return total #return total



int_number_game()