print('''
Feb 25, 2021

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
''')

# take input

n_ = int(input('How long is the list of numbers? '))
list_ = []
for i in range (0,n_):
    num = int(input(f'enter the {i+1}\'th number in the list: '))
    list_.append(num)

k_ = int(input('Enter the number k: '))


# solution

## O(n^2) lmao
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