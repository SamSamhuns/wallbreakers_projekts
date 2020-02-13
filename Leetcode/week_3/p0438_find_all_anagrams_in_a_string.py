from typing import List


class Solution:
    """
    WARNING TLE
    """
    def findAnagrams(self, string: str, pat: str) -> List[int]:
        if len(pat) > len(string):
            return []

        sliding_window = []
        pat = sorted(pat)
        anagrams = []

        for i in range(len(string)):
            sliding_window = sorted(string[i:i + len(pat)])
            if self.are_equal(pat, sliding_window):
                anagrams.append(i)

        return anagrams

    def are_equal(self, A, B) -> bool:
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            if A[i] != B[i]:
                return False
        return True


"""
A better sorting solution would be using counting sort, but it uses a hashtable idea
and we want to use a pure sorting method.
WARNING THIS SOLUTION is a TLE on Leetcode
Runtime: O(sslogs+pplogp)
Space: Extra space O(1)

Runtime: 168 ms, faster than 36.66% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find All Anagrams in a String.
"""
