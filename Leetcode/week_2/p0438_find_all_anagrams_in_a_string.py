from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen, slen = len(p), len(s)
        anagram = []
        if plen > slen:
            return anagram

        p_counter = Counter(p)  # can use hash map counts
        s_counter = Counter(s[:plen])

        if p_counter == s_counter:
            anagram.append(0)

        for i in range(plen, slen):

            # sliding window idea,
            # do not iterate through entire subsections
            s_counter[s[i]] += 1
            s_counter[s[i - plen]] -= 1

            if s_counter[s[i - plen]] == 0:
                del s_counter[s[i - plen]]

            if p_counter == s_counter:
                anagram.append(i - plen + 1)

        return anagram


"""
Runtime: O(s+p)
Space: O(p)

Runtime: 168 ms, faster than 36.66% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find All Anagrams in a String.
"""
