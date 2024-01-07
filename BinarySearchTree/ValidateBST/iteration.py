import math


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


a = TreeNode(8)
b = TreeNode(6)
c = TreeNode(5)
d = TreeNode(7)
e = TreeNode(11)
f = TreeNode(9)
g = TreeNode(12)

a.left = b
a.right = e

b.left = c
b.right = d

e.left = f
e.right = g

sol = Solution()
result = sol.isValidBST(a)
print(result)

'''
Time complexity: O(N)
Space complexity: O(N)
'''
