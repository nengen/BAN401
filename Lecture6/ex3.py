'''Write a function called middle that takes a list and returns a new list
that contains all but the first and last elements. '''

def middle(x):
    return x[1:-1]

t = [1, 2, 3, 4]
print(middle(t))
