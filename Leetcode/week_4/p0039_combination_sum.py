from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.valid = []

        def backtrack(path, index, csum):
            if csum == target:
                self.valid.append(path)
                return

            for i, n in enumerate(candidates[index:], start=index):
                if csum + n <= target:
                    backtrack(path + [n], i, csum + n)

        backtrack([], 0, 0)
        return self.valid


"""
Runtime: 52 ms, faster than 85.73% of Python3 online submissions for Combination Sum.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum.
"""
