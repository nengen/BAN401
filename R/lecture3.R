#lecture3
matrix1 <- matrix(data = 1, nrow = 3, ncol = 3)
matrix2 <- matrix(data = NA, nrow = 3, ncol = 7)
print(matrix2)
dim(matrix2)
vector9 <- 1:12
matrix3 <- matrix(data = vector9, nrow = 4)
print(matrix3)
vector10 <- 1:10
vector11 <- vector10^2
matrix4 <- rbind(vector10,vector11)
matrix4
matrix6 <- cbind(vector10,vector11,vector10)
matrix6
matrix7 <- diag(5)
matrix7
matrix7[1,1]
eigen(matrix7)
eigen(matrix1)






