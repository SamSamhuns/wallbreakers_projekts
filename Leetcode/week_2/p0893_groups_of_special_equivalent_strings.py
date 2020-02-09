from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        pattern_set = set()
        for word in A:
            even, odd = [], []
            for i, char in enumerate(word):
                if i % 2 == 0:
                    even.append(char)
                else:
                    odd.append(char)
            even.sort()
            odd.sort()
            even.extend(odd)
            key = ''.join(even)
            pattern_set.add(key)

        return len(pattern_set)


"""
Runtime: O(w * nlogn) where w = no of words, n = average length of words
Space: O(w)

Runtime: 44 ms, faster than 70.58% of Python3 online submissions for Groups of Special-Equivalent Strings.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Groups of Special-Equivalent Strings.
"""
