import sys
sys.path.append('..')
from helpers import helpers

print('''
[MEDIUM] Mar. 1, 2021
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
''')

# solution

# cons returns a function on a and b --> car and cdr take a function as a parameter
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair): # takes f(a,b)
    def return_first(first, last):
        return first;
    
    return pair(return_first)

def cdr(pair): # takes f(a, b)
    def return_last(first, last):
        return last;

    return pair(return_last);


print(cons(3,4)) # returns f(3,4)

print(car(cons(3,4))) # returns 3
# p much this calls
# cons.pair(return_first(a,b))

print(cdr(cons(3,4))) # returns 4
# p much this calls
# cons.pair(return_first(a,b))