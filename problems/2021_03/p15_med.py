import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[med] mar. 11, 2021
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
''')

# implement solution
import random as rand
class Solution:
    
    def __init__(self):
        self.count = 0
        self.res = None
    
    def selectRandom(self, new_value):
        self.count+=1
        
        if (self.count==1):
            self.res = new_value
        elif (rand.randint(1, self.count) == 1):
            self.res = new_value

# driver code
if __name__=='__main__':
    test_stream = ['a', 'b', 'c', 'd', 'e', 'f']

    s = Solution()
    for i in range(len(test_stream)):
        s.selectRandom(test_stream[i])
        print(f'partial result after {i+1} values: {s.res}')
    
    print(f'\nfinal result: {s.res}')