from math import sqrt

list = [53.21, 50.73, 75.34, 45.18, 51.95, 47.47,
52.85, 49.93, 49.66, 46.09, 50.16, 47.21, 46.02,
47.87, 49.40, 51.47, 22.80, 46.80, 49.66, 53.24] #the input data

def check_if_normal_distr(observations):

    mean = calc_mean(observations) #call helper function to calculate mean
    stdev = calc_st_dev(observations) #call helper function to calculate standard deviation

    for observation in observations:
        print("Observation value "+ str(observation) + " " + is_withing_three(stdev,mean,observation))
        #using the is_within_three function prints out if observation value is within control limits




def calc_mean(observations):
    return (1/len(observations)) * sum(observations) #returns the mean


def calc_st_dev(observations):
    temp = 0
    mean = calc_mean(observations)
    for observation in observations: #loop throug list to find sum of (x-u)^2
        temp += (observation-mean)**2 #this is the :(x-u)^2
    return sqrt((1/len(observations)) * temp) #returns standard deviation

def is_withing_three(stdev, mean, observation):
    upperLimit = (mean+3*stdev) #set the upper limit
    lowerLimit = (mean-3*stdev) #set the lower limit
    if(observation >= lowerLimit and observation <= upperLimit ): #ifelse statement to print correct output
        return "is within the control limits"
    elif(observation>upperLimit):
        return "is above the upper control limit"
    elif(observation<lowerLimit):
        return "is under the lower control limit"
    else:
        "error"


check_if_normal_distr(list)