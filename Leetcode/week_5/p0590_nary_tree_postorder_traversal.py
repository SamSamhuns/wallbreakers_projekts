from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def postorder_recur(self, root: 'TreeNode') -> List[int]:
        postorder = []
        self.recursive_soln(root, postorder)
        return postorder

    def postorder_iter(self, root: 'TreeNode') -> List[int]:
        postorder = []
        self.iterative_soln(root, postorder)
        return postorder

    def recursive_soln(self, root: 'TreeNode', postorder: List[int]) -> None:
        """
        Runtime: 52 ms, faster than 58.42% of Python3 online submissions for N-ary Tree Postorder Traversal.
        Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for N-ary Tree Postorder Traversal.
        """
        if root:
            for child in root.children:
                self.recursive_soln(child, postorder)
            postorder.append(root.val)

    def iterative_soln(self, root: 'TreeNode', postorder: List[int]) -> None:
        """
        Runtime: 48 ms, faster than 82.30% of Python3 online submissions for N-ary Tree Postorder Traversal.
        Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for N-ary Tree Postorder Traversal.
        """
        if not root:
            return
        stack = [root]
        while stack:
            cnode = stack.pop()
            postorder.append(cnode.val)
            _ = [stack.append(child) for child in cnode.children]
        postorder.reverse()


"""
Runtime: 52 ms, faster than 58.42% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
