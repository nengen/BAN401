# R problem #2 - lecture 3 & 4

mat <- matrix(seq(1,25), nrow = 5, ncol = 5, byrow = TRUE)
print(mat)

#automatic way
diag_of_mat <- diag(mat)
print(diag)

#first way
matrix_as_dataframe <- as.data.frame(mat, row.names = c("I", "II", "III", "IV", "V"))
colnames(matrix_as_dataframe) <-  c("One", "Two", "Three", "Four", "Five")
print(matrix_as_dataframe)

#second way
dimnames(mat) <- list(c("I", "II", "III", "IV", "V"), c("One", "Two", "Three", "Four", "Five"))
matrix_as_dataframe2 <- as.data.frame(mat)
print(matrix_as_dataframe2)

summary(matrix_as_dataframe)
