#greenteapress
from array import *
from math import sqrt

i = 0



def mySqrt(a):
    x = 20
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
            break
        x = y


myData = [["a", "mysqrt(a)", "math.sqrt(a)", "diff"]]
tempArray = []

for i in range(4):
    tempArray.append("-"*len(myData[0][i]))
myData.insert(1,tempArray)



i = 1
while i<10:
    tempArray = []
    tempArray.append(str(i))
    mysq = round(mySqrt(i),2)
    sq = round(sqrt(i))
    diff = round(mysq - sq,2)
    tempArray.append(str(mysq))
    tempArray.append(str(sq))
    tempArray.append(str(diff))
    myData.insert(1+i, tempArray)
    i += 1




col_width = max(len(word) for row in myData for word in row) + 2  # padding
for row in myData:
    print ("".join(word.ljust(col_width) for word in row))