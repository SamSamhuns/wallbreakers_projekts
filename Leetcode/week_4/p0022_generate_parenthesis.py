from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.combinations = []

        def backtrack_gen(balance_tuple, path):
            open_b, close_b = balance_tuple
            if open_b - close_b < 0 or open_b > n or close_b > n:
                return

            if len(path) == n * 2:
                self.combinations.append(''.join(path))
                return

            backtrack_gen((open_b + 1, close_b), path + ['('])
            backtrack_gen((open_b, close_b + 1), path + [')'])

        backtrack_gen((0, 0), [])
        return self.combinations


"""
Runtime: 36 ms, faster than 38.24% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.1 MB, less than 91.11% of Python3 online submissions for Generate Parentheses.
"""
