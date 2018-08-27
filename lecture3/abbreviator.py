state = input("Please enter a state in the us: \n")
state = state.upper()
abbreviaton = " "
if (" " in state):
    if state[0:3] == "NEW":
        abbreviaton = (state[0] + state[4])
    elif state[0:4] == "WEST":
        abbreviaton = (state[0] + state[5])
    elif(state[0:5] == "NORTH" or state[0:5] == "SOUTH"):
        abbreviaton = (state[0] + state[6])
    else:
        print("Something went wrong")
else:
    abbreviaton(state[0:2].upper())
print(abbreviaton +  " is " + state + " abbreviated")