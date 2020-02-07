from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        O(n) runtime and O(n) space solution
        """
        if len(s) != len(t):
            return False

        sd, td = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sd[s[i]] += 1
            td[t[i]] += 1

        for char in sd:
            if char not in td:
                return False
            if sd[char] != td[char]:
                return False
            del td[char]
        return True


"""
Runtime: O(s+t)
Space: O(s+t)

Runtime: 48 ms, faster than 63.24% of Python3 online submissions for Valid Anagram.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
"""
