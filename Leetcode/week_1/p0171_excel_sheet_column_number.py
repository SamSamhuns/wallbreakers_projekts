class Solution:
    def titleToNumber(self, s: str) -> int:

        ctitle = 0
        for i, char in enumerate(s):
            ctitle += (ord(char) - 64) * (26 ** (len(s) - 1 - i))

        return ctitle


"""
Runtime O(n)
Space O(1)

Runtime: 32 ms, faster than 53.51% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.
"""
