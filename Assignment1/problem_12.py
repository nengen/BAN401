#TODO add winning condition

game_board = [['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-']]

def insert_pieces(row, column,shape):
    game_board[row][column] = shape

def print_game_board():
    for i in game_board:
        print(*i)
    print("")



def game():
    gameover = False
    while gameover != True:
        print_game_board()
        row = input("Enter row index (type q to quit): ")
        if row == 'q':
            gameover = True
            break
        column = input("Enter col index: ")
        shape = input("Enter shape: ")
        insert_pieces(int(row),int(column),shape)

game()