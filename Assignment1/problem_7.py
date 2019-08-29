revenueProductA = [700, 10000, 200, 33333, 4000, 666, 777, 150203] # from month 1 to 8
revenueProductB = [3333, 38586, 190293, 38383,70999, 13868, 113969, 40290] # from month 1 to 8




def maxRevenues(revenueProductA, revenueProductB):
    months = len(revenueProductA)
    highestRev = 0
    highestMonth = []
    for i in range (0,months):
        totalRev = revenueProductA[i] + revenueProductB[i]
        if totalRev > highestRev:
            highestRev = totalRev
            highestMonth.clear()
            highestMonth.append(str(i+1))
        elif totalRev == highestRev:
            highestMonth.append(str(i+1))

    print("${:,.2f} is the highest revenue over months".format(highestRev))
    print("That was the revenue for the following months: " + ' and '.join(highestMonth))



maxRevenues(revenueProductA,revenueProductB)