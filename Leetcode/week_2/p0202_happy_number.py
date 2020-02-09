class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])

        while n != 1:
            sqr = 0
            while n:
                n, rem = divmod(n, 10)
                sqr += rem**2
            if sqr in seen:
                return False
            seen.add(sqr)
            n = sqr

        return True


"""
Runtime: O(n)
Space: O(n)

Runtime: 24 ms, faster than 96.89% of Python3 online submissions for Happy Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Happy Number.
"""
