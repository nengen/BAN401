

def write_to_file(n):
    with open("test.txt", mode="w+") as file:
        file.write(write_asterisks())
        for i in range(1,n+1):
            for j in range(1,n+1):
                file.write("{0:>2} times {1:>2} is {2:>3} \n".format(str(j),   str(i), str(j * i)))
            file.write(write_asterisks())




def write_asterisks():
    return ("*"*18+"\n")


write_to_file(10)




