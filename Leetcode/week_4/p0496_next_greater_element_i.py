class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Solution with stack and hashmap
        """
        n2_stack = []
        nums1_map = {n: -1 for n in nums1}

        for n in reversed(nums2):
            while n2_stack:
                if n2_stack[-1] < n:
                    n2_stack.pop()
                else:
                    break

            if n2_stack:
                if n in nums1_map:
                    nums1_map[n] = n2_stack[-1]

            n2_stack.append(n)

        return [nums1_map[n] for n in nums1]


"""
Runtime: O(n1+n2)
Space: O(n1+n2)

Runtime: 44 ms, faster than 86.81% of Python3 online submissions for Next Greater Element I.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Next Greater Element I.
"""
