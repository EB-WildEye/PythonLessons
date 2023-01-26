# ~~~~~~~~~~ TicTacToe Game ~~~~~~~~~~
""" In our lesson today we will create together a TicTacToe game.
    The game will be played by two players at the terminal.
    follow the instructions in the code and try to complete the game."""


# define the game functions:

# print the board
def print_board(board_matrix):
    for i in range(len(board_matrix)):
        for j in range(len(board_matrix[i])):
            print(board_matrix[i][j], end=" ")
        print()


# Start menue - get the user input
def start_menue():
    print("Welcome to TicTacToe Game !")
    userNameO = input("Enter your name here : ")
    print("hey " + userNameO + "your symbol is O, GoodLuck !")

    userNameX = input("Enter your name here : ")
    print("hey " + userNameX + "your symbol is X, GoodLuck !")

    # print the game instructions
    print("""In each turn insert the row and column number of the cell
    you want to fill with your symbol, for example: 1,1""")
    return userNameO, userNameX



def game():
    #initialize the board and the players names
    board_matrix = [[ 0 for i in range(3)] for j in range(3)]
    userNameO, userNameX = start_menue()
    print_board(board_matrix)

    # get the user input and update the board , print the board after each turn



    # if the game is over print message and ask if the user want to play again
   
      

# run the game
game()