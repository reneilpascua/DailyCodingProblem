import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[easy] apr. 11, 2021
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
''')

'''
Implement solution
'''
import random as rand
import numpy as np

def rand5():
    return rand.randint(1,5)

def rand7():
    '''returns a value [1,7] only using rand5()'''
    s = 0
    for _ in range(7):
        s+=rand5()
    return s%7 + 1

def rand5times7distr():
    ''' shows that adding 7 rand5()s together is not uniform'''
    probs = np.zeros(29)
    for i in range(10000):
        s = -7
        for j in range(7):
            s+=rand5()
        probs[s] += 1
    return probs

'''
Driver
'''
if __name__ == '__main__':
    nums = np.empty(0)
    for _ in range(10000):
        nums = np.append(nums, rand7())
    print(nums.mean()) # should be 4ish