# Definition for a binary tree TreeNode.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class rev_postorder_iterator:

    def __init__(self, root):
        self.root = root
        self.stack = [root]

    def get_next(self):
        if self.root is None:
            return False

        while self.stack:
            cnode = self.stack.pop()

            if cnode.left:
                self.stack.append(cnode.left)
            if cnode.right:
                self.stack.append(cnode.right)

            if cnode and cnode.left is None and cnode.right is None:
                return cnode.val
        return False


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        r1, r2 = rev_postorder_iterator(root1), rev_postorder_iterator(root2)

        while True:
            r1_next, r2_next = r1.get_next(), r2.get_next()
            if r1_next != r2_next:
                return False
            if r1_next == r2_next == False:
                break
        return True


"""
Runtime: O(2N)
Space: O(1)

Runtime: 32 ms, faster than 54.19% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Leaf-Similar Trees.
"""
