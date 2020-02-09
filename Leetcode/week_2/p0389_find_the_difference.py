from collections import defaultdict, Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return self.counter_soln(s, t)

    def hmap_soln(self, s: str, t: str) -> str:
        """
        Runtime: 32 ms, faster than 68.51% of Python3 online submissions for Find the Difference.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find the Difference.
        """
        # Can be done with a multiset/bag/collections.Counter as well

        smap, tmap = defaultdict(int), defaultdict(int)
        for c in s:
            smap[c] += 1
        for c in t:
            tmap[c] += 1

        for char in tmap:
            if char not in smap:
                return char
            if tmap[char] > smap[char]:
                return char

    def counter_soln(self, s: str, t: str) -> str:
        """
        Runtime: 28 ms, faster than 87.61% of Python3 online submissions for Find the Difference.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find the Difference.
        """
        sbag, tbag = Counter(s), Counter(t)
        for char in tbag:
            if char not in sbag:
                return char
            if tbag[char] > sbag[char]:
                return char

    def bit_manipulation(self, s: str, t: str) -> str:
        """
        Runtime O(s+t)
        Space O(1)
        """
        xor = 0
        for c in s:
            xor ^= ord(c)
        for c in t:
            xor ^= ord(c)

        return chr(xor)

"""
Counter Soluiton
Runtime: O(s+t)
Space: O(s+t)

Solution with collections.Counter object
Runtime: 28 ms, faster than 87.61% of Python3 online submissions for Find the Difference.
Memory Usage: 1
"""
