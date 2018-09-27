revenueProductA = [700, 10000, 200, 33333, 4000, 666, 777, 150203] # from month 1 to 8
revenueProductB = [3333, 38586, 190293, 38383,70999, 13868, 113969, 40290] # from month 1 to 8

#TODO: fix format of output


def max_revenues(list1, list2):
    max_of_list1 = max(list1)
    max_of_list2 = max(list2)
    if max_of_list1 > max_of_list2:
        print( '${:,.2f}'.format(max_of_list1) + " is the highest revenue over months")
        print("That was the revenue for the following months: " + '{}'.format(
            str(find_max_months(list1, max_of_list1)).strip('[]')))
    else:
        print('${:,.2f}'.format(max_of_list2) + " is the highest revenue over months")
        print("That was the revenue for the following months: " + '{}'.format(str(find_max_months(list2, max_of_list2)).strip('[]')))



def find_max_months(list, max_rev): #use this instead of .index() to find multiple values
    indexes = []
    for i in range(len(list)):
        if (list[i] == max_rev):#if we find the value append it to the empty list of indexes
            indexes.append(i+1)
    return indexes #return the index(es)



max_revenues(revenueProductA,revenueProductB)