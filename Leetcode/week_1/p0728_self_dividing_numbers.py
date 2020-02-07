from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right + 1) if self.is_self_dividing(num)]

    def is_self_dividing(self, n: int) -> bool:
        orig = n
        while n:
            n, rem = divmod(n, 10)
            if rem == 0 or orig % rem != 0:
                return False

        return True

"""
Runtime: O(nlogn)
Space: O(n)

Runtime: 44 ms, faster than 78.06% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Self Dividing Numbers.
"""
