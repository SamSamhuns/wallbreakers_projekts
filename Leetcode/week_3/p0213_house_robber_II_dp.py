from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(2N)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        # just run the max non
        return max(self.get_max_non_adj(nums[1:]),
                   self.get_max_non_adj(nums[:-1]))

    def get_max_non_adj(self, nums: List[int]) -> int:
        # get maximum non-adj elem sum
        max_money = nums[0]
        prev_money = nums[0]
        before_prev_money = 0

        for idx, money in enumerate(nums[1:]):
            temp = before_prev_money
            max_money = max(before_prev_money + money, prev_money)
            before_prev_money = prev_money
            prev_money = max_money

        return max_money


"""
Runtime: O(2N) ~ O(N)
Space: O(1)

Runtime: 24 ms, faster than 93.70% of Python3 online submissions for House Robber II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber II.
"""
