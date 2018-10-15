#Rproblem2
randNumbs <- seq(1:100)
set.seed(1000)
my_vector <- sample(randNumbs,100)
print(my_vector)
first_vec <- my_vector[1:50]
bool_vec <- seq(1:100)
bool_vec[which(my_vector >= 50)] <- "FALSE"
bool_vec[which(my_vector < 50)] <- "TRUE"
bool_vec <- as.logical(bool_vec)
less_than_vec <- my_vector[which(my_vector < 50)]
print(my_vector)
print(first_vec)
print(bool_vec)
print(less_than_vec)
