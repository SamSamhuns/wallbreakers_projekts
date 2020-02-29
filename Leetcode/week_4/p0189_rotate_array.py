from typing import List
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.queue_soln(nums, k)

    def queue_soln(self, nums: List[int], k: int) -> None:
        """
        Runtime: O(2N)
        Space: O(N)
        """
        k %= len(nums)  # more k len rotations are redundant
        if k == 0:
            return nums
        queue = deque([])
        _ = [queue.append(n) for n in nums[:len(nums) - k]]
        _ = [queue.appendleft(n) for n in reversed(nums[len(nums) - k:])]
        for i, n in enumerate(queue):
            nums[i] = n

    def direct_assign(self, nums: List[int], k: int) -> None:
        """
        Runtime: O(2N)
        Space: O(N)
        Illegal in other languages most likely
        """
        k %= len(nums)
        if k == 0:
            return nums

        sec1, sec2 = nums[:len(nums) - k], nums[len(nums) - k:]
        nums[:k] = sec2
        nums[k:] = sec1

    def inplace_three_reverse(self, nums: List[int], k: int) -> None:
        """
        Runtime: O(N)
        Space: O(1)
        """
        k %= len(nums)
        if k == 0:
            return nums

        def _reverse(nums, start, end):
            n = start + (end - start)
            mid = start + ((end - start) // 2)
            for i in range(start, mid):
                nums[i], nums[n - 1 - i + start] = nums[n - 1 - i + start], nums[i]

        _reverse(nums, 0, len(nums))
        _reverse(nums, 0, k)
        _reverse(nums, k, len(nums))


"""
Queue Solution
Runtime: O(N)
Space: O(N)

Runtime: 60 ms, faster than 80.27% of Python3 online submissions for Rotate Array.
Memory Usage: 14.4 MB, less than 5.09% of Python3 online submissions for Rotate Array.
"""
