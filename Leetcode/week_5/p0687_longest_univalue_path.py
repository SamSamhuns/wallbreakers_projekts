class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest_path = 0

        def _dfs_check(head: TreeNode) -> None:
            if head is None:
                return (0, None)

            ldist, lval = _dfs_check(head.left)
            rdist, rval = _dfs_check(head.right)

            if head.val == lval == rval:
                self.longest_path = max(self.longest_path, ldist + rdist)
                return (max(ldist, rdist) + 1, head.val)
            elif head.val == lval:
                self.longest_path = max(self.longest_path, ldist)
                return (ldist + 1, head.val)
            elif head.val == rval:
                self.longest_path = max(self.longest_path, rdist)
                return (1 + rdist, head.val)
            else:
                return (1, head.val)

        _dfs_check(root)
        return self.longest_path


"""
Runtime: O(N) N = number of nodes
Space: O(1)

Runtime: 376 ms, faster than 95.19% of Python3 online submissions for Longest Univalue Path.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Longest Univalue Path.
"""
