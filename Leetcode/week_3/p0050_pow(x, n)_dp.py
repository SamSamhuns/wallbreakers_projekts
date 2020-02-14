class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.binary_exp_iterative(x, n)

    def binary_exp_iterative(self, x: float, n: int) -> float:
        # binary exponentiation iterative
        base = x
        exp = abs(n)
        result = 1
        while exp > 0:
            if exp & 1:
                result *= base
            base *= base
            exp >>= 1

        if n == 0:
            return 1.0
        return result if n > 0 else 1 / result


"""
Runtime: O(logn)
Space: O(1)

Runtime: 28 ms, faster than 67.64% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
"""
