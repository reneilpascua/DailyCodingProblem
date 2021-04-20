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
from datetime import datetime
class SudokuSolver:
    
    def __init__(self):
        self.is_init = [] # says whether to protect this cell because it's an initial value.
        self.soln = [] # solution to the sudoku
        self.solved = False
        self.n_backtracks = 0
        self.soln_time = 0

    def validate_input(self,grid):
        if not ((len(grid) == 9) and (len(grid[0]) == 9)): return False

        for i in range(9):
            for j in range(9):
                if grid[i][j] not in range(10): # ie. 0, 1, 2, ..., 8, or 9
                    return False
        return True

    def set_sudoku(self, grid):
        '''
        checks the input is a 9x9 list then sets initial sudoku and remembers which values are set.
        for empty spaces, use a 0.
        '''
        if self.validate_input(grid):
            self.soln = grid
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
    
    def __next_with_wrap(self,i, j, backward = False):
        j = j-1 if backward else j+1
        if j == 9:
            i +=1
            j = 0
        elif j==-1:
            i -=1
            j = 8
        # print(f'next: [{i},{j}]')
        return i,j

    def solve(self):
        start_time = datetime.now()
        i,j=0,0 # initialize indices
        while 0 <= i < 9: # row
            # 1. go to next non-init cell (including this current one)
            while self.is_init[i][j]:
                i, j = self.__next_with_wrap(i,j)

            # 2. increment that cell
            if self.soln[i][j] < 9:
                self.soln[i][j] += 1
            else:
                self.soln[i][j] = 0
                i, j = self.__backtrack(i, j)
                continue
            

            is_valid = self.__validate_all()
            # 3.a if it's valid, target the next cell
            # 3.b else if cell value < 9, increment... go back to 3
            # 3.c else if cell value == 9, **backtrack** and skip to next iteration
            
            while not is_valid:
                if self.soln[i][j] == 9:
                    # print('oops, time to backtrack...')
                    # print('current soln state:')
                    # print(self.soln)
                    self.soln[i][j] = 0 # reset the value
                    
                    # backtrack to next non-init value
                    i, j = self.__backtrack(i,j)
                    break 
                self.soln[i][j] += 1
                is_valid = self.__validate_all()

            # 4.b valid! let's target the next cell for the next iteration
            if is_valid: i, j = self.__next_with_wrap(i, j)
        
        # while loop terminated. is it solved?
        if i >= 9:
            self.solved = True
            self.soln_time = datetime.now() - start_time
        elif i < 0:
            self.solved = False
        return self.soln

    def __backtrack(self, i, j):
        self.n_backtracks += 1
        i, j = self.__next_with_wrap(i,j,backward=True)
        while self.is_init[i][j]:
            i, j = self.__next_with_wrap(i, j, backward=True)
        return i, j
    
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

    def __sub_index(self, cell_row, cell_col):
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
            testval = i+1 # isnt enough to just do subgrid.count(i+1)
            if subgrid.count(testval) > 1:
                return False
        return True
    
    def soln_details(self):
        '''
        prints out the solution's details
        make sure to run the .solve() method first!
        '''
        if self.solved:
            print('the initial puzzle:')
            self.__print_initial()
            print('\none solution:')
            self.__print_soln()
            print('')
            print(f'backtracks:\t\t{self.n_backtracks}')
            print(f'time:\t\t\t{self.soln_time}')
        else:
            print('no solution has been found for')
            self.__print_initial()

    def __print_initial(self):
        init = []
        for i in range(9):
            new_row = []
            for j in range(9):
                item = self.soln[i][j] if self.is_init[i][j] else 0
                new_row.append(item)
            init.append(new_row)
        # print in a human readable form
        for i in range(9):
            print(init[i])
    
    def __print_soln(self):
        for i in range(9):
            print(self.soln[i])

'''
Driver
'''
if __name__ == '__main__':
    no_soln = [
        [1,2,3,0,0,0,7,8,9],
        [0,0,0,4,5,6,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    test_sudoku = [
        [1,2,3,0,0,0,0,0,0],
        [0,0,0,4,5,6,0,0,0],
        [0,0,0,0,0,0,7,8,9],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    solver = SudokuSolver()
    solver.set_sudoku(test_sudoku)
    solver.solve()
    solver.soln_details()