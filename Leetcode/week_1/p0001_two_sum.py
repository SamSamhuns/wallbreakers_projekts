from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement_dict = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in complement_dict:
                return [complement_dict[target - num], i]

            complement_dict[num] = i


"""
Runtime O(N)
Space complexity O(N)

Runtime: 48 ms, faster than 79.33% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 53.95% of Python3 online submissions for Two Sum.
"""
