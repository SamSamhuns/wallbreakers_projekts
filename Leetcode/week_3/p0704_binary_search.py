from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l if nums[l] == target else -1


"""
Runtime: O(logN)
Space: O(1)

Runtime: 260 ms, faster than 74.53% of Python3 online submissions for Binary Search.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Binary Search.
"""
