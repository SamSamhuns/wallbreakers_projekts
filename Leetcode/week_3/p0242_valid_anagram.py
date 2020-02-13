class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagram_sort_soln(s, t)

    def isAnagram_sort_soln(self, s: str, t: str) -> bool:
        # O(nlogn + mlogm + n + 2m) where n=len(s), m=len(t)
        # Extra space O(1)
        if len(s) != len(t):
            return False
        s, t = sorted(s), sorted(t)
        return s == t

"""
Runtime: O(nlogn + mlogm + m + n) 
Space: O(1)

Runtime: 48 ms, faster than 62.72% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.6 MB, less than 34.38% of Python3 online submissions for Valid Anagram.
"""
