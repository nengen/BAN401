



def char_counter():
    dict = {}
    sentence = input("Please enter a sentence\n")
    for char in sentence:
        if char == char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    print(dict)



char_counter()






