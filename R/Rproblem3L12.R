#Rproblem3L12
labels <- c("Price(NOK)", "Cost(NOK)", "Number_of_Units_Sold")
pLabels <- c("X", "Y", "Z")
df <- as.data.frame(matrix(c(1,2,3), nrow = 3, ncol = 3),row.names = pLabels)
colnames(df) <- labels
df$`Price(NOK)` <- c(55,63,85)
df$`Cost(NOK)` <- c(25,15,25)
df$Number_of_Units_Sold <- c(250,133,821)
max(df$`Price(NOK)`)
min(df$`Price(NOK)`)
mean(df$`Price(NOK)`)
thisYearsProfitInNOK <- (df$`Price(NOK)`-df$`Cost(NOK)`)*df$Number_of_Units_Sold
thisYearsProfitInNOK <- sum(thisYearsProfit)
thisYearsProfitInUSD <- thisYearsProfitInNOK/9
cat("This years profit in NOK is:" , thisYearsProfitInNOK , "and in USD:" , thisYearsProfitInUSD)


nextDF <- df
nextDF$`Price(NOK)` <- nextDF$`Price(NOK)`*1.03
nextDF$`Cost(NOK)` <- nextDF$`Cost(NOK)`*0.95
totalMarket <- df$Number_of_Units_Sold/0.05 #find total market share
nextDF$Number_of_Units_Sold <- totalMarket*0.25

priceOfY <- nextDF$`Price(NOK)`[2]
round(priceOfY)

#if we have to find next years profits
nextYearsProfitInNOK <- (nextDF$`Price(NOK)`-nextDF$`Cost(NOK)`)*nextDF$Number_of_Units_Sold
nextYearsProfitInNOK <- sum(nextYearsProfitInNOK)
nextYearsProfitInUSD <- nextYearsProfitInNOK/9
cat("This years profit in NOK is:" , round(nextYearsProfitInNOK) , "and in USD:" , round(nextYearsProfitInUSD))
