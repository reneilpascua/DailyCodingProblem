import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[hard] apr. 19, 2021
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. 
The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
''')

'''
Implement solution
'''
class SudokuSolver():
    '''
    solves a sudoku using backtracking algo.

    a more efficient solver is probably out of scope for an interview question lol
    '''
    def __init__(self):
        self.initial = [] # the initial sudoku
        self.soln = [] # solution to the sudoku

    def set_unsolved_sudoku(self, grid):
        '''
        checks the input is a 9x9 list then sets initial sudoku.
        for empty spaces, use a 0.
        '''
        if (len(grid) == 9) and (len(grid[0]) == 9):
            self.initial = grid

    def solve(self):
        # try a number
        # validate it
        # if invalid, backtrack
        return self.soln

    
    def __validate(self):
        '''checks to see if the current state of the (partial) solution is valid'''
        pass


    def __validate_row(self, row_index):
        '''returns false if a non-zero number in this row is repeated.'''
        row = self.soln[row_index]

        for i in range(9): # i= 0->8
            if row.count(i+1) > 1:
                return False
        return True

    def __validate_column(self, col_index):
        '''returns false if a non-zero number in this column is repeated.'''
        # get the column's values
        column = []
        for i in range(9):
            column.append(self.soln[i][col_index])
        
        for i in range(9): # i= 0->8
            if column.count(i+1) > 1:
                return False
        return True

    def __validate_subgrid(self, sub_index):
        '''returns false if a non-zero number in this subgrid is repeated.'''
        # get the subgrid's values
        subgrid = []

    def __row_index(cell_index):
        '''given the cell's index, what row is it in?'''
        pass

    def __col_index(cell_index):
        '''given the cell's index, what column is it in?'''
        pass

    def __sub_index(cell_index):
        '''given the cell's index, what subgrid is it in?'''
        pass


'''
Driver
'''
if __name__ == '__main__':
    pass