#Rproblem1L34
matrix <- matrix(c(120,121,140,145,160,65,66,77,87,60), ncol = 5, byrow = TRUE)
colnames(matrix) <- c("Monday","Tuesday","Wednesday","Thursday", "Friday")
rownames(matrix) <- c("Tesla", "Toyota")
Honda <- c(110,112,113,98,98)
matrix <- rbind(matrix, Honda)
print(matrix)

returns <- (matrix[,5]-matrix[,1])/matrix[,1]
print(round(returns,digits=2))
returns2 <- ((matrix[,5]*8.0)-(matrix[,1]*7.5))/(matrix[,1]*7.5)
print(round(returns2,digits=2))
