from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return self.loop_gen(n)

    def bin_to_dec(self, bit_arr):
        ans = 0
        for n in bit_arr:
            ans = ans * 2 + n
        return ans

    def loop_gen(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        gray = [[0], [1]]
        max_len = 2**n
        while len(gray) < max_len:
            new_gray = []
            for code in gray:
                new_gray.append([0] + code)
            for code in reversed(gray):
                new_gray.append([1] + code)
            gray = new_gray

        return [self.bin_to_dec(code) for code in gray]

    def backtrack(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        self.gray = [0] * 32
        self.all_code = []

        def recursive_gen(k):
            if k == 0:
                self.all_code.append(self.bin_to_dec(self.gray))
                return

            recursive_gen(k - 1)
            self.gray[31 - (k - 1)] ^= 1
            recursive_gen(k - 1)

        recursive_gen(n)
        return self.all_code


"""
Runtime: 32 ms, faster than 59.48% of Python3 online submissions for Gray Code.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Gray Code.
"""
