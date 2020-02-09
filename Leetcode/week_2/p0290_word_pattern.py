from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        return self.two_pass_str_split_hashmap(pattern, str)

    def two_pass_str_split_hashmap(self, pattern: str, str: str) -> bool:
        """
        Two pass
        Time O(n)
        Space O(n)
        """
        string = str.split(' ')
        if len(pattern) != len(string):
            return False

        pat_dict, str_dict = defaultdict(), defaultdict()

        for i in range(len(string)):
            pat, word = pattern[i], string[i]
            if pat in pat_dict:
                if pat_dict[pat] != word:
                    return False
            if word in str_dict:
                if str_dict[word] != pat:
                    return False
            pat_dict[pat] = word
            str_dict[word] = pat

        return True


"""
Runtime: O(2N) ~ O(N)
Space: O(s+p)

Runtime: 24 ms, faster than 87.17% of Python3 online submissions for Word Pattern.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Word Pattern.
"""
