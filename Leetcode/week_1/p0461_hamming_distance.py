class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        hdist = 0

        while xor:
            xor, rem = divmod(xor, 2)
            hdist += rem

        return hdist


"""
Runtime: O(log(max(x,y)))
Space: O(1)

Runtime: 28 ms, faster than 65.27% of Python3 online submissions for Hamming Distance.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Hamming Distance.
"""
