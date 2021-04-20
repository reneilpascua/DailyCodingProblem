import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[easy] apr. 20, 2021
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
''')

'''
Implement solution
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
alnum = list(alphabet + alphabet.upper() + nums) # a list of chars to use

import random
class URLShortener():
    def __init__(self):
        self.shortened=dict() # key is the short, value is the url

    def shorten(self, url):
        if url not in self.shortened.values(): 
            short = []
            while len(short) < 6:
                short.append(alnum[random.randint(0,len(alnum)-1)])
            shortenedUrl = ''.join(short)
            self.shortened[shortenedUrl] = url
            return shortenedUrl

        return self.__retrieve_short(url)

    def restore(self, short):
        return self.shortened.get(short) if short in self.shortened else f'{short} not found'

    def __retrieve_short(self, url):
        '''precondition: the url is in the dict already'''
        return list(self.shortened.keys())[list(self.shortened.values()).index(url)]

'''
Driver
'''
if __name__ == '__main__':
    shortener = URLShortener()
    short = shortener.shorten('facebook.com')
    print(short)
    short2 = shortener.shorten('facebook.com')
    print(short2)
    print(shortener.restore(short))
    print(shortener.restore('asdf12'))