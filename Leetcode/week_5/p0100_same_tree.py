class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p or q:
            if not p or not q or p.val != q.val:
                return False
            if not self.isSameTree(p.left, q.left):
                return False
            if not self.isSameTree(p.right, q.right):
                return False
        return True


"""
Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Same Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Same Tree.
"""
