
new_list = [11, 2, 4, 5, 6, 7, 8, 9, 10]

def odd_printer(list):
    for i in range(len(list)): #go through array, using len(list) as the stopping point, this makes it so we can do it on any list of any length
        if new_list[i]%2 != 0 and i%2 != 0: #first check if element is odd, then check if index is odd
            print(new_list[i]) #print element if both element and index is odd




odd_printer(new_list) #test the odd_printer on the given list