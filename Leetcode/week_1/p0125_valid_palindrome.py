import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.regex_solution(s)

    def regex_solution(self, s: str) -> bool:
        """
        O(3N) solution
        """
        matcher = re.compile(r"[A-Za-z0-9]")
        splitted = matcher.findall(s)
        splitted = [x.lower() if x.isalpha() else x for x in splitted]
        return splitted == splitted[::-1]

    def string_solution(self, s: str) -> bool:
        """
        O(N) solution
        """
        ns = []
        for i, char in enumerate(s):
            if char.isalpha():
                ns.append(char.lower())
            elif char.isdigit():
                ns.append(char)

        return ns == ns[::-1]


"""
Runtime O(3n) ~ O(n)
Space O(n)
Where n = number of characters in string

Runtime: 52 ms, faster than 46.04% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.2 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.
"""
