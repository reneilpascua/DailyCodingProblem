import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[hard] apr. 11, 2021
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
''')

'''
Implement solution
'''
def find_longest_pal(s):
    longest_pal = ''
    longest_begin = 0
    longest_end = 0

    # traverse through the string using i as left pointer, j as right pointer
    for i in range(len(s)):
        j = len(s) - 1
        
        while j > i:    
            if (j-i < longest_end-longest_begin): break # no need to keep searching if longest possible is found

            if  s[j] == s[i]: # then we may have a palindrome
                print(f'match found at {i}-{j}')
                tmp = 0
                while s[j-tmp] == s[i+tmp]:
                    if (j-tmp)-(i+tmp) <= 1: # then the left and right pointer have met, and this is a palindrome
                        print(f'we found a palindrome at {i}-{j}: {s[i:j+1]}')
                        if (j-i) >= longest_end - longest_begin:
                            longest_end, longest_begin = j, i
                            longest_pal = s[i:j+1]
                        break
                    else:
                        tmp+=1
                j-=1
            else:
                j-=1

    print(f'\nlongest palindrome in {s} is\n{longest_begin}-{longest_end}: {longest_pal}') if longest_pal!='' else print(f'no palindrome in {s}')
            


'''
Driver
'''
if __name__ == '__main__':
    find_longest_pal('xxxaabcddddcbxaaaxxx')