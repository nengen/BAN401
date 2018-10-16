#Rproblem4L12
randNumbs <- seq(1:20)
set.seed(1000)
my_vector <- sample(randNumbs,20,replace = TRUE)
sequence <- seq(4,length(my_vector),by=4)
vectorOfFour <- sum(my_vector[sequence])
print(vectorOfFour)

vectorOfFour <- sapply(split(my_vector, ceiling(seq_along(my_vector)/4)), sum)

reversed_factor_new <-c(rev(my_vector)[10:20],my_vector[12:20])

print(my_vector)
print(reversed_factor_new)
