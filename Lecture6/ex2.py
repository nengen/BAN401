'''Write a function called cumsum that takes a list of numbers and returns
the cumulative sum; that is, a new list where the ith element is the sum
of the first i+1 elements from the original list. For example:'''

def cumsum(x):
    total = 0
    result = []
    for i in x:
        total += i
        result.append(total)
    return result

t = [1, 2, 3]
print(cumsum(t))