from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        snum, tnum = 1, 1
        s_map = defaultdict(set)
        t_map = defaultdict(set)

        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = snum
                snum += 1
            if t[i] not in t_map:
                t_map[t[i]] = tnum
                tnum += 1

            if s_map[s[i]] != t_map[t[i]]:
                return False

        return True


"""
Runtime: O(s+t)
Space: O(s+t)

Runtime: 28 ms, faster than 97.72% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Isomorphic Strings.
"""
