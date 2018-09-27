

nestedDict= { 'APL': {'startTime': 0, 'endTime':1, 'startValue':1500, 'endValue':2000,},
              'TRVX': {'startTime': 1, 'endTime':2, 'startValue':750, 'endValue':800},
              'AKA': {'startTime': 3, 'endTime':5, 'startValue':4500, 'endValue':5300},
              'NAS': {'startTime': 0, 'endTime':2, 'startValue':250, 'endValue':400},
              'TEL': {'startTime': 1, 'endTime':2, 'startValue':900, 'endValue':1300},
              }

def CAGR(startTime, endTime, startValue, endValue):
    pow = (1/(endTime-startTime))
    valueChange = endValue/startValue
    return (valueChange**pow)-1


def add_cagr(nestedDict):
    for dict in nestedDict:
        nestedDict[dict]['CAGR'] = CAGR(nestedDict[dict]['startTime'],nestedDict[dict]['endTime']
                                        ,nestedDict[dict]['startValue'], nestedDict[dict]['endValue'])

def print_highest_cagr(nestedDict):
    add_cagr(nestedDict)
    max = 0
    dicts = []
    nameOfMax = "None"
    for name, dict in nestedDict.items():
        for key, value in sorted(dict.items()):
            if key == 'CAGR' and value > max:
                max = value
                nameOfMax = name
    print("The company with the highest CAGR is: {0} with a CAGR of: {1}".format(nameOfMax,round(max,2)))



print_highest_cagr(nestedDict)


