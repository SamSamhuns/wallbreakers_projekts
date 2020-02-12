from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change_dict = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            change_dict[bill] += 1
            if bill == 10:
                change_dict[5] -= 1
            elif bill == 20:
                change_dict[5] -= 1
                if change_dict[10] == 0:
                    change_dict[5] -= 2
                else:
                    change_dict[10] -= 1

            if change_dict[5] < 0 or change_dict[10] < 0:
                return False

        return True


"""
Runtime: O(n)
Space: O(1)

Runtime: 156 ms, faster than 37.77% of Python3 online submissions for Lemonade Change.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Lemonade Change.
"""
