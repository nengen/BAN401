#lecture2
answer <- 3
print(answer)
answer
is(answer) #get the type
answer1 <- 43
rm(answer1)
vector1 <- c(1,2,3,4,5,6,7,8,9,10)
vector2 <- c(1,2,3,4,5,6,7,8,9,10)
vector3 <- c(vector1,vector2)
round(log(vector1),digit = 1)
median(vector1)
prod(vector1)
sd(vector1)
length(vector1)
vector4 <- seq(0,10)
vector5 <- seq(0,10,length.out = 40)
vector5
rep(0,time=25)
vector4[3:5]
x <- c(1,2,3,4,NA,6,7,8,9,NA)
na.omit(x) #in console to remove NA
summary(x) #gives us amount of NA
#remove na
x.noNA <- subset(x, is.na(x) == FALSE)
x.noNA
vector <- 1:500
sample(vector, size=5, replace = FALSE)
x <- 5
y <- 2
m <- 10
res <- paste(x, "*", y, "is equal to",m )
res

a <- list("false" = FALSE,"true" = TRUE )
append(a,("three" = 3),after = 2)
a[-2]

#interactive input
input <- readline(prompt = "Enter you age")
age <- as.integer(input) #convert to ingteger
