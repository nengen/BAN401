



def char_counter():
    dict = {} #create empty dictionary
    sentence = input("Please enter a sentence\n") #get user input
    for char in sentence: #loop trough each character in the sentence
        if char == ' ':
            continue
        elif char == char in dict: #if the char is equal to a key in the dictionary. We increment the value of the key
            dict[char] += 1
        else: #if the char is not already in the dictionary we add the char to the dictionary
            dict[char] = 1
    print(dict)



char_counter()






