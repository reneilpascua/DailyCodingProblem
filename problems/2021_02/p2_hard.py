import sys
sys.path.append('../..')
from helpers import helpers

print('''
[HARD] Feb. 26, 2021
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
''')

# take input
n_, list_ = helpers.get_list_of_integers();

# solution

from functools import reduce

def sol1(n, list):
    # multiply each element together
    bigprod = reduce((lambda x, y:x*y), list)
    soln = []
    for i in range(0, n):
        soln.append(int(bigprod/list[i]))
    return soln

# follow up what if you can't use division?
def sol2(n, list):
    '''
    construct 2 arrays starting from left and right
    left: {1, a[0], a[0]a[1], a[0][1][2]}
    right: {a[3]a[2]a[1], a[3]a[2], a[3], 1}
    and multiply them together
    '''
    arr_left = []
    p_left=1
    for i in range(0,n):
        arr_left.append(p_left)
        p_left*=list[i]

    arr_right = []
    p_right = 1
    for i in range(0, n):
        arr_right.insert(0, p_right)
        p_right*=list[n-1-i]

    print(len(arr_left))
    print(len(arr_right))
    # multiply them together
    soln = []
    for i in range(0,n):
        num = arr_left[i] * arr_right[i]
        soln.append(int(num))

    return soln



# print(sol1(n_, list_))
print(sol2(n_,list_))