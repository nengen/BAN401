

def chop(x):
    del x[0]
    del x[-1]


t = [1, 2, 3, 4]
print(chop(t))
print(t)