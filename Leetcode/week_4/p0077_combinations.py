from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return nCk where n = {1 .... n}
        self.combinations = []

        def backtrack_generate(index, path):
            if len(path) == k:
                self.combinations.append(path)
                return

            for i, n in enumerate(nums[index:], start=index):
                backtrack_generate(i + 1, path + [n])

        nums = [i for i in range(1, n + 1)]
        for i, n in enumerate(nums):
            backtrack_generate(i + 1, [n])

        return self.combinations


"""
Runtime: 676 ms, faster than 17.43% of Python3 online submissions for Combinations.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Combinations.
"""
