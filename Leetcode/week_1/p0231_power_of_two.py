class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        while n:
            n, rem = divmod(n, 2)
            if rem == 1 and n > 0:
                return False

        return True

    def isPowerOfTwo_bit_manipulation(self, n: int) -> bool:
        if n <= 0:
            return False

        return not(n & (n - 1))


"""
Runtime = O(logN)
Space = O(1)

isPowerOfTwo_bit_manipulation solution has a constant runtime

Runtime: 28 ms, faster than 77.33% of Python3 online submissions for Power of Two.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Power of Two.
"""
