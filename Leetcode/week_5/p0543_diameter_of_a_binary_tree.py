class TreeNode:
    __slots__ = ['val', 'left', 'right']

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.diameter = 0

        def _recursive_check(head: TreeNode) -> None:
            if head is None:
                return 0

            left = _recursive_check(head.left)
            right = _recursive_check(head.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        _recursive_check(root)
        return self.diameter


"""
Runtime: O(N) N = number of nodes
Space: O(1)

Runtime: 44 ms, faster than 67.39% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
"""
