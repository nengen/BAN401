#source = http://greenteapress.com/thinkpython2/html/thinkpython2002.html

print("Hello world!")

constant = 4/3
pi = 3.14
radius = 5

volumeOfSphere = float( constant * pi * radius**3)
print(volumeOfSphere)


priceOfBook = 24.95
discount = 0.4
shippingCostsFirstCopy = 3
shippingCostsRest = 0.75
amountOfCopiesSold = 60

totalWholeSaleCost = (priceOfBook*discount)*amountOfCopiesSold + shippingCostsFirstCopy + (amountOfCopiesSold-1)*shippingCostsRest
print(totalWholeSaleCost)

