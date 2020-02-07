class Solution:
    def binaryGap(self, N: int) -> int:

        b_gap = 0
        one_counter = 0
        while N:
            N, rem = divmod(N, 2)
            if rem == 1:
                if one_counter >= 1:  # zeros seen before
                    b_gap = max(b_gap, one_counter)
                one_counter = 1
            else:
                if one_counter > 0:  # one was seen before
                    one_counter += 1

        return b_gap

"""
Runtime: O(logN)
Space: O(1)

Runtime: 32 ms, faster than 28.42% of Python3 online submissions for Binary Gap.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Gap.
"""
