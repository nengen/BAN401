

num = [[2, 3, 4], [3, 4, 5], [5, 6, 8], [45, 67, 4]]



def sum_sublist(list):
    total = 0 #initalize an int
    for i in list: #loop through a sublist and add each number to total
        total += i
    return total #return total

def max_of_lists(list):
    max = 0 #initialize an int
    for i in list: #loop through the whole list
        temp = sum_sublist(i) #get the sum of sublist
        if temp > max: #if the sum of the sublist is bigger than what we have found before we set max to it
            max = temp
    return max

def print_max_of_lists(list):
    print("The list provided to the function is" + str(list)) #print first list
    print("The maximum sum of the list is: " + str(max_of_lists(list))) #print the max of the list using max_of_lists function



print_max_of_lists(num)



