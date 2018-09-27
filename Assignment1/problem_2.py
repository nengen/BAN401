



def tax():
    annual_income = input("Enter your annual income in numbers: ") #prompt user for inpit
    tax = tax_calculator(int(annual_income)) #use the tax_calculator helper function to calculate the tax, we do this in a helper function for abstraction
    print("Your tax is: " + str(tax)) #cast tax to string and print it
    print("Your after tax income is: " + str(int(annual_income)-int(tax))) #calc after tax income and cast it to string


def tax_calculator(income):
    #use variables instead of numbers in the ifelif statement
    #This way it's easier to change the tax classes if later needed
    taxClass1 = 55000
    taxClass2 = 90000
    taxClass3 = 190000
    taxClass4 = 390000

    if(income < taxClass1): #this ifelif statement calculates the tax using a progressive tax system
        return income * 0.00
    elif(income <= taxClass2):
        return (income-taxClass2) * 0.1
    elif(income <= taxClass3):
        return (income-taxClass2) * 0.2+(taxClass2-taxClass1) * 0.1
    elif(income <= taxClass4):
        return (income-taxClass3) * 0.3 + (taxClass3 - taxClass2) * 0.2 + (taxClass2-taxClass1) * 0.1
    elif(income >= taxClass4):
        return (income - taxClass4)*0.4 + (taxClass4-taxClass3) * 0.3 + (taxClass3 - taxClass2) * 0.2 + (taxClass2-taxClass1) * 0.1


tax() #call the tax function