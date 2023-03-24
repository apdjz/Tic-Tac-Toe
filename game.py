import random

# Define the board as a list of empty strings
board = [""] * 9

# Define the numbers that correspond to the cells of the board
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Define the winning combinations
wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Define the function that displays the board
def display_board():
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("-----------")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("-----------")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))

# Define the function that checks if a player has won
def check_win(player):
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Define the function that checks if the board is full
def check_full():
    return "" not in board

# Define the function that checks if the move is valid
def check_valid(move):
    return move in numbers and board[int(move)-1] == ""

# Define the function that gets the player's move
def get_move(player):
    while True:
        move = input("Player {}'s turn. Enter a cell number: ".format(player))
        if check_valid(move):
            return int(move) - 1
        else:
            print("Invalid move. Try again.")

# Define the function that gets the computer's move in easy mode
def get_computer_move_easy():
    return random.choice([i for i, x in enumerate(board) if x == ""])

# Define the function that gets the computer's move in advanced mode
def get_computer_move_advanced(player):
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == player and board[combo[2]] == "":
            return combo[2]
        elif board[combo[1]] == board[combo[2]] == player and board[combo[0]] == "":
            return combo[0]
        elif board[combo[0]] == board[combo[2]] == player and board[combo[1]] == "":
            return combo[1]
    return get_computer_move_easy()

# Define the function that gets the computer's move in hard mode
def get_computer_move_hard(player):
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == player and board[combo[2]] == "":
            return combo[2]
        elif board[combo[1]] == board[combo[2]] == player and board[combo[0]] == "":
            return combo[0]
        elif board[combo[0]] == board[combo[2]] == player and board[combo[1]] == "":
            return combo[1]
    for combo in wins:
        if board[combo[0]] == board[combo[2]] != "" and board[combo[1]]
