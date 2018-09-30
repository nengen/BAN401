revenueProductA = [700, 10000, 200, 33333, 4000, 666, 777, 150203] # from month 1 to 8
revenueProductB = [3333, 38586, 190293, 38383,70999, 13868, 113969, 190293] # from month 1 to 8




def max_revenues(list1, list2):
    max_of_list1 = max(list1) #get the max value(s) of list 1
    max_of_list2 = max(list2) #get the max value(s) of list 2
    if max_of_list1 > max_of_list2: #compare the max of each list
        print( '${:,.2f}'.format(max_of_list1) + " is the highest revenue over months") #use.format to get a nice output
        print("That was the revenue for the following months: " + '{}'.format(
            str(format_custom_string(find_max_months(list1, max_of_list1))))) #format the list from the find_max_months function using format_custom_string
    else:
        print('${:,.2f}'.format(max_of_list2) + " is the highest revenue over months") #same as above
        print("That was the revenue for the following months: " '{}'.format(str(format_custom_string(find_max_months(list2, max_of_list2)))))



def find_max_months(list, max_rev): #use this instead of .index() to find multiple values
    indexes = [] #empty list
    for i in range(len(list)):
        if (list[i] == max_rev):#if we find the value append it to the empty list of indexes
            indexes.append(i+1)
    return indexes #return the index(es)


def format_custom_string(list):
    temp_str = "" #make an empty string
    for item in list:
        temp_str += (str(item)) #add item name
        temp_str += (" and ") #add and to separate the items
    temp_str = temp_str[:-5] #remove the extra and the for loop adds
    return temp_str #returns the string giving us a nice output


max_revenues(revenueProductA,revenueProductB)