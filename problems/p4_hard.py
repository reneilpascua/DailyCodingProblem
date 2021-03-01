import sys
sys.path.append('..')
from helpers import helpers

print('''
[HARD] [UNFINISHED] Feb. 28, 2021
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
''')
'''
mental notes:
- O(1) space means can't create another data structure (--> should modify original array)
- O(n) time means can't sort
- see p4_ramblings.txt
''' 

# take input
n_, list_ = helpers.get_list_of_integers()

# solution
