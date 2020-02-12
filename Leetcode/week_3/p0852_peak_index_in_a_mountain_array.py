from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return self.binary_search_max_elem(A)

    def binary_search_max_elem(self, A: List[int]) -> int:
        # Works for duplicates values on either side of mountain
        # Runtime: 72 ms, faster than 95.63% of Python3 online submissions for Peak Index in a Mountain Array.
        # Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.
        left, right = 0, len(A) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            l, r = mid - 1, mid + 1
            if A[l] < A[mid] > A[r]:
                return mid

            while A[l] == A[r]:
                l -= 1
                r += 1
            if A[l] < A[r]:  # go right
                left = mid + 1
            else:           # go left
                right = mid


"""
Runtime: O(n) ~ amortized O(logn)
Space: O(1)

Runtime: 72 ms, faster than 95.63% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.
"""
