class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeSum(root):
    if not root:
        return 0

    return root.val + treeSum(root.left) + treeSum(root.right)


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
    /   \     \
   4     -2    1

   = 21
'''

result = treeSum(a)
print(result)
