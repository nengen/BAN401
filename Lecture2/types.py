#Here double means twice not the double type

string = "2.555"
doubleOfString = float(string) #converts the string to a float if possible
doubleString = 2*doubleOfString
print(doubleOfString)
print(doubleString)


#Same for string

s = "123"
intOfString = int(s)
doubleOfS = intOfString*2
print(doubleOfS)


#String to float to int

x = "1.23"
stringToFloatToInt = int(float(x))
double = stringToFloatToInt * 2
print(double)

#Int to string (same for float just use the float keyword)
int = 3
randomString = "I have " + str(int) + " cats"
print(randomString)