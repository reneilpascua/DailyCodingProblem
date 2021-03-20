import re

def validate_token_as_int(str):
    return True

def get_int(msg):
    n_ = int(input(msg))
    return n_

# user input: an integer list of known length n
def get_list_of_integers():
    n_ = get_int('How long is the list of integers? ')
    list_ = []
    for i in range (0,n_):
        num = int(input(f'enter the {i+1}\'th integer in the list: '))
        list_.append(num)
    return [n_, list_]

# user input: an integer list of known length, without specifying length
def get_continuous_list_of_integers():
    print('Enter a list of integers, and when you\'re finished, enter a non-integer.')
    list_ = []
    done = False
    while not done:
        try:
            num = int(input('Enter an integer: '))
            list_.append(num)
        except: # general exception, namely from converting non-integer
            done = True
    return list_
