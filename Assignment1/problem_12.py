#TODO add winning condition

game_board = [['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-']] #initialize the empty game board using a nested list

def insert_pieces(row, column,shape):
    game_board[row][column] = shape #set the given spot of the game_board to the shape

def print_game_board():
    for i in game_board:#loop through game_board and print it
        print(*i) #the asteriks makes it so we dont get the '' around each -, which makes it look nicer
    print("") #get the next line



def game():
    gameover = False #gamestatus
    while gameover != True:
        print_game_board()#each loop we print the current game board
        row = input("Enter row index (type q to quit): ") #get row as input
        if row == 'q': #if the user types q we quit the game
            gameover = True
            break
        column = input("Enter col index: ") #get column as input
        shape = input("Enter shape: ") #get the shape the user wants to add
        insert_pieces(int(row),int(column),shape) #insert piece into game board

game() #run the game