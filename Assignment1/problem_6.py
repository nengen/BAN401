

def write_to_file(n):
    with open("test.txt", mode="w+") as file: #open the file test.txt, if it doesnt exist then it makes a file names test.txt. We then tell the computer to open it for reading and writing using w+ as the mode
        file.write(write_asterisks()) #call the asterisks function to print the asterisks
        for i in range(1,n+1): #outer loop for the value which we multiply by
            for j in range(1,n+1): #inner loop for the value which is the 1-10 for each outer loop number
                file.write("{0:>2} times {1:>2} is {2:>3} \n".format(str(j),   str(i), str(j * i))) #write to the file using .format for a good output
            file.write(write_asterisks()) #write asterisks at end of each times table




def write_asterisks():
    return ("*"*18+"\n") #returns the right amount of asterisks for the times table


write_to_file(10)




