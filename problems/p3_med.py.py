import sys
sys.path.append('..')
from helpers import helpers

print('''
[MEDIUM] Feb. 27, 2021
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
''')

## given class Node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution

def serialize(root):
    # base case
    if root is None: return '()'

    root_left = serialize(root.left)
    root_right = serialize(root.right)

    return f'({root.val} {root_left} {root_right})'
    # use brackets and spaces to distinguish nodes in serialized form
    #   serialized tree of 1 parent, 2 children
    #   (root (root.left () ()) (root.right () ()))

def deserialize(s):
    # example string from serialize:
    #   (root (left (left.left () ()) ()) (right () ()))
    
    # base case
    if s=='()': return None

    # parse s for round brackets
    #   a complete node is one that opens and closes all brackets
    #   TODO: validate structure of s
    
    # set the value of this node as the first token (minus the first bracket)
    val = s[1:].split(' ')[0]
    
    # set up parsing
    bracket_stack = []
    i=1
    c = s[i]

    # find left node
    while c is not '(':
        i+=1
        c = s[i]
    bracket_stack.append(c)
    start_left = i

    while bracket_stack: # ie. while bracket_stack is not empty
        i+=1
        c = s[i]
        if c == '(': bracket_stack.append(c)
        elif c==')': bracket_stack.pop()
    end_left = i
    left_node = deserialize(s[start_left:end_left+1])

    # find right node
    while c is not '(':
        i+=1
        c = s[i]
    bracket_stack.append(c)
    start_right = i

    while bracket_stack: # ie. while bracket_stack is not empty
        i+=1
        c = s[i]
        if c == '(': bracket_stack.append(c)
        elif c==')': bracket_stack.pop()
    end_right = i
    right_node = deserialize(s[start_right:end_right+1])

    # finally, return node with left and right
    return Node(val, left_node, right_node)

## given test
##  assumption: node values are strings that do not contain whitespace nor round brackets, as these are used to distinguish in serialized form.
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
