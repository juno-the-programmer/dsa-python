'''
Write a function, treeSum, that takes in the root of a binary tree that contains number values.
The function should return the total sum of all values in the tree.
'''


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeSum(root):
    if not root:
        return 0

    queue = [root]
    sum = 0

    while len(queue) > 0:
        current_node = queue.pop(0)

        sum += current_node.val
        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return sum


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
