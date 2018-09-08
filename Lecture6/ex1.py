'''Write a function called nested_sum that takes a list of lists
of integers and adds up the elements from all of the nested lists. '''

def nestedLists(x):
    total = 0
    for nested in x:
        total += sum(nested)
    return total



