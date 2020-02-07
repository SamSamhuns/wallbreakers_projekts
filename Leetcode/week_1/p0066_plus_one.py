from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == []:
            digits = [1]
        elif digits[-1] < 9:  # trivial case
            digits[-1] += 1
        else:
            carry = 0
            digits[-1] += 1
            if digits[-1] >= 10:
                carry = digits[-1] // 10
                digits[-1] = digits[-1] % 10

            for i, digit in enumerate(reversed(digits[:-1]), start=1):
                idx = len(digits) - 1 - i
                digits[idx] += carry
                carry = digits[idx] // 10
                if digits[idx] >= 10:
                    digits[idx] = digits[idx] % 10

            if carry == 1:
                digits = [1] + digits  # O(n) operation here

        return digits

"""
Runtime O(n) where n = number of elements in digits list
Space O(n)

Runtime: 28 ms, faster than 80.62% of Python3 online submissions for Plus One.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Plus One.
"""
