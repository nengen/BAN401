

def doTwice(function, val):
    function(val)
    function(val)

def printTwice(bruce):
    print(bruce)
    print(bruce)

doTwice(printTwice,"spam")

def doFour(function, val):
    doTwice(function,val)
    doTwice(function,val)

doFour(print, "spam")