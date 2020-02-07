from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        for i in range(len(A)):
            alen = len(A[i])
            for j in range(alen):
                if j < alen // 2:
                    A[i][j], A[i][alen - 1 - j] = A[i][alen - 1 - j], A[i][j]
                A[i][j] ^= 1

        return A


"""
Runtime: O(mn)
Space: O(mn)
where m = no of rows and n = no of cols

Runtime: 48 ms, faster than 78.81% of Python3 online submissions for Flipping an Image.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Flipping an Image.
"""
