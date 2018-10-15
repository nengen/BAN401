#Rproblem1
vec <- seq(1:200)
#solution 1
vec <-  vec[which(xor(vec%%5 != 0,vec%%7 != 0))]

#solution 2
vec <- vec[which(vec%%5 == 0 | vec%%7 == 0)]
temp <- vec[which(vec%%5 == 0 & vec%%7 == 0)]
vec <- setdiff(vec,temp)

#solution3
vec <- vec[which((vec%%5 == 0 | vec%%7 == 0) & !(vec%%5 == 0 & vec%%7 == 0))]

print(vec)

sum(vec)
mean(vec)

