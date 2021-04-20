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
class Hello:
    
    def __init__(self):
        self.initial = [] # the initial sudoku
        self.is_init = [] # says whether to protect this cell because it's an initial value.
        self.soln = [] # solution to the sudoku

    def set_sudoku(self, grid):
        '''
        checks the input is a 9x9 list then sets initial sudoku and remembers which values are set.
        for empty spaces, use a 0.
        '''
        if self.__validate_input(grid):
            self.initial = grid
            # populate is_init grid
            for i in range(9):
                new_row = []
                for j in range(9):
                    new_row.append(grid[i][j] != 0)
                self.is_init.append(new_row)
        else:
            print('''
            please check that your input is in the form of:
            [
                [row 1], [row 2], [row 3], ..., [row 8], [row 9]
            ]
            where each row has 9 ints -- the empty cells are 0.
            ''')
            
    def solve(self):
        
        # restarting everything because of while loop bug

                
        return self.soln

    def __forwardtrack(self, i, j):
        '''
        increments the current cell.
        returns:
            True = go ahead to the next cell
            False = backtrack

        if the soln state is valid, returns True
        else reincrements

        if cant increment further, returns False
        '''
        if self.is_init[i][j]: return True

        # see if this cell is maxed out
        if self.soln[i][j] == 9:
            # then reset and signal for backtrack
            self.soln[i][j] = 0
            return False
        else:
            self.soln[i][j] += 1        
            is_valid = self.__validate_all()
        
        # if doesnt result in valid state, keep looping
        while (not is_valid): # python doesnt have a do-while loop lol
            if self.soln[i][j] == 9: # same logic as above
                self.soln[i][j] = 0
                return False
            else: # try the next number
                self.soln[i][j] += 1
                is_valid = self.__validate_all()
        
        return True
    
    def __validate_all(self):
        '''checks to see if the current state of the (partial) solution is valid'''
        for i in range(9): # row
            for j in range(9): # col
                if not (self.__validate_row(i)
                    and self.__validate_column(j)
                    and self.__validate_subgrid(self.__sub_index(i, j))):
                    return False
        return True


    def __validate_row(self, row_index):
        '''returns false if a non-zero number in this row is repeated.'''
        for i in range(9): # i= 0->8
            if self.soln[row_index].count(i+1) > 1:
                return False
        return True

    def __validate_column(self, col_index):
        '''returns false if a non-zero number in this column is repeated.'''
        # first, get the column's values
        column = []
        for i in range(9):
            column.append(self.soln[i][col_index])
        
        for i in range(9): # i= 0->8
            if column.count(i+1) > 1:
                return False
        return True

    def __sub_index(cell_row, cell_col):
        '''
        given the cell's row and col, what subgrid is it in?

        0 1 2
        3 4 5
        6 7 8
        '''
        subrow = cell_row//3 # integer division
        subcol = cell_col//3 # integer division
        return 3*subrow + subcol

    def __validate_subgrid(self, sub_index):
        '''returns false if a non-zero number in this subgrid is repeated.'''
        # get the subgrid's values
        subgrid = []
        leftcorner = [3*(sub_index//3), 3*(sub_index%3)] # [row, col]
        for i in range(3):
            for j in range(3):
                subgrid.append(
                    self.soln[leftcorner[0]+i][leftcorner[1]+j]
                )
        
        for i in range(9):
            if subgrid.count(i+i) > 1:
                return False
        return True
    
    def __validate_input(self, grid):
        if not ((len(grid) == 9) and (len(grid[0]) == 9)): return False

        for i in range(9):
            for j in range(9):
                if grid[i][j] not in range(10): # ie. 0, 1, 2, ..., 8, or 9
                    return False
        return True

'''
Driver
'''
if __name__ == '__main__':
    solver = Hello()
    solver.set_sudoku(
        [
            [1,2,3,4,5,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
    )
    print(solver.solve())