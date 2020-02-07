from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        max_match = list(strs[0])

        for string in strs:
            min_len = min(len(max_match), len(string))
            break_len = min_len

            for i in range(min_len):
                if max_match[i] != string[i]:
                    break_len = i
                    break
            max_match = max_match[:break_len]
        return ''.join(max_match)

"""
Runtime O(S) where S = sum of all chars in the words in strs 
Space Complexity O(s) where s = len of first string
Runtime: 28 ms, faster than 88.01% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
"""
