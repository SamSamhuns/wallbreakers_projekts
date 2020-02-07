from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        parity_A = [0] * len(A)
        even, odd = 0, len(A) - 1

        for elem in A:
            if elem % 2 == 0:
                parity_A[even] = elem
                even += 1
            else:
                parity_A[odd] = elem
                odd -= 1

        return parity_A


"""
Runtime: O(N)
Space: O(N)

Runtime: 80 ms, faster than 77.14% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 13.4 MB, less than 98.70% of Python3 online submissions for Sort Array By Parity.
"""
