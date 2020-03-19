from typing import List
from functools import lru_cache

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deep_clone(self, tree: TreeNode) -> TreeNode:
        """ Similar to deep copy """
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.deep_clone(tree.left)
        new_tree.right = self.deep_clone(tree.right)
        return new_tree

    @lru_cache(None)
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        """
        if N = 7,
        think of the nodes as 1, 2, 3, 4, 5, 6, 7
        Even values cannot be lead nodes
        and all Odd values are leaf nodes
        """
        if not(N & 1):
            return []
        elif N == 1:
            return [TreeNode(0)]
        rtn = []

        for i in range(2, N + 1, 2):
            left_branch = self.allPossibleFBT(i - 1)
            right_branch = self.allPossibleFBT(N - i)
            for left_count, left in enumerate(left_branch, 1):
                for right_count, right in enumerate(right_branch, 1):
                    tree = TreeNode(0)

                    tree.left = self.deep_clone(
                        left) if right_count < len(right_branch) else left
                    tree.right = self.deep_clone(
                        right) if left_count < len(left_branch) else right

                    rtn.append(tree)
        return rtn


"""
Runtime: 264 ms, faster than 38.88% of Python3 online submissions for All Possible Full Binary Trees.
Memory Usage: 21.9 MB, less than 42.86% of Python3 online submissions for All Possible Full Binary Trees.
"""
