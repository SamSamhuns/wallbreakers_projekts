from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        start = 0
        for n in nums:
            start = start ^ n
        return start


"""
Runtime O(N) where N = no of digits in nums array
Space O(1)

Runtime: 80 ms, faster than 95.74% of Python3 online submissions for Single Number.
Memory Usage: 15.2 MB, less than 9.84% of Python3 online submissions for Single Number.
"""
