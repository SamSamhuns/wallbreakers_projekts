# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        """
        # string = aa
        # pat    = a* True

        # s = "aab"
        # p = "c*a*b" True

        # s = "mississippi"
        # p = "mis*is*[]p*." False

        # '.' Matches any single character. [a-zA-Z0-9_]
        # '*' Matches zero or more of the preceding element

        We use a boolean 2D matrix where
        dp[i][j] reprs does pattern[:j] match string[:i]
               0 1 2 3 4 5 6 7 8
        #     '' . * b c . * . e
        # 0 '' T T T T T T T T T
        # 1 a  F T
        # 2 b  F
        # 3 c  F
        # 4 b  F
        # 5 b  F
        # 6 e  F
        """
        return self.dp_soln(string, pattern)

    def dp_soln(self, string: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]

        dp[0][0] = True
        # deal with patterns like a*, .*, a*b*
        for i in range(1, len(pattern) + 1):
            if pattern[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(string) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1] in {string[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # use zero elems for *
                    if pattern[j - 2] == '.' or pattern[j - 2] == string[i - 1]:
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[-1][-1]


"""
Runtime: 52 ms, faster than 61.10% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14.1 MB, less than 5.55% of Python3 online submissions for Regular Expression Matching.
"""
