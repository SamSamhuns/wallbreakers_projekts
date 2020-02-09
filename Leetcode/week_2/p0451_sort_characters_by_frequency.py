from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        return self.counter_soln(s)

    def defaultdict_soln(self, s: str) -> str:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        scounter = defaultdict(int)
        for char in s:
            scounter[char] += 1

        sorted_chars = sorted(scounter, key=scounter.get, reverse=True)
        return ''.join([char * scounter[char] for char in sorted_chars])

    def counter_soln(self, s: str) -> str:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        scounter = Counter(s)

        sorted_chars = sorted(scounter, key=scounter.get, reverse=True)
        return ''.join([char * scounter[char] for char in sorted_chars])


"""
Both Counter and defaultdict solution
Runtime: O(nlogn)
Space: O(n)

Counter Solution:
Runtime: 32 ms, faster than 94.55% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 13.9 MB, less than 50.00% of Python3 online submissions for Sort Characters By Frequency.
"""
