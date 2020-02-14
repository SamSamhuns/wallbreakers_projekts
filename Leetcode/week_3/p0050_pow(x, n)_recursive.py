class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.binary_exp_recursive(x, n)

    def binary_exp_recursive(self, x: float, n: int) -> float:
        exp = abs(n)
        ans = self.recurse(x, exp)
        return ans if n > 0 else 1 / ans

    def recurse(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        ans = self.recurse(x, n // 2)
        if n & 1:
            return x * ans * ans
        else:
            return ans * ans


"""
Runtime: O(logn)
Space: O(1)

Runtime: 28 ms, faster than 67.64% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
"""
