
def print_x(n):
        for i in range(n):
            for j in range(n):
                if(j == i): #print first x in the row
                    print("#", end = '')
                elif(j == n-1-i): #print last x in row, decremented by i each loop
                    print("#", end= '')
                else:
                    print(" ", end = '') #print space
            print("") #print nothing so we get next line

print_x(5)
print_x(10)