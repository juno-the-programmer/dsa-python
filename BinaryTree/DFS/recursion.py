class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def depthFirstValues(root):
    if not root:
        return []

    leftValues = depthFirstValues(root.left)
    rightValues = depthFirstValues(root.right)

    return [root.val] + leftValues + rightValues


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
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
'''
result = depthFirstValues(a)
print(result)
