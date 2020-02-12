from typing import List


class Solution:
    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        # O(NlogN + MlogM) N = len of children, M = len of cookies

        children.sort(reverse=True)
        cookies.sort(reverse=True)

        i, j = 0, 0  # child and cookie index two ptr
        while i < len(children) and j < len(cookies):
            if children[i] <= cookies[j]:  # greed matched with cookie
                j += 1
            i += 1

        return j


"""
Runtime: O(nlogn + mlogm)
Space: O(1)

Runtime: 168 ms, faster than 89.77% of Python3 online submissions for Assign Cookies.
Memory Usage: 14.6 MB, less than 42.86% of Python3 online submissions for Assign Cookies.
"""
