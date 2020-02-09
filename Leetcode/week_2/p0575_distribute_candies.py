from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:

        girl = set()
        bc, gc = 0, 0
        half_len = len(candies) // 2
        for candy in candies:
            if gc == half_len:
                break
            if candy not in girl or bc > half_len:
                girl.add(candy)
                gc += 1
            else:
                bc += 1

        return len(girl)


"""
Runtime: O(n)
Space: O(n)

Runtime: 960 ms, faster than 26.81% of Python3 online submissions for Distribute Candies.
Memory Usage: 14.7 MB, less than 33.33% of Python3 online submissions for Distribute Candies.
"""
