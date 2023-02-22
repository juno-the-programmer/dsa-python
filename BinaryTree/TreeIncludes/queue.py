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

    queue = [root]

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node.val == target:
            return True

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return False


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
