class Solution:
    def findComplement(self, num: int) -> int:

        binary = []
        while num:
            num, rem = divmod(num, 2)
            binary.append(rem ^ 1)

        complement = 0
        for i, bit in enumerate(binary):
            complement += ((2**i) * bit)
        return complement


"""
Runtime: O(log num)
Space: O(log num)

Runtime: 24 ms, faster than 83.55% of Python3 online submissions for Number Complement.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Number Complement.
"""
