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
    tempArray.append(i)
    mysq = round(mySqrt(i),2)
    sq = round(sqrt(i))
    diff = mysq - sq
    str(mysq)
    str(sq)
    str(diff)
    tempArray.append(mysq)
    tempArray.append(sq)
    tempArray.append(diff)
    myData.insert(1+i, tempArray)
    i += 1



#todo, fix output to look better
max = len(myData[0])
max2 = len (myData)
string = []

for a in range(0,max):
    for b in range(0,max2):
        if len(string) == max2:
            string = []
        string.append(myData[b][a])
    print (string)