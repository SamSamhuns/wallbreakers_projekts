from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) > 1:
            slen = len(s)
            for i in range(slen // 2):
                s[i], s[slen - 1 - i] = s[slen - 1 - i], s[i]


"""
Runtime: O(N/2)
Space: O(1)

Runtime: 216 ms, faster than 56.34% of Python3 online submissions for Reverse String.
Memory Usage: 17.3 MB, less than 94.19% of Python3 online submissions for Reverse String.
"""
