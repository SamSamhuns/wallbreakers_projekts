from collections import deque


class Solution:
    def isSubsequence_greedy(self, s: str, t: str) -> bool:
        # Greedy solution
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        s_idx = 0
        for char in t:
            if char == s[s_idx]:
                s_idx += 1
            if s_idx == len(s):
                return True

        return False


"""
Runtime: O(s+t)
Space: O(1)

Runtime: 188 ms, faster than 51.04% of Python3 online submissions for Is Subsequence.
Memory Usage: 17.3 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
"""
