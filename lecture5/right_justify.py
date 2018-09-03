

def rightJustify(s):
    while len(s) < 70:
        s = " " + s
    return s


print(rightJustify("world"))
print(rightJustify("helloworld"))
