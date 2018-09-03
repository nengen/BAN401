def printPlus():
    print("+", end = ' ')

def printDash():
    print(" - ", end = ' ')

def printBar():
    print("|", end = ' ')

def printEnd():
    print()

def printNothing():
    return


def doTwice(function):
    function()
    function()

def doFour(function):
    doTwice(function)
    doTwice(function)



def oneFourOne(func1, func2, func3):
    func1()
    doFour(func2)
    func3()


def printVerticalBar():
    printBar()
    print("               ", end = ' ')



def printHoriz(n):
    for i in range(0,n):
        if(i == 0):
            oneFourOne(printPlus,printDash, printPlus)
        else:
            oneFourOne(printNothing, printDash, printPlus)
        oneFourOne(printNothing, printDash, printPlus)
    printEnd()

def printOneBarLine(m):
    for i in range(0,m):
        doTwice(printVerticalBar)
    printBar()

def printBarLines(m):
    for i in range(0,m):
        for j in range(0,4):
            printOneBarLine(m)
            printEnd()



def printNGrid(n,m):
    for i in range(0,m):
        printHoriz(n)
        printBarLines(m)

printNGrid(4,4)