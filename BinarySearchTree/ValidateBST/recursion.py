import math


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True

            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)


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
