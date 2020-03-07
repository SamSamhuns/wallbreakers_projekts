class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        self.left_sum = 0

        def inorder(head: TreeNode) -> None:
            if head:
                if head.left and not head.left.left and not head.left.right:
                    self.left_sum += head.left.val
                inorder(head.left)
                inorder(head.right)

        inorder(root)
        return self.left_sum


"""
Runtime: O(logN) N = number of nodes
Space: O(1)

Runtime: 28 ms, faster than 83.11% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 13.5 MB, less than 92.31% of Python3 online submissions for Sum of Left Leaves.
"""
