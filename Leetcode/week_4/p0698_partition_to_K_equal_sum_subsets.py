from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        Backtracking solution
        """
        t_sum = sum(nums)
        self.used = [False] * len(nums)
        self.target, rem = divmod(t_sum, k)
        if rem != 0:
            return False

        nums.sort(reverse=True)
        if nums[0] > self.target:
            return False

        def fill_recursively(idx, k, csum):
            # base cases
            if k == 0:
                return True
            if csum == self.target:
                return fill_recursively(0, k - 1, 0)

            for i, val in enumerate(nums[idx:], start=idx):
                if not self.used[i] and csum + val <= self.target:
                    self.used[i] = True
                    if fill_recursively(idx + 1, k, csum + val):
                        return True
                    self.used[i] = False
            return False

        return fill_recursively(0, k, 0)


"""
Runtime: O(k*2^n)
Space: O(n)

Runtime: 92 ms, faster than 48.63% of Python3 online submissions for Partition to K Equal Sum Subsets.
Memory Usage: 13 MB, less than 94.44% of Python3 online submissions for Partition to K Equal Sum Subsets.
"""
