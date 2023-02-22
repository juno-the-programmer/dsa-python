'''
Write a function, treeIncludes, that takes in the root of a binary tree and a target value.
The function should return a boolean indicating whether or not the value is contained in the tree.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeIncludes(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    return treeIncludes(root.left, target) or treeIncludes(root.right, target)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

'''
      a
    /   \
   b     c
  / \     \
 d   e     f

Time: O(n)
Space: O(n)
'''

result = treeIncludes(a, 'e')  # True
print(result)
