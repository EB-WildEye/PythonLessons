# ~~~~~~~~~~ TicTacToe Game ~~~~~~~~~~
""" In our lesson today we will create together a TicTacToe game.
    The game will be played by two players at the terminal.
    follow the instructions in the code and try to complete the game."""


# define the game functions:

# print the board
def print_board(board_matrix):
    for rows in range(3):
        print("---"* 4)
        for cols in range(3):
            if board_matrix[rows][cols] == 0:
                print("|", " ", end=" ")
            else:
                print("|", board_matrix[rows][cols], end=" ")
        print("|")
    print("---"* 4)
    return None
   

# Start menue - get the user input 
def start_menue():
    print("~~~~~~~~ Welcome to TicTacToe Game ! ~~~~~~~~ ")
    userNameO = input("Enter your name here : ")
    print("hey " + userNameO + " your symbol is O, GoodLuck !")

    userNameX = input("Enter your name here : ")
    print("hey " + userNameX + " your symbol is X, GoodLuck !")

    # print the game instructions
    print("""In each turn insert the row and column number of the cell\nyou want to fill with your symbol, for example: 1,1""")
    return userNameO, userNameX


# winner function : check if there is a winner
def check_winner(board_matrix):
    # check rows
    for i in range(3):
        if board_matrix[i][0] == board_matrix[i][1] == board_matrix[i][2] != 0 :
            return board_matrix[i][0]
        # check columns
        if board_matrix[0][i] == board_matrix[1][i] == board_matrix[2][i] != 0 :
            return board_matrix[0][i]
    # check diagonals
    if board_matrix[0][0] == board_matrix[1][1] == board_matrix[2][2] != 0 :  # \
        return board_matrix[0][0]

    if board_matrix[0][2] == board_matrix[1][1] == board_matrix[2][0] != 0 :  # /
        return board_matrix[0][2]

    # check if the game is not over
    for i in range(3):
        for j in range(3):
            if board_matrix[i][j] == 0:
                return '->'
    return '^'


# turn function : play a turn and return True if there is a winner
def play_turn(board_matrix, curr_player_name, curr_player_symbol, other_player_name, other_player_symbol):
    # get the user input, convert from string to int
    print("It's " + curr_player_name + ' turn now.')
    turn = input('Insert row, colunm here : ').split(',')
    row = int(turn[0]) - 1
    col = int(turn[1]) - 1
    
    # check if the cell is empty
    while board_matrix[row][col] != 0:
        print("This cell isn't empty, choose a new cell")
        turn = input('Insert row, colunm here : ').split(',')
        row = int(turn[0]) - 1
        col = int(turn[1]) - 1

    # update the board
    board_matrix[row][col] = curr_player_symbol

    # print the board
    print_board(board_matrix)

    # check if there is a winner
    winner = check_winner(board_matrix)
    if winner == curr_player_symbol:
        print("Yahoo! " + curr_player_name + " you're the winner !" )
        return True
    elif winner == other_player_symbol:
        print("Yahoo! " + other_player_name + " you're the winner !" ) 
        return True
    elif winner == '^':
        print("It's a tie !")
        return True
    else:
        return False
    

def game():
    #initialize the board and the players names
    board_matrix = [[ 0 for i in range(3)] for j in range(3)] 
    userNameO, userNameX = start_menue()
    print_board(board_matrix)

    # get the user input and update the board , print the board after each turn
    game_over = False
    while not game_over:
        game_over = play_turn(board_matrix, userNameO, 'O', userNameX, 'X')
        if game_over:
            break
        game_over = play_turn(board_matrix, userNameX, 'X', userNameO, 'O')


def main():
    game()


if __name__ == '__main__':
    main()
