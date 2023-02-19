'''
Write a function, treeMinValue, that takes in the root of a binary tree that contains number values.
The function should return the minimum value within the tree.
You may assume that the input tree is non-empty.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeMinValue(root):

    stack = [root]

    min_value = float("inf")

    while len(stack) > 0:
        current_node = stack.pop()

        min_value = min(current_node.val, min_value)

        if current_node.left:
            stack.append(current_node.left)

        if current_node.right:
            stack.append(current_node.right)

    return min_value


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
    / \     \
  4    -2    1
  = -2
'''
result = treeMinValue(a)
print(result)
