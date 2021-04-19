import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[med] apr. 16, 2021
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
''')

'''
Implement solution
'''
import random as rand
def rand_1k(k): # uniform
    return rand.randint(1,k)

def new_deck():
    '''creates a new deck'''
    deck = []
    nums = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
    suits = ['spd', 'clb', 'hrt', 'dmd']
    for n in nums:
        for s in suits:
            deck.append(f'{n} {s}')
    return deck

def new_deck_ints():
    '''creates new deck of ints [1,...,52]'''
    deck = []
    for i in range(52): deck.append(i+1)
    return deck

def swap(list,i,j):
    list[i], list[j] = list[j], list[i]

def shuffle(deck):
    '''shuffles a given deck (ideally a list of 52 elements)'''
    for i in range(len(deck)):
        j = rand_1k(52-i) - 1
        swap(deck, i, i+j) 

'''
first loop:
    i=0, k=52, j=[0-51]
    there are 52 options that can go into index 0. whatever is in j is swapped to 0. if j=0, theres no swap

second loop:
    i=1, k=51, j=[0-50]
    there are 51 options that can go into index 1. whatever is in j is swapped to 1. if j=0, theres no swap

Xth loop:
    i=X, k=52-X, j=[0 - (52-X-1)]
'''
import numpy as np
import matplotlib.pyplot as plt
def probability_density(card, num_shuffles):
    '''
    @param card:            a card to track (use int 1-52 inclusive)
    @param num_shuffles:    number of shuffles (pick something big like 10000)

    looks at distribution of places where a card could end up. if each of 52! permutations are likely, each element will be the sameish
    '''
    freqs = np.zeros(52)
    pct_res = np.zeros(52)
    for i in range(num_shuffles):
        deck = new_deck_ints()
        shuffle(deck)
        where_is_the_card = deck.index(card)
        freqs[where_is_the_card] += 1
    
    mean = freqs.mean()
    for i in range(len(pct_res)):
        pct_res[i] = 100*(freqs[i] - mean)/mean
    
    plt.plot(pct_res)
    plt.show()




'''
Driver
'''
if __name__ == '__main__':
    deck = new_deck_ints()
    print(f'original: {deck}')
    shuffle(deck)
    print(f'shuffled: {deck}')
    print('\nis this shuffle uniform over many shuffles?')
    probability_density(card=23, num_shuffles=10000) # shows that the card 23 can end up in any part of the deck uniformally
    # probability_density(1, 10000) # edge case
    # probability_density(52, 10000) # edge case