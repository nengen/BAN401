#Rproblem6L12
require(plyr)
set.seed(1)
n <- 1000
runif.vector <- runif(n, min=0, max=100)
NA.index <- sample(1:n, floor(runif(1, min=1, max=n)))
numeric.vector <- runif.vector
numeric.vector[NA.index] <- NA
print(numeric.vector)
naInVector<- sum(is.na(numeric.vector))
print(naInVector)
meanInVector <- mean(na.omit(numeric.vector))
print(meanInVector)
numeric.vector[is.na(numeric.vector)] <- sample(numeric.vector[!is.na(numeric.vector)], sum(is.na(numeric.vector)), replace=TRUE)
print(numeric.vector)
