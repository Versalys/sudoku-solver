# A simple sudoku solver
# Written by Aidan Erickson
#
# This was a simple project I did to wipe some rust off programming-wise. It uses a common
# technique called 'backtracking', wherein you keep trying things until you reach an invalid
# state, where you go back. If you reach the end in a valid state, the board is valid. Honestly,
# I didn't know it was called backtracking until after I was done lol.
#
# This is an implementation to the hard leetcode problem sudoku-solver (#37)
# https://leetcode.com/problems/sudoku-solver/description/

from typing import List

def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    nums = [str(i) for i in range(1,10)]
    def check_cell(num, idx, idy):

        for x in range(9): # check row
            if board[x][idy] == num:
                return False

        for y in range(9): # check col
            if board[idx][y] == num:
                return False

        x_div = idx // 3 # check 3x3
        y_div = idy // 3
        for x in range(3):
            for y in range(3):
                if board[x+3*x_div][y+3*y_div] == num:
                    return False

        return True


    def helper(idx, idy):
        new_y = idy if idx < 8 else idy+1
        new_x = idx+1 if idx < 8 else 0

        if idy == 9: # base case, board done.
            return True
        if board[idx][idy] != '.':
            return helper(new_x, new_y)

        for n in nums:
            if check_cell(n, idx, idy):
                board[idx][idy] = n
                if helper(new_x, new_y):
                    return True

        board[idx][idy] = '.' # did not find any valid board on this tree. go back.
        return False

    return helper(0,0)

def main():
    # change this for a different board
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

    if not solveSudoku(board):
        print("Something went wrong! Perhaps your board is unsolvable or entered in incorrectly?")
        print("Your input:\n")
    else:
        print('Success!\nOutputting board...\n')

    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


if __name__ == '__main__':
    main()
