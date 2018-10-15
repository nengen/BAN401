#lecture5
#control flow
a <- readline(prompt = 'Enter your number: ')
b <- 2
class(a)
result <- as.numeric(a)+b
class(result)
#AND = &
#OR = |
#NOT = !

#if statement
if(1+1 == 2){
  print("true")
}else{
  print("false")
}

ifelse(1+1==2,print("true"),print("false"))


#rnorm -> random var for norm dist
#runif -> random var for uniform dist
#rbinom -> random var for bin dist
#rweibull -> random var for weibull dist

#for loop
vec <- c(1,2,3,4,5)
for (number in vec) {
  print("hi")
}


