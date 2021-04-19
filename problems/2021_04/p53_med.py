import sys
sys.path.append('../..')
from helpers import helpers # only works if the script is in problems/month_folder/

print('''
[med] apr. 18, 2021
This problem was asked by Apple.

Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
''')

'''
Implement solution
'''
class MyQueue:
    '''
    queue implementation using 2 stacks.

    uses list as stack because of O(1) pop and append.
    '''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        '''
        add to the back (left) of the queue

        using stacks:
            1. pop from stack 1 and push onto stack 2 until stack 1 empty
            2. push new item to stack 1 so that it's last out
            3. pop from stack 2 and push onto stack 1 until stack 2 empty
        '''
        while len(self.stack1) > 0:
            tmp = self.stack1.pop()
            self.stack2.append(tmp)
        
        self.stack1.append(item)

        while len(self.stack2) > 0:
            tmp = self.stack2.pop()
            self.stack1.append(tmp)
        

    def dequeue(self):
        '''
        remove from the front (right) of the queue

        ie. just pop from stack 1
        '''
        return self.stack1.pop()


'''
Driver
'''
if __name__ == '__main__':
    myq = MyQueue()
    myq.enqueue('first')
    myq.enqueue('second')
    myq.enqueue('third')

    print(myq.dequeue())
    print(myq.dequeue())
    print(myq.dequeue())