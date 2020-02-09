from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return self.hash_set_soln(nums)

    def hash_set_soln(self, nums: List[int]) -> List[int]:
        """
        O(n) time
        O(n) space
        """
        nset = set()
        missed = []

        nsum = 0
        for n in nums:
            if n in nset:
                missed.append(n)
            nsum += n
            nset.add(n)

        # 1 3 3 4
        # actual_sum = 10, missed[0]=3, nsum = 11
        # so 10-x+3 = 11
        # x = 2

        nlen = len(nums)
        actual_sum = (nlen * (nlen + 1)) // 2
        missed.append(actual_sum + missed[0] - nsum)

        return missed


"""
Runtime: O(n)
Memory: O(n)

Runtime: 208 ms, faster than 73.54% of Python3 online submissions for Set Mismatch.
Memory Usage: 14.6 MB, less than 22.22% of Python3 online submissions for Set Mismatch.
"""
