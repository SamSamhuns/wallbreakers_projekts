from collections import deque


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValueDFS(self, root: TreeNode) -> int:
        """
        BFS Solution with queue
        """

        queue = deque([root])
        cur_lv = []
        while queue:

            cur_lv = []
            for i in range(len(queue)):
                cnode = queue.popleft()
                if not cur_lv:
                    cur_lv.append(cnode.val)

                if cnode.left:
                    queue.append(cnode.left)
                if cnode.right:
                    queue.append(cnode.right)

        return cur_lv[0]

    def findBottomLeftValueBFS(self, root: TreeNode) -> int:
        """
        DFS Solution with stack
        """
        maxDepth = [0]
        leftmost = [0]
        curDepth = 0

        def dfs(head, curDepth, maxDepth, leftmost):
            if head:
                curDepth += 1
                dfs(head.right, curDepth, maxDepth, leftmost)
                if curDepth >= maxDepth[0]:
                    leftmost[0] = head.val
                    maxDepth[0] = curDepth
                dfs(head.left, curDepth, maxDepth, leftmost)

        dfs(root, curDepth, maxDepth, leftmost)

        return leftmost[0]


"""
BFS Solution
Runtime: 40 ms, faster than 83.95% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Find Bottom Left Tree Value.
"""
