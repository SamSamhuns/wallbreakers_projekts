from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.separate_sets(nums1, nums2)

    def separate_sets(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2_set = set(nums2)
        num1_set = set()
        intersection = []
        for n in nums1:
            if n in num2_set and n not in num1_set:
                intersection.append(n)
            num1_set.add(n)
        return intersection


"""
Runtime: O(n1 + n2)
Space: O(n1 + n2 + intersect(n1, n2))

Runtime: 40 ms, faster than 91.10% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays.
"""
