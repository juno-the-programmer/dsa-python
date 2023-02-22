'''
Write a function, maxPathSum, that takes in the root of a binary tree that contains number values.
The function should return the maximum sum of any root to leaf path within the tree.

You may assume that the input tree is non-empty.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    if not root:
        return float('-inf')

    if not root.left and not root.right:
        return root.val

    maxChildPathSum = max(maxPathSum(root.left), maxPathSum(root.right))
    return root.val + maxChildPathSum


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

'''
      3
    /   \
   11    4
  /  \    \
 4   -2     1
'''
result = maxPathSum(a)
print(result)
# 18
