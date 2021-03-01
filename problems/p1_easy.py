import sys
sys.path.append('..')
from helpers import helpers

print('''
[EASY] Feb. 25, 2021
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
''')

# take input
n_, list_ = helpers.get_list_of_integers()
k_ = int(input('Enter the number k: '))


# solution

## O(n^2) lol
def sol1(n, list, k):
    for i in range(0, n):
        ref = list[i]
        for j in range(0, n):
            if j==i: continue
            psum = ref + list[j]
            if psum == k:
                return True
    
    return False

## bonus: one pass
def sol2(n, list, k):
    my_set = set()
    for i in range(0, n):
        if (my_set.__contains__(k - list[i])): return True
        my_set.add(list[i])
    return False




# print(sol1(n_, list_, k_))
print(sol2(n_, list_, k_))