

num = [[2, 3, 4], [3, 4, 5], [5, 6, 8], [45, 67, 4]]



def sum_sublist(list):
    total = 0
    for i in list:
        total += i
    return total

def max_of_lists(list):
    max = 0
    for i in list:
        temp = sum_sublist(i)
        if temp > max:
            max = temp
    return max

def print_max_of_lists(list):
    print("The list provided to the function is" + str(list))
    print("The maximum sum of the list is: " + str(max_of_lists(list)))



print_max_of_lists(num)



