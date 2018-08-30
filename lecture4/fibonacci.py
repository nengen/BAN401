a,b = 1,2

for i in range(10):
    print(a+b, end=" ")
    x = a
    a = b
    b = a + x

