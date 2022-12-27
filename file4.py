#Python program to implement n-queens problem using backtracking

"""
The n-queens problem is a problem where a chess board is given and the goal is to
place n queens on the board such that no queen can attack any other queen. A queen
can attack horizontally, vertically and diagonally.
"""

#Define the n-queens function
def n_queens(n):
    #Create a board
    board = [[0 for x in range(n)] for x in range(n)]

    #Check if a queen can be placed on the board
    if n_queens_helper(board, 0) == False:
        print("No solution exists")

    #Print the board
    print_board(board)

#Define the n-queens helper function
def n_queens_helper(board, col):
    #If all queens are placed, return true
    if col >= len(board):
        return True

    #Place a queen on the board
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            #Check if the queen can be placed on the board
            if n_queens_helper(board, col + 1) == True:
                return True

            #If the queen cannot be placed, backtrack
            board[i][col] = 0

    #Return false if no queen can be placed on the board
    return False

#Define the is safe function
def is_safe(board, row, col):
    #Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    #Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    #Check the lower diagonal on the left side
    i = row
    j = col
    while j >= 0 and i < len(board):
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    #Return true if the queen can be placed on the board
    return True

#Define the print board function
def print_board(board):
    #Print the board
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end = ' ')
        print()

#Define the main function
def main():
    #Define the number of queens
    n = 4

    #Print the result
    n_queens(n)

#Call the main function
if __name__ == '__main__':
    main()