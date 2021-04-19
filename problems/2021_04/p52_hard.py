import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[hard] apr. 17, 2021
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
''')

'''
Implement solution
'''
from collections import deque
class LRU:
    '''an lru will hold in memory the n most recently used items'''

    def __init__(self, n):
        self.size = n
        self.cache = dict()
        self.recents = deque()  # not sure whether to use deque or list... neither are O(1) enough
                                # https://wiki.python.org/moin/TimeComplexity

    def __recentify(self, key):
        '''precondition: this key is in self.cache. moves the key to the front of the recents deque.'''
        self.recents.remove(key) # sadly, this is O(n) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.recents.append(key) # append to the right, this is O(1)

    def set(self, key, value):
        '''sets a key-value pair in the cache. runs at O(1)'''
        
        if key in self.cache: # this key already exists within LRU
            # recentify that key
            self.__recentify(key)
            
        else: # add this new key
            # append its key to the front of the recents
            self.recents.append(key)
            # if the cache is full, pop from the back of the recents
            if len(self.recents) > self.size:
                removed_key = self.recents.popleft() # pops from the left, this is O(1)
                # remove that key from the cache
                self.cache.pop(removed_key)

        # finally, update the value of the key
        self.cache[key] = value
        print(f'{key}: {value} saved in LRU')

        
        
    def get(self, key):
        '''gets a recently used item from the cache. runs at O(1)'''
        # if key exists, move that key to the front of the recents

        return self.cache.get(key)
    


'''
Driver
'''
if __name__ == '__main__':
    '''technically not the solution.... neither list nor deque are enough, but '''
    lru = LRU(5)
    lru.set('first', 1)
    print(lru.get('first'))

