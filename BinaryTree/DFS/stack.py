class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def depthFirstSearch(root):
    if not root:
        return []

    result = []
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result


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
result = depthFirstSearch(a)
print(result)
