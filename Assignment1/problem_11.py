

nestedDict= { 'APL': {'startTime': 0, 'endTime':1, 'startValue':1500, 'endValue':2000,},
              'TRVX': {'startTime': 1, 'endTime':2, 'startValue':750, 'endValue':800},
              'AKA': {'startTime': 3, 'endTime':5, 'startValue':4500, 'endValue':5300},
              'NAS': {'startTime': 0, 'endTime':2, 'startValue':250, 'endValue':400},
              'TEL': {'startTime': 1, 'endTime':2, 'startValue':900, 'endValue':1300},
              } #the dictionary for the assignment

def CAGR(startTime, endTime, startValue, endValue):
    pow = (1/(endTime-startTime)) #calculate the power to use
    valueChange = endValue/startValue #calculate the change in value from start to end
    return (valueChange**pow)-1 #return the valuechange with ther power we found and substract 1, this is the formula for CAGR

#this adds cagr for each company in the dictionary
def add_cagr(nestedDict):
    for dict in nestedDict: #loop trough the nested dictionary
        nestedDict[dict]['CAGR'] = CAGR(nestedDict[dict]['startTime'],nestedDict[dict]['endTime']
                                        ,nestedDict[dict]['startValue'], nestedDict[dict]['endValue']) #add cagr to each dictionary using cagr function

def print_highest_cagr(nestedDict):
    add_cagr(nestedDict)#calculate CAGR and add it to each companies dictionary
    max = 0 #initialize max for holding the max value
    dicts = [] #initialize an empty dictionary
    nameOfMax = "None" #the string we will use for storing the name of the company with the highest CAGR
    for name, dict in nestedDict.items(): #loop throug each company name
        for key, value in sorted(dict.items()): #loop through each key in the dictionary
            if key == 'CAGR' and value > max: #if the key found is CAGR and the value is bigger than max
                max = value #set max to the value
                nameOfMax = name #set the nameOFMax to the name of the company
    print("The company with the highest CAGR is: {0} with a CAGR of: {1}".format(nameOfMax,round(max,2))) #print the company with the highest CAGR and format it



print_highest_cagr(nestedDict)


