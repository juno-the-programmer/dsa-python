class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def breathFirstSearch(root):
    if not root:
        return []

    result = []
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

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
result = breathFirstSearch(a)
print(result)
